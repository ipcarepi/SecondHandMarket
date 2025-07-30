package com.sc.secondHandMarket.domain.user.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class User {

    @Id
    @GeneratedValue
    private Long id;

    private String email;
    private String password;
    private String nickname;
    private String phone;
    private LocalDateTime created_at;

    public User(String email, String password, String nickname, String phone) {
        this.email = email;
        this.password = password;
        this.nickname = nickname;
        this.phone = phone;
        this.created_at = LocalDateTime.now();
    }
}
