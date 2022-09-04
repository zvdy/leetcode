# Write your MySQL query statement below
SELECT Product.product_id,
    product_name
FROM Product
JOIN Sales
    ON Sales.product_id = Product.product_id
GROUP BY Sales.product_id
HAVING min(sale_date) >=  CAST('2019-01-01' AS date)
    && max(sale_date) <= CAST('2019-03-31' AS date);