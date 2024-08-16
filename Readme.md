# Brazilian E-Commerce ETL Project
## Overview
This project involves an end-to-end ETL (Extract, Transform, Load) process for analyzing the Brazilian E-Commerce dataset. The dataset provides detailed informations on e-commerce transactions, and the project leverages tools such as PostgreSQL, Docker, Apache Airflow, dbt, and BigQuery to process and analyze the data.

### Project Features:
* Environment : I setup a virtual environment for my windows machine.
>>> python -m venv venv

>>> venv/scripts/activate 

* Data Ingestion: I used docker in Loading raw e-commerce data from CSV files into PostgreSQL.
* ETL Orchestration: Used Apache Airflow to manage and schedule ETL workflows.
* Data Transformation: I Utilize dbt to clean, transform, and model the data.
* Data Analysis: Query and analyze the data in BigQuery to derive meaningful insights for the shareholder.

## Project Structure

Folllowing the project structure in sequence.

### Staging Models:

1. stg_orders.sql:  Raw orders data with necessary joins.
2. stg_products.sql: Raw product data.

### Intermediate Models:

1. int_sales_by_category.sql: Aggregated sales data by product category.
2. int_avg_delivery_time.sql: Calculated average delivery time for each order.
3. int_orders_by_state.sql: Count of orders per state.
### Final Models.
1. fct_sales_by_category.sql: Final sales by category model.
2. fct_avg_delivery_time.sql: Final average delivery time model.
3. fct_orders_by_state.sql: Final orders by state model.

## Steps involve in start the project:

### Setting up PostgreSQL and Docker:

-  Configure PostgreSQL using Docker and Docker Compose.
-  Load CSV data into PostgreSQL.

### Configure Apache Airflow:

* Install and configure Airflow using Docker Compose.
* Create an Airflow DAG to orchestrate the ETL process.

### Setup dbt:

* Install dbt and initialize a new dbt project.
>>> pip install dbt-bigquery

>>> dbt init " Project_name"

>>> dbt debug

>>> dbt run
* Configure dbt to connect to your BigQuery dataset.

### Create and Run Models:

* Develop staging, intermediate, and final models in dbt.
* Run dbt commands to build and test models.

## dbt Models
### Staging Models:
* stg_orders.sql: Transforms raw orders data with necessary joins.
* stg_products.sql: Transforms raw product data.

### Intermediate Models:
* int_sales_by_category.sql: Aggregates sales data by product category.
* int_avg_delivery_time.sql: Calculates the average delivery time for orders.
* int_orders_by_state.sql: Counts the number of orders per state.
### Final Models
* fct_sales_by_category.sql: Final model for sales by category.
* fct_avg_delivery_time.sql: Final model for average delivery time.
* fct_orders_by_state.sql: Final model for orders by state.

## The Analytical Question Answered:
**Top Product Categories by Sales:**


>>> SELECT * FROM `altsch-captone-project.ecommerce_transformation.fct_sales_by_category` ORDER BY total_sales DESC LIMIT 10;

**Average Delivery Time for Orders:**

>>>SELECT avg_delivery_time 
FROM `altsch-captone-project.ecommerce_transformation.fct_avg_delivery_time` 
LIMIT 10

**States with the Highest Number of Orders:**

>>> SELECT *
FROM `altsch-captone-project.ecommerce_transformation.fct_orders_by_state`
ORDER BY orders_count DESC
LIMIT 10

### Required Installations:
* Python 3: Required for dbt and other Python-based tools.
* Docker & Docker Compose: For setting up PostgreSQL and Airflow.
* VSCode: Recommended for development with Python extensions.
* Git: For version control and repository management.


### Conclusion:
This project involves multiple tools and configurations. Ensure that all dependencies are installed and properly configured. Review the dbt models and Airflow DAGs to customize them according to your specific needs.

Feel free to adapt and extend the project with additional functionality or analysis as required.



MIT License:

Copyright (c) [2024] [Idiyeli Sunday]

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.