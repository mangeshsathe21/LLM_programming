# 🤖 LLM Organization Review Generator

An AI-powered web application that generates organization and employee reviews using **React**, **FastAPI**, and local **Ollama** LLMs.

---

## 📸 Application Preview

<p align="center">
  <img src="./assets/app-screenshot.png" alt="LLM Review Generator Screenshot" width="800" />
</p>

> *Place your application screenshots inside the `assets/` folder as `app-screenshot.png`.*

---

## ✨ Features

- **AI-Powered Review Generation:** Leverages local LLMs via Ollama to generate contextual reviews.
- **FastAPI Backend:** Lightweight, fast, and async API server managed with `uv`.
- **Interactive React UI:** Responsive frontend for inputting details and displaying AI output in real time.
- **100% Local & Private:** Runs entirely on your machine—no external API keys required.

---

## 🛠️ Tech Stack

- **Frontend:** React, Vite, Node.js (`npm`)
- **Backend:** FastAPI, Python (`uv`)
- **LLM Engine:** [Ollama](https://ollama.com/) (Local runner)

---

## 🚀 Local Setup & Run Guide

Follow these steps to run the application on your local machine.

### Prerequisites

Ensure you have the following installed:
1. **[Node.js](https://nodejs.org/)** (v18+)
2. **[Python](https://www.python.org/)** (v3.10+) and **[uv](https://docs.astral.sh/uv/)**
3. **[Ollama](https://ollama.com/)**

---

### Step 1: Start Ollama

Download and launch your desired LLM model (e.g., `llama3`):

```bash
ollama run llama3