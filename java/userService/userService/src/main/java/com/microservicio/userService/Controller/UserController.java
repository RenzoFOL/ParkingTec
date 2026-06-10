/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.microservicio.userService.Controller;

import com.microservicio.userService.DTO.*;
import com.microservicio.userService.Service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 *
 * @author renol
 */

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserService service;

    @PostMapping("/register")
    public MessageResponse register(@RequestBody UserCreateRequest request, @RequestHeader("Authorization") String token){
        return service.register(request, token);
    }

    @PutMapping("/update")
    public MessageResponse update(@RequestBody UserUpdateRequest request, @RequestHeader("Authorization") String token){
        return service.update(request, token);
    }

    @GetMapping("/profile")
    public UserProfileResponse profile(@RequestHeader("Authorization") String token){
        return service.profile(token);
    }

    @PatchMapping("/status/{id}")
    public MessageResponse changeStatus(@PathVariable Integer id, @RequestHeader("Authorization") String token){
        return service.changeStatus(id, token);
    }
}