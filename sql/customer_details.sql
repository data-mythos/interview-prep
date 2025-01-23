/*
Customer Details

Find the details of each customer regardless of whether the customer made an order. 
Output the customer's first name, last name, and the city along with the order details.
Sort records based on the customer's first name and the order details in ascending order.

Step-by-Step Approach to Retrieve Customer Details:

1. **Understand the Problem**:
   We need to retrieve customer information along with their order details, ensuring that customers without orders are also included in the results.

2. **Identify the Tables**:
   - `customers`: This table contains customer details such as first name, last name, and city.
   - `orders`: This table contains order details associated with customers.

3. **Use a LEFT JOIN**:
   To include all customers regardless of whether they have made an order, we will use a LEFT JOIN between the `customers` table and the `orders` table.

4. **Select Required Columns**:
   We will select the customer's first name, last name, city, and order_details.

5. **Sort the Results**:
   Finally, we will sort the results based on the customer's first name and the order details in ascending order.

SQL Query:
*/

SELECT 
    c.first_name,
    c.last_name,
    c.city,
    o.order_details
FROM 
    customers c
LEFT JOIN 
    orders o ON c.id = o.cust_id
ORDER BY 
    c.first_name ASC, 
    o.id ASC;
