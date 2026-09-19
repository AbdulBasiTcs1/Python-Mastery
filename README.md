<div align="center">

# 🐍 Python Mastery

**A structured, hands-on journey from Python fundamentals to real projects, with notes, code, exercises and tests for every concept.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Last commit](https://img.shields.io/github/last-commit/AbdulBasiTcs1/python-mastery)
![Repo size](https://img.shields.io/github/repo-size/AbdulBasiTcs1/python-mastery)
![Code style](https://img.shields.io/badge/code%20style-ruff-261230)
![Status](https://img.shields.io/badge/status-actively%20learning-brightgreen)

</div>

---

## 📖 About

This repository is my complete Python learning lab. I'm revisiting Python from the ground up, going deeper than syntax and focusing on *understanding* each concept, practicing it, and applying it in small projects.

Every topic follows the same pattern, so the repo stays easy to navigate:

| File | Purpose |
|------|---------|
| `notes.md` | The concept explained in my own words |
| `examples.py` | Clean, commented, runnable code |
| `exercises.py` | Practice problems I solved myself |

The goal is to build a reference I can come back to, and one that anyone learning Python can follow.

---

## 🗺️ Learning Roadmap & Progress

Status: ✅ Done · 🔄 In progress · ⬜ Not started

| # | Module | Topics | Status |
|---|--------|--------|:------:|
| 01 | [Basics](01-basics/) | Variables, data types, operators, input/output, control flow, loops | ⬜ |
| 02 | [Data Structures](02-data-structures/) | Strings, lists, tuples, sets, dictionaries | ⬜ |
| 03 | [Functions](03-functions/) | Arguments, `*args`/`**kwargs`, lambda, scope, recursion | ⬜ |
| 04 | [Files & Errors](04-files-and-errors/) | File I/O, JSON/CSV, exceptions | ⬜ |
| 05 | [OOP](05-oop/) | Classes, inheritance, polymorphism, dunder methods | ⬜ |
| 06 | [Modules & Packages](06-modules-and-packages/) | Imports, packages, `pip`, virtual environments | ⬜ |
| 07 | [Advanced Python](07-advanced/) | Comprehensions, iterators, generators, decorators, context managers | ⬜ |
| 08 | [Standard Library & Tools](08-stdlib-and-tools/) | `datetime`, `pathlib`, `logging`, `pytest` | ⬜ |
| 09 | [Web & APIs](09-web-and-apis/) | `requests`, REST basics, FastAPI/Flask intro | ⬜ |
| 10 | [Data & AI](10-data-and-ai/) | NumPy, Pandas, Matplotlib | ⬜ |

> The full checklist lives in [`ROADMAP.md`](ROADMAP.md).

---

## 🚀 Projects

Each module ends with a small project that applies what I learned.

| Project | Concepts used | Status |
|---------|---------------|:------:|
| CLI To-Do App | Functions, file I/O, JSON | ⬜ |
| Expense Tracker | OOP, CSV, error handling | ⬜ |
| Weather CLI | APIs, `requests`, exceptions | ⬜ |
| Data Analysis Report | Pandas, Matplotlib | ⬜ |

Projects live in [`projects/`](projects/).

---

## 📂 Repository Structure

```
python-mastery/
├── 01-basics/
├── 02-data-structures/
├── 03-functions/
├── 04-files-and-errors/
├── 05-oop/
├── 06-modules-and-packages/
├── 07-advanced/
├── 08-stdlib-and-tools/
├── 09-web-and-apis/
├── 10-data-and-ai/
├── projects/
├── tests/
├── archive/            # my original learning files, kept for history
├── ROADMAP.md
├── requirements.txt
└── README.md
```

Each module contains one folder per topic:

```
01-basics/
└── variables-and-types/
    ├── notes.md
    ├── examples.py
    └── exercises.py
```

---

## ⚙️ Getting Started

**Requirements:** Python 3.10 or newer and Git.

```bash
# 1. Clone the repository
git clone https://github.com/AbdulBasiTcs1/python-mastery.git
cd python-mastery

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run any example
python 01-basics/variables-and-types/examples.py
```

### Run the tests

```bash
pytest
```

---

## 🧭 How I Work

- **One topic per commit**, with clear messages, for example `Add: decorators notes and examples`.
- **Every file runs.** I run the code before committing.
- **Notes in my own words.** If I can't explain it simply, I haven't learned it yet.
- **Apply it.** Each module ends with a project.
- **Consistent style.** Formatting and linting with `ruff`.

---

## 🛠️ Tools

| Tool | Use |
|------|-----|
| Python 3.10+ | Language |
| `venv` + `pip` | Environments & dependencies |
| `pytest` | Testing |
| `ruff` | Linting & formatting |
| Git & GitHub | Version control |

---

## 📌 Notes

- The `archive/` folder holds my earlier Python practice files. I'm keeping them to show how far I've come, and I'm rewriting the best ones into the new structure as I revise.
- This is a learning repo, so code favors clarity over cleverness.

---

## 🤝 Feedback

Found a mistake or have a better way to explain something? Open an [issue](../../issues) or a pull request. Suggestions are welcome.

---

## 👨‍💻 Author

**Abdul Basit**, Full-Stack Developer (MERN + AI) and Computer Science student.

- GitHub: [@AbdulBasiTcs1](https://github.com/AbdulBasiTcs1)
- YouTube: [@AbdulBasit-ProDev](https://www.youtube.com/@AbdulBasit-ProDev)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<div align="center">

⭐ If this repo helps you learn Python, consider giving it a star.

</div>
