from Db.connection import get_connection


class VehicleRepository:

    def obtener_por_usuario(self, id_usuario):

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT
                v.idVehiculo,
                v.idUsuario,
                v.idModelo,
                m.modelo,
                ma.idMarca,
                ma.marca,
                v.placa,
                v.color,
                v.anio,
                v.descripcion,
                v.estatus
            FROM vehiculos v
            INNER JOIN modelos m
                ON v.idModelo = m.idModelo
            INNER JOIN marcas ma
                ON m.idMarca = ma.idMarca
            WHERE v.idUsuario = %s
        """

        cursor.execute(sql, (id_usuario,))

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado

    def buscar_por_placa(self, placa):

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT *
            FROM vehiculos
            WHERE placa = %s
        """

        cursor.execute(sql, (placa,))

        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return resultado

    def contar_activos(self, id_usuario):

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT COUNT(*) AS total
            FROM vehiculos
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
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT *
            FROM vehiculos
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
            INSERT INTO vehiculos
            (
                idUsuario,
                idModelo,
                placa,
                color,
                anio,
                descripcion,
                estatus
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s
            )
        """

        cursor.execute(
            sql,
            (
                datos["idUsuario"],
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
            UPDATE vehiculos
            SET
                idModelo = %s,
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

    def actualizar_estatus(
        self,
        id_vehiculo,
        estatus
    ):

        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE vehiculos
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