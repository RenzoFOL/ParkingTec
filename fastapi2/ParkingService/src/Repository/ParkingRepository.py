from src.Db.connection import get_connection
import datetime
import math

class ParkingRepository:
    def obtener_cajones_libres(self):
        connection = get_connection()
        cursor = connection.cursor()
        
        sql = """
            SELECT idEspacio, 
            claveEspacio, 
            tipo, 
            ocupado, 
            estatus 
            FROM espacioestacionamiento 
            WHERE ocupado = 0 AND estatus = 1
        """
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return resultados
    
    def contar_autos_adentro(self, ids_vehiculos: list):
        if not ids_vehiculos:
            return 0
            
        connection = get_connection()
        cursor = connection.cursor()
        try:
            format_strings = ','.join(['%s'] * len(ids_vehiculos))
            
            sql = f"""
                SELECT COUNT(*) as total 
                FROM movimiento 
                WHERE idVehiculo IN ({format_strings}) AND tiempoSalida = tiempoEntrada
            """
            cursor.execute(sql, tuple(ids_vehiculos))
            resultado = cursor.fetchone()
            return resultado['total'] if resultado else 0
        finally:
            cursor.close()
            connection.close()
    
    def registrar_entrada(self, id_vehiculo: int):
        connection = get_connection()
        cursor = connection.cursor()
        
        try:
            sql_buscar = "SELECT idEspacio FROM espacioestacionamiento WHERE ocupado = 0 AND estatus = 1 LIMIT 1"
            cursor.execute(sql_buscar)
            cajon = cursor.fetchone()
            
            if not cajon:
                return {"error": "El estacionamiento está lleno"}
                
            id_espacio = cajon['idEspacio']
            
            sql_ocupar = "UPDATE espacioestacionamiento SET ocupado = 1 WHERE idEspacio = %s"
            cursor.execute(sql_ocupar, (id_espacio,))
            
            tiempo_actual = datetime.datetime.now()
            tarifa_base = 15.00 
            
            sql_movimiento = """
                INSERT INTO movimiento (
                    idVehiculo, 
                    tiempoEntrada, 
                    tiempoSalida, 
                    minutosEstacionado, 
                    horasCobradas, 
                    costoTotal, 
                    tarifaHora, 
                    tiempoCreacion, 
                    tiempoActualizacion, 
                    idEspacio
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                id_vehiculo, 
                tiempo_actual,
                tiempo_actual,
                0,
                0,
                0.0,
                tarifa_base, 
                tiempo_actual,
                tiempo_actual,
                id_espacio
            )
            
            cursor.execute(sql_movimiento, valores)
            
            connection.commit()
            
            id_movimiento = cursor.lastrowid
            
            return {
                "idMovimiento": id_movimiento,
                "tiempoEntrada": tiempo_actual,
                "espacioAsignado": id_espacio,
                "tarifaPorHora": tarifa_base
            }
            
        except Exception as e:
            connection.rollback()
            return {"error": str(e)}
            
        finally:
            cursor.close()
            connection.close()

    def registrar_salida(self, id_vehiculo: int):
        connection = get_connection()
        cursor = connection.cursor()
        
        try:
            sql_buscar = "SELECT idMovimiento, idEspacio, tiempoEntrada FROM movimiento WHERE idVehiculo = %s AND tiempoSalida = tiempoEntrada LIMIT 1"
            cursor.execute(sql_buscar, (id_vehiculo,))
            movimiento = cursor.fetchone()
            
            if not movimiento:
                return {"error": "No se encontró un movimiento activo para este vehículo"}
                
            id_movimiento = movimiento['idMovimiento']
            id_espacio = movimiento['idEspacio']
            tiempo_entrada = movimiento['tiempoEntrada']
            
            tiempo_salida = datetime.datetime.now()
            diferencia = tiempo_salida - tiempo_entrada
            minutos = int(diferencia.total_seconds() / 60)
            horas_cobradas = math.ceil(minutos / 60)
            if horas_cobradas == 0:
                horas_cobradas = 1

            tarifa_hora = 15.00
            costo = horas_cobradas * tarifa_hora
            
            sql_update_mov = """
                UPDATE movimiento SET tiempoSalida = %s, minutosEstacionado = %s, 
                horasCobradas = %s, costoTotal = %s, tiempoActualizacion = %s 
                WHERE idMovimiento = %s
            """
            cursor.execute(sql_update_mov, (tiempo_salida, minutos, horas_cobradas, costo, tiempo_salida, id_movimiento))
            
            sql_liberar = "UPDATE espacioestacionamiento SET ocupado = 0 WHERE idEspacio = %s"
            cursor.execute(sql_liberar, (id_espacio,))
            
            connection.commit()
            return {
            "idMovimiento": id_movimiento,
            "tiempoEntrada": tiempo_entrada.isoformat() if hasattr(tiempo_entrada, 'isoformat') else str(tiempo_entrada),
            "tiempoSalida": tiempo_salida.isoformat(),
            "espacioAsignado": id_espacio,
            "tarifaHora": tarifa_hora,
            "costoTotal": round(costo, 2),
            "horasCobradas": horas_cobradas
        }
            
        except Exception as e:
            connection.rollback()
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()