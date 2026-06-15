/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.userService.Repository;

import org.apache.ibatis.annotations.*;
import com.microservicio.userService.Entity.Usuario;

/**
 *
 * @author renol
 */
@Mapper
public interface UserRepository {

    @Select("""
        SELECT
            "idUsuario",
            nombre,
            "apellidoPaterno",
            "apellidoMaterno",
            "claveUsuario",
            email,
            telefono,
            username,
            password,
            estatus = B'1' AS estatus,
            "idRol",
            rol,
            "idTipoUsuario",
            "tipoUsuario",
            "idProgramaEducativo",
            "programaEducativo"
        FROM "usuarioFullInfo"
        WHERE email = #{email}
    """)
    Usuario buscarPorCorreo(String email);

    @Select("""
        SELECT
            "idUsuario",
            nombre,
            "apellidoPaterno",
            "apellidoMaterno",
            "claveUsuario",
            email,
            telefono,
            username,
            password,
            estatus = B'1' AS estatus,
            "idRol",
            rol,
            "idTipoUsuario",
            "tipoUsuario",
            "idProgramaEducativo",
            "programaEducativo"
        FROM "usuarioFullInfo"
        WHERE username = #{username}
    """)
    Usuario buscarPorUsername(String username);

    @Select("""
        SELECT
            "idUsuario",
            nombre,
            "apellidoPaterno",
            "apellidoMaterno",
            "claveUsuario",
            email,
            telefono,
            username,
            password,
            estatus = B'1' AS estatus,
            "idRol",
            rol,
            "idTipoUsuario",
            "tipoUsuario",
            "idProgramaEducativo",
            "programaEducativo"
        FROM "usuarioFullInfo"
        WHERE "idUsuario" = #{id}
        LIMIT 1
    """)
    Usuario buscarPorId(@Param("id") Integer id);

    @Select("""
        SELECT
            "idUsuario",
            nombre,
            "apellidoPaterno",
            "apellidoMaterno",
            "claveUsuario",
            email,
            telefono,
            username,
            password,
            estatus = B'1' AS estatus,
            "idRol",
            rol,
            "idTipoUsuario",
            "tipoUsuario",
            "idProgramaEducativo",
            "programaEducativo"
        FROM "usuarioFullInfo"
        WHERE "claveUsuario" = #{claveUsuario}
    """)
    Usuario buscarPorClaveUsuario(String claveUsuario);

    @Insert("""
        INSERT INTO "usuario"
        (
            "idUsuario",
            nombre,
            "apellidoPaterno",
            "apellidoMaterno",
            "claveUsuario",
            email,
            telefono,
            username,
            password,
            estatus,
            "idRol",
            "idTipoUsuario",
            "idProgramaEducativo",
            "tiempoCreacion"
        )
        VALUES
        (
            (SELECT COALESCE(MAX("idUsuario"), 0) + 1 FROM "usuario"),
            #{nombre},
            #{apellidoPaterno},
            #{apellidoMaterno},
            #{claveUsuario},
            #{email},
            #{telefono},
            #{username},
            #{password},
            B'1',
            #{idRol},
            #{idTipoUsuario},
            #{idProgramaEducativo},
            NOW()
        )
    """)
    void insertar(Usuario usuario);

    @Update("""
        UPDATE "usuario"
        SET
            nombre = #{nombre},
            "apellidoPaterno" = #{apellidoPaterno},
            "apellidoMaterno" = #{apellidoMaterno},
            email = #{email},
            telefono = #{telefono},
            "idRol" = #{idRol},
            "idTipoUsuario" = #{idTipoUsuario},
            "idProgramaEducativo" = #{idProgramaEducativo},
            "tiempoActualizacion" = NOW()
        WHERE "idUsuario" = #{idUsuario}
    """)
    void actualizar(Usuario usuario);

    @Update("""
        UPDATE "usuario"
        SET estatus = CASE WHEN estatus = B'1' THEN B'0' ELSE B'1' END,
            "tiempoActualizacion" = NOW()
        WHERE "idUsuario" = #{idUsuario}
    """)
    void cambiarEstatus(Integer idUsuario);
}
