Entity	DB 테이블과 매핑되는 클래스 (JPA)
Repository	DB와 직접 연결, 쿼리 처리 (JPA 인터페이스 활용)
Service	비즈니스 로직 담당. 트랜잭션 처리, 여러 repository 간 조합 등 로직 수행
Controller	클라이언트로부터 HTTP 요청 받아서 Service에 전달, 결과를 HTTP 응답으로 반환

DTO는 계층 간 데이터를 주고받을 때 사용하는 "데이터용 객체

mysql -u root -p
DESC product;
use secondhand;
SHOW TABLES;
SHOW DATABASES;
SELECT * FROM PRODUCT;
DELETE FROM product;