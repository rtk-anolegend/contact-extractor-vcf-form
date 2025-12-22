<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3059/3059518.png" width="120" alt="Contact Extractor">
</p>

<h1 align="center">📱 TXT to VCF Contact Extractor</h1>

<p align="center">
  <b>Convert text-based phone numbers into import-ready contacts</b><br>
  Fast • Mobile-Friendly • Clean UI
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  <img src="https://img.shields.io/badge/Flask-Web%20App-black">
  <img src="https://img.shields.io/badge/UI-Mobile%20Friendly-success">
  <img src="https://img.shields.io/badge/Status-Stable-green">
</p>

---

## ✨ Overview

**TXT to VCF Contact Extractor** is a lightweight web application designed to quickly extract phone numbers from text files and convert them into **VCF (vCard)** format.

The generated VCF file can be directly imported into:
- Android phones  
- iPhones  
- Google Contacts  
- Any modern contact manager  

Built with a focus on **simplicity, speed, and real-world usability**.

---

## 🚀 Key Highlights

✔ Handles mixed text files (names, symbols, random text)  
✔ Smart phone number detection  
✔ Automatic duplicate removal  
✔ One-click VCF generation  
✔ Optimized for mobile browsers  
✔ Clean, distraction-free interface  

---

## 🖼️ Interface Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/rtk-anolegend/assets/main/txt-to-vcf-ui.png" alt="App UI" width="360">
</p>

<p align="center">
  <i>Minimal, modern UI designed for daily use</i>
</p>

---

## ⚙️ How It Works

1. Open the web app in your browser  
2. Upload a `.txt` file containing phone numbers  
3. Click **Generate VCF**  
4. Download the VCF file  
5. Import contacts into your phone  

No login. No tracking. No clutter.

---

## 🧠 Technology Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css" />
</p>

- **Python** → Core logic & data processing  
- **Flask** → Lightweight backend framework  
- **HTML5** → Semantic, accessible structure  
- **CSS3** → Responsive, modern UI styling  

Designed with a clear separation between frontend and backend.

---

## 📊 Language Breakdown

- 🐍 **Python** – Contact extraction logic & VCF generation  
- 🌐 **HTML** – UI structure and form handling  
- 🎨 **CSS** – Styling, layout, and responsiveness  

---

## 👨‍💻 Developer

<p align="center">
  <b>RTK</b><br>
  <a href="https://instagram.com/tyagirtk">Instagram • @tyagirtk</a><br>
  <a href="https://github.com/rtk-anolegend">GitHub • rtk-anolegend</a>
</p>

<p align="center">
  <i>Focused on building practical tools with clean UI and scalable logic.</i>
</p>

---

## 📱 Run on Android using Termux (Beginner Friendly)

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/888/888857.png" width="90" alt="Android">
  &nbsp;&nbsp;
  <img src="https://cdn-icons-png.flaticon.com/512/919/919851.png" width="90" alt="Terminal">
</p>

You can run this project **directly on an Android phone** using **Termux**.  
👉 **Laptop / PC ki zarurat nahi hai**.

This method is perfect for:
- 📚 Students  
- 👶 Beginners  
- 📱 Mobile-only users  

---

### 🔹 Step 1: Install Termux (Correct & Safe Way)

<p align="center">
  <img src="https://f-droid.org/repo/icons-640/org.fdroid.fdroid.1014050.png" width="80" alt="F-Droid">
</p>

⚠️ **Important:**  
❌ Play Store wala Termux **outdated** hota hai  
✅ **F-Droid se install karna zaruri hai**

#### 👉 Follow these steps carefully:

1. Open your mobile browser (Chrome / Firefox)
2. Go to 👉 **https://f-droid.org**
3. Download & install **F-Droid**
4. Open **F-Droid App**
5. Search for **Termux**
6. Install **Termux** 

---

### 🔹 Step 2: Open Termux & Update System

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="70" alt="Update">
</p>

After installing **Termux**:

1. Open the **Termux app**
2. You will see a **black screen (terminal)**  
   👉 This is normal

Now copy-paste this command and press **Enter**:

```bash

pkg update -y && pkg upgrade -y && termux-setup-storage && pkg install python git clang make openssl libffi -y && pip install --upgrade pip && git clone https://github.com/rtk-anolegend/txt-to-vcf-contact-extractor.git && cd txt-to-vcf-contact-extractor && pip install -r requirements.txt && python app.py
