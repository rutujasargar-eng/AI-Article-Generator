# 🤖 AI Article Generator

> **AI-Powered Article Generation, Improvement & SEO Assistant**

AI Article Generator is an AI-powered web application that generates high-quality articles based on a given **topic, tone, and length**.

The application also provides AI-powered tools for **article improvement, grammar correction, content simplification, and SEO assistance** using Google's Gemini API.

---

## 🚀 Features

### 📝 AI Article Generation

Generate structured articles using Google Gemini AI.

Users can:

* Enter any topic
* Select the article tone
* Select the article length
* Generate structured content including:

  * Title
  * Introduction
  * Headings
  * Main Content
  * Conclusion

---

### ✨ AI Article Improver

Improve generated articles using different AI-powered options:

* Make it more professional
* Make it more engaging
* Fix grammar
* Simplify the language
* Make it SEO-friendly

---

### 🔍 AI SEO Assistant

Analyze an article and generate:

* 5 relevant SEO keywords
* SEO-friendly meta description

---

### 📋 Copy Article

Users can copy the generated article directly to their clipboard with a single click.

---

### 📱 Responsive Design

The application is designed to work across different screen sizes:

* 💻 Desktop
* 💻 Laptop
* 📱 Mobile

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI / LLM

* Google Gemini API
* `google-genai`

### Environment Management

* Python-dotenv

---

## 🏗️ Project Structure

```text id="9e2xq3"
AI-Article-Generator/
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash id="2h9c8m"
git clone https://github.com/rutujasargar-eng/AI-Article-Generator.git
```

### 2. Open the Project

```bash id="7x4q1a"
cd AI-Article-Generator
```

### 3. Create a Virtual Environment

```bash id="5k8n2p"
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell id="m6p3qz"
venv\Scripts\activate
```

### 5. Install Dependencies

```bash id="r4t8wy"
pip install -r requirements.txt
```

### 6. Configure the Gemini API Key

Create a file named:

```text id="q2n7vd"
.env
```

Add your Gemini API key:

```env id="k3f9sx"
GEMINI_API_KEY=your_gemini_api_key
```

> ⚠️ **Never upload your `.env` file or API key to GitHub.**

Make sure `.env` is included in your `.gitignore` file.

### 7. Run the Application

```bash id="u8c5le"
python app.py
```

The application will be available locally at:

```text id="v1r6ka"
http://127.0.0.1:5000
```

---

## 🧠 AI Model

This project uses Google's Gemini API through the official **Google GenAI Python SDK**.

The application currently uses:

```text id="n4y8tc"
gemini-3.5-flash-lite
```

The AI model is used for:

* Article generation
* Article rewriting
* Grammar improvement
* Content simplification
* SEO analysis
* Content optimization

---

## 🔄 Application Workflow

```text id="b7q2md"
User Enters Article Topic
          ↓
Selects Tone and Length
          ↓
Frontend Sends Request
          ↓
Flask Backend Receives Request
          ↓
Flask Creates AI Prompt
          ↓
Gemini Generates Response
          ↓
Flask Returns AI Response
          ↓
Article Displayed on Website
          ↓
User Can Improve Article
          ↓
User Can Generate SEO Information
```

---

## 🔐 Security

The Gemini API key is stored securely using an environment variable:

```text id="z3m8kp"
.env
```

The `.env` file is excluded from Git using `.gitignore`.

This helps prevent sensitive API credentials from being accidentally uploaded to the public GitHub repository.

> **Security Best Practice:** Never hard-code API keys directly into Python, JavaScript, HTML, or other source files.

---

## 📌 Future Improvements

Potential future enhancements include:

* 👤 User Authentication
* 📚 Article History
* 📥 Download Articles as PDF
* 🔢 Word Count Analysis
* ⏱️ Reading-Time Analysis
* 📊 SEO Score
* 🔑 Keyword Density Analysis
* 🤖 Multiple AI Model Support
* 🗄️ Database Integration
* ☁️ Cloud Deployment

---

## 🎯 Project Purpose

This project was developed as an **AI/ML portfolio project** to demonstrate practical experience with:

* Generative AI
* Large Language Models (LLMs)
* LLM API Integration
* Prompt Engineering
* Flask Backend Development
* REST API Communication
* Frontend Development
* Environment Variable Management
* AI-Powered Content Processing

---

## 💡 Project Highlights

The project demonstrates how a traditional web application can be enhanced with **Generative AI capabilities**.

It combines a simple web interface with a Flask backend and Gemini API to provide an end-to-end AI-powered content generation and optimization workflow.

---

## 👨‍💻 Author

**Hrishikesh**

**B.Tech Artificial Intelligence**

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ **Star** on GitHub!
