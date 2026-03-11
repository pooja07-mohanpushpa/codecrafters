<div align="center">
  <img src="https://img.shields.io/badge/Progress-Hackathon_Idea-brightgreen?style=for-the-badge" alt="Hackathon Project" />
</div>

# 🧠 AI-Powered Programming E-Learning Platform

[![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)](https://expressjs.com/)

> **"Learn to Code Smarter, Not Harder – With AI Tutors and Gamified Practice!"**

---

## 🎯 Project Overview

This project is an **interactive web-based e-learning platform** designed to help users learn programming languages from basic to advanced levels. 

The goal of the platform is to provide a structured learning environment where beginners can easily understand programming concepts visually and interactively, while staying motivated through **AI-generated video lectures, practice problems, quizzes, and a gamified leaderboard system**.

---

## ✨ Key Features

### 1. 📚 Structured Programming Courses
We provide structured learning paths starting from beginner concepts (Variables, Loops) to advanced topics (OOP).
- **Initially supported languages:** 🐍 Python | 🟨 C programming

### 2. 🤖 AI-Generated Lecture Videos
Each topic includes a short **AI-generated lecture video**. A virtual AI teacher explains the concept in a simple, visual manner—perfect for visual and auditory learners.
- 🎬 **Pre-Generated Content:** To ensure high quality and fast loading times, each lesson features a carefully curated, pre-generated AI instructional video that perfectly aligns with the topic.

### 3. 🤔 Interactive Coding Sessions
A dedicated arena to solve programming-related questions in real-time.
- 💻 **Integrated Code Editor:** Practice directly in the browser with an interactive code editor, similar to platforms like HackerRank, complete with syntax highlighting and instant code execution/validation.
- 🎁 **Reward system:** Earn **PathPoints** for successfully passing all test cases on a coding problem!

### 4. 📝 Interactive Quiz Section
A separate quiz module allows users to test their knowledge using targeted multiple-choice questions (MCQs).
- 🧠 **Dynamic Generation:** Quizzes are generated on-the-fly using the **Google Gemini API**, adapting to the lesson content to provide fresh, relevant questions every time.
- 🎁 **Reward system:** Earn **PathPoints** for correctly answering quiz questions!

### 5. 🏆 Global Leaderboard
Rankings based on total accumulated `PathPoints` earned from both the **Coding Sessions** and the **Quiz Section**. This gamified system creates a competitive learning environment and encourages learners to practice and test their knowledge frequently!

### 6. 📊 Progress & Badges
Visual progress indicators track your journey for each course. To keep motivation high, we've integrated a **Star Badge System**:
- Earn a ⭐ **Star Badge** for every **20%** of the course you complete (20%, 40%, 60%, 80%).
- *Example: 📈 Python Course: 40% Completed -> ⭐⭐*

### 7. 🎓 Certificate Generation
Upon reaching **100% completion (5 Stars ⭐⭐⭐⭐⭐)** and finishing the required assessments, users unlock a personalized, downloadable certificate showcasing their achievement.
The certificate includes:
* User Name
* Course Name
* Completion Date
* Platform Name

---

## 🛠️ Technology Stack

### 🎨 Frontend/UI
- **Template Engine**: Django Templates (HTML/CSS)
- **Styling**: Tailwind CSS

### ⚙️ Backend Framework
- **Core**: Python
- **Framework**: Django (Full-Stack)
- **Database**: SQLite (Development) / PostgreSQL (Production)

### 🔧 Auxiliary Tools
- **Code Execution**: Judge0 API / Piston API
- **Code Editor UI**: CodeMirror or Monaco Editor injected via CDN
- **AI Integration**: **Google Gemini API** (Quiz/Content Generation)

---

## 🚀 Project Goal

Our primary objective is to create a modern learning platform that combines:

* 🤖 AI-powered teaching
* 💻 Interactive programming practice
* 🎮 Gamified learning
* 🏆 Competitive leaderboards

This approach helps learners stay engaged while developing programming skills effectively.





---

## 🏃‍♂️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   ```

2. **Navigate to the directory:**
   ```bash
   cd pathmind
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver 
   ```

---
*Built with ❤️ for [Hackathon Name]*