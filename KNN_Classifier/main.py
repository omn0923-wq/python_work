import joblib
from fastapi import FastAPI
from schemas import FishInput, FishOutput
import numpy as np

ml_models= {}


# 처음 서버가 실행될 때 딱 한 번 실행되는 함수
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  # 서버 시작하고 1회 모델 로딩
  saved_model = joblib.load("models/fish_knn_model.pkl")
  # "model": kn, "scaler": ss
  ml_models["model"] = saved_model["model"]
  ml_models["scaler"] = saved_model["scaler"]
  print("모델 로드 완료")

  yield  # 여기서부터 서버가 요청을 받아서 처리

  # 서버 죽을 때 실행(정리)
  ml_models.clear()
  print("모델 언로드 완료")

# FastAPI app 생성
app = FastAPI(
  title="도미/빙어 분류 API", 
  version="1.0.0", 
  lifespan=lifespan)

######### 컨트롤러 시작
@app.get("/")
def root():
  return {"message": "도미/빙어 분류 API. /docs에서 확인하세요"}

@app.post("/predict", response_model=FishOutput)
def predict(fish: FishInput):
  model = ml_models["model"]
  scaler = ml_models["scaler"]

  # predict([[20, 150]])
  # 넘어온 length, weight를 2차원 배열로 변환
  raw = np.array([[fish.length, fish.weight]])
  # 스케일러: train_input을 갖고 평균과 표준편차로 구한 스케일러
  scaled = scaler.transform(raw)
  # 예측
  # 1. 분류
  pred = model.predict(scaled)[0]
  # 2. 확률
  # [빙어 확률 0.8, 도미 확률 0.2]
  proba = model.predict_proba(scaled)[0]

  # FishOut 담아서 리턴
  label = "도미" if pred == 1 else "빙어"
  print(label)
  # prediction: str
  # probability: float
  # 예측 결과 중 큰 놈 선택: 확률로 전달
  probability = float(max(proba))
  # 객체 생성해서 리턴
  return FishOutput(prediction=label, probability=probability)

######### 컨트롤러 끝


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
