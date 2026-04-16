# classifier.py — fixed output path version

import pandas as pd
import matplotlib.pyplot as plt
import nltk, os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ── NLTK Setup ─────────────────────────────────────────────
nltk.download("vader_lexicon", quiet=True)
vader = SentimentIntensityAnalyzer()

# ── DEFINE BASE PATH (🔥 THIS IS THE FIX) ───────────────────
BASE_DIR = r"C:\Users\PARVATHY\Desktop\projects\customer-intelligence"
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Saving files to:", OUTPUT_DIR)

# ── Load data ──────────────────────────────────────────────
df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "amazon_reviews_multilingual_US_v1_00.tsv"),
    sep="\t",
    on_bad_lines="skip"
).head(30000).copy()

df = df.dropna(subset=["review_body"])
print(f"Loaded {len(df):,} reviews")

# ── Sentiment (VADER) ──────────────────────────────────────
def get_sentiment(text):
    c = vader.polarity_scores(str(text))["compound"]
    if c >= 0.5:
        return "Positive"
    elif c >= 0.05:
        return "Neutral"
    elif c >= -0.5:
        return "Negative"
    else:
        return "Very Negative"

df["ai_sentiment"] = df["review_body"].apply(get_sentiment)

# ── Category (ML + rules) ──────────────────────────────────
RULES = {
    "product defect or quality issue": ["broken","defect","damage","quality","stopped working","faulty"],
    "delivery or shipping problem": ["shipping","deliver","late","arrived","package","days"],
    "return or refund request": ["refund","return","money back","credit","exchange"],
    "billing or payment issue": ["charged","bill","price","fee","payment","overcharged"],
    "customer service complaint": ["support","service","representative","help","response","rude"],
    "feature request or product suggestion": ["wish","would be better","suggest","improve","add"],
    "positive experience or praise": ["great","love","excellent","perfect","amazing","happy"],
    "account or access issue": ["login","account","password","access","locked"],
}

def keyword_label(text):
    text = str(text).lower()
    for cat, keywords in RULES.items():
        if any(w in text for w in keywords):
            return cat
    return "customer service complaint"

df["seed_label"] = df["review_body"].apply(keyword_label)

print("Training TF-IDF + Logistic Regression classifier...")
vec = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X = vec.fit_transform(df["review_body"].astype(str))
y = df["seed_label"]

clf = LogisticRegression(max_iter=1000)
clf.fit(X, y)

df["ai_category"] = clf.predict(X)

# ── Severity ───────────────────────────────────────────────
def get_severity(row):
    sent, stars = row["ai_sentiment"], row.get("star_rating", 3)
    try:
        stars = int(stars)
    except:
        stars = 3

    if sent == "Very Negative" or stars <= 1:
        return "High"
    elif sent == "Negative" or stars <= 2:
        return "Medium"
    else:
        return "Low"

df["ai_severity"] = df.apply(get_severity, axis=1)

# ── Save outputs (🔥 FIX APPLIED HERE) ──────────────────────
csv_path = os.path.join(OUTPUT_DIR, "classified_reviews.csv")
img_path = os.path.join(OUTPUT_DIR, "dashboard.png")

df.to_csv(csv_path, index=False)
print("Saved:", csv_path)

# ── Dashboard ──────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Customer Intelligence Dashboard — Parvathy Menon", fontsize=16, fontweight="bold")

cat_counts = df["ai_category"].value_counts()
axes[0,0].barh(cat_counts.index, cat_counts.values)
axes[0,0].set_title("Complaint Categories")

sev_counts = df["ai_severity"].value_counts()
axes[0,1].pie(sev_counts.values, labels=sev_counts.index, autopct="%1.0f%%")
axes[0,1].set_title("Severity Distribution")

sent_counts = df["ai_sentiment"].value_counts()
axes[1,0].bar(sent_counts.index, sent_counts.values)
axes[1,0].set_title("Customer Sentiment")

cat_sent = df.groupby("ai_category")["ai_sentiment"].apply(
    lambda x: (x.isin(["Negative","Very Negative"])).mean() * 100
).sort_values(ascending=False).head(5)

axes[1,1].bar(range(len(cat_sent)), cat_sent.values)
axes[1,1].set_xticks(range(len(cat_sent)))
axes[1,1].set_xticklabels(cat_sent.index, rotation=30, ha="right")
axes[1,1].set_title("% Negative Sentiment by Category (Top 5)")

plt.tight_layout()
plt.savefig(img_path, dpi=150, bbox_inches="tight")

print("Saved:", img_path)

# ── Summary ────────────────────────────────────────────────
print("\n=== EXECUTIVE SUMMARY ===")
print(f"Reviews analysed  : {len(df):,}")
print(f"Top complaint     : {cat_counts.index[0]}")
print(f"High severity     : {(df.ai_severity=='High').sum()}")
print(f"Negative sentiment: {(df.ai_sentiment.isin(['Negative','Very Negative'])).sum()}")