/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.authService.Service;

/**
 *
 * @author renol
 */
import com.microservicio.authService.dto.*;
import com.microservicio.authService.AuthRepository;
import com.microservicio.authService..JwtUtil;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AuthService {

    @Autowired
    private AuthRepository repository;

    @Autowired
    private JwtUtil jwtUtil;

    public LoginResponse login(LoginRequest request){
        var usuario = repository.buscarPorUsuario(request.getUsuario());

        if(usuario == null){
            throw new RuntimeException("Usuario no existe");
        }

        if(!usuario.getPassword().equals(request.getPassword())){
            throw new RuntimeException("Contraseña incorrecta");
        }

        String token =
                jwtUtil.generarToken(
                        usuario.getIdUsuario(),
                        usuario.getUsuario(),
                        usuario.getRol()
                );

        LoginResponse response =
                new LoginResponse();

        response.setIdUsuario(
                usuario.getIdUsuario()
        );

        response.setIdRol(
                usuario.getIdRol()
        );

        response.setRol(
                usuario.getRol()
        );

        response.setUsuario(
                usuario.getUsuario()
        );

        response.setNombreCompleto(
                usuario.getNombre()
        );

        response.setIdTipoUsuario(
                usuario.getIdTipoUsuario()
        );

        response.setTipoUsuario(
                usuario.getTipoUsuario()
        );

        response.setToken(token);

        return response;
    }
}
