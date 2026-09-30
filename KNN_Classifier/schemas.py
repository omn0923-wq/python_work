from pydantic import BaseModel

# 프론트에서 넘겨줄 데이터 클래스
class FishInput(BaseModel):
  """
  생선 분류를 위한 입력 데이터
  - length: 생선의 길이(cm 단위, 예: 30.0)
  - weight: 생선의 무게(g 단위, 예: 600.0)
  두 값 모두 실수(float)로 입력하며, 필수값입니다.
  """
  length: float
  weight: float

class FishOutput(BaseModel):
  """
  예측한 결괏값과 예측 확률을 전달
  """  
  prediction: str
  probability: float