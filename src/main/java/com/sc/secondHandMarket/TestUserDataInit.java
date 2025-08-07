package com.sc.secondHandMarket;

import com.sc.secondHandMarket.domain.user.entity.User;
import com.sc.secondHandMarket.domain.user.repository.UserRepository;
import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

/**
 *  User 데이터 넣는 코드
 *
 *  주석화 해놓은 @Component와 @PostConstruct를 주석화 헤제한 뒤
 *  메인 코드를 실행시키면 자동으로 들어감.
 *
 *  이후에는 다시 두 어노테이션을 주석화할 것.
 *
 *  * 마음대로 더 추가 가능
 */

//@Component
@RequiredArgsConstructor
public class TestUserDataInit {

    private final UserRepository userRepository;

//    @PostConstruct
    public void testUserData() throws InterruptedException {
        User user1 = new User("user1", "123123", "random1@naver.com", "010-1254-2314");
        Thread.sleep(1000);
        User user2 = new User("user2", "456456", "random2@naver.com", "010-1459-0897");
        Thread.sleep(1000);
        User user3 = new User("user3", "789789", "random3@naver.com", "010-9854-0283");

        userRepository.save(user1);
        userRepository.save(user2);
        userRepository.save(user3);
    }
}
