import streamlit as st
import numpy as np

# Game Constants
ROWS, COLS = 8, 10  # Larger Grid
EMPTY, PLAYER1, PLAYER2 = "⚫", "🔴", "🟡"

# Initialize Game State with Error Handling
try:
    if "board" not in st.session_state:
        st.session_state.board = np.full((ROWS, COLS), EMPTY)  # Empty grid
    if "turn" not in st.session_state:
        st.session_state.turn = PLAYER1  # Red starts
    if "winner" not in st.session_state:
        st.session_state.winner = None
except Exception as e:
    st.error(f"Error initializing game state: {e}")

# Drop Piece in Column with Error Handling
def drop_piece(col):
    try:
        if st.session_state.winner:
            return  # Stop if game is over

        for row in range(ROWS-1, -1, -1):  # Check from bottom to top
            if st.session_state.board[row, col] == EMPTY:
                st.session_state.board[row, col] = st.session_state.turn
                if check_winner(row, col, st.session_state.turn):
                    st.session_state.winner = st.session_state.turn
                st.session_state.turn = PLAYER1 if st.session_state.turn == PLAYER2 else PLAYER2
                return
    except Exception as e:
        st.error(f"Error dropping piece: {e}")

# Check for Win with Error Handling
def check_winner(r, c, piece):
    try:
        board = st.session_state.board
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vertical, Horizontal, Diagonal 1, Diagonal 2

        for dr, dc in directions:
            count = 1
            for i in [1, -1]:  # Check both forward and backward
                nr, nc = r + dr * i, c + dc * i
                while 0 <= nr < ROWS and 0 <= nc < COLS and board[nr, nc] == piece:
                    count += 1
                    nr += dr * i
                    nc += dc * i
                    if count >= 4:
                        return True
        return False
    except Exception as e:
        st.error(f"Error checking winner: {e}")
        return False

# Display Title with Muhammad Mudasir's Name
st.title("🟡🔴 Connect Four (Large Grid 8x10) – by Muhammad Mudasir")
st.markdown(f"### 🎯 **Current Turn:** {st.session_state.turn}")

# Display Board
try:
    game_display = []
    for row in range(ROWS):
        game_display.append("".join(st.session_state.board[row]))
    st.markdown(f"```\n{chr(10).join(game_display)}\n```")  # Show the game grid
except Exception as e:
    st.error(f"Error displaying board: {e}")

# Column Buttons for Dropping Pieces
try:
    cols = st.columns(COLS)
    for i, col in enumerate(cols):
        if col.button(f"⬇️ {i+1}"):
            drop_piece(i)
except Exception as e:
    st.error(f"Error creating buttons: {e}")

# Winner Message
if st.session_state.winner:
    st.success(f"🏆 **{st.session_state.winner} Wins!** 🎉")

# Footer with Restart Button and Your Name
st.markdown("---")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("👨‍💻 **Developed by SABAHAT** | 🚀 Powered by Streamlit")
with col2:
    if st.button("🔄 Restart Game"):
        try:
            st.session_state.board = np.full((ROWS, COLS), EMPTY)
            st.session_state.turn = PLAYER1
            st.session_state.winner = None
        except Exception as e:
            st.error(f"Error resetting game: {e}")
