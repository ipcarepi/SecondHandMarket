package com.sc.secondHandMarket.domain.user.dto.request;

import com.sc.secondHandMarket.domain.user.entity.User;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class UserRequestDto {
    private String nickname;
    private String password;
    private String email;
    private String phone;

    public User toUser() {
        return new User(
                nickname,
                password,
                email,
                phone);
    }

}
