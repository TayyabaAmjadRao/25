import streamlit as st
import time
import random

# Grid Size
GRID_SIZE = 20

# Initialize Game State
if "snake" not in st.session_state:
    st.session_state.snake = [(10, 10), (9, 10), (8, 10)]  # Initial snake body
if "direction" not in st.session_state:
    st.session_state.direction = "RIGHT"
if "food" not in st.session_state:
    st.session_state.food = (random.randint(1, GRID_SIZE - 2), random.randint(1, GRID_SIZE - 2))
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Move Snake
def move_snake():
    if st.session_state.game_over:
        return

    head_x, head_y = st.session_state.snake[0]

    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Collision Detection
    if (
        head_x < 0 or head_x >= GRID_SIZE or
        head_y < 0 or head_y >= GRID_SIZE or
        new_head in st.session_state.snake
    ):
        st.session_state.game_over = True
        return

    # Add new head
    st.session_state.snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (
            random.randint(1, GRID_SIZE - 2),
            random.randint(1, GRID_SIZE - 2),
        )
    else:
        st.session_state.snake.pop()  # Remove last part if no food eaten

# UI Layout
st.title("🐍 Streamlit Snake Game")
st.markdown(f"### 🎯 Score: {st.session_state.score}")

# **Game Grid (20x20)**
game_display = ["⬛" * GRID_SIZE]
for i in range(1, GRID_SIZE):
    row = ["⬛"] * GRID_SIZE
    if st.session_state.food == (i, st.session_state.food[1]):
        row[st.session_state.food[1]] = "🍎"
    for x, y in st.session_state.snake:
        if i == y:
            row[x] = "🟩"
    game_display.append("".join(row))
game_display.append("⬛" * GRID_SIZE)

st.markdown(f"```\n{chr(10).join(game_display)}\n```")  # Display the game

# Controls for movement (side buttons)
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")  # Empty space for alignment
    if st.button("⬅ Left"):
        if st.session_state.direction != "RIGHT":
            st.session_state.direction = "LEFT"

with col2:
    if st.button("⬆ Up"):
        if st.session_state.direction != "DOWN":
            st.session_state.direction = "UP"
    st.write("")  # Empty space for alignment
    if st.button("⬇ Down"):
        if st.session_state.direction != "UP":
            st.session_state.direction = "DOWN"

with col3:
    st.write("")  # Empty space for alignment
    if st.button("➡ Right"):
        if st.session_state.direction != "LEFT":
            st.session_state.direction = "RIGHT"

# Game Over Message
if st.session_state.game_over:
    st.error("💀 Game Over! Refresh the page to restart.")

# Move Snake Automatically
time.sleep(0.2)
move_snake()
st.rerun()
