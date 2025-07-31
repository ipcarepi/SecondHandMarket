package com.sc.secondHandMarket.domain.sale.entity;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.user.entity.User;
import jakarta.persistence.*;
import lombok.NoArgsConstructor;
import java.time.LocalDateTime;

import static jakarta.persistence.FetchType.*;

@Entity
@NoArgsConstructor
public class Sale {

    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne(fetch= LAZY)
    @JoinColumn(name = "user_id")
    private User user;
    @ManyToOne(fetch = LAZY)
    @JoinColumn(name = "product_id")
    private Product product;

//    private Long size_option_id;

    private int price;
    private String status;
    private LocalDateTime created_at;

    public Sale(User user, Product product, int price, String status) {
        this.user = user;
        this.product = product;
        this.price = price;
        this.status = status;
        this.created_at = LocalDateTime.now();
    }
}
