# 🔗 URL_SHORTENER_QR

**Smart Short Links + Instant QR Codes — Share with Style**

![last-commit](https://img.shields.io/github/last-commit/YourUsername/url_shortener_qr)
![repo-top-language](https://img.shields.io/github/languages/top/YourUsername/url_shortener_qr)
![repo-language-count](https://img.shields.io/github/languages/count/YourUsername/url_shortener_qr)

---

## 🛠️ Built with the tools and technologies:

- Python  
- Tkinter  
- SQLite  
- qrcode  
- Markdown  

---

## 📚 Table of Contents

- [Overview](#overview)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Usage](#usage)  
- [Testing](#testing)  

---

## 🔍 Overview

**URL_SHORTENER_QR** is a modern, desktop-based utility that shortens any long URL and instantly generates a scannable QR code for it.  
Perfect for students, marketers, developers, or anyone looking to share short URLs with style.

---

### 🚀 Why url_shortener_qr?

- 🖥️ **Tkinter Desktop Interface** – No server needed, works offline  
- 🔐 **SQLite-powered Database** – Keeps track of URLs and shortcodes  
- 📷 **QR Code Integration** – Generates sharable QR code images instantly  
- ⚡ **One-click Sharing** – Open links directly from the app  
- 💾 **Auto Saves QR** – All QR codes saved in the `qrcodes/` folder  

---

## 🧰 Getting Started

### ✅ Prerequisites

- **Python 3.7+**
- Recommended: Virtual Environment

### 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/url_shortener_qr
cd url_shortener_qr
```

2. Install the required packages:

```bash
pip install qrcode[pil]
```

> Tkinter is included with standard Python distributions.

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Then:

- Paste your original URL  
- Click **⚡ Generate Short URL**  
- You’ll receive a short link and a QR image  
- QR code is saved to `qrcodes/`  
- Use the **🌐 Open Original URL** button to test the link  

---

## 🧪 Testing

No external framework needed. To test manually:

1. Run the app  
2. Generate a few short URLs  
3. Check the `qrcodes/` folder  
4. Scan QR codes with your mobile camera  
5. Verify that redirects open in your browser

---

⬆ [Return to top](#url_shortener_qr)
