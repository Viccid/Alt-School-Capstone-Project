WITH sales_by_category AS (
    SELECT 
        p.product_category_name,
        SUM(oi.price) AS total_sales
    FROM 
        {{ ref('stg_products') }} p
    JOIN 
        {{ ref('stg_order_items') }} oi
    ON 
        p.product_id = oi.product_id
    GROUP BY 
        p.product_category_name
)

SELECT 
    product_category_name,
    total_sales
FROM 
    sales_by_category