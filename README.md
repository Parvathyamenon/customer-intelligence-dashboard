# Customer Intelligence Dashboard

Live dashboard:
https://Parvathyamenon.github.io/customer-intelligence-dashboard/

---

## 📌 Project Overview

This project builds an end-to-end **customer intelligence pipeline** that analyses **30,000 Amazon reviews** using Natural Language Processing (NLP) to uncover complaint trends, sentiment patterns, and business risk signals.

The system classifies reviews into complaint categories, scores sentiment, assigns severity levels, and surfaces insights using SQL and visual dashboards.

---

## 📊 Key Results

* **30,000 reviews analysed**
* **Top complaint:** Customer service issues
* **3,673 high-severity cases identified**
* **4,954 negative sentiment reviews**
* **45.5% of all complaints** linked to customer service

👉 Key insight: Customer service failures are the dominant driver of negative customer experience and high-risk cases.

---

## ⚙️ Tech Stack

* **Python** – data processing pipeline
* **pandas** – data cleaning & transformation
* **scikit-learn** – TF-IDF + Logistic Regression (classification)
* **NLTK (VADER)** – sentiment analysis
* **SQL (SQLite)** – business insight queries
* **matplotlib** – dashboard visualisation

---

## 🔄 Pipeline Architecture

1. **Data Ingestion**
   Load Amazon review dataset (30,000 rows)

2. **Sentiment Analysis**
   VADER assigns sentiment: Positive / Neutral / Negative / Very Negative

3. **Category Classification**
   TF-IDF + Logistic Regression assigns complaint categories

4. **Severity Scoring**
   Combines sentiment + rating into High / Medium / Low risk

5. **SQL Analysis**
   Extracts business insights (top complaints, risk areas, trends)

6. **Dashboard Output**
   Generates visual summary and portfolio dashboard

---

## 📈 Example Insights

* Customer service complaints dominate all other categories
* High-severity issues strongly correlate with negative sentiment
* Certain complaint types consistently produce lower star ratings
* Business risk can be prioritised using severity + volume

---

## 📂 Repository Structure

```
customer-intelligence-dashboard/
│
├── index.html              # Live dashboard (GitHub Pages)
├── classifier.py           # NLP pipeline
├── analysis.sql            # SQL insight queries
├── requirements.txt        # Dependencies
│
├── data/
│   └── sample_reviews.csv  # Small sample dataset (optional)
│
├── output/
│   └── dashboard.png       # Generated visual output
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the pipeline:

```
python classifier.py
```

3. View output:

* Dashboard image saved in `/output`
* Insights generated via SQL queries

---

## 📌 Notes

* Full dataset (30,000 reviews) not included due to size
* Sample dataset provided for demonstration
* Project built with **zero API cost**

---

## 👤 Author

**Parvathy Menon**
 Business Analyst · Data & Product Operations

GitHub: https://github.com/Parvathyamenon

---

## 💡 Resume Line

Built an NLP-powered customer intelligence pipeline analysing 30,000 Amazon reviews; identified customer service as the top complaint driver, with 3,673 high-severity cases and 4,954 negative sentiment reviews, using Python, SQL, and machine learning.

---
