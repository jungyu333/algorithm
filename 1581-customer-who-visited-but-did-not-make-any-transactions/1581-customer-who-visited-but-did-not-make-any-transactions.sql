# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
GROUP BY v.customer_id, t.transaction_id
HAVING t.transaction_id is NULL