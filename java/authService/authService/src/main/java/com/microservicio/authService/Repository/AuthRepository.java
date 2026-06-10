/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package com.microservicio.authService.Repository;

import com.microservicio.authService.Entity.Usuario;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

/**
 *
 * @author renol
 */
@Mapper
public interface AuthRepository {

    @Select("""
        SELECT *
        FROM "usuarioFullInfo"
        WHERE username = #{username}
    """)
    Usuario buscarPorUsuario(
            String username
    );

}
