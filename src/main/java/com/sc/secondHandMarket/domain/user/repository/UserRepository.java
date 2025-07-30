package com.sc.secondHandMarket.domain.user.repository;

import com.sc.secondHandMarket.domain.user.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
