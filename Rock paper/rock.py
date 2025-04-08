import random
import streamlit as st

st.title("✊✋✌ Rock, Paper, Scissors - Streamlit Edition")

# Choices mapping
choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

# User selects an option
user_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

# Convert user choice to its shorthand
user_choice_short = {"Rock": "r", "Paper": "p", "Scissors": "s"}[user_choice]

# Computer randomly chooses
computer_choice_short = random.choice(["r", "p", "s"])
computer_choice = choices[computer_choice_short]

# Game logic
def is_win(player, opponent):
    return (player == "r" and opponent == "s") or \
           (player == "s" and opponent == "p") or \
           (player == "p" and opponent == "r")

result_message = ""
if st.button("Play"):
    st.write(f"💻 Computer chose: **{computer_choice}**")
    
    if user_choice_short == computer_choice_short:
        result_message = "It's a tie! 🤝"
    elif is_win(user_choice_short, computer_choice_short):
        result_message = "🎉 You won!"
    else:
        result_message = "😞 You lost!"

    st.subheader(result_message)

# Restart button
if st.button("🔄 Play Again"):
    st.rerun()
