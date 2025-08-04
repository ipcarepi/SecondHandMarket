package com.sc.secondHandMarket.domain.product.service;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.product.dto.request.ProductRequestDto;

import java.util.List;

public interface ProductService {

    List<Product> findAll();

    Product findById(Long productId);

    Product findByName(String productName);

    Product saveProduct(ProductRequestDto dto);

    Product deleteProduct(Long productId);
}
