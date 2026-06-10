/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.userService.Service;

import com.microservicio.userService.DTO.MessageResponse;
import com.microservicio.userService.DTO.UserCreateRequest;
import com.microservicio.userService.DTO.UserProfileResponse;
import com.microservicio.userService.DTO.UserUpdateRequest;
import com.microservicio.userService.Entity.Usuario;
import com.microservicio.userService.Repository.UserRepository;
import com.microservicio.userService.Security.JwtUtil;
import java.util.Random;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.stereotype.Service;

/**
 *
 * @author renol
 */

@Service
public class UserService {

    @Autowired
    private UserRepository repository;

    @Autowired
    private JwtUtil jwtUtil;

    public MessageResponse register(UserCreateRequest request, String token) {
        Integer idRol = jwtUtil.getRol(token);
        if (idRol != 1) {
            throw new RuntimeException("Solo administradores pueden registrar usuarios");
        }

        if (repository.buscarPorCorreo(request.getEmail()) != null) {
            throw new RuntimeException("Correo ya registrado");
        }

        if (repository.buscarPorUsername(request.getUsername()) != null) {
            throw new RuntimeException("Usuario ya registrado");
        }

        Usuario usuario = new Usuario();
        usuario.setNombre(request.getNombre());
        usuario.setApellidoPaterno(request.getApellidoPaterno());
        usuario.setApellidoMaterno(request.getApellidoMaterno());
        usuario.setEmail(request.getEmail());
        usuario.setTelefono(request.getTelefono());
        usuario.setUsername(request.getUsername());
        usuario.setPassword(BCrypt.hashpw(request.getPassword(), BCrypt.gensalt()));
        usuario.setClaveUsuario(generarClaveUnica());
        usuario.setIdRol(request.getIdRol());
        usuario.setIdTipoUsuario(request.getIdTipoUsuario());
        usuario.setIdProgramaEducativo(request.getIdProgramaEducativo());
        usuario.setEstatus(true); // activo por defecto

        repository.insertar(usuario);

        MessageResponse response = new MessageResponse();
        response.setSuccess(true);
        response.setMessage("Usuario registrado correctamente");
        return response;
    }

    public MessageResponse update(UserUpdateRequest request, String token) {
        Integer idUsuario = jwtUtil.getUserId(token);
        Usuario usuario = repository.buscarPorId(idUsuario);

        if (usuario == null) {
            throw new RuntimeException("Usuario no encontrado");
        }

        Usuario correoExistente = repository.buscarPorCorreo(request.getEmail());
        if (correoExistente != null && !correoExistente.getIdUsuario().equals(idUsuario)) {
            throw new RuntimeException("Correo ya registrado");
        }

        // No se permite editar username, password ni claveUsuario
        usuario.setNombre(request.getNombre());
        usuario.setApellidoPaterno(request.getApellidoPaterno());
        usuario.setApellidoMaterno(request.getApellidoMaterno());
        usuario.setEmail(request.getEmail());
        usuario.setTelefono(request.getTelefono());
        usuario.setIdRol(request.getIdRol());
        usuario.setIdTipoUsuario(request.getIdTipoUsuario());
        usuario.setIdProgramaEducativo(request.getIdProgramaEducativo());

        repository.actualizar(usuario);

        MessageResponse response = new MessageResponse();
        response.setSuccess(true);
        response.setMessage("Usuario actualizado correctamente");
        return response;
    }

    public UserProfileResponse profile(String token) {
        Integer idUsuario = jwtUtil.getUserId(token);
        Usuario usuario = repository.buscarPorId(idUsuario);

        if (usuario == null) {
            throw new RuntimeException("Usuario no encontrado");
        }

        UserProfileResponse response = new UserProfileResponse();
        response.setIdUsuario(usuario.getIdUsuario());
        response.setRol(usuario.getRol());
        response.setNombreCompleto(usuario.getNombre() + " " + usuario.getApellidoPaterno() +
                (usuario.getApellidoMaterno() != null ? " " + usuario.getApellidoMaterno() : ""));
        response.setTipoUsuario(usuario.getTipoUsuario());
        response.setProgramaEducativo(usuario.getProgramaEducativo());
        response.setUsername(usuario.getUsername());
        response.setEmail(usuario.getEmail());
        response.setTelefono(usuario.getTelefono());
        response.setEstatus(usuario.getEstatus());
        response.setClaveUsuario(usuario.getClaveUsuario());
        return response;
    }

    public MessageResponse changeStatus(Integer idUsuario, String token) {
        Integer idRol = jwtUtil.getRol(token);
        if (idRol != 1) {
            throw new RuntimeException("Solo administradores pueden cambiar estatus");
        }

        Usuario usuario = repository.buscarPorId(idUsuario);
        if (usuario == null) {
            throw new RuntimeException("Usuario no encontrado");
        }

        repository.cambiarEstatus(idUsuario);

        MessageResponse response = new MessageResponse();
        response.setSuccess(true);
        response.setMessage("Estatus actualizado correctamente");
        return response;
    }

    private String generarClaveUnica() {
        Random random = new Random();
        String clave;
        do {
            clave = "USR-" + (100 + random.nextInt(900));
        } while (repository.buscarPorClaveUsuario(clave) != null);
        return clave;
    }
}

