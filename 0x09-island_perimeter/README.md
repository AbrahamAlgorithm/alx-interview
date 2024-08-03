# Island Perimeter

## Description
This project contains a Python function that calculates the perimeter of an island in a grid. The grid is represented as a 2D list of integers, where 0 represents water and 1 represents land.

## Function Specification
The main function `island_perimeter(grid)` takes a grid as input and returns the perimeter of the island described in the grid.

### Parameters:
- `grid`: A list of list of integers where:
  - 0 represents water
  - 1 represents land

### Returns:
- An integer representing the perimeter of the island

### Constraints:
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Files
- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function
- `0-main.py`: A main file to test the function

## Usage
To use the function, import it into your Python script:

```python
island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
