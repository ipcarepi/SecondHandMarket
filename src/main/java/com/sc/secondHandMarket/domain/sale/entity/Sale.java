package com.sc.secondHandMarket.domain.sale.entity;

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
    private Long user_id;
    @ManyToOne(fetch = LAZY)
    private Long product_id;

//    private Long size_option_id;

    private int price;
    private String status;
    private LocalDateTime created_at;

    public Sale(Long user_id, Long product_id, int price, String status) {
        this.user_id = user_id;
        this.product_id = product_id;
        this.price = price;
        this.status = status;
        this.created_at = LocalDateTime.now();
    }
}
