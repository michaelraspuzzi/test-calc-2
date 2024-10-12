import streamlit as st

# Title of the form
st.title("Emergency Department Assessment of Chest Pain Score (EDACS)")

# Description
st.write("Identifies chest pain patients with low risk of major adverse cardiac event.")

# Input: Age
age = st.number_input("Age", min_value=18, step=1)

# Input: Sex
sex = st.radio("Sex", ("Female", "Male"))
sex_score = 0 if sex == "Female" else 6

# Input: Diaphoresis (Yes = 3 points)
diaphoresis = st.radio("Diaphoresis (sweating)", ["No", "Yes"])
diaphoresis_score = 3 if diaphoresis == "Yes" else 0

# Input: Pain radiates to arm, shoulder, neck, or jaw (Yes = 5 points)
pain_radiates = st.radio("Pain radiates to arm, shoulder, neck, or jaw", ["No", "Yes"])
pain_radiates_score = 5 if pain_radiates == "Yes" else 0

# Input: Pain occurred or worsened with inspiration (Yes = -4 points)
pain_inspiration = st.radio("Pain occurred or worsened with inspiration", ["No", "Yes"])
pain_inspiration_score = -4 if pain_inspiration == "Yes" else 0

# Input: Pain is reproduced by palpation (Yes = -6 points)
pain_palpation = st.radio("Pain is reproduced by palpation", ["No", "Yes"])
pain_palpation_score = -6 if pain_palpation == "Yes" else 0

# Calculate total score
total_score = sex_score + diaphoresis_score + pain_radiates_score + pain_inspiration_score + pain_palpation_score

# Display the result
st.subheader("Result:")
if st.button("Calculate EDACS Score"):
    st.write(f"Your EDACS Score is: {total_score}")
    if total_score > 0:
        st.write("This indicates a higher risk of adverse cardiac event.")
    else:
        st.write("This indicates a lower risk of adverse cardiac event.")
