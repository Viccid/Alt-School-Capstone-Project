-- Which states have the highest number of orders?
-- below query shows the state with highest orders.

SELECT *
FROM `altsch-captone-project.ecommerce_transformation.fct_orders_by_state`
ORDER BY orders_count DESC
LIMIT 10

-- Note: SP state has highest order - 41746