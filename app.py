import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3, string, random, os, qrcode, webbrowser

# === Setup Directories ===
DB_NAME = 'urls.db'
QR_DIR = 'qrcodes'
os.makedirs(QR_DIR, exist_ok=True)

# === Initialize SQLite DB ===
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE,
                clicks INTEGER DEFAULT 0
            )
        ''')
init_db()

# === Generate short URL code ===
def generate_short_url(original_url):
    if not original_url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    short_url = f"http://localhost:8080/{short_code}"

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))

    # Generate QR code
    qr_img = qrcode.make(short_url)
    qr_path = os.path.join(QR_DIR, f"{short_code}.png")
    qr_img.save(qr_path)

    result_label.config(text=f"Short URL: {short_url}")
    qr_label.config(text=f"QR Code saved to: {qr_path}")

    # Button to open shortened link
    open_button.config(command=lambda: webbrowser.open(original_url))
    open_button.pack(pady=5)

# === GUI Setup ===
root = tk.Tk()
root.title("🔗 URL Shortener & QR Generator")
root.geometry("600x400")
root.configure(bg="#0f172a")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="#ffffff", background="#0ea5e9", font=("Consolas", 12))
style.configure("TLabel", foreground="#38bdf8", background="#0f172a", font=("Consolas", 12))
style.configure("TEntry", foreground="#00ff00", fieldbackground="#1e1e1e", font=("Consolas", 12))

tk.Label(root, text="🔗 Enter URL to Shorten:", bg="#0f172a", fg="#38bdf8", font=("Orbitron", 14)).pack(pady=20)

url_entry = ttk.Entry(root, width=60)
url_entry.pack(pady=10)

generate_btn = ttk.Button(root, text="⚡ Generate Short URL", command=lambda: generate_short_url(url_entry.get()))
generate_btn.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

qr_label = ttk.Label(root, text="")
qr_label.pack()

open_button = ttk.Button(root, text="🌐 Open Original URL")

tk.Label(root, text="Made with 💙 by Tkinter", bg="#0f172a", fg="#64748b", font=("Consolas", 10)).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
