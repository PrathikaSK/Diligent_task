SELECT
    c.customer_id,
    c.name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COALESCE(SUM(p.amount), 0) AS total_amount_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
LEFT JOIN payments AS p ON o.order_id = p.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_amount_spent DESC;

