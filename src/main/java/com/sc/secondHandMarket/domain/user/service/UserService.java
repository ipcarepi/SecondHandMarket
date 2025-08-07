package com.sc.secondHandMarket.domain.user.service;

import com.sc.secondHandMarket.domain.user.dto.response.UserResponseDto;
import com.sc.secondHandMarket.domain.user.entity.User;

import java.util.List;

public interface UserService {
    List<UserResponseDto> findAll();

    UserResponseDto findById(Long userId);

    User save(User user);

    User deleteById(Long userId);
}
