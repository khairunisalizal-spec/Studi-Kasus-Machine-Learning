from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data_kelulusan.csv"
MODEL_PATH = BASE_DIR / "model_kelulusan.joblib"

def main():
    data = pd.read_csv(DATA_PATH)
    features = ["kehadiran", "nilai_tugas", "nilai_uts"]
    X = data[features]
    y = data["lulus_tepat_waktu"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(random_state=42, max_iter=1000))
    ])
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("=== Evaluasi Model ===")
    print(f"Akurasi : {accuracy_score(y_test, predictions):.2f}")
    print(f"Presisi : {precision_score(y_test, predictions, zero_division=0):.2f}")
    print(f"Recall  : {recall_score(y_test, predictions, zero_division=0):.2f}")
    print("\\nLaporan klasifikasi:")
    print(classification_report(y_test, predictions, zero_division=0))

    joblib.dump(model, MODEL_PATH)
    print(f"Model disimpan di: {MODEL_PATH.name}")

if __name__ == "__main__":
    main()
