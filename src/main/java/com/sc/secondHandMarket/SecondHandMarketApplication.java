package com.sc.secondHandMarket;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.product.repository.ProductRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SecondHandMarketApplication implements CommandLineRunner {

    private final ProductRepository productRepository;

    public SecondHandMarketApplication(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    public static void main(String[] args) {
        SpringApplication.run(SecondHandMarketApplication.class, args);
    }

    @Override
    public void run(String... args) {
        productRepository.findAll().forEach(p -> {
            System.out.println("🟢 상품명: " + p.getName());
            System.out.println("   모델번호: " + p.getModel_number());
            System.out.println("   가격: " + p.getCurrent_price());
            System.out.println("   색상: " + p.getColor());
            System.out.println("   설명: " + p.getDescription());
            System.out.println("   배송정보: " + p.getDelivery_info());
            System.out.println("   리뷰 수: " + p.getReviewCount());
            System.out.println("   이미지: " + p.getImageUrl());
            System.out.println("-------------------------------------------------");
        });
    }
}
