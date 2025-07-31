package com.sc.secondHandMarket.domain.product.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
//    private int brand_id;
    private String model_number;
    // private int release_price;
    private int current_price;
    // private int last_trade_price;
    private String color;
    private String description;
    private String delivery_info;
    private String imageUrl;
    private int reviewCount;
    private LocalDateTime created_at;

    public Product(String name, String model_number, 
                   int current_price, String color,
                   String description, String delivery_info, String imageUrl, int reviewCount) {
        this.name = name;
        this.model_number = model_number;
        // this.release_price = release_price;
        this.current_price = current_price;
        // this.last_trade_price = last_trade_price;
        this.color = color;
        this.description = description;
        this.delivery_info = delivery_info;
        this.imageUrl = imageUrl;
        this.reviewCount = reviewCount;
        this.created_at = LocalDateTime.now();
    }
}
