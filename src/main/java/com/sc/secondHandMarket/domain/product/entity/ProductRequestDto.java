package com.sc.secondHandMarket.domain.product.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class ProductRequestDto {
    private String name;
    private String model_number;
    private int current_price;
    private String color;
    private String description;
    private String delivery_info;
    private String imageUrl;
    private int reviewCount;

    public Product toEntity() {
        return new Product(
            name,
            model_number,
            current_price,
            color,
            description,
            delivery_info,
            imageUrl,
            reviewCount
        );
    }
}
