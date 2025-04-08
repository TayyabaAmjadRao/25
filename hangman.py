import random
import string
import streamlit as st
from words import words
from hangman_visual import lives_visual_dict

# Function to get a valid word
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# Initialize session state variables
if "word" not in st.session_state:
    st.session_state.word = get_valid_word(words)
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 7
    st.session_state.game_over = False

# Streamlit UI
st.title("🎩 Hangman Game - Streamlit Edition")
st.write("Guess the word letter by letter before you run out of lives!")

# Display lives and used letters
st.subheader(f"Lives Remaining: {st.session_state.lives}")
st.code(lives_visual_dict.get(st.session_state.lives, "💀 Game Over!"), language="python")  
st.write(f"Used Letters: {' '.join(sorted(st.session_state.used_letters)) if st.session_state.used_letters else 'None'}")

# Display the current word with blanks
word_display = [letter if letter in st.session_state.used_letters else "_" for letter in st.session_state.word]
st.subheader("Word: " + " ".join(word_display))

# User input for guessing
user_input = st.text_input("Guess a letter:", max_chars=1).strip().upper()

# Error messages list
error_msg = ""

# Process guess with proper validation
if st.button("Submit Guess") and not st.session_state.game_over:
    if not user_input:
        error_msg = "⚠️ Please enter a letter!"
    elif len(user_input) != 1 or user_input not in string.ascii_uppercase:
        error_msg = "⚠️ Invalid input! Please enter a single letter (A-Z)."
    elif user_input in st.session_state.used_letters:
        error_msg = f"⚠️ You already guessed '{user_input}'!"
    else:
        # Valid guess
        st.session_state.used_letters.add(user_input)
        if user_input in st.session_state.word_letters:
            st.session_state.word_letters.remove(user_input)
        else:
            st.session_state.lives -= 1
            st.warning(f"❌ '{user_input}' is not in the word!")

        st.rerun()  # Refresh the UI after processing the guess

# Display error message if any
if error_msg:
    st.error(error_msg)

# Check for win/lose conditions
if st.session_state.lives == 0:
    st.session_state.game_over = True
    st.error(f"💀 Game Over! The word was **{st.session_state.word}**")

elif not st.session_state.word_letters:
    st.session_state.game_over = True
    st.success(f"🎉 Congratulations! You guessed the word **{st.session_state.word}**")

# Restart button with alert
if st.session_state.game_over:
    if st.button("🔄 Restart Game"):
        st.toast("Restarting the game...")  # Alert message before restarting
        st.session_state.clear()  # Clear session state
        st.rerun()  # Refresh the app
