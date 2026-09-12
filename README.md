# 🤖 AI Article Generator

An AI-powered web application that generates high-quality articles based on a given topic, tone, and length. It also provides AI-powered article improvement and SEO assistance.

## 🚀 Features

### 📝 AI Article Generation
- Generate articles using Google Gemini AI
- Enter any topic
- Select article tone
- Select article length
- Generates structured content with:
  - Title
  - Introduction
  - Headings
  - Main content
  - Conclusion

### ✨ AI Article Improver
Improve generated articles using different options:

- Make it more professional
- Make it more engaging
- Fix grammar
- Simplify the language
- Make it SEO-friendly

### 🔍 AI SEO Assistant
Analyze an article and generate:

- 5 relevant SEO keywords
- SEO-friendly meta description

### 📋 Copy Article
Copy the generated article directly to the clipboard.

### 📱 Responsive Design
The application is designed to work on:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### AI / LLM
- Google Gemini API
- `google-genai`

### Environment Management
- Python-dotenv

---

## 🏗️ Project Structure

```text
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

⚙️ How to Run Locally
1. Clone the repository
git clone https://github.com/rutujasargar-eng/AI-Article-Generator.git
2. Open the project
cd AI-Article-Generator
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Create a .env file

Create a file named:

.env

Add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key

Never upload your .env file or API key to GitHub.

7. Run the application
python app.py

The application will run locally at:

http://127.0.0.1:5000
🧠 AI Model

This project uses Google's Gemini API through the official Python SDK.

The application currently uses:

gemini-3.5-flash-lite

The model is used for:

Article generation
Article rewriting
Grammar improvement
Content simplification
SEO analysis
🔄 Application Workflow
User enters article topic
          ↓
Selects tone and length
          ↓
Frontend sends request to Flask
          ↓
Flask creates AI prompt
          ↓
Gemini generates article
          ↓
Flask returns AI response
          ↓
Article displayed on website
          ↓
User can improve article
          ↓
User can generate SEO information
🔐 Security

The Gemini API key is stored in an environment variable:

.env

The .env file is excluded from Git using .gitignore.

This prevents sensitive API credentials from being uploaded to the public repository.

📌 Future Improvements
User authentication
Article history
Download article as PDF
Word count and reading-time analysis
SEO score
Keyword density analysis
Multiple AI model support
Database integration
Cloud deployment
🎯 Project Purpose

This project was developed as an AI/ML portfolio project to demonstrate practical experience with:

Generative AI
LLM API integration
Prompt engineering
Flask backend development
REST API communication
Frontend development
Environment variable management
AI-powered content processing
👨‍💻 Author

Hrishikesh

B.Tech Artificial Intelligence

⭐ If you find this project useful, consider giving it a star!


### 3. Save the file

Press:

```text
Ctrl + S