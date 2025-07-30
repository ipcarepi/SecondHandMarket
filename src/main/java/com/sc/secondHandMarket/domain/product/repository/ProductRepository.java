package com.sc.secondHandMarket.domain.product.repository;

import com.sc.secondHandMarket.domain.product.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
}
