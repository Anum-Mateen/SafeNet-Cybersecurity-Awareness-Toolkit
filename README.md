# 🔐 SafeNet — Cybersecurity Awareness Toolkit (CLI)

[![License](https://img.shields.io/github/license/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)](./LICENSE)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Repo Size](https://img.shields.io/github/repo-size/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)
![Last Commit](https://img.shields.io/github/last-commit/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit/issues)

<p align="center">
  <img src="https://raw.githubusercontent.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit/main/TITLE.png" alt="SafeNet Title Screenshot" width="700"/>
</p>

> A comprehensive command-line interface (CLI) toolkit for cybersecurity education and awareness, featuring interactive learning modules and practical security tools.

---

## 📑 Table of Contents  
- [🔐 SafeNet — Cybersecurity Awareness Toolkit (CLI)](#-safenet--cybersecurity-awareness-toolkit-cli)
  - [📑 Table of Contents](#-table-of-contents)
  - [📖 Overview](#-overview)
  - [✨ Features](#-features)
  - [📦 Installation](#-installation)
    - [⚙ Prerequisites](#-prerequisites)
    - [⚙️ Setup Instructions](#️-setup-instructions)
  - [🚀 Step-by-Step Usage](#-step-by-step-usage)
  - [📂 Project Structure](#-project-structure)
  - [🛠️ Module Details](#️-module-details)
  - [👥 Development Team](#-development-team)
    - [Anum Mateen *(Project Leader)*](#anum-mateen-project-leader)
    - [Syeda Muqaddas Bibi *(Contributor)*](#syeda-muqaddas-bibi-contributor)
  - [🔧 Technical Details](#-technical-details)
    - [Data Storage](#data-storage)
    - [Compatibility](#compatibility)
    - [Project Architecture](#project-architecture)
  - [📋 Testing](#-testing)
  - [📜 License](#-license)
  - [🤝 Contributing](#-contributing)
  - [📞 Support](#-support)
  - [🎯 Future Enhancements](#-future-enhancements)

---


## 📖 Overview  

**SafeNet** is a Python-based Cybersecurity Awareness Toolkit developed as part of the **BanoQabil 4.0 Summer (Advanced Python & FastAPI)** mid-term project, taught by **[Sir Shaukat Sohail](https://github.com/Shaukat456)**.  
It is a **pure Python, menu-driven CLI tool** designed to educate, test, and protect users through interactive learning and practical cybersecurity tools.

---

## ✨ Features  

- 🧠 **Interactive Cybersecurity Quiz** – Multiple difficulty levels with scoring system
- 🎣 **Phishing Detection** – Identify suspicious URLs and email addresses
- 🔐 **Password Strength Analyzer** – Evaluate and improve password security
- 💡 **Security Tips Generator** – Get actionable cybersecurity advice
- 🔍 **Data Breach Simulator** – Understand breach impacts with mock data
- 📊 **Performance Statistics** – Track progress with personal stats and leaderboard

---

## 📦 Installation

### ⚙ Prerequisites  

- **Python 3.8+** is required to run this project.  
- **Git** (for cloning the repository)
- ***Note:** This project uses only standard Python libraries. No extra installation is required.*

### ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit.git
   cd SafeNet-Cybersecurity-Awareness-Toolkit
   ```

2. **Verify Python installation**
    ```bash
    python --version
    # Should return: Python 3.8.x or higher
    ```

---

## 🚀 Step-by-Step Usage

1. **Run the toolkit**
   ```bash
   python main.py
   ```

2. **Enter your username** when prompted.

3. You'll be **presented with the main menu** to access different features of the toolkit.
<p align="center">
  <img src="https://raw.githubusercontent.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit/main/MENU.png" alt="SafeNet Main Menu Screenshot" width="700"/>
</p>

4. **Navigation:** Use number keys to select options and follow the on-screen instructions.

---

## 📂 Project Structure

```plaintext
SafeNet-Cybersecurity-Awareness-Toolkit/
|
├── main.py                # Main application entry point
├── quiz.py                # Quiz module implementation
├── phish.py               # Phishing detection functionality
├── password.py            # Password strength checking
├── tips.py                # Security tips generator
├── breach.py              # Data breach simulation
├── stats.py               # Statistics and leaderboard handling
├── data/                  # Data storage directory
│   ├── quiz_questions.py       # Quiz questions database
│   ├── mock_breached_data.py   # Mock breach data
│   └── leaderboard_data.py     # User performance records
├── LICENSE                # MIT License file
├── README.md              # Project documentation
└── .gitignore             # Git exclusion rules
```
***⚡ Note:** Unlike JSON files, data is stored in Python dictionaries (`.py` files) due to scope limitations. This keeps the toolkit lightweight and dependency-free.*


---

## 🛠️ Module Details

1. **Cybersecurity Quiz**
   - Three difficulty levels: Beginner, Intermediate, Advanced
   - Randomized question selection
   - Immediate feedback and explanations
   - Score tracking and progress saving

2. **Phishing Email/URL Detector**
   - Analyzes URLs for suspicious patterns
   - Checks for known phishing indicators
   - Validates email address structures
   - Provides detailed risk assessment

3. **Password Strength Checker**
   - Evaluates password complexity
   - Provides strength score (0-100)
   - Offers improvement suggestions
   - Checks against common weak passwords

4. **Cybersecurity Tips Generator**
   - Curated cybersecurity best practices
   - Random selection (1–3 per request)

5. **Mock Data Breach Checker**
   - Mock database of breached accounts
   - Educational simulation of breach impacts
   - Demonstrates importance of password hygiene

6. **Stats & Leaderboard**
   - Personal performance tracking
   - Historical score data
   - Comparative leaderboard
   - Achievement system

---

## 👥 Development Team

### [Anum Mateen](https://github.com/Anum-Mateen) *(Project Leader)*
- **Role:** Project Lead & Full-Stack Developer
- **Primary Contributions:**
  -   Overall project architecture and design
  -   Main application entry point (`main.py`)
  -   Comprehensive quiz system with 30+ questions (`quiz.py`)
  -   Security tips generator module (`tips.py`)
  -   Statistics and leaderboard system (`stats.py`)
  -   Data structure design and `/data/*.py` implementation
  -   Project documentation and README
  -   Integration of all modules
  -   Testing and debugging across all components

### [Syeda Muqaddas Bibi](https://github.com/syeda-muqaddas) *(Contributor)*
- **Role:** Module Contributor
- **Contributions:**
  -   Phishing detection module (`phish.py`)
  -   Password strength analyzer (`password.py`)
  -   Data breach simulation module (`breach.py`)

---

## 🔧 Technical Details

### Data Storage

All data is stored in Python dictionary format within the `/data` directory. Files created by the development team include:
-   `quiz_questions.py`: Quiz questions and answers (created by Anum Mateen)
-   `leaderboard_data.py`: User statistics and scores (created by Anum Mateen)
-   `mock_breached_data.py`: Simulated breach data (provided by contributor)

### Compatibility

-   Compatible with Windows, macOS, and Linux systems
-   Built using standard Python libraries only
-   No external dependencies required
-   Lightweight and easy to deploy

### Project Architecture

The project follows a modular architecture with clear separation of concerns:
-   **Core Framework:** Developed by Anum Mateen (`main.py`)
-   **Educational Modules:** Quiz and tips system by Anum Mateen
-   **Security Tools:** Phishing, password, and breach modules integrated from the contributor
-   **Data Management:** Python-based dictionary storage system implemented by Anum Mateen
 
---

## 📋 Testing

The application includes comprehensive functionality testing:
-   Quiz system with all difficulty levels
-   Phishing Detection with various input types
-   Password strength evaluation accuracy
-   Data breach simulation functionality
-   Statistics tracking and leaderboard updates
-   Error handling for invalid inputs
 
---

## 📜 License  
This project is licensed under the **MIT License** - see the [MIT License](https://github.com/Anum-Mateen/SafeNet-Cybersecurity-Awareness-Toolkit/blob/main/LICENSE) file for details.  

---

## 🤝 Contributing

We welcome contributions to enhance SafeNet! Please feel free to:
-   Submit bug reports or feature requests
-   Suggest additional quiz questions
-   Improve detection algorithms
-   Enhance the user experience

---

## 📞 Support

For questions or support regarding this project, please contact:
-   Anum Mateen: [GitHub Profile](https://github.com/Anum-Mateen)
-   Syeda Muqaddas Bibi: [GitHub Profile](https://github.com/syeda-muqaddas)

---

## 🎯 Future Enhancements

Potential improvements for future versions:
-   GUI implementation alongside CLI
-   Integration with FastAPI as taught in the course
-   Store data in JSON format
-   Additional cybersecurity modules
-   Docker support for easy deployment
-   Real-time threat intelligence integration
-   Multi-language support
-   Mobile application version

---