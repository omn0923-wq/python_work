from fish_data import load_fish_data

# 데이터 생성
fish_data, fish_target = load_fish_data()

# 1. 훈련 셋/테스트 셋으로 분리
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
  fish_data, fish_target,
  random_state=42,
  stratify=fish_target,
  test_size=0.3
)

# 2. 스케일 작업: 표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# 3. 모델 선언
# 최근접 이웃 분류 모델
from sklearn.neighbors import KNeighborsClassifier
# 특정 모델 정의할 때 시용자가 수정해서 반영하는 값: 하이퍼파라미터(Hyper-Parameter)
kn = KNeighborsClassifier(n_neighbors=5)

# 4. 모델 학습
kn.fit(train_scaled, train_target)

# 5. 모델 평가
from sklearn.metrics import accuracy_score

test_pred = kn.predict(test_scaled)
test_accuracy = accuracy_score(test_target, test_pred)
print(f"테스트 정확도: {test_accuracy}")

# 6. 모델 저장
import joblib
import os

os.makedirs("models", exist_ok=True)
joblib.dump(
  {"model": kn, "scaler": ss},
  "models/fish_knn_model.pkl"
)
# pkl: 피클
# - 파이썬 객체 자체 저장

print("모델 저장 완료: models/fish_knn_model.pkl")