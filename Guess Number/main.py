import random
import streamlit as st

st.title("🎯 Number Guessing Game - Streamlit Edition")

game_mode = st.radio("Select a Game Mode:", ["You Guess the Number", "Computer Guesses Your Number"])

if game_mode == "You Guess the Number":
    x = st.number_input("Select the range (1 to X):", min_value=10, max_value=1000, value=100, step=10)
    
    if "random_number" not in st.session_state:
        st.session_state.random_number = random.randint(1, x)
        st.session_state.guess = None
        st.session_state.feedback = ""

    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=x, step=1)

    if st.button("Submit Guess"):
        if user_guess < st.session_state.random_number:
            st.session_state.feedback = "📉 Too low! Try again."
        elif user_guess > st.session_state.random_number:
            st.session_state.feedback = "📈 Too high! Try again."
        else:
            st.session_state.feedback = f"🎉 Congrats! You guessed the number {st.session_state.random_number} correctly!"
    
    st.write(st.session_state.feedback)

elif game_mode == "Computer Guesses Your Number":
    x = st.number_input("Choose a range (1 to X):", min_value=10, max_value=1000, value=100, step=10)
    
    if "low" not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = x
        st.session_state.comp_guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.feedback = ""

    st.write(f"Computer's Guess: {st.session_state.comp_guess}")

    feedback = st.radio("Is the guess correct?", ["Too High", "Too Low", "Correct"], index=2)

    if st.button("Give Feedback"):
        if feedback == "Too High":
            st.session_state.high = st.session_state.comp_guess - 1
        elif feedback == "Too Low":
            st.session_state.low = st.session_state.comp_guess + 1
        else:
            st.session_state.feedback = f"🎉 Yay! The computer guessed your number, {st.session_state.comp_guess}, correctly!"

        if st.session_state.low <= st.session_state.high:
            st.session_state.comp_guess = random.randint(st.session_state.low, st.session_state.high)
        else:
            st.session_state.feedback = "🤔 Something went wrong. Try again!"

    st.write(st.session_state.feedback)

# Restart Button
if st.button("🔄 Restart Game"):
    st.session_state.clear()
    st.rerun()
