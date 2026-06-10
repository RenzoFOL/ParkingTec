/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.authService.DTO;

/**
 *
 * @author renol
 */
public class LoginResponse {
    private Integer idUsuario;

    private Integer idRol;

    private String rol;

    private String usuario;

    private String nombreCompleto;

    private Integer idTipoUsuario;

    private String tipoUsuario;

    private String token;

    public void setIdUsuario(Integer idUsuario) {
        this.idUsuario = idUsuario;
    }

    public void setIdRol(Integer idRol) {
        this.idRol = idRol;
    }

    public void setRol(String rol) {
        this.rol = rol;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public void setNombreCompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public void setIdTipoUsuario(Integer idTipoUsuario) {
        this.idTipoUsuario = idTipoUsuario;
    }

    public void setTipoUsuario(String tipoUsuario) {
        this.tipoUsuario = tipoUsuario;
    }

    public void setToken(String token) {
        this.token = token;
    }

    
}
