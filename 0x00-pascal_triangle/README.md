# Pascal's Triangle Project

This project involves generating Pascal's Triangle in Python. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Explanation](#explanation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Pascal's Triangle is a useful mathematical concept with applications in algebra, probability, and combinatorics. This project provides a Python function `pascal_triangle(n)` that generates the triangle up to the `n`th row.

## Requirements
- Python 3.x

## Usage
To use the `pascal_triangle` function, you need to import it into your Python script and call it with an integer `n` representing the number of rows you want to generate.

### Example
```python
from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
Output
csharp
Copy code
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
Explanation
Pascal's Triangle Structure
Start with a single 1 at the top.
Each subsequent row starts and ends with 1.
Each number inside the row is the sum of the two numbers directly above it from the previous row.
Function Implementation
Base Case: If n is 0 or less, return an empty list.
Initialize Triangle: Start with the first row [1].
Build Rows: Use a loop to create each row:
Begin and end each row with 1.
Calculate the middle values by summing the two values directly above from the previous row.
Return the Triangle: Return the list of lists representing the triangle.
Function Code
python
Copy code
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)
    
    return triangle
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
