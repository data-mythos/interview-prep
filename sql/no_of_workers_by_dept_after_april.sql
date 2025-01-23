/*
Number of Workers by Department Starting in April or Later

Problem:
Find the number of workers by department who joined in or after April.
Output the department name along with the corresponding number of workers.
Sort records based on the number of workers in descending order.

Approach:
1. Filter workers:
   - Use EXTRACT(MONTH FROM joining_date) >= 4
   - This gets only workers who joined in April (month 4) or later months

2. Group results:
   - GROUP BY department
   - This creates separate groups for each unique department

3. Count workers:
   - Use COUNT(*) for each department group
   - This counts all workers that passed the filter condition

4. Sort output:
   - ORDER BY worker_count DESC
   - This ensures departments with most workers appear first

Tables:
- worker table:
  - worker_id (bigint)
  - first_name (text)
  - last_name (text)
  - salary (bigint)
  - joining_date (date)
  - department (text)

Example:
worker_id | first_name | last_name | salary  | joining_date | department
1         | Monika     | Arora     | 100000  | 2014-02-20  | HR
2         | Niharika   | Verma     | 80000   | 2014-06-11  | Admin
...

Expected Output:
department | worker_count
Admin      | 4
HR         | 2
Account    | 1
*/

SELECT 
    department,
    COUNT(*) as worker_count
FROM 
    worker
WHERE 
    EXTRACT(MONTH FROM joining_date) >= 4
GROUP BY 
    department
ORDER BY 
    worker_count DESC;
