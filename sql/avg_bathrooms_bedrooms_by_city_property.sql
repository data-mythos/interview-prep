/*
Number Of Bathrooms And Bedrooms

Problem:
Find the average number of bathrooms and bedrooms for each city's property types.
Output the result along with the city name and the property type.

Approach:
1. Group data:
   - GROUP BY both city and property_type
   - This creates unique combinations of cities and property types

2. Calculate averages:
   - Use AVG() for both bathrooms and bedrooms
   - ROUND to 2 decimal places for cleaner output

3. Handle NULL values:
   - No special handling needed as AVG() automatically skips NULL values

4. Order results:
   - ORDER BY city, property_type
   - Makes output more organized and readable

Tables:
- airbnb_host_searches table:
  - city (text)
  - property_type (text)
  - bathrooms (bigint)
  - bedrooms (bigint)
  - ... (other columns not needed for this query)

Example Output:
city    | property_type | avg_bathrooms | avg_bedrooms
NYC     | Apartment    | 1.50          | 1.20
NYC     | House        | 2.00          | 2.50
LA      | Villa        | 2.75          | 2.80
*/

SELECT 
    city,
    property_type,
    ROUND(AVG(bathrooms)::numeric, 2) as avg_bathrooms,
    ROUND(AVG(bedrooms)::numeric, 2) as avg_bedrooms
FROM 
    airbnb_host_searches
GROUP BY 
    city,
    property_type
ORDER BY 
    city,
    property_type; 