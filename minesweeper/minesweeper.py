import streamlit as st
import random
import numpy as np

# Game Settings
GRID_SIZE = 8  # 8x8 Board
NUM_BOMBS = 10

def initialize_game():
    """Initialize the game board and place bombs."""
    board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)  # Empty grid
    bombs = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_BOMBS)  # Random bomb locations
    for bomb in bombs:
        r, c = divmod(bomb, GRID_SIZE)
        board[r, c] = -1  # Mark bombs with -1
    
    # Calculate numbers around bombs
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r, c] == -1:
                continue
            board[r, c] = sum(
                board[nr, nc] == -1
                for nr in range(max(0, r - 1), min(GRID_SIZE, r + 2))
                for nc in range(max(0, c - 1), min(GRID_SIZE, c + 2))
            )

    return board

# Initialize Session State
if "board" not in st.session_state:
    st.session_state.board = initialize_game()
    st.session_state.revealed = np.full((GRID_SIZE, GRID_SIZE), False)  # Track revealed cells
    st.session_state.game_over = False
    st.session_state.win = False

# Helper Functions
def reveal_cell(row, col):
    """Reveals a cell and recursively reveals adjacent empty cells."""
    if st.session_state.revealed[row, col] or st.session_state.game_over:
        return

    st.session_state.revealed[row, col] = True

    if st.session_state.board[row, col] == -1:  # If bomb, game over
        st.session_state.game_over = True
        return

    if st.session_state.board[row, col] == 0:  # Auto-reveal empty neighbors
        for nr in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
            for nc in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
                if not st.session_state.revealed[nr, nc]:
                    reveal_cell(nr, nc)

    check_win()

def check_win():
    """Check if all non-bomb cells are revealed."""
    total_cells = GRID_SIZE * GRID_SIZE
    revealed_count = np.count_nonzero(st.session_state.revealed)
    if revealed_count == total_cells - NUM_BOMBS:
        st.session_state.win = True
        st.session_state.game_over = True

def restart_game():
    """Reset the game."""
    st.session_state.board = initialize_game()
    st.session_state.revealed = np.full((GRID_SIZE, GRID_SIZE), False)
    st.session_state.game_over = False
    st.session_state.win = False
    st.rerun()

# UI Layout
st.title("🕵️ Minesweeper in Streamlit 🎮")
st.markdown("Click a tile to reveal it. Avoid bombs! 💣")

# Display Board
cols = st.columns(GRID_SIZE)
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        cell_value = st.session_state.board[row, col]
        is_revealed = st.session_state.revealed[row, col]

        # Button or revealed value
        if is_revealed:
            if cell_value == -1:
                display_value = "💣"
            elif cell_value == 0:
                display_value = "⬜"
            else:
                display_value = str(cell_value)
        else:
            display_value = "🟦"

        with cols[col]:  # Organize in grid format
            if not is_revealed and not st.session_state.game_over:
                if st.button(" ", key=f"{row}-{col}", use_container_width=True):
                    reveal_cell(row, col)
                    st.rerun()
            else:
                st.write(f"**{display_value}**")

# Game Status
if st.session_state.game_over:
    if st.session_state.win:
        st.success("🎉 Congratulations! You won!")
    else:
        st.error("💥 Game Over! You hit a bomb.")

# Restart Button
st.button("🔄 Restart Game", on_click=restart_game, use_container_width=True)
