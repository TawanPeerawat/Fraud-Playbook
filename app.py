# สร้างไฟล์ใหม่ที่ปรับเปลี่ยนเป็น Fraud Framework Assistant โดยใช้แนวทาง Chapter 5 - MADT7104
fraud_framework_app_code = """
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fraud Framework Assistant", layout="wide")
st.title("🔍 Fraud Strategy Framework Assistant")
st.markdown("AI จะช่วยวิเคราะห์ปัญหาทุจริตจาก Playbook และออกแบบแนวทางกลยุทธ์ โดยใช้แนวคิดจาก Chapter 5 - MADT7104")

# Load Gemini API Key
try:
    genai.configure(api_key=st.secrets["AIzaSyANjCc-PtzNhNqq27ow2SnyP1Pl96g0BJ8
 "])
    model = genai.GenerativeModel("gemini-2.0-pro")
except Exception as e:
    st.error(f"❌ ไม่สามารถตั้งค่า Gemini API: {e}")
    st.stop()

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Section: Input Problem Description
st.header("1️⃣ ระบุปัญหาจาก Fraud Playbook")
fraud_description = st.text_area("📝 ป้อนข้อความอธิบายปัญหาทุจริต (จาก Playbook, Observation หรือ Customer Painpoint)")

# Section: Select Focus Dimension
st.header("2️⃣ ระบุ Focus Dimensions ตามแนวทาง MADT7104")
dimensions = st.multiselect(
    "เลือกมุมที่เกี่ยวข้องในการวิเคราะห์",
    ["Customer", "Process", "Technology", "Finance", "People"]
)

# Section: Generate IPSO Strategy
if st.button("🚀 Generate IPSO Framework Summary"):
    if fraud_description:
        with st.spinner("AI กำลังวิเคราะห์และออกแบบ Framework..."):
            ipso_prompt = f'''
You are a strategy consultant trained in MADT7104 - Chapter 5 (Designing with Data Technologies).
Your job is to help identify IPSO elements (Input, Process, Storage, Output) for a fraud-related case.

Fraud Description:
{fraud_description}

Selected Dimensions: {", ".join(dimensions)}

Please respond in Thai language and follow this structure:
- 🎯 Problem Summary:
- 📥 Input:
- ⚙️ Process:
- 🗂 Storage:
- 📤 Output:
- 🧠 Suggestion (เชิงกลยุทธ์):
            '''
            try:
                response = model.generate_content(ipso_prompt)
                summary = response.text
                st.markdown(summary)
                st.session_state.history.append(summary)
            except Exception as e:
                st.error(f"⚠️ Error from Gemini: {e}")
    else:
        st.warning("⚠️ กรุณาใส่ข้อมูลคำอธิบายปัญหา")

# Section: History
if st.session_state.history:
    with st.expander("📚 ดูสรุปที่เคยวิเคราะห์"):
        for item in st.session_state.history[::-1]:
            st.markdown("---")
            st.markdown(item)
"""

# Save to file
fraud_app_path = "/mnt/data/fraud_framework_ai_assistant.py"
with open(fraud_app_path, "w", encoding="utf-8") as f:
    f.write(fraud_framework_app_code)

fraud_app_path
