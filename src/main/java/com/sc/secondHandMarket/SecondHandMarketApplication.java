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
        Product product = new Product("나이키 덩크 로우", null, 139000,
                139000, 139000, "black", "nike dunk low", "delivery");
        productRepository.save(product);

        productRepository.findAll().forEach(p ->
                System.out.println("🟢 상품명: " + p.getName() + ", 가격: " + p.getLast_trade_price()));
    }
}
