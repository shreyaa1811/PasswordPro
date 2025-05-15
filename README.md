# 🔐 PasswordPro - Password Strength Checker

PasswordPro is a lightweight Flask-based web application that evaluates the strength of user passwords and provides actionable suggestions to improve them. It features a live password visibility toggle, a dynamic progress bar with visual cues, and a modern UI built using Bootstrap.

---

## 🚀 Features

- ✅ Real-time password strength evaluation  
- ✅ Suggestions to improve weak passwords  
- ✅ Visual strength indicator using Bootstrap progress bar  
- ✅ Password visibility toggle with eye icon  
- ✅ Responsive and clean UI with Bootstrap 5  

---


## 🧠 Password Strength Criteria

A password is evaluated based on:

- Length (minimum 8 characters)  
- Use of uppercase letters  
- Use of lowercase letters  
- Inclusion of numbers  
- Use of special characters (`!@#$%^&*()_+`)  

Based on these criteria, the password is rated as:  
- 🟥 Weak  
- 🟨 Medium  
- 🟩 Strong

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- HTML5, CSS3  
- Bootstrap 5  
- Bootstrap Icons  

---

## 🔧 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyaa1811/PasswordPro.git
   cd PasswordPro
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open your browser and visit:

   [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
PasswordPro/
│
├── app.py              # Flask backend logic
├── templates/
│   └── index.html      # Frontend HTML template
├── README.md
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Contributions are welcome! Please open an issue first to discuss any major changes.
