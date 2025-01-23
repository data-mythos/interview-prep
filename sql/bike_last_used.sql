/*
Problem: Find the last time each bike was in use
- Output bike number and date-timestamp of bike's last use (return time)
- Order by most recently used bikes
- Using end_time as the return time of the bike

Approach:
1. Group by bike_number to get data for each bike
2. Use MAX(end_time) to get the latest return time
3. Order by end_time in descending order for most recent first
*/

-- Main query to find last usage of each bike
SELECT 
    bike_number,
    MAX(end_time) as last_used_time  -- Get the most recent end_time for each bike
FROM 
    dc_bikeshare_q1_2012
GROUP BY 
    bike_number  -- Group results by bike to get one row per bike
ORDER BY 
    last_used_time DESC;  -- Sort by most recent first

-- Alternative version with additional usage information
SELECT 
    bike_number,
    MAX(end_time) as last_used_time,
    end_station as last_station,  -- Shows where the bike was last parked
    COUNT(*) as total_trips  -- Shows how many times the bike was used
FROM 
    dc_bikeshare_q1_2012
GROUP BY 
    bike_number,end_station
ORDER BY 
    last_used_time DESC;

/*
Note: 
- First query provides the minimal required information
- Second query adds context about usage patterns
- Both queries will show bikes ordered from most recently used to least recently used
- Results can be limited using LIMIT if needed
*/
