# AI381 Lab 2 — Docker and CI

![CI Pipeline](https://github.com/dana10888/lab2-churn-api/actions/workflows/ci.yml/badge.svg)

## About the Project

This project predicts customer churn using a machine learning model and FastAPI.

In Lab 2, we added Docker, automated tests, GitHub Actions, a Trivy security scan, and Docker image publishing to GHCR.

## Run the Application

Build the Docker image:

```bash
docker build -t churn-api:lab2 .
```

Run the container:

```bash
docker run --rm -p 8000:8000 churn-api:lab2
```

Open the API documentation:

http://localhost:8000/docs

## API Endpoints

- GET /health — checks if the API is running.
- POST /predict — makes a churn prediction.

## Run Tests

```bash
python -m pytest tests/ -v
```

The project includes five tests for the API, model loading, invalid input, edge cases, and consistent predictions.

## CI Pipeline

GitHub Actions automatically:

1. Runs the tests.
2. Builds the Docker image.
3. Scans the image using Trivy.
4. Publishes the image to GHCR.

## Published Docker Image

```bash
docker pull ghcr.io/dana10888/lab2-churn-api:sha-a52034c
```

## Branch Protection

A branch protection rule is configured for `main`, with pull request, approval, and CI check requirements.
d fill it in as you go |

## The race (start your stopwatch first)

1. **Round 1.** Run the notebook with `churn_v1.csv`. Start the API by hand:
   `uvicorn app.main:app --port 8000`
   Send three predictions with curl, changing the values each time:
   `curl -X POST localhost:8000/predict -H "Content-Type: application/json" -d @sample_request.json`
2. **Twist 1.** Change the notebook to `churn_v2.csv`, retrain and redeploy. Find and fix what breaks.
3. **Twist 2.** Create a brand-new virtual environment (or a Codespace) and rebuild everything using only your own notes.
4. **Twist 3.** Answer: "Which model version is your API serving right now?" and explain why it is hard to prove.
5. Finish `pain_log.txt`: minutes per step, every failure, every unanswered question.

## Setup

- Python 3.11 or newer and a terminal. On Windows, use WSL2 with Ubuntu.
- `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

## Turning it in

Record one 5–8 minute video with your face and voice, say each checkpoint aloud, and turn it in on the
**Lab 1** assignment in the **AI381 MLOPs** team on Microsoft Teams (Lab Submissions channel, Assignments tab).
The full instructions, checkpoints and rubric are on e-learning and on the Teams assignment.

Questions: Thursday online office hours on Teams, the Lab Submissions channel, or talomari@just.edu.jo.
