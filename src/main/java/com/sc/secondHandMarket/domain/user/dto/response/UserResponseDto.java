package com.sc.secondHandMarket.domain.user.dto.response;

import com.sc.secondHandMarket.domain.user.entity.User;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Getter
@NoArgsConstructor
public class UserResponseDto {

    private String nickname;
    private String email;
    private String phone;
    private LocalDateTime created_at;

    public UserResponseDto(User user) {
        this.nickname = user.getNickname();
        this.email = user.getEmail();
        this.phone = user.getPhone();
        this.created_at = user.getCreated_at();
    }
}
