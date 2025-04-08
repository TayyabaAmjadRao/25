import streamlit as st
import time

# Set up the Streamlit app
st.title("⏳ Countdown Timer with Stop & Resume")

# Initialize session state variables safely
if "running" not in st.session_state:
    st.session_state.running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = 0
if "paused_at" not in st.session_state:
    st.session_state.paused_at = None
if "initial_time" not in st.session_state:
    st.session_state.initial_time = 10  # Default countdown time

# Input field always visible
seconds = st.number_input("Enter countdown time (seconds):", min_value=1, step=1, value=st.session_state.initial_time)

# Buttons for controlling the timer
col1, col2, col3, col4 = st.columns(4)
start_btn = col1.button("▶ Start")
stop_btn = col2.button("⏹ Stop")
resume_btn = col3.button("⏳ Resume")
clear_btn = col4.button("🔄 Clear")

# Handle Start button safely
if start_btn:
    try:
        st.session_state.time_left = int(seconds)
        st.session_state.initial_time = int(seconds)  # Store initial value for resetting
        st.session_state.running = True
        st.session_state.start_time = time.time()
        st.session_state.paused_at = None  # Reset pause tracking
    except Exception as e:
        st.error(f"⚠ Failed to start the timer: {e}")

# Handle Stop button safely
if stop_btn and st.session_state.running:
    try:
        elapsed_time = time.time() - st.session_state.start_time  # Time passed since start
        st.session_state.time_left = max(0, st.session_state.time_left - int(elapsed_time))  # Update remaining time
        st.session_state.running = False
        st.session_state.paused_at = st.session_state.time_left  # Store paused time
    except Exception as e:
        st.error(f"⚠ Error stopping the timer: {e}")

# Handle Resume button safely
if resume_btn and st.session_state.paused_at is not None:
    try:
        st.session_state.running = True
        st.session_state.start_time = time.time()  # Set new start time
        st.session_state.time_left = st.session_state.paused_at  # Resume from paused time
        st.session_state.paused_at = None  # Clear paused state
    except Exception as e:
        st.error(f"⚠ Error resuming the timer: {e}")

# Handle Clear button (resets everything)
if clear_btn:
    st.session_state.running = False
    st.session_state.time_left = 0
    st.session_state.paused_at = None
    st.session_state.initial_time = 10  # Reset input field
    st.rerun()  # FIXED: Use st.rerun() instead of st.experimental_rerun()

# Countdown logic with error handling
if st.session_state.running and st.session_state.time_left > 0:
    countdown_placeholder = st.empty()

    while st.session_state.time_left > 0 and st.session_state.running:
        try:
            elapsed_time = int(time.time() - st.session_state.start_time)
            remaining_time = max(0, st.session_state.time_left - elapsed_time)

            mins, secs = divmod(remaining_time, 60)
            countdown_placeholder.subheader(f"🕒 {mins:02}:{secs:02}")

            if remaining_time == 0:
                st.success("⏰ Time's Up!")
                st.session_state.running = False
                break

            time.sleep(1)
            st.rerun()  # FIXED: Use st.rerun() instead of st.experimental_rerun()
        except Exception as e:
            st.error(f"⚠ Countdown error: {e}")
            break

# Display frozen time if stopped
if not st.session_state.running and st.session_state.paused_at is not None:
    mins, secs = divmod(st.session_state.paused_at, 60)
    st.subheader(f"🕒 {mins:02}:{secs:02} (Paused)")

# Footer with your name
st.markdown("---")
st.markdown("💻 **Developed by SABAHAT** 🎨")
