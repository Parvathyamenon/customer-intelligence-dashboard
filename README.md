# 🚀 Customer Intelligence Dashboard

🔗 **Live Demo**
https://Parvathyamenon.github.io/customer-intelligence-dashboard/

---

## 📌 Overview

This project builds a full **customer intelligence pipeline** that analyses **30,000 Amazon product reviews** using Natural Language Processing (NLP) to identify:

* Complaint categories
* Customer sentiment
* High-risk issues
* Business impact drivers

The output is a **decision-ready dashboard** that translates unstructured text into actionable insights.

---

## 📊 Key Business Impact

| Metric                     | Value                       |
| -------------------------- | --------------------------- |
| Reviews analysed           | **30,000**                  |
| Top complaint              | **Customer service issues** |
| High-severity cases        | **3,673**                   |
| Negative sentiment reviews | **4,954**                   |
| Customer service share     | **45.5% of complaints**     |

> 💡 **Insight:** Customer service failures are the dominant driver of dissatisfaction and high-risk customer experience issues.

---

## 🧠 Problem Statement

Customer feedback is often:

* Unstructured (text-heavy)
* Difficult to quantify
* Hard to prioritise

👉 This project solves that by converting raw reviews into:

* Structured categories
* Measurable sentiment
* Actionable risk signals

---

## ⚙️ Tech Stack

| Layer            | Tools                                         |
| ---------------- | --------------------------------------------- |
| Data Processing  | `pandas`                                      |
| NLP              | `NLTK (VADER)`                                |
| Machine Learning | `scikit-learn (TF-IDF + Logistic Regression)` |
| Visualisation    | `matplotlib`                                  |
| Query Layer      | `SQL (SQLite)`                                |
| Deployment       | `GitHub Pages`                                |

---

## 🔄 Pipeline Architecture

```text
Raw Reviews → Sentiment Analysis → Category Classification → Severity Scoring → SQL Analysis → Dashboard
```

### Steps:

1. **Data Ingestion**
   Load 30,000 Amazon reviews

2. **Sentiment Analysis**
   VADER assigns sentiment polarity

3. **Category Classification**
   TF-IDF + Logistic Regression model

4. **Severity Scoring**
   Combines sentiment + rating

5. **SQL Analysis**
   Extracts business insights

6. **Dashboard Generation**
   Visual output for decision-making

---

## 📈 Key Insights

* **Customer service complaints dominate (45.5%)**
* High-severity issues strongly align with negative sentiment
* Complaint categories directly impact star ratings
* Business risk can be prioritised using severity + volume

---

## 🧾 Sample SQL Insight

```sql
SELECT
  ai_category,
  COUNT(*) AS volume,
  SUM(CASE WHEN ai_severity = 'High' THEN 1 ELSE 0 END) AS high_risk
FROM classified_reviews
GROUP BY ai_category
ORDER BY high_risk DESC;
```

---

## 📂 Repository Structure

```text
customer-intelligence-dashboard/
│
├── index.html              # Live dashboard
├── classifier.py           # NLP pipeline
├── analysis.sql            # SQL queries
├── requirements.txt        # Dependencies
│
├── data/
│   └── sample_reviews.csv
│
├── output/
│   └── dashboard.png
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python classifier.py
```

Outputs:

* Classified dataset
* Dashboard visual (`output/dashboard.png`)
* SQL insights

---

## 📌 Design Decisions

* Used **VADER** for fast, interpretable sentiment scoring
* Chose **TF-IDF + Logistic Regression** for explainability over deep models
* Combined sentiment + ratings for **business-aligned severity scoring**
* Used SQL layer for **analyst-style querying**

---

## 🚧 Limitations

* Rule-based sentiment (not context-aware like transformers)
* No real-time data pipeline
* Static dashboard (HTML-based)

---

## 🔮 Future Improvements

* Replace with **BERT-based classifier**
* Add **interactive dashboard (Streamlit / Power BI)**
* Deploy as API
* Automate data ingestion

---

## 👤 Author

**Parvathy Menon**
Senior Business Analyst · Data & Product Operations

🔗 GitHub: https://github.com/Parvathyamenon

---

## 💼 Resume Highlight

> Built an NLP-powered customer intelligence pipeline analysing 30,000 Amazon reviews; identified customer service as the top complaint driver, with 3,673 high-severity cases and 4,954 negative sentiment reviews using Python, SQL, and machine learning.

---

## ⭐ Why This Project Matters

This project demonstrates:

* End-to-end data pipeline design
* NLP + machine learning application
* SQL-based business analysis
* Data storytelling & visualisation

👉 Bridging the gap between **data science and business decision-making**

---
