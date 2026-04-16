-- Q1: Sentiment distribution by complaint category
SELECT
  ai_category,
  COUNT(*) AS total_reviews,
  ROUND(100.0 * SUM(CASE 
      WHEN ai_sentiment IN ('Negative','Very Negative') THEN 1 
      ELSE 0 END) / COUNT(*), 1) AS negative_pct,
  ROUND(AVG(CAST(star_rating AS FLOAT)), 2) AS avg_rating
FROM classified_reviews
GROUP BY ai_category
ORDER BY negative_pct DESC;


-- Q2: High severity issues by product category
SELECT
  product_category,
  COUNT(*) AS total_reviews,
  SUM(CASE WHEN ai_severity = 'High' THEN 1 ELSE 0 END) AS high_severity_count,
  ROUND(100.0 * SUM(CASE 
      WHEN ai_severity = 'High' THEN 1 
      ELSE 0 END) / COUNT(*), 1) AS high_severity_pct
FROM classified_reviews
GROUP BY product_category
ORDER BY high_severity_pct DESC
LIMIT 10;


-- Q3: Model validation — sentiment vs star rating
SELECT
  star_rating,
  ai_sentiment,
  COUNT(*) AS count,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) 
        OVER (PARTITION BY star_rating), 1) AS pct
FROM classified_reviews
GROUP BY star_rating, ai_sentiment
ORDER BY star_rating, count DESC;


-- Q4: Monthly trend of negative reviews
SELECT
  SUBSTR(review_date, 1, 7) AS month,
  COUNT(*) AS total_reviews,
  SUM(CASE 
      WHEN ai_sentiment IN ('Negative','Very Negative') THEN 1 
      ELSE 0 END) AS negative_reviews
FROM classified_reviews
GROUP BY month
ORDER BY month;


-- Q5: Executive risk summary
SELECT
  ai_category AS complaint_type,
  COUNT(*) AS volume,
  ROUND(AVG(CAST(star_rating AS FLOAT)), 1) AS avg_rating,
  SUM(CASE WHEN ai_severity = 'High' THEN 1 ELSE 0 END) AS high_risk_count,
  CASE
    WHEN SUM(CASE WHEN ai_severity = 'High' THEN 1 ELSE 0 END) > 100
      THEN 'URGENT - escalate immediately'
    WHEN SUM(CASE WHEN ai_severity = 'High' THEN 1 ELSE 0 END) > 50
      THEN 'MONITOR - weekly review'
    ELSE 'LOW RISK'
  END AS recommended_action
FROM classified_reviews
GROUP BY ai_category
ORDER BY high_risk_count DESC;