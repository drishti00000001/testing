import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("💪 Advanced BMI Calculator")

# Sidebar Inputs
st.sidebar.header("Enter your details")
name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", 1, 120, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
height_cm = st.sidebar.number_input("Height (cm)", 50.0, 250.0, 170.0)
weight_kg = st.sidebar.number_input("Weight (kg)", 10.0, 300.0, 70.0)

# Calculate BMI
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# Display Results
st.subheader(f"Hello, {name} 👋")
st.write(f"*Age:* {age} | *Gender:* {gender}")
st.write(f"Your *BMI* is: {bmi:.2f}")

# Category interpretation
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "🔹 Eat more protein and calories.", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Normal", "✅ Keep up your healthy lifestyle!", "green"
    elif 25 <= bmi < 29.9:
        return "Overweight", "⚠ Consider regular exercise and healthier eating.", "orange"
    else:
        return "Obese", "🚨 Consult a doctor or nutritionist.", "red"

category, tip, color = interpret_bmi(bmi)
st.markdown(f"*Category:* <span style='color:{color}'>{category}</span>", unsafe_allow_html=True)
st.info(tip)

# Save results to CSV
if st.button("Save Result"):
    df = pd.DataFrame({
        "Name": [name],
        "Age": [age],
        "Gender": [gender],
        "Height_cm": [height_cm],
        "Weight_kg": [weight_kg],
        "BMI": [bmi],
        "Category": [category]
    })
    df.to_csv("bmi_results.csv", mode='a', header=False, index=False)
    st.success("✅ Result saved to bmi_results.csv")

# BMI Chart
st.subheader("📊 BMI Categories")

bmi_ranges = ["Underweight", "Normal", "Overweight", "Obese"]
bmi_values = [18.5, 24.9, 29.9, 40]

fig, ax = plt.subplots()
ax.bar(bmi_ranges, bmi_values, color=['blue', 'green', 'orange', 'red'])
ax.axhline(y=bmi, color='purple', linestyle='--', label=f"Your BMI: {bmi:.2f}")
ax.set_ylabel("BMI Value")
ax.legend()

st.pyplot(fig)