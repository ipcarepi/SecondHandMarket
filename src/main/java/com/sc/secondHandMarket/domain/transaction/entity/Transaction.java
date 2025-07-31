package com.sc.secondHandMarket.domain.transaction.entity;

import jakarta.persistence.*;

import java.time.LocalDateTime;

import static jakarta.persistence.FetchType.LAZY;

@Entity
public class Transaction {

    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne(fetch= LAZY)
    private Long buyer_id;
    @ManyToOne(fetch= LAZY)
    private Long seller_id;
    @ManyToOne(fetch= LAZY)
    private Long product_id;

//    private Long size_option_id;

    private int price;
    private LocalDateTime traded_at;

    public Transaction(Long buyer_id, Long seller_id, Long product_id, int price) {
        this.buyer_id = buyer_id;
        this.seller_id = seller_id;
        this.product_id = product_id;
        this.price = price;
        this.traded_at = LocalDateTime.now();
    }
}
