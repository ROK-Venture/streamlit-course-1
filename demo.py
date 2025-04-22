import streamlit as st
import pandas as pd

# 1. Title
st.title("Streamlit Components Demo")

# 2. Header
st.header("This is a Header")

# 3. Subheader
st.subheader("This is a Subheader")

# 4. Text
st.text("Streamlit makes it easy to create web apps for data science.")

# 5. Markdown
st.markdown("**Markdown** lets you style text with *italics*, **bold**, and [links](https://streamlit.io).")

# 6. Input Widgets
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

# 7. Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# 8. Button
if st.button("Click Me"):
    st.write("Button clicked!")

# 9. Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

# 10. Selectbox
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# 11. Bar Chart
st.subheader("Simple Bar Chart")
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
})
st.bar_chart(data, x="Category", y="Values")