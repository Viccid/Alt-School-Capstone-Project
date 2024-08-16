SELECT 
    product_id,
    product_category_name
FROM 
    {{ source('ecommerce_data','olist_products_dataset') }}