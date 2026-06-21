# K8s Doctor AI ☸️🤖

AI-powered Kubernetes Troubleshooting Assistant built with Python, Streamlit, and Ollama.

## Overview

K8s Doctor AI helps developers and DevOps engineers quickly identify Kubernetes issues from pod logs and describe outputs.

The application combines:

* Rule-based Kubernetes issue detection
* AI-powered root cause analysis using Ollama
* Streamlit web interface
* Hybrid diagnosis engine with fallback support

---

## Features

### Rule-Based Analysis

Detects common Kubernetes issues such as:

* CrashLoopBackOff
* ImagePullBackOff
* ErrImagePull
* OOMKilled
* CreateContainerError
* CreateContainerConfigError

### AI-Powered Diagnosis

Uses Ollama to generate:

* Root cause explanations
* Human-friendly troubleshooting guidance
* Suggested remediation steps

### Hybrid Engine

The application follows a hybrid approach:

1. Parser identifies known Kubernetes issues.
2. Analyzer maps issues to predefined solutions.
3. Ollama enhances the response with AI-generated explanations.
4. Fallback handling ensures graceful behavior when AI is unavailable.

---

## Project Structure

```text
k8s-doctor-ai/
│
├── app.py
├── parser.py
├── analyzer.py
├── test_ai.py
├── requirements.txt
├── README.md
│
└── sample_data/
```

---

## Current Progress

### Day 1 ✅

* Repository created
* Project planning completed
* Initial README added

### Day 2 ✅

* Parser implementation
* Analyzer implementation
* Modular project structure
* Kubernetes issue mapping engine

### Day 3 ✅

* Ollama integration
* AI response testing
* Hybrid engine implementation
* Error handling and fallback support

---

## Tech Stack

* Python
* Streamlit
* Ollama
* Kubernetes
* Regex
* Log Parsing

---

## Future Enhancements

* Upload Kubernetes logs directly
* Enhanced Streamlit dashboard
* Docker support
* More Kubernetes issue signatures
* Multi-cluster troubleshooting support

---

