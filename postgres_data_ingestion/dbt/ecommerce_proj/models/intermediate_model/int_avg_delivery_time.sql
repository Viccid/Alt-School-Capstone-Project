WITH delivery_time AS (
    SELECT 
        o.order_id,
        TIMESTAMP_DIFF(o.order_delivered_customer_date, o.order_purchase_timestamp, DAY) AS delivery_time_days
    FROM 
        {{ ref('stg_orders') }} o
)

SELECT 
    order_id,
    delivery_time_days
FROM 
    delivery_time