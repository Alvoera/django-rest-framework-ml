from django.db import models

# Create your models here.
# pyrefly: ignore [missing-import]
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1. Load dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# 2. Latih model klasifikasi
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 3. Simpan model ke file .pkl
joblib.dump(model, 'model_iris.pkl')
print("Model berhasil disimpan sebagai 'model_iris.pkl'")