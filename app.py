from pathlib import Path
import subprocess
import sys

from flask import Flask, render_template, request
import joblib
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model_kelulusan.joblib"

app = Flask(__name__)

def load_model():
    if not MODEL_PATH.exists():
        subprocess.run([sys.executable, str(BASE_DIR / "train_model.py")], check=True)
    return joblib.load(MODEL_PATH)

model = load_model()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    values = {"attendance": "", "assignment": "", "midterm": ""}
    error = None

    if request.method == "POST":
        try:
            values = {
                "attendance": request.form.get("attendance", "").strip(),
                "assignment": request.form.get("assignment", "").strip(),
                "midterm": request.form.get("midterm", "").strip(),
            }
            attendance = float(values["attendance"])
            assignment = float(values["assignment"])
            midterm = float(values["midterm"])

            if not (0 <= attendance <= 100 and 0 <= assignment <= 100 and 0 <= midterm <= 100):
                raise ValueError("Semua nilai harus berada pada rentang 0 sampai 100.")

            prediction = int(model.predict(np.array([[attendance, assignment, midterm]]))[0])
            probabilities = model.predict_proba(np.array([[attendance, assignment, midterm]]))[0]
            confidence = round(float(max(probabilities)) * 100, 1)

            result = {
                "label": "Berpotensi lulus tepat waktu" if prediction == 1 else "Perlu pendampingan belajar",
                "status": "success" if prediction == 1 else "attention",
                "confidence": confidence,
                "note": (
                    "Pertahankan kebiasaan belajar dan kehadiran yang baik."
                    if prediction == 1 else
                    "Pertimbangkan konsultasi dengan dosen, memperbaiki kehadiran, dan mengerjakan tugas secara konsisten."
                )
            }
        except ValueError as exc:
            error = str(exc) or "Masukkan angka yang valid pada semua kolom."
        except Exception:
            error = "Terjadi kesalahan saat memproses data. Periksa input lalu coba lagi."

    return render_template("index.html", result=result, values=values, error=error)

if __name__ == "__main__":
    app.run(debug=True)
