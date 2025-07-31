package com.sc.secondHandMarket.domain.product.service;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.product.entity.ProductRequestDto;
import com.sc.secondHandMarket.domain.product.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductRepository productRepository;

    public Product saveProduct(ProductRequestDto dto) {
        return productRepository.save(dto.toEntity());
    }
}
