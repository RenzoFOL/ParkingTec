/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.authService.Controller;

import com.microservicio.authService.DTO.*;
import com.microservicio.authService.Service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 *
 * @author renol
 */
@RestController
@RequestMapping("/auth")
public class AuthController {
    
    @Autowired
    private AuthService service;

    @PostMapping("/login")
    public LoginResponse login(@RequestBody LoginRequest request) {
        return service.login(request);
    }
}
