package com.sc.secondHandMarket.domain.transaction.entity;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.user.entity.User;
import jakarta.persistence.*;

import java.time.LocalDateTime;

import static jakarta.persistence.FetchType.LAZY;

@Entity
public class Transaction {

    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne(fetch= LAZY)
    @JoinColumn(name = "buyer_id")
    private User buyer;
    @ManyToOne(fetch= LAZY)
    @JoinColumn(name = "seller_id")
    private User seller;
    @ManyToOne(fetch= LAZY)
    @JoinColumn(name = "product_id")
    private Product product;

//    private Long size_option_id;

    private int price;
    private LocalDateTime traded_at;

    public Transaction(User buyer, User seller, Product product, int price) {
        this.buyer = buyer;
        this.seller = seller;
        this.product = product;
        this.price = price;
        this.traded_at = LocalDateTime.now();
    }
}
