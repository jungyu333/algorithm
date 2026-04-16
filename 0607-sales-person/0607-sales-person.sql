# Write your MySQL query statement below
SELECT sp.name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
    SELECT orders.sales_id
    FROM Orders orders
    JOIN Company com
    ON orders.com_id = com.com_id AND com.name = 'RED'
);




