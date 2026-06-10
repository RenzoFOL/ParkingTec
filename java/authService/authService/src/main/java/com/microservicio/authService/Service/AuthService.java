/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.authService.Service;

import com.microservicio.authService.DTO.LoginRequest;
import com.microservicio.authService.DTO.LoginResponse;
import com.microservicio.authService.Entity.Usuario;
import com.microservicio.authService.Repository.AuthRepository;
import com.microservicio.authService.Security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.stereotype.Service;


/**
 *
 * @author renol
 */
 
@Service
public class AuthService {

    @Autowired
    private AuthRepository repository;

    @Autowired
    private JwtUtil jwtUtil;

    public LoginResponse login(LoginRequest request) {
        Usuario usuario = repository.buscarPorUsuario(request.getUsuario());

        if (usuario == null) {
            throw new RuntimeException("Usuario no encontrado");
        }

        if (!usuario.getEstatus()) {
            throw new RuntimeException("Usuario inactivo");
        }

        boolean passwordValida =
                BCrypt.checkpw(request.getPassword(), usuario.getPassword());

        if (!passwordValida) {
            throw new RuntimeException("Contraseña incorrecta");
        }

        String token = jwtUtil.generarToken(
                usuario.getIdUsuario(),
                usuario.getUsername(),
                usuario.getIdRol(),
                usuario.getRol(),
                usuario.getIdTipoUsuario(),
                usuario.getTipoUsuario()
        );

        LoginResponse response = new LoginResponse();
        response.setIdUsuario(usuario.getIdUsuario());
        response.setIdRol(usuario.getIdRol());
        response.setRol(usuario.getRol());
        response.setUsuario(usuario.getUsername());
        response.setNombreCompleto(
                usuario.getNombre() + " " +
                usuario.getApellidoPaterno() + " " +
                (usuario.getApellidoMaterno() != null ? usuario.getApellidoMaterno() : "")
        );
        response.setIdTipoUsuario(usuario.getIdTipoUsuario());
        response.setTipoUsuario(usuario.getTipoUsuario());
        response.setToken(token);

        return response;
    }
}