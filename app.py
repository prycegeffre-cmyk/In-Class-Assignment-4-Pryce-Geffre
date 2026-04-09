import streamlit as st

st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.info("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.error("Height must be greater than 0")
