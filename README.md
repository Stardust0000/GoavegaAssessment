# Cron Formatter

## Problem Statement
Given a cron expression as a single string, the task is to parse the expression and expand each time field to show the exact times at which the command will run.

---

## Understanding the Problem
A cron expression is used to schedule tasks on an operating system.

For this assignment:
- The cron expression consists of **5 time fields** followed by a **command**
- The fields are:
minute hour day-of-month month day-of-week command
- Each time field has a fixed range and may contain special characters that define how the values should be expanded.

---

## Assumptions
Based on the problem statement and example provided, the following assumptions were made.

### Supported Fields and Ranges
- Minutes: `0–59`
- Hours: `0–23`
- Day of Month: `1–31`
- Month: `1–12`
- Day of Week: `1–7`

### Supported Characters
- `*` (Asterisk): Represents all values within the field range
- `/` (Forward Slash): Step values, supported as `*/n` or `a/b`
- `,` (Comma): List of values (e.g., `1,15`)
- `-` (Dash): Range of values (e.g., `1-5`)

The input is assumed to be valid and follow the standard cron format shown in the problem description.

---

## Approach
1. Read the input cron expression as a string
2. Split the input into individual fields
3. Process each of the first five fields independently:
   - Assign the valid range based on field position
   - Expand values based on the special character used
4. Print the expanded values in a tabular format along with the command

The pattern expansion logic is kept separate from position-based rules for clarity and ease of extension.

---

## Time Complexity
The solution runs in constant time; O(n), as each cron field has a fixed and bounded range of values.  
Space complexity is also bounded by the maximum size of the expanded fields.

---

## How to Run the Program

### Prerequisites
- Python 3 installed on the system

### Steps
1. Clone the repository
2. Navigate to the project directory
3. Run the script: python cronFormatter.py
4. Enter the cron expression when prompted
Each time field has a fixed range and may contain special characters that define how the values should be expanded.

---

## Example: 
### Input
" */15 0 1,15 * 1-5 /user/bin/find "
### Ouput
minute        0 15 30 45 
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
Command       /user/bin/find