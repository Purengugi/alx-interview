#!/usr/bin/python3
"""defines function to solves N-gueen challenge"""
import sys


def is_safe(brd, row, col, N):
    """checks whether it's safe to place a queen in the
    specified row and column of the chessboard"""
    # Check the left side of the current row
    for i in range(col):
        if brd[i] == row or brd[i] - i == row - col or brd[i] + i == row + col:
            return False
    return True


def solve_nqueens(N):
    """Initiates the solving of the N Queens problem"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N

    def solve_util(col):
        """is a recursive function that attempts to
        place queens column-wise."""
        if col == N:
            print_solution(board)
            return True

        for i in range(N):
            if is_safe(board, i, col, N):
                board[col] = i
                solve_util(col + 1)
                board[col] = -1

    def print_solution(board):
        """formats and prints the solution in the desired format"""
        solution = [[i, board[i]] for i in range(N)]
        print(solution)

    solve_util(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
