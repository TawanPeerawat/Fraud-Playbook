## 🧩 Retail Fraud Strategy Framework

### 1. ปัญหาหลัก
Retail Fraud Risk — ปัญหาการฉ้อโกงที่เกิดขึ้นในธุรกิจค้าปลีก โดยมีความหลากหลายทั้งจากพนักงานภายในและลูกค้าภายนอก

### 2. ประเภทการทุจริต (Fraud Types) และ Use Cases

#### 🔒 Internal Fraud
**1.1 Inventory & Fulfillment Fraud**
- พนักงานสลับสินค้าจริงเป็นของปลอม
- รายงาน stock ผิดจากความเป็นจริง

**1.2 Insider / Collusion Fraud**
- สมรู้ร่วมคิดกับ supplier (kickback, order ปลอม)
- แก้ไขระบบ stock หรือโปรโมชั่นเพื่อลดหลักฐาน

#### 🌐 External Fraud
**2.1 Transaction Fraud**
- ปลอมแปลง slip การโอนเงิน
- ออกใบเสร็จปลอม

**2.2 Promotion & Loyalty Fraud**
- ใช้คูปองซ้ำโดยเปลี่ยนบัญชี
- สร้างบัญชีปลอมเพื่อแลกของรางวัล

**2.3 Return & Refund Fraud**
- ส่งคืนของปลอม / กล่องเปล่า
- พนักงานอนุมัติ refund โดยไม่ตรวจสอบของจริง

**2.4 Digital & Channel-Specific Fraud**
- ใช้ข้อมูลบัตรเครดิตที่ถูกขโมย

### 3. Fraud Focus Area
ผู้ใช้สามารถเลือกปัญหาเฉพาะ (Problem Space) ที่ต้องการวิเคราะห์เพิ่มเติม เช่น “Promotion & Loyalty Fraud”

### 4. Key Dimensions
| Category     | Factors                                 |
|--------------|------------------------------------------|
| Customer     | Redemption Pattern, Fake Accounts        |
| Process      | Refund Flow, Stock Control Override      |
| Technology   | Device ID, IP Address, Email             |
| Finance      | Coupon Loss Rate, Refund Cost per Order  |

### 5. Model Selection
| Type        | Examples                       |
|-------------|--------------------------------|
| Analytical  | Fishbone, PRA Tree             |
| Behavioral  | COM-B                          |
| Strategic   | 2x2 Matrix                     |
| Financial   | Unit Economics                 |
| Process     | Design Thinking, DMAIC         |

### 6. Visualization
- Fraud Type Breakdown (bullet style)
- Risk vs Impact 2x2 Matrix
- Refund/Return Workflow Mapping

### 7. Hypotheses
- กลุ่ม fraud เดิมเปลี่ยน device/account แล้วทำพฤติกรรมเดิม
- การคืนสินค้าช่วงโปรมีแนวโน้มเป็น nominee หรือ insider
- Refund ที่อนุมัติเร็วผิดปกติมักทำโดยพนักงานกลุ่มเดียวกัน

### 8. Data Sources
| Source         | Fields                | Purpose                        |
|----------------|------------------------|--------------------------------|
| Order Logs     | Order ID, Time, Items  | วิเคราะห์ pattern              |
| Refund Records | Amount, Approver       | ตรวจ refund loop               |
| Customer       | Email, Device, IP      | ตรวจพฤติกรรม / linkage        |
| Inventory Logs | Stock Adjust, SKU      | หาเหตุผล stock ผิดปกติ       |
| Card Data      | Payment Method         | จับ transaction fraud          |

### 9. Playbook Phases
| Phase    | Task                          | Tools/Examples                |
|----------|-------------------------------|-------------------------------|
| Diagnose | แยกประเภทปัญหา, linkage map  | Stakeholder Map, PRA Tree    |
| Design   | วาง rule + behavior model     | COM-B, Risk Pattern Grouping |
| Execute  | ติดตั้งระบบ monitor           | Alert Engine, Dashboard      |
| Monitor  | Evaluate, retrain model       | KPI Dashboard, Feedback Loop |
