/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.userService.DTO;

/**
 *
 * @author renol
 */
public class UserProfileResponse {
    private Integer idUsuario;

    private String rol;

    private String nombreCompleto;

    private String tipoUsuario;

    private String programaEducativo;

    private String username;

    private String email;

    private String telefono;

    private Boolean estatus;

    private String claveUsuario;

    public void setIdUsuario(Integer idUsuario) {
        this.idUsuario = idUsuario;
    }

    public void setRol(String rol) {
        this.rol = rol;
    }

    public void setNombreCompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public void setTipoUsuario(String tipoUsuario) {
        this.tipoUsuario = tipoUsuario;
    }

    public void setProgramaEducativo(String programaEducativo) {
        this.programaEducativo = programaEducativo;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public void setEstatus(Boolean estatus) {
        this.estatus = estatus;
    }

    public void setClaveUsuario(String claveUsuario) {
        this.claveUsuario = claveUsuario;
    }
    
    
}
