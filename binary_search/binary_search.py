import streamlit as st
import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

st.title("Binary Search vs. Naive Search")

length = st.slider("Select list length", min_value=10, max_value=10000, value=1000)

target = st.number_input("Enter a number to search", value=0)

sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

if st.button("Search"):
    iterations = 1000  # Run multiple times for better precision
    
    start_time = time.perf_counter()
    for _ in range(iterations):
        naive_result = naive_search(sorted_list, target)
    naive_time = (time.perf_counter() - start_time) / iterations  # Average time

    start_time = time.perf_counter()
    for _ in range(iterations):
        binary_result = binary_search(sorted_list, target)
    binary_time = (time.perf_counter() - start_time) / iterations  # Average time

    st.write(f"**Naive Search Result:** {naive_result} (Time: {naive_time:.10f} seconds)")
    st.write(f"**Binary Search Result:** {binary_result} (Time: {binary_time:.10f} seconds)")

    st.write("\n**Time Comparison:**")
    st.write(f"Naive Search took {naive_time:.10f} seconds on average")
    st.write(f"Binary Search took {binary_time:.10f} seconds on average")
    st.write("Binary Search is significantly faster for large lists!")

st.write("\n---")
st.write("Made by SABAHAT")