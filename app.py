import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fraud Strategy Framework Assistant", layout="wide")
st.title("🛡️ Retail Fraud Strategy Dashboard")
st.markdown("วิเคราะห์และติดตามความเสี่ยง Fraud แบบ IPSO Framework + AI")

# Load Gemini API
try:
    genai.configure(api_key=st.secrets["AIzaSyANjCc-PtzNhNqq27ow2SnyP1Pl96g0BJ8"])
    model = genai.GenerativeModel("gemini-2.0-pro")
except Exception as e:
    st.error(f"❌ ไม่สามารถตั้งค่า Gemini API: {e}")
    st.stop()

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Section: KPI Overview
st.subheader("📊 Fraud KPIs")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Transactions", "156,789", "+5.2%")
col2.metric("Fraud Detected", "234", "-2.1%")
col3.metric("Fraud Rate", "0.15%", "-0.3%")
col4.metric("Prevented Loss", "฿2.5M", "+12.5%")
col5.metric("Risk Score", "7.2", "-1.2")

# Section: Input Fraud Scenario
st.header("📝 ระบุปัญหาทุจริตที่พบ")
fraud_description = st.text_area("เล่าเคสปัญหาที่ต้องการให้ AI วิเคราะห์:")

# Section: Choose Dimensions
dimensions = st.multiselect("เลือกมุมวิเคราะห์:", ["Customer", "Process", "Technology", "Finance", "People"])

# Section: Analyze with Gemini
if st.button("🚀 วิเคราะห์ IPSO Framework ด้วย AI"):
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
        st.warning("⚠️ กรุณากรอกข้อมูลก่อนวิเคราะห์")

# History Section
if st.session_state.history:
    with st.expander("📚 ผลลัพธ์ก่อนหน้า"):
        for item in reversed(st.session_state.history):
            st.markdown("---")
            st.markdown(item)
