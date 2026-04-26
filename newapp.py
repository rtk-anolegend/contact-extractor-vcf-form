import re, os, uuid
from flask import Flask, render_template, request, send_file, after_this_request
import pytesseract
from PIL import Image
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔹 SET TESSERACT PATH (Termux users adjust if needed)
# Example:
# pytesseract.pytesseract.tesseract_cmd = "/data/data/com.termux/files/usr/bin/tesseract"


# ---------------------------
# 📞 Extract Numbers
# ---------------------------
def extract_numbers(text):
    nums = re.findall(r'(?:\+91[\s-]?)?[6-9]\d{9}', text)
    clean = set()

    for n in nums:
        n = re.sub(r'\D', '', n)
        clean.add(n[-10:])

    return list(clean)


# ---------------------------
# 📷 OCR from Image
# ---------------------------
def extract_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return extract_numbers(text)


# ---------------------------
# 📇 VCF
# ---------------------------
def create_vcf(numbers):
    filename = f"contacts_{uuid.uuid4().hex}.vcf"

    with open(filename, "w", encoding="utf-8") as v:
        for i, num in enumerate(numbers, 1):
            v.write(
                "BEGIN:VCARD\n"
                "VERSION:3.0\n"
                f"N:Contact{i};Contact{i};;;\n"
                f"FN:Contact {i}\n"
                f"TEL;TYPE=CELL:+91{num}\n"
                "END:VCARD\n\n"
            )

    return filename


# ---------------------------
# 📊 CSV
# ---------------------------
def create_csv(numbers):
    filename = f"contacts_{uuid.uuid4().hex}.csv"
    df = pd.DataFrame({
        "Name": [f"Contact {i+1}" for i in range(len(numbers))],
        "Phone": [f"+91{n}" for n in numbers]
    })
    df.to_csv(filename, index=False)
    return filename


# ---------------------------
# 📊 Excel
# ---------------------------
def create_excel(numbers):
    filename = f"contacts_{uuid.uuid4().hex}.xlsx"
    df = pd.DataFrame({
        "Name": [f"Contact {i+1}" for i in range(len(numbers))],
        "Phone": [f"+91{n}" for n in numbers]
    })
    df.to_excel(filename, index=False)
    return filename


# ---------------------------
# 🌐 Main Route
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file = request.files.get("file")
        export_type = request.form.get("export")  # vcf / csv / excel

        if not file or file.filename == "":
            return "No file selected"

        filename = file.filename.lower()
        filepath = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_{filename}")
        file.save(filepath)

        numbers = []

        # 🔹 TXT Processing
        if filename.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
                numbers = extract_numbers(text)

        # 🔹 Image Processing
        elif filename.endswith((".png", ".jpg", ".jpeg")):
            numbers = extract_from_image(filepath)

        else:
            return "Unsupported file type"

        if not numbers:
            return "No valid contacts found"

        # 🔹 Export selection
        if export_type == "csv":
            output_file = create_csv(numbers)
        elif export_type == "excel":
            output_file = create_excel(numbers)
        else:
            output_file = create_vcf(numbers)

        # 🧹 Cleanup
        @after_this_request
        def cleanup(response):
            try:
                os.remove(filepath)
                os.remove(output_file)
            except Exception:
                pass
            return response

        return send_file(output_file, as_attachment=True)

    return render_template("index.html")


# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
