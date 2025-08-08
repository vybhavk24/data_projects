# 🛒 Database management for a sales company

This project demonstrates SQL database design and analysis for a fictional retail company using a raw `.csv` dataset.

## 📌 Project Goals
- Convert raw sales CSV data into a normalized relational database
- Practice database design, data wrangling, and SQL analytics
- Gain experience relevant to database and data management modules in Master's programs

## 🧰 Tools Used
- SQLite (via DB Browser for SQLite)
- SQL (standard dialect)
- Git + GitHub
- VS Code

## 📂 Dataset
The dataset `retail_sales.csv` contains sales records including:
- Order ID
- Customer ID
- Product ID
- Order and Shipping dates
- Sales, Quantity, Category, Segment, etc.

---

## 🗃️ Database Design

The CSV was normalized into **4 relational tables**:

### 1. `customers`
| Column         | Type    |
|----------------|---------|
| customer_id    | TEXT PK |
| customer_name  | TEXT    |
| segment        | TEXT    |
| city           | TEXT    |
| state          | TEXT    |
| region         | TEXT    |

### 2. `orders`
| Column      | Type    |
|-------------|---------|
| order_id    | TEXT PK |
| order_date  | TEXT    |
| ship_date   | TEXT    |
| ship_mode   | TEXT    |
| customer_id | FK      |

### 3. `products`
| Column      | Type    |
|-------------|---------|
| product_id  | TEXT PK |
| product_name| TEXT    |
| category    | TEXT    |
| sub_category| TEXT    |

### 4. `order_items`
| Column      | Type    |
|-------------|---------|
| order_id    | FK      |
| product_id  | FK      |
| sales       | REAL    |
| PRIMARY KEY (order_id, product_id)

---

## 🔍 SQL Analytics

Below are some key insights derived from SQL queries:

- **Top 5 products by total sales**
- **Most sold product categories**
- **Sales by region**
- **Monthly avg sales trends**
- **Preferred shipping modes**
- **Top-performing states/cities**

> All queries and results are available in the Queries folder

---

## ✅ Learning Outcome

This project enhanced my skills in:
- Database normalization
- Writing complex SQL queries
- Using SQLite for data storage and analytics
- Structuring projects for GitHub portfolio

---

## Credits

Inspired by real-world sales data simulation and guided SQL practice.
Applying the skills i've gained through SQL for data science by UC Davis.