import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
grid_rows, grid_cols = 20, 10
shapes = [
    np.array([[1, 1, 0], [0, 1, 1]]),  # S shape
    np.array([[0, 1, 1], [1, 1, 0]]),  # Z shape
    np.array([[1, 1, 1, 1]]),  # I shape
    np.array([[1, 1], [1, 1]]),  # O shape
    np.array([[1, 0, 0], [1, 1, 1]]),  # J shape
    np.array([[0, 0, 1], [1, 1, 1]]),  # L shape
    np.array([[0, 1, 0], [1, 1, 1]]),  # T shape
]

def init_game():
    st.session_state.grid = np.zeros((grid_rows, grid_cols), dtype=int)
    st.session_state.current_piece = random.choice(shapes)
    st.session_state.piece_x, st.session_state.piece_y = 4, 0
    st.session_state.game_over = False

def draw_grid():
    grid_copy = st.session_state.grid.copy()
    shape = st.session_state.current_piece
    px, py = st.session_state.piece_x, st.session_state.piece_y
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and 0 <= px + j < grid_cols and 0 <= py + i < grid_rows:
                grid_copy[py + i][px + j] = 1
    fig, ax = plt.subplots()
    ax.imshow(grid_copy, cmap="gray_r")
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)

def is_valid_position(px, py, shape):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                x, y = px + j, py + i
                if x < 0 or x >= grid_cols or y >= grid_rows or st.session_state.grid[y][x]:
                    return False
    return True

def move_piece(dx, dy):
    if not st.session_state.game_over:
        new_x, new_y = st.session_state.piece_x + dx, st.session_state.piece_y + dy
        if is_valid_position(new_x, new_y, st.session_state.current_piece):
            st.session_state.piece_x, st.session_state.piece_y = new_x, new_y

def rotate_piece():
    rotated_piece = np.rot90(st.session_state.current_piece)
    if is_valid_position(st.session_state.piece_x, st.session_state.piece_y, rotated_piece):
        st.session_state.current_piece = rotated_piece

def drop_piece():
    while is_valid_position(st.session_state.piece_x, st.session_state.piece_y + 1, st.session_state.current_piece):
        st.session_state.piece_y += 1
    lock_piece()

def lock_piece():
    shape = st.session_state.current_piece
    px, py = st.session_state.piece_x, st.session_state.piece_y
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and 0 <= px + j < grid_cols and 0 <= py + i < grid_rows:
                st.session_state.grid[py + i][px + j] = 1
    clear_rows()
    spawn_new_piece()

def clear_rows():
    new_grid = [row for row in st.session_state.grid if not all(row)]
    while len(new_grid) < grid_rows:
        new_grid.insert(0, [0] * grid_cols)
    st.session_state.grid = np.array(new_grid)

def spawn_new_piece():
    new_piece = random.choice(shapes)
    if is_valid_position(4, 0, new_piece):
        st.session_state.current_piece = new_piece
        st.session_state.piece_x, st.session_state.piece_y = 4, 0
    else:
        st.session_state.game_over = True

def restart_game():
    init_game()

if 'grid' not in st.session_state:
    init_game()

st.title("Tetris in Streamlit")

draw_grid()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Left"):
        move_piece(-1, 0)
with col2:
    if st.button("Rotate"):
        rotate_piece()
with col3:
    if st.button("Right"):
        move_piece(1, 0)
if st.button("Drop"):
    drop_piece()
if st.session_state.game_over:
    st.error("Game Over! Click Restart to play again.")
    if st.button("Restart Game"):
        restart_game()

st.markdown("---")
st.markdown("### Developed by SABAHAT")
