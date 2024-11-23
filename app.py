import streamlit as st
import math

st.title("Scientific Calculator")

# Dropdown menu for operation selection
operation = st.selectbox(
    "Select an operation:",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Square Root (√)",
        "Power (^)",
        "Sine (sin)",
        "Cosine (cos)",
        "Tangent (tan)",
        "Logarithm (log)",
    ]
)

# Input fields
if operation in ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]:
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

    if st.button("Calculate"):
        if operation == "Addition (+)":
            st.success(f"The result is: {num1 + num2}")
        elif operation == "Subtraction (-)":
            st.success(f"The result is: {num1 - num2}")
        elif operation == "Multiplication (*)":
            st.success(f"The result is: {num1 * num2}")
        elif operation == "Division (/)":
            if num2 != 0:
                st.success(f"The result is: {num1 / num2}")
            else:
                st.error("Error: Division by zero is not allowed.")

elif operation == "Square Root (√)":
    num = st.number_input("Enter the number:", format="%.2f")

    if st.button("Calculate"):
        if num >= 0:
            st.success(f"The result is: {math.sqrt(num)}")
        else:
            st.error("Error: Cannot calculate the square root of a negative number.")

elif operation == "Power (^)":
    base = st.number_input("Enter the base:", format="%.2f")
    exp = st.number_input("Enter the exponent:", format="%.2f")

    if st.button("Calculate"):
        st.success(f"The result is: {math.pow(base, exp)}")

elif operation in ["Sine (sin)", "Cosine (cos)", "Tangent (tan)", "Logarithm (log)"]:
    num = st.number_input("Enter the number (in degrees):", format="%.2f")

    if st.button("Calculate"):
        rad = math.radians(num)
        if operation == "Sine (sin)":
            st.success(f"The result is: {math.sin(rad)}")
        elif operation == "Cosine (cos)":
            st.success(f"The result is: {math.cos(rad)}")
        elif operation == "Tangent (tan)":
            st.success(f"The result is: {math.tan(rad)}")
        elif operation == "Logarithm (log)":
            if num > 0:
                st.success(f"The result is: {math.log(num)}")
            else:
                st.error("Error: Logarithm undefined for non-positive numbers.")

