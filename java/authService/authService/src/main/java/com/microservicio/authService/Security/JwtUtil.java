/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.authService.Security;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import java.nio.charset.StandardCharsets;
import java.util.Date;
import javax.crypto.SecretKey;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 *
 * @author renol
 */
@Component
public class JwtUtil {

    private final SecretKey key;

    public JwtUtil(@Value("${jwt.secret}") String secret) {
        this.key = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
    }

    public String generarToken(
            Integer idUsuario,
            String username,
            Integer idRol,
            String rol,
            Integer idTipoUsuario,
            String tipoUsuario
    ) {
        return Jwts.builder()
                .claim("idUsuario", idUsuario)
                .claim("username", username)
                .claim("idRol", idRol)
                .claim("rol", rol)
                .claim("idTipoUsuario", idTipoUsuario)
                .claim("tipoUsuario", tipoUsuario)
                .issuedAt(new Date())
                .expiration(new Date(System.currentTimeMillis() + 86400000))
                .signWith(key)
                .compact();
    }
}

