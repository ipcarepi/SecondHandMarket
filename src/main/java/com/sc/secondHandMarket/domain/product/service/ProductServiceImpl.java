package com.sc.secondHandMarket.domain.product.service;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.product.dto.request.ProductRequestDto;
import com.sc.secondHandMarket.domain.product.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService{

    private final ProductRepository productRepository;

    @Override
    public List<Product> findAll() {
        return productRepository.findAll();
    }

    @Override
    public Product findById(Long productId) {
        return productRepository.findById(productId).orElseThrow();
    }

    @Override
    public Product findByName(String productName) {
        return productRepository.findByName(productName);
    }

    @Override
    public Product saveProduct(ProductRequestDto dto) {
        return productRepository.save(dto.toEntity());
    }

    @Override
    public Product deleteProduct(Long productId) {
        Product product = productRepository.findById(productId).orElseThrow();
        productRepository.deleteById(productId);
        return product;
    }
}
