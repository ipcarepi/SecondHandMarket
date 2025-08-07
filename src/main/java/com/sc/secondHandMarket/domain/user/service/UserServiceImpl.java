package com.sc.secondHandMarket.domain.user.service;

import com.sc.secondHandMarket.domain.user.dto.response.UserResponseDto;
import com.sc.secondHandMarket.domain.user.entity.User;
import com.sc.secondHandMarket.domain.user.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService{

    private final UserRepository userRepository;

    @Override
    public List<UserResponseDto> findAll() {
        List<UserResponseDto> dtoList = new ArrayList<>();
        for (User user : userRepository.findAll()) {
            dtoList.add(toDto(user));
        }
        return dtoList;
    }

    @Override
    public UserResponseDto findById(Long userId) {
        return toDto(userRepository.findById(userId).orElseThrow());
    }

    @Override
    public User save(User user) {
        return userRepository.save(user);
    }

    // DTO로 변환
    private UserResponseDto toDto(User user) {
        return new UserResponseDto(user);
    }

    @Override
    public User deleteById(Long userId) {
        User user = userRepository.findById(userId).orElseThrow();
        userRepository.deleteById(userId);
        return user;
    }
}
