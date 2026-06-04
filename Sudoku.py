import random
import copy

# ----------------------------
# Sudoku Solver
# ----------------------------

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    nums = list(range(1, 10))
    random.shuffle(nums)

    for num in nums:
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# ----------------------------
# Generate Full Sudoku Board
# ----------------------------

def generate_complete_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)
    return board

# ----------------------------
# Create Puzzle
# ----------------------------

def create_puzzle(board, difficulty):
    puzzle = copy.deepcopy(board)

    if difficulty == "easy":
        remove = 35
    elif difficulty == "medium":
        remove = 45
    elif difficulty == "hard":
        remove = 55
    else:
        remove = 45

    removed = 0

    while removed < remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1

    return puzzle

# ----------------------------
# Print Board
# ----------------------------

def print_board(board):
    print()

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            value = board[i][j]
            print(value if value != 0 else ".", end=" ")

        print()

    print()

# ----------------------------
# Main Program
# ----------------------------

print("=" * 40)
print("      SUDOKU GENERATOR")
print("=" * 40)

difficulty = input(
    "Choose difficulty (easy/medium/hard): "
).lower()

solution_board = generate_complete_board()

puzzle_board = create_puzzle(
    solution_board,
    difficulty
)

print("\nGenerated Puzzle:")
print_board(puzzle_board)

choice = input(
    "Show solution? (y/n): "
).lower()

if choice == "y":
    print("\nSolution:")
    print_board(solution_board)

else:
    print("\nThanks for playing!")