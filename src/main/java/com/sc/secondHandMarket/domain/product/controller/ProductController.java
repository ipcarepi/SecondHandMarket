package com.sc.secondHandMarket.domain.product.controller;

import com.sc.secondHandMarket.domain.product.entity.Product;
import com.sc.secondHandMarket.domain.product.dto.request.ProductRequestDto;
import com.sc.secondHandMarket.domain.product.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/products")
public class ProductController {

    private final ProductService productService;

    // 전체 상품 목록 조회
    @GetMapping
    public ResponseEntity<List<Product>> findAll() {
        return ResponseEntity.ok()
                .body(productService.findAll());
    }

    // 상품 id로 조회
    @GetMapping("/{productId}")
    public ResponseEntity<Product> findByName(@PathVariable Long productId) {
        return ResponseEntity.ok()
                .body(productService.findById(productId));
    }

    // 상품 등록
    @PostMapping
    public ResponseEntity<String> saveProduct(@RequestBody ProductRequestDto dto) {
        productService.saveProduct(dto);
        return ResponseEntity.ok("저장 완료");
    }

    // 상품 삭제
    @DeleteMapping("/{productId}")
    public ResponseEntity<String> deleteProduct(@PathVariable Long productId) {
        Product product = productService.deleteProduct(productId);
        return ResponseEntity.ok(product.getName() + " : 삭제 완료");
    }

}