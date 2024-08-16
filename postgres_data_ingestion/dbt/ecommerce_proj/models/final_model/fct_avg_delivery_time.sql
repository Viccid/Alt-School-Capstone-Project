WITH delivery_time AS (
    SELECT
        o.order_id,
        DATE_DIFF(o.order_delivered_customer_date, o.order_purchase_timestamp, DAY) AS delivery_days
    FROM {{ ref('stg_orders') }} o
)

SELECT
    AVG(delivery_days) AS avg_delivery_time
FROM delivery_time