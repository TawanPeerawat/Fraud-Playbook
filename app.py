import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Fraud Strategy Builder", layout="centered")
st.title("🛡️ Retail Fraud Strategy Builder")

# Initialize session state for clearing
if "clear" not in st.session_state:
    st.session_state.clear = False

def clear_all():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.clear = True

# Clear button
if st.button("🧹 Clear All"):
    clear_all()
    st.rerun()

# Step 1: Choose domain
st.header("1. เลือกปัญหาหลัก")
st.markdown("**Retail Fraud Risk** — การทุจริตภายในธุรกิจค้าปลีก")

# Step 2: Select Internal vs External
st.header("2. เลือกประเภท Fraud หลัก")
fraud_group = st.radio("Fraud Type", ["Internal Fraud", "External Fraud"], key="fraud_group")

# Step 3: Fraud Subtypes
fraud_types = {
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
selected_fraud_subtype = st.selectbox("3. เลือก Fraud Subtype", fraud_types[fraud_group], key="fraud_subtype")

# Step 4: Specific Use Cases
fraud_use_cases = {
    "Inventory & Fulfillment Fraud": [
        "พนักงานสลับสินค้าจริงเป็นของปลอม",
        "รายงาน stock ผิดจากความเป็นจริง"
    ],
    "Insider / Collusion Fraud": [
        "สมรู้ร่วมคิดกับ supplier (kickback, orderปลอม)",
        "แก้ไขระบบ stock หรือโปรโมชั่นเพื่อลดหลักฐาน"
    ],
    "Transaction Fraud": [
        "ปลอมแปลง slip การโอนเงิน",
        "ออกใบเสร็จปลอม"
    ],
    "Promotion & Loyalty Fraud": [
        "ใช้คูปองซ้ำโดยเปลี่ยนบัญชี",
        "สร้างบัญชีปลอมเพื่อแลกของรางวัล"
    ],
    "Return & Refund Fraud": [
        "ส่งคืนของปลอม / กล่องเปล่า",
        "พนักงานอนุมัติ refund โดยไม่ตรวจสอบของจริง"
    ],
    "Digital & Channel-Specific Fraud": [
        "ใช้ข้อมูลบัตรเครดิตที่ถูกขโมย"
    ]
}
st.header("4. เลือก Use Cases ที่เกี่ยวข้อง")
selected_use_cases = st.multiselect("Use Cases", fraud_use_cases.get(selected_fraud_subtype, []), key="use_cases")

# Step 5: Reconfirm Focus Area
st.header("5. ยืนยัน Problem Space ที่ต้องการโฟกัส")
st.markdown(f"คุณกำลังโฟกัสที่: **{selected_fraud_subtype}**")

# Step 6: Key Dimensions
st.header("6. ระบุ Key Dimensions")
dimensions = st.multiselect("เลือก Dimensions ที่เกี่ยวข้อง", ["Customer", "Process", "Technology", "Finance"], key="dimensions")

# Step 7: Select Models
st.header("7. เลือก Model ที่เหมาะสม")
models = st.multiselect("เลือกประเภทโมเดล", ["Analytical", "Behavioral", "Strategic", "Financial", "Process"], key="models")

# Step 8: Visualization Method
st.header("8. วิธีการ Visualization ที่เหมาะสม")
viz = st.selectbox("เลือก Visualization", ["2x2 Matrix", "Flow Diagram", "Network Graph", "Timeline", "Bar/Heatmap"], key="viz")

# Step 9: Hypotheses
st.header("9. ตั้งสมมติฐาน (Hypotheses)")
hypo = st.text_area("เขียน Hypotheses หรือเงื่อนไขที่คิดว่าน่าจะทุจริต", key="hypo")

# Step 10: Data Sources
st.header("10. ระบุ Data Sources ที่ใช้วิเคราะห์")
data_sources = st.multiselect("เลือกแหล่งข้อมูล", ["Order Logs", "Refund Records", "Customer Info", "Inventory Logs", "Card Transactions"], key="sources")

# Step 11: Generate Playbook
if st.button("🚀 สร้าง Data Strategy Playbook"):
    st.subheader("🎯 สรุป Framework & Strategy ของคุณ")
    st.write("**Fraud Group:**", fraud_group)
    st.write("**Subtype:**", selected_fraud_subtype)
    st.write("**Use Cases:**", ", ".join(selected_use_cases))
    st.write("**Key Dimensions:**", ", ".join(dimensions))
    st.write("**Model Types:**", ", ".join(models))
    st.write("**Visualization:**", viz)
    st.write("**Hypothesis:**", hypo)
    st.write("**Data Sources:**", ", ".join(data_sources))

    with st.expander("📘 ดู Playbook Summary"):
        try:
            with open("framework.md", "r", encoding="utf-8") as f:
                st.markdown(f.read())
        except FileNotFoundError:
            st.warning("⚠️ ไม่พบไฟล์ framework.md กรุณาตรวจสอบว่าอยู่ใน repo เดียวกันกับ app.py")
