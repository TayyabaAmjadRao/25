import streamlit as st
import time

# Initialize session state for paddles, ball, and score
if "paddle_a" not in st.session_state:
    st.session_state.paddle_a = 10
if "paddle_b" not in st.session_state:
    st.session_state.paddle_b = 10
if "ball_x" not in st.session_state:
    st.session_state.ball_x = 10
if "ball_y" not in st.session_state:
    st.session_state.ball_y = 10
if "ball_dx" not in st.session_state:
    st.session_state.ball_dx = 1
if "ball_dy" not in st.session_state:
    st.session_state.ball_dy = 1
if "score_a" not in st.session_state:
    st.session_state.score_a = 0
if "score_b" not in st.session_state:
    st.session_state.score_b = 0

# UI Title
st.title("🏓 Streamlit Pong (Side Controls)")
st.markdown("👨‍💻 Created by **SABAHAT

# Layout: Buttons on Left - Game Grid in Center - Buttons on Right
left_col, game_col, right_col = st.columns([1, 4, 1])

# Left Paddle Controls (Player A)
with left_col:
    st.write("### 🟥 Player A")
    if st.button("⬆ Up", key="a_up"):
        st.session_state.paddle_a = max(1, st.session_state.paddle_a - 2)
    if st.button("⬇ Down", key="a_down"):
        st.session_state.paddle_a = min(18, st.session_state.paddle_a + 2)

# Ball Movement
st.session_state.ball_x += st.session_state.ball_dx
st.session_state.ball_y += st.session_state.ball_dy

# Collision with top/bottom
if st.session_state.ball_y <= 1 or st.session_state.ball_y >= 19:
    st.session_state.ball_dy *= -1

# Paddle collision
if (st.session_state.ball_x == 2 and abs(st.session_state.paddle_a - st.session_state.ball_y) < 3) or \
   (st.session_state.ball_x == 18 and abs(st.session_state.paddle_b - st.session_state.ball_y) < 3):
    st.session_state.ball_dx *= -1

# Scoring logic
if st.session_state.ball_x < 1:
    st.session_state.score_b += 1
    st.session_state.ball_x, st.session_state.ball_y = 10, 10

if st.session_state.ball_x > 19:
    st.session_state.score_a += 1
    st.session_state.ball_x, st.session_state.ball_y = 10, 10

# **Game Display Grid (20x20)**
with game_col:
    st.markdown("### 🏓 Pong Game")
    game_display = ["⬛" * 20]
    for i in range(1, 20):
        row = ["⬛"] * 20
        if st.session_state.paddle_a - 1 <= i <= st.session_state.paddle_a + 1:
            row[1] = "🟥"  # Paddle A
        if st.session_state.paddle_b - 1 <= i <= st.session_state.paddle_b + 1:
            row[-2] = "🟦"  # Paddle B
        if i == st.session_state.ball_y:
            row[st.session_state.ball_x] = "⚪"  # Ball
        game_display.append("".join(row))
    game_display.append("⬛" * 20)
    st.markdown(f"```\n{chr(10).join(game_display)}\n```")  # Display the game

# Right Paddle Controls (Player B)
with right_col:
    st.write("### 🟦 Player B")
    if st.button("⬆ Up", key="b_up"):
        st.session_state.paddle_b = max(1, st.session_state.paddle_b - 2)
    if st.button("⬇ Down", key="b_down"):
        st.session_state.paddle_b = min(18, st.session_state.paddle_b + 2)

# Scores
st.markdown(f"### 🎯 Score: A {st.session_state.score_a} | B {st.session_state.score_b}")

# Refresh
time.sleep(0.2)
st.rerun()
