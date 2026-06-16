from src.Db.connection import get_connection

class VehicleRepository:

    def obtener_por_usuario(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT
                idVehiculo,
                idUsuario,
                claveVehiculo,
                idMarca,
                marca,
                idModelo,
                modelo,
                placa,
                color,
                anio,
                descripcion,
                estatus
            FROM vehiculofullinfo
            WHERE idUsuario = %s
        """

        cursor.execute(sql, (id_usuario,))
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado
    

    def buscar_por_placa(self, placa):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT *
            FROM vehiculo
            WHERE placa = %s
        """

        cursor.execute(sql, (placa,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return resultado
    
    def contar_activos(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT COUNT(*) AS total
            FROM vehiculo
            WHERE idUsuario = %s
            AND estatus = 1
        """

        cursor.execute(sql, (id_usuario,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return resultado["total"]
    
    def obtener_por_id(self, id_vehiculo):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT *
            FROM vehiculo
            WHERE idVehiculo = %s
        """

        cursor.execute(sql, (id_vehiculo,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return resultado

    def guardar(self, datos):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO vehiculo
            (
                idUsuario,
                claveVehiculo,
                idModelo,
                placa,
                color,
                anio,
                descripcion,
                estatus
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s
            )
        """

        cursor.execute(
            sql,
            (
                datos["idUsuario"],
                datos["claveVehiculo"],
                datos["idModelo"],
                datos["placa"],
                datos["color"],
                datos["anio"],
                datos["descripcion"],
                datos["estatus"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def actualizar(self, id_vehiculo, datos):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE vehiculo
            SET
                idModelo = %s,
                claveVehiculo = %s,
                placa = %s,
                color = %s,
                anio = %s,
                descripcion = %s
            WHERE idVehiculo = %s
        """

        cursor.execute(
            sql,
            (
                datos["idModelo"],
                datos["claveVehiculo"],
                datos["placa"],
                datos["color"],
                datos["anio"],
                datos["descripcion"],
                id_vehiculo
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    
    def actualizar_estatus(self, id_vehiculo, estatus):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE vehiculo
            SET estatus = %s
            WHERE idVehiculo = %s
        """

        cursor.execute(
            sql,
            (
                estatus,
                id_vehiculo
            )
        )

        conn.commit()

        cursor.close()
        conn.close()