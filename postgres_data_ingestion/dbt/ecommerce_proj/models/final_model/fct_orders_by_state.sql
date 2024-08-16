WITH orders_by_state AS (
    SELECT
        o.order_id,
        c.customer_state
    FROM {{ ref('stg_orders') }} o
    JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id
)

SELECT
    customer_state,
    COUNT(order_id) AS orders_count
FROM orders_by_state
GROUP BY customer_state