import streamlit as st

# Streamlit UI
st.title("🎭 Mad Libs Game - Streamlit Edition")
st.write("Fill in the blanks and create your own funny story! 🎉")

# User inputs
adj = st.text_input("Adjective:")
verb1 = st.text_input("Verb:")
verb2 = st.text_input("Another Verb:")
famous_person = st.text_input("Famous Person:")

# Generate Mad Libs story
if st.button("Generate Mad Lib"):
    if adj and verb1 and verb2 and famous_person:
        madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
        
        st.subheader("📜 Your Mad Lib Story:")
        st.write(madlib)
    else:
        st.warning("⚠️ Please fill in all the fields!")

# Restart button
if st.button("🔄 Generate Again"):
    st.session_state.clear()
    st.rerun()
