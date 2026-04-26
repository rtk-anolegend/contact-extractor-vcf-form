"""
TXT to VCF Contact Extractor
Developer: RTK
Instagram: https://instagram.com/tyagirtk
GitHub: https://github.com/rtk-anolegend
"""

import re, os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_numbers(text):
    nums = re.findall(r'(?:\+91[\s-]?)?[6-9]\d{9}', text)
    clean = set()
    for n in nums:
        n = re.sub(r'\D', '', n)
        clean.add(n[-10:])
    return list(clean)

def create_vcf(numbers, filename="contacts.vcf"):
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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("txtfile")
        if not file:
            return "No file uploaded"

        text = file.read().decode("utf-8", errors="ignore")
        numbers = extract_numbers(text)

        if not numbers:
            return "No valid contacts found"

        vcf = create_vcf(numbers)
        return send_file(vcf, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
