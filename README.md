# K8s Doctor AI ☸️🤖

AI-powered Kubernetes Troubleshooting Assistant built using Python, Streamlit, and Ollama.

## 🚀 Overview

K8s Doctor AI helps DevOps Engineers, Cloud Engineers, and SREs quickly diagnose Kubernetes issues from pod logs and describe outputs.

Instead of manually searching documentation and troubleshooting guides, users can paste Kubernetes logs and instantly receive:

* Issue Detection
* Root Cause Analysis
* Suggested Fixes
* AI-Powered Explanations

The project combines rule-based troubleshooting with AI-assisted analysis to provide faster and more reliable diagnostics.

---

## ✨ Features

### 🔍 Kubernetes Issue Detection

Detects common Kubernetes failures including:

* CrashLoopBackOff
* ImagePullBackOff
* ErrImagePull
* OOMKilled
* CreateContainerError
* CreateContainerConfigError

### 🧠 AI-Powered Analysis

Powered by Ollama to provide:

* Root cause explanations
* Troubleshooting guidance
* Human-friendly summaries
* Recommended remediation steps

### ⚡ Hybrid Diagnosis Engine

The application follows a hybrid approach:

1. Parse Kubernetes logs
2. Detect known issues using rule-based logic
3. Map issues to predefined solutions
4. Generate AI-enhanced explanations using Ollama
5. Fall back gracefully if AI services are unavailable

### 🎨 Streamlit User Interface

* Easy-to-use web interface
* Example Kubernetes logs included
* Interactive troubleshooting experience

---

## 🏗️ Architecture

```text
User Input
     │
     ▼
 Streamlit UI
     │
     ▼
   Parser
     │
     ▼
  Analyzer
     │
     ▼
 Issue Mapping
     │
     ▼
 Ollama AI
     │
     ▼
 Diagnosis + Fix
```

---

## 📂 Project Structure

```text
k8s-doctor-ai/
│
├── app.py
├── ui.py
├── parser.py
├── analyzer.py
├── test_ai.py
├── requirements.txt
├── README.md
│
├── sample_data/
│
└── __pycache__/
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama
* Kubernetes
* Regex
* Log Parsing

---

## 📈 Development Progress

### Day 1 ✅

* Repository created
* Project planning completed
* Initial README added

### Day 2 ✅

* Implemented parser module
* Implemented analyzer module
* Added Kubernetes issue mappings
* Modularized project structure
* CLI testing completed

### Day 3 ✅

* Integrated Ollama
* Built AI troubleshooting layer
* Added hybrid diagnosis engine
* Added error handling and fallback logic
* Tested AI responses

### Day 4 ✅

* Added Streamlit UI
* Added example Kubernetes logs
* Improved user experience
* Fixed dependency issues
* Connected UI with diagnosis engine

---

## 🎯 Example Workflow

1. Paste Kubernetes logs
2. Click Analyze
3. Detect issue automatically
4. Generate AI-powered explanation
5. View recommended fixes

---



