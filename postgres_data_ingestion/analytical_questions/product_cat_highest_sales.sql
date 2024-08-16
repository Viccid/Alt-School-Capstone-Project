-- Which product categories have the highest sales?
-- below query provide the product category with highest sale

SELECT product_category_name,total_sales  
FROM `altsch-captone-project.ecommerce_transformation.fct_sales_by_category`  
ORDER BY total_sales
DESC LIMIT 10


--Note highest sale: beleza_saude - 1258681.339999
        

