# 1. artists 테이블에서 Name 칼럼을 대문자로 출력해주세요.

#SELECT  UPPER(Name) 
#FROM artists a 


# 2.tracks 테이블에서 곡 이름을 추출하여 길이를 출력해주세요. 

SELECT LENGTH (name) # 우리가 원하는 것은 변수이다.  
FROM tracks t

# 3.invoices 테이블에서 청구서의 총 금액을 반올림한 결과를 표시

SELECT ROUND(Total) 
FROM  invoices i 

# 1. customers 테이블에서 각 나라별로 고객 수가 5명 이상인 나라의 이름 선택

SELECT Country 
FROM customers c
GROUP By Country 
HAVING Country > 5

# 3. tracks 테이블에서 각 곡의 장르별로 평균 길이가 300000 밀리초(5분) 이상인
장르를 선택

SELECT GenreId 
FROM tracks t 
Group by GenreId 
HAVING AVG(Milliseconds) > 300000


# 5. tracks 테이블에서 각 앨범의 트랙 수가 15개 이상인 앨범을 선택
- 문제가 의미하는 것을 모르겠음
SELECT * 
FROM tracks t


