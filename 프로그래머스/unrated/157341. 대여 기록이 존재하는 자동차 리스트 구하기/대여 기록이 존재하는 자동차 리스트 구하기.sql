-- 코드를 입력하세요
SELECT CAR.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR CAR
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY HIS
ON CAR.CAR_ID = HIS.CAR_ID AND CAR.CAR_TYPE = '세단'
WHERE month(HIS.START_DATE) = 10
GROUP BY CAR.CAR_ID
ORDER BY CAR.CAR_ID DESC;