# Model selection

## The question
The model predicts whether a customer is likely to churn (leave the service). Wrong predictions can hurt customers who miss useful retention offers and the company through lost revenue or unnecessary retention costs.

## Candidates

| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---|---|---|---|---|---|
| Logistic Regression | Simple and fast baseline model | 0.798 | 0.495 | 0.25 | 5.72 | 3.55 | 8f422d4fe7654b669caba5b9557b1bc9 |
| Random Forest | To test nonlinear relationships using multiple decision trees | 0.759 | 0.454 | 0.22 | 25.66 | 3160.13 | 45d150d3fa84419d8227b8d564d0344a |
| Gradient Boosting | To test whether sequentially trained trees improve predictions | 0.748 | 0.417 | 0.22 | 10.21 | 141.68 | 31cc0a7914c644e6abe7bc3ea495038b |

## The champion

I selected **Logistic Regression** as the champion because it achieved the highest AUC (0.798) and F1 (0.495), with the lowest p95 latency (5.72 ms) and smallest size (3.55 KB).

It also achieved the highest minimum slice F1 (0.25). I did not have to sacrifice overall performance, speed, or model size. However, its performance on some contract groups remains relatively low.

## My promotion rules

- **Latency budget (p95): 30 ms**, because predictions should be fast enough for responsive service, while allowing some room for more complex models.
- **Minimum gain to replace the champion (F1 points): 0.02**, because a new model should improve F1 by at least two percentage points to justify replacing the current champion.

## What I would check next

I would monitor model performance across different contract types, especially groups with low F1 scores. I would also check for data drift, since customer behavior may change over time.