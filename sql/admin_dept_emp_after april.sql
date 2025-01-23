/*
Problem: Find the number of employees working in the Admin department that joined in April or later.

Approach:
1. Filter for Admin department employees
2. Filter for employees who joined in April or later (month >= 4)
3. Count the filtered results

Note: Using EXTRACT to get the month from joining_date
*/

SELECT 
    COUNT(*) as admin_count  -- Count employees meeting our criteria
FROM 
    worker
WHERE 
    department = 'Admin'  -- Filter for Admin department
    AND EXTRACT(MONTH FROM joining_date) >= 4;  -- Filter for April (month 4) or later

-- Alternative version with more details
SELECT 
    COUNT(*) as admin_count,
    STRING_AGG(first_name || ' ' || last_name, ', ') as employee_names,  -- List of employees
    STRING_AGG(joining_date::text, ', ') as join_dates  -- Their joining dates
FROM 
    worker
WHERE 
    department = 'Admin'
    AND EXTRACT(MONTH FROM joining_date) >= 4;
