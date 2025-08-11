# 🔐 SafeNet — Cybersecurity Awareness Toolkit (CLI)
> A CLI toolkit for cybersecurity learning, testing, and awareness.
[![License](https://img.shields.io/github/license/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)](./LICENSE)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Repo Size](https://img.shields.io/github/repo-size/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)
![Last Commit](https://img.shields.io/github/last-commit/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)

---


## 📑 Table of Contents  
- [About the Project](#about-the-project)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Prerequisites](#prerequisites)  
- [Features in Detail](#features-in-detail)  
- [Team & Responsibilities](#team--responsibilities)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Data Storage](#data-storage)  
- [Development Timeline](#development-timeline)  
- [Testing Checklist](#testing-checklist)  
- [License](#license)  
- [Demo Screenshots](#demo-screenshots)  
- [Authors](#authors)  

---


## 📖 About the Project  

**SafeNet** is a Python-based Cybersecurity Awareness Toolkit built as a **BanoQabil 4.0 Summer (Advanced Python & FastAPI)** mid-term project, taught by **Sir Shaukat Sohail**.  
It is a **pure Python, menu-driven CLI tool** designed to educate, test, and protect users through interactive learning and practical cybersecurity tools.

---

## ✨ Features  

- 📝 **Cybersecurity Quiz** – Test your knowledge with interactive questions  
- 🎯 **Phishing Detection** – Learn to identify phishing attempts  
- 🔑 **Password Strength Checker** – Check and improve your passwords  
- 📢 **Security Tips Generator** – Get random safety tips  
- 🚨 **Data Breach Simulator** – Understand how breaches affect users  
- 📊 **Stats & Leaderboard** – Track your progress  

---

## 📂 Project Structure

SafeNet/
│
├── main.py # Program entry & menu loop
├── quiz.py # Quiz logic & question bank handling
├── phish.py # Phishing detection logic
├── password.py # Password strength checker
├── tips.py # Cybersecurity tips generator
├── breach.py # Data breach simulator
├── stats.py # Stats & leaderboard handling
├── utils.py # Shared helper functions
├── data/
│   ├── questions.json
│   ├── breached_accounts.json
│   ├── leaderboard.json
│
├── README.md
├── .gitignore
└── requirements.txt # (if needed)

---

## ⚙ Prerequisites  

- **Python 3.8+** is required to run this project.  
- To check your Python version:  

```bash
python --version
```

---

## 🚀 Features in details

- **Multi-level Cybersecurity Quiz**
  - Beginner, Intermediate, Advanced
  - Randomized questions, no repeats per session
  - Score tracking & progress history

- **Phishing Email/URL Detector**
  - Detects suspicious patterns in links and emails
  - Finds insecure protocols, suspicious keywords, misspelled domains

- **Password Strength Checker**
  - Evaluates length, character variety, and complexity
  - Gives actionable improvement suggestions

- **Cybersecurity Tips Generator**
  - 20+ immutable tips stored in tuples
  - Random selection (1–3 per request)

- **Mock Data Breach Checker**
  - Checks input email/username against mock breached data
  - Case-insensitive matching

- **Stats & Leaderboard**
  - Tracks quiz scores, phishing detections, and password checks
  - Saves per-user history and displays the leaderboard

---

## 👥 Team & Responsibilities

**Member A — Anum Mateen** *(Backend & Learning Flow)*
- Modules: `quiz.py`, `tips.py`, `stats.py` (primary), assists in `utils.py`
- **Key Tasks:**
  - Create question bank (30+ questions, 10 per level)
  - Implement quiz logic, randomization, and scoring
  - Create a tips generator with 20+ entries
  - Implement JSON-based stats storage & leaderboard
  - Provide test data (`questions.json`, sample `leaderboard.json`)
  - Review Member B’s code

**Member B — Syeda Muqaddas Bibi** *(Detection & Security Tools)*
- Modules: `phish.py`, `password.py`, `breach.py` (primary), assists in `utils.py`
- **Key Tasks:**
  - Implement phishing detection rules (protocol, keywords, domain checks)
  - Implement password strength analysis & suggestions
  - Create a mock breached accounts database
  - Implement breach simulator logic
  - Provide test cases for phishing/password/breach checks
  - Review Member A’s code

**Shared / Joint Responsibilities**
- Integration in `main.py`
- Writing helper functions in `utils.py`
- Cross-testing and debugging
- Writing documentation (`README.md`)
- Preparing presentation & demo

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit.git
   cd SafeNet-Cybersecurity-Awareness-Toolkit
   ```

 2. **Install dependencies (if required)**
    ```bash
    pip install -r requirements.txt
    ```
    *If no external libraries are used, this step can be skipped.*
 
---

## ▶️ Usage
 
**Run the toolkit:**
 ```bash
 python main.py
 ```
 
**Follow the menu prompts to:**
 - Take the quiz
 - Detect phishing attempts
 - Test password strength
 - Get cybersecurity tips
 - Check for mock data breaches
 - View your stats & leaderboard
 
---

## 🗂 Data Storage

 - `questions.json` → Quiz questions & answers
 - `leaderboard.json` → User scores & stats
 - `breached_accounts.json` → Mock breach database
 
> All stored in `/data` directory in JSON format.
 
---

## 📅 Development Timeline

 | Day | Task                                      | Owner      |
 |-----|-------------------------------------------|------------|
 | 1   | Repo setup, module stubs, sample JSON files | Both       |
 | 2   | Quiz system & question bank               | Anum       |
 | 2   | Phishing detection & password checker     | Muqaddas   |
 | 3   | Tips generator & stats storage skeleton   | Anum       |
 | 3   | Breach simulator                          | Muqaddas   |
 | 4   | Integration, finalize stats/leaderboard, manual testing | Both |
 | 5   | Polish, write README, run demo, prepare presentation | Both |
 
---

## ✅ Testing Checklist
 - [ ] Quiz runs for all levels & saves scores
 - [ ] Phishing detector catches multiple suspicious patterns
 - [ ] Password checker scores correctly with suggestions
 - [ ] Breach simulator finds or does not find entries as expected
 - [ ] Stats update correctly after each activity
 - [ ] No crashes on invalid input
 
---

## 📜 License  
Licensed under the [MIT License](https://github.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit/blob/main/LICENSE).  

---

 ## 📸 Demo Screenshots
 (To be added after project completion)
 
---

## 🏆 Authors
 - **Anum Mateen** — Quiz, Tips, Stats
 - **Syeda Muqaddas Bibi** — Phishing, Password, Breach
