import pandas as pd
import streamlit as st

# -----------------------------
# Healthcare Cost Data
# -----------------------------
data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Department": [
        "Cardiology", "Neurology", "Orthopedics", "Cardiology",
        "Pediatrics", "Neurology", "Orthopedics", "Pediatrics",
        "Cardiology", "Neurology"
    ],
    "Treatment": [
        "Heart Surgery", "Brain Scan", "Fracture Treatment",
        "Angioplasty", "Child Checkup", "MRI",
        "Bone Surgery", "Vaccination", "ECG",
        "Neurological Treatment"
    ],
    "Healthcare_Cost": [
        85000, 45000, 30000, 70000, 5000,
        40000, 55000, 3000, 8000, 60000
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Healthcare Cost Analysis Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Cost Analysis Dashboard")
st.write("Analysis of healthcare costs across departments and treatments.")

# -----------------------------
# Department Filter
# -----------------------------
department = st.selectbox(
    "Select Department",
    ["All"] + sorted(df["Department"].unique())
)

if department == "All":
    filtered_df = df
else:
    filtered_df = df[df["Department"] == department]

# -----------------------------
# Key Metrics
# -----------------------------
total_cost = filtered_df["Healthcare_Cost"].sum()
average_cost = filtered_df["Healthcare_Cost"].mean()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Healthcare Cost",
        f"₹{total_cost:,.0f}"
    )

with col2:
    st.metric(
        "Average Treatment Cost",
        f"₹{average_cost:,.0f}"
    )

# -----------------------------
# High Cost Alert
# -----------------------------
st.subheader("🚨 High Cost Alert")

high_cost = filtered_df[filtered_df["Healthcare_Cost"] >= 50000]

if len(high_cost) > 0:
    st.warning(
        f"{len(high_cost)} high-cost treatment(s) found. "
        "These treatments may require closer cost monitoring."
    )
    st.dataframe(
        high_cost[["Department", "Treatment", "Healthcare_Cost"]],
        use_container_width=True
    )
else:
    st.success("No high-cost treatment found for the selected department.")

# -----------------------------
# Data Table
# -----------------------------
st.subheader("Healthcare Cost Data")
st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# Department-wise Cost
# -----------------------------
st.subheader("Department-wise Healthcare Cost")

department_cost = (
    filtered_df.groupby("Department")["Healthcare_Cost"]
    .sum()
)

st.bar_chart(department_cost)

# -----------------------------
# Treatment-wise Cost
# -----------------------------
st.subheader("Treatment-wise Healthcare Cost")

treatment_cost = (
    filtered_df.groupby("Treatment")["Healthcare_Cost"]
    .sum()
)

st.bar_chart(treatment_cost)
