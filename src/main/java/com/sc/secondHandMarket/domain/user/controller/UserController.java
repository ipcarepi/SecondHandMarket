package com.sc.secondHandMarket.domain.user.controller;

import com.sc.secondHandMarket.domain.user.dto.request.UserRequestDto;
import com.sc.secondHandMarket.domain.user.dto.response.UserResponseDto;
import com.sc.secondHandMarket.domain.user.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    // 전체 User 조회
    @GetMapping
    public ResponseEntity<List<UserResponseDto>> findAll() {
        return ResponseEntity.ok(userService.findAll());
    }

    // ID로 User 조회
    @GetMapping("/{userId}")
    public ResponseEntity<UserResponseDto> findById(@PathVariable Long userId) {
        return ResponseEntity.ok(userService.findById(userId));
    }

    // User 저장
    @PostMapping
    public ResponseEntity<String> saveUser(@RequestBody UserRequestDto userDto) {
        userService.save(userDto.toUser());
        return ResponseEntity.ok("User saved");
    }

    //ID로 User 삭제
    @DeleteMapping("/{userId}")
    public ResponseEntity<String> deleteUser(@PathVariable Long userId) {
        userService.deleteById(userId);
        return ResponseEntity.ok("User deleted");
    }

}
