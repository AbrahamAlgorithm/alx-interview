#!/usr/bin/python3
'''
N queen Algorithm problem
'''
import sys


board = []
num = 0
col = set()
diag1 = set()
diag2 = set()
result = []


def main():
    '''
    main function to run the program
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    global num
    num = sys.argv[1]
    try:
        num = int(num)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
    global board
    board = [["."] * num for i in range(num)]
    play(0)
    for r in result:
        output = []
        for row in r:
            row_pos = r.index(row)
            col_pos = list(row).index("Q")
            final = [row_pos, col_pos]
            output.append(final)
        print((output))


def play(row):
    '''
    This is the function that does the backtracing part'''
    if row == num:
        board2 = ["".join(r) for r in board]
        result.append(board2)
        return
    for i in range(num):
        if i in col or (row + i) in diag1 or (row - i) in diag2:
            continue

        col.add(i)
        diag1.add(row + i)
        diag2.add(row - i)
        board[row][i] = 'Q'

        play(row + 1)

        col.remove(i)
        diag1.remove(row + i)
        diag2.remove(row - i)
        board[row][i] = '.'


if __name__ == "__main__":
    '''
    run if its not imported
    '''
    main()
