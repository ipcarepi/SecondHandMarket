package com.sc.secondHandMarket;

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
        Product product = new Product();
        product.setName("나이키 덩크 로우");
        product.setPrice(139000);
        productRepository.save(product);

        productRepository.findAll().forEach(p ->
                System.out.println("🟢 상품명: " + p.getName() + ", 가격: " + p.getPrice()));
    }
}
