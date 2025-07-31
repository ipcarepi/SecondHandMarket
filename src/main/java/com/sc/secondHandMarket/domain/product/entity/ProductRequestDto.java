package com.sc.secondHandMarket.domain.product.entity;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class ProductRequestDto {

    @JsonProperty("name")
    private String name;

    // modelNumber: camelCase가 기본, model_number도 허용
    @JsonProperty("modelNumber")
    @JsonAlias("model_number")
    private String modelNumber;

    // currentPrice: camelCase가 기본, current_price도 허용
    @JsonProperty("currentPrice")
    @JsonAlias("current_price")
    private Integer currentPrice;   // primitive int → Integer 로 변경 (null 구분)

    @JsonProperty("color")
    private String color;

    @JsonProperty("description")
    private String description;

    // deliveryInfo: camelCase가 기본, delivery_info도 허용
    @JsonProperty("deliveryInfo")
    @JsonAlias("delivery_info")
    private String deliveryInfo;

    // imageUrl: camelCase가 기본, image_url도 허용
    @JsonProperty("imageUrl")
    @JsonAlias("image_url")
    private String imageUrl;

    // reviewCount: camelCase가 기본, review_count도 허용
    @JsonProperty("reviewCount")
    @JsonAlias("review_count")
    private Integer reviewCount;    // primitive int → Integer 로 변경

    public Product toEntity() {
        // ⬇⬇ 엔티티의 필드 타입에 맞춰 아래 한 줄만 조정하면 됩니다.
        // 만약 Product의 currentPrice가 'int'면 null일 때 0으로 대체
        int cp = (currentPrice == null ? 0 : currentPrice);
        int rc = (reviewCount == null ? 0 : reviewCount);

        return new Product(
                name,
                modelNumber,
                cp,              // Product가 int를 받는 경우
                color,
                description,
                deliveryInfo,
                imageUrl,
                rc               // Product가 int를 받는 경우
        );
    }
}
