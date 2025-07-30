package com.sc.secondHandMarket.domain.product.controller;

import com.sc.secondHandMarket.domain.product.entity.ProductRequestDto;
import com.sc.secondHandMarket.domain.product.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/products")
public class ProductController {

    private final ProductService productService;

    @PostMapping
    public ResponseEntity<String> saveProduct(@RequestBody ProductRequestDto dto) {
        productService.saveProduct(dto);
        return ResponseEntity.ok("✅ 저장 완료");
    }
}
