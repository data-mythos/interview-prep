# Interview Preparation

This repository contains solutions to various coding problems commonly asked in technical interviews.

## Repository Structure
```
.
├── dsa/                    # Data Structures and Algorithms
│   ├── arrays/            # Array-based problems
│   │   ├── two_sum.py
│   │   └── buy_and_sell_stock.py
│   └── Readme.md         # DSA problems tracking
├── sql/                   # SQL Problems
│   ├── bike_last_used.sql
│   ├── admin_dept_emp_after april.sql
│   └── Readme.md         # SQL problems tracking
└── Readme.md             # Main documentation
```

## Problem Tracking
Detailed problem lists with approaches and complexity analysis:
- [DSA Problems](dsa/Readme.md)
- [SQL Problems](sql/Readme.md)

## Running the Solutions

### Python (DSA)
```bash
# Run specific solution
python dsa/arrays/two_sum.py

# Each solution includes unit tests
```

### SQL
Execute queries in your preferred SQL environment (PostgreSQL recommended)
```sql
-- Run specific query
psql -d your_database -f sql/bike_last_used.sql

-- Each solution includes sample data
```

## Testing
- DSA solutions include:
  - Unit tests with multiple test cases
  - Print statements for visualization
  - Example usage in main block

- SQL solutions include:
  - Sample data for testing
  - Alternative query versions
  - Expected outputs