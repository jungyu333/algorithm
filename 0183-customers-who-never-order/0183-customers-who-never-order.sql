# Write your MySQL query statement below
SELECT customer.name AS Customers
FROM Customers customer
LEFT JOIN Orders orders
    ON orders.customerId = customer.id
WHERE orders.id is Null;