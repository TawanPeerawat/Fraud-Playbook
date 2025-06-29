
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Fraud Strategy Builder", layout="centered")
st.title("🛡️ Retail Fraud Strategy Builder")

# --- Clear Session Button ---
if st.button("🧹 Clear All"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- Step 1 ---
st.header("1. เลือกปัญหาหลัก")
st.markdown("**Retail Fraud Risk** — การทุจริตภายในธุรกิจค้าปลีก")

# --- Step 2 ---
st.header("2. เลือกประเภท Fraud หลัก")
fraud_type = st.radio("Fraud Type", ["Internal Fraud", "External Fraud"])

# --- Step 3 ---
st.subheader("เลือก Fraud Subtype")
subtypes = {
    "Internal Fraud": [
        "Inventory & Fulfillment Fraud",
        "Insider / Collusion Fraud"
    ],
    "External Fraud": [
        "Transaction Fraud",
        "Promotion & Loyalty Fraud",
        "Return & Refund Fraud",
        "Digital & Channel-Specific Fraud"
    ]
}
selected_subtype = st.selectbox("เลือก Fraud Subtype", subtypes[fraud_type])

# --- Step 4 ---
st.header("4. เลือก Use Cases ที่เกี่ยวข้อง")
use_case_options = {
    "Inventory & Fulfillment Fraud": ["Stock Audit", "Fulfillment Alerts"],
    "Insider / Collusion Fraud": ["Access Monitoring", "Role Conflict Check"],
    "Transaction Fraud": ["Slip Verification", "Transaction Monitoring"],
    "Promotion & Loyalty Fraud": ["Coupon Abuse Detection", "Fake Account Flagging"],
    "Return & Refund Fraud": ["Return Abuse", "Refund Pattern Analysis"],
    "Digital & Channel-Specific Fraud": ["Card Theft Detection", "IP Velocity Monitoring"]
}
use_case = st.selectbox("Use Cases", use_case_options.get(selected_subtype, []))

# --- Step 5 ---
st.header("5. ยืนยัน Problem Space ที่ต้องการโฟกัส")
st.markdown(f"คุณกำลังโฟกัสที่: **{selected_subtype}**")

# --- Step 6 ---
st.header("6. ระบุ Key Dimensions")
dimensions = st.multiselect("เลือก Dimensions ที่เกี่ยวข้อง", ["Customer", "Process", "Technology", "Finance"])

# --- Step 7 ---
st.header("7. เลือก Model ที่เหมาะสม")
models = st.multiselect("เลือกประเภทโมเดล", ["Analytical", "Behavioral", "Strategic", "Financial", "Process"])

# --- Step 8 ---
st.header("8. วิธีการ Visualization ที่เหมาะสม")
viz = st.selectbox("เลือก Visualization", ["Flow Diagram", "Fraud Tree", "Heatmap", "Graph Analysis"])

# --- Step 9 ---
st.header("9. ตั้งสมมติฐาน (Hypotheses)")
hypo = st.text_area("เขียน Hypotheses หรือเงื่อนไขที่คิดว่าจะทุจริต")

# --- Step 10 ---
st.header("10. ระบุ Data Sources ที่ใช้วิเคราะห์")
sources = st.multiselect("เลือกแหล่งข้อมูล", ["Transaction Data", "Customer Info", "Order Logs", "Device Fingerprint", "Promotion Logs"])

# --- Output ---
if st.button("🚀 Generate Strategy Summary"):
    st.subheader("📌 สรุปกลยุทธ์การวิเคราะห์ Fraud")
    st.markdown(f"**Fraud Type:** {fraud_type}")
    st.markdown(f"**Subtype:** {selected_subtype}")
    st.markdown(f"**Use Case:** {use_case}")
    st.markdown(f"**Dimensions:** {', '.join(dimensions)}")
    st.markdown(f"**Models:** {', '.join(models)}")
    st.markdown(f"**Visualization:** {viz}")
    st.markdown(f"**Hypothesis:** {hypo}")
    st.markdown(f"**Data Sources:** {', '.join(sources)}")
