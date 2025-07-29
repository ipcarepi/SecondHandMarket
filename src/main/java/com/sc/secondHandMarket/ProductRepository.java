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
        product.setName("나이키 에어포스 1");
        product.setPrice(130000);
        productRepository.save(product);

        productRepository.findAll().forEach(p ->
                System.out.println("📦 상품명: " + p.getName() + ", 가격: " + p.getPrice()));
    }
}
