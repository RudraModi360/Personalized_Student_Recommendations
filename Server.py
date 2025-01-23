from plots import plot_Score, plot_Accuracy, plot_Mistake_Count, plot_Time
import pickle
from fastapi import FastAPI
import uvicorn
import pandas as pd
from pydantic import BaseModel

app = FastAPI()


with open("Models\\model.pkl", "rb") as f:
    similarity = pickle.load(f)

df = pd.read_csv("C:\\Users\\rudra\\Desktop\\Student_Reccomendations\\Data\\final.csv")


class RecommendRequest(BaseModel):
    title: str
    score: int


@app.get("/ping")
async def ping():
    return "hi"


@app.post("/recommend")
def recommend(input: RecommendRequest):
    title = input.title
    score = input.score
    idx = df[(df["title"] == title) & (df["score"] == score)].index[0]
    ans = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[
        1:3
    ]
    results = set()
    for row in ans:
        results.add(df["topic"][row[0]].strip())
    return results


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port="8000")
