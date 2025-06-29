## 🧩 Retail Fraud Detection – Full Framework Summary

### 1. Problem Space
Retail Fraud Detection — focused on transaction, return, inventory, and loyalty frauds in both internal and external forms.

### 2. Key Dimensions
| Dimension     | Factors                                           |
|---------------|---------------------------------------------------|
| Customer      | Repeat returns, fake accounts, nominee behavior  |
| Process       | Manual refund loop, override abuse, stock issues |
| Technology    | IP/device/email/shipping overlap, session links  |
| Finance       | Promo loss, refund %, fraud cost per order       |

### 3. Selected Models
| Type       | Model              | Purpose                       |
|------------|--------------------|-------------------------------|
| Analytical | Fishbone, PRA Tree | Identify root cause           |
| Behavioral | COM-B              | Understand fraud motivation   |
| Strategic  | 2x2 Matrix         | Prioritize by risk/impact     |
| Financial  | Unit Economics     | Quantify cost per event/order |
| Process    | Design Thinking    | Redesign detection process    |

### 4. Visualization
- ✅ Problem Decomposition Diagram
- ✅ 2x2 Matrix (Impact vs Risk)
- ✅ Fraud Network Flow
- ✅ Refund Loop Process Map

### 5. Hypotheses
- Users with similar emails/devices & same address may form a fraud ring
- Refunds during flash sales are prone to nominee insider abuse
- Repeat manual refunds by same employee suggest internal fraud risk

### 6. Data Sources
| Source         | Fields                          | Purpose                  |
|----------------|----------------------------------|--------------------------|
| Transactions   | Order ID, Timestamp              | Behavior pattern         |
| Fulfillment    | Stock log, Action by staff       | Insider or process gap   |
| Customer Data  | Email, IP, Device ID             | Fraud network detection  |
| Refund Records | Refund Reason, Approver          | Spot manipulation abuse  |
| Logs           | Alerts, Suspicious actions       | Monitor model accuracy   |

### 7. Playbook Phases
| Phase     | Action                     | Toolset                        |
|-----------|----------------------------|--------------------------------|
| Diagnose  | Map linkage + actors       | Stakeholder Map, PRA Tree     |
| Design    | Rule + ML hybrid plan      | Causal Loop, Behavior Model   |
| Execute   | Deploy detection pipeline  | Streaming Rules, Dashboards   |
| Monitor   | Track + retrain alerts     | KPI Reports, Alert Tuning     |
