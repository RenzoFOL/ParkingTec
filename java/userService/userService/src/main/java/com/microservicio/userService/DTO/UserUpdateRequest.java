/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.userService.DTO;

/**
 *
 * @author renol
 */
public class UserUpdateRequest {
    private Integer idRol;

    private Integer idTipoUsuario;

    private Integer idProgramaEducativo;

    private String nombre;

    private String apellidoPaterno;

    private String apellidoMaterno;

    private String email;

    private String telefono;

    public Integer getIdRol() {
        return idRol;
    }

    public Integer getIdTipoUsuario() {
        return idTipoUsuario;
    }

    public Integer getIdProgramaEducativo() {
        return idProgramaEducativo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellidoPaterno() {
        return apellidoPaterno;
    }

    public String getApellidoMaterno() {
        return apellidoMaterno;
    }

    public String getEmail() {
        return email;
    }

    public String getTelefono() {
        return telefono;
    }
    
    

}
