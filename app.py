from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os
import time


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# CREATE FLASK APPLICATION
# ==========================================

app = Flask(__name__)

# ==========================================
# GEMINI API CONFIGURATION
# ==========================================

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=gemini_api_key)

# Gemini model
MODEL_NAME = "gemini-3.5-flash-lite"


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# GENERATE ARTICLE
# ==========================================

@app.route("/generate", methods=["POST"])
def generate_article():

    try:

        # Get data from frontend
        data = request.get_json()

        topic = data.get("topic", "").strip()
        tone = data.get("tone", "Professional")
        length = data.get("length", "Medium")

        # ----------------------------------
        # Validate topic
        # ----------------------------------

        if not topic:

            return jsonify({
                "error": "Please enter an article topic."
            }), 400

        # ----------------------------------
        # Create prompt
        # ----------------------------------

        prompt = f"""
You are an expert AI article writer.

Write a high-quality article about:

Topic: {topic}
Tone: {tone}
Length: {length}

Requirements:

- Create an engaging title.
- Write a strong introduction.
- Organize the article using clear headings.
- Provide useful and informative content.
- Keep the writing original and easy to understand.
- Use proper paragraphs.
- End with a meaningful conclusion.
- Do not include unnecessary explanations.
- Return only the article.
"""

        # ----------------------------------
        # Generate article with retry
        # ----------------------------------

        max_retries = 3
        article = None

        for attempt in range(max_retries):

            try:

                print(
                    f"Generating article..."
                    f" (Attempt {attempt + 1}/{max_retries})"
                )

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                article = response.text

                print("Article generated successfully!")

                break

            except Exception as e:

                print(f"Gemini error: {e}")

                # Last attempt
                if attempt == max_retries - 1:

                    return jsonify({
                        "error": str(e)
                    }), 503

                # Wait before retry
                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

        # ----------------------------------
        # Check generated article
        # ----------------------------------

        if not article:

            return jsonify({
                "error": "Unable to generate article."
            }), 500

        # ----------------------------------
        # Send article to frontend
        # ----------------------------------

        return jsonify({
            "article": article
        })

    except Exception as e:

        print("Application error:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# IMPROVE ARTICLE
# ==========================================

@app.route("/improve", methods=["POST"])
def improve_article():

    try:

        # Get data from frontend
        data = request.get_json()

        article = data.get("article", "").strip()
        improve_type = data.get(
            "improve_type",
            "professional"
        )

        # ----------------------------------
        # Validate article
        # ----------------------------------

        if not article:

            return jsonify({
                "error": "Please generate an article first."
            }), 400

        # ----------------------------------
        # Improvement instructions
        # ----------------------------------

        instructions = {

            "professional":
                "Rewrite the article in a more professional and polished tone.",

            "engaging":
                "Rewrite the article to make it more engaging, interesting, and reader-friendly.",

            "grammar":
                "Fix grammar, spelling, punctuation, and sentence structure while preserving the original meaning.",

            "simple":
                "Rewrite the article using simpler and easier-to-understand language.",

            "seo":
                "Rewrite the article to make it more SEO-friendly while keeping it natural and informative."
        }

        instruction = instructions.get(
            improve_type,
            instructions["professional"]
        )

        # ----------------------------------
        # Create improvement prompt
        # ----------------------------------

        prompt = f"""
You are an expert AI content editor.

{instruction}

Important requirements:

- Preserve the main information and meaning.
- Do not add false information.
- Keep the article well structured.
- Keep the title and headings.
- Improve readability.
- Return only the improved article.

ARTICLE:

{article}
"""

        # ----------------------------------
        # Improve article with retry
        # ----------------------------------

        max_retries = 3
        improved_article = None

        for attempt in range(max_retries):

            try:

                print(
                    f"Improving article..."
                    f" (Attempt {attempt + 1}/{max_retries})"
                )

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                improved_article = response.text

                print("Article improved successfully!")

                break

            except Exception as e:

                print(f"Gemini error: {e}")

                # Last attempt
                if attempt == max_retries - 1:

                    return jsonify({
                        "error": str(e)
                    }), 503

                # Wait before retry
                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

        # ----------------------------------
        # Check improved article
        # ----------------------------------

        if not improved_article:

            return jsonify({
                "error": "Unable to improve article."
            }), 500

        # ----------------------------------
        # Send improved article
        # ----------------------------------

        return jsonify({
            "article": improved_article
        })

    except Exception as e:

        print("Application error:", e)

        return jsonify({
            "error": str(e)
        }), 500

# ==========================================
# SEO ASSISTANT
# ==========================================

@app.route("/seo", methods=["POST"])
def generate_seo():

    try:

        data = request.get_json()

        article = data.get("article", "").strip()

        if not article:
            return jsonify({
                "error": "Please generate an article first."
            }), 400

        prompt = f"""
You are an expert SEO content strategist.

Analyze the following article and create SEO information.

ARTICLE:

{article}

Return the result in exactly this format:

SEO KEYWORDS:
keyword 1
keyword 2
keyword 3
keyword 4
keyword 5

META DESCRIPTION:
Write a compelling SEO meta description between 140 and 160 characters.

Requirements:
- Provide exactly 5 relevant keywords.
- Keywords should be directly related to the article.
- Make the meta description clear and attractive.
- Do not use hashtags.
- Do not add explanations outside this format.
"""

        max_retries = 3
        seo_result = None

        for attempt in range(max_retries):

            try:

                print(
                    f"Generating SEO..."
                    f" (Attempt {attempt + 1}/{max_retries})"
                )

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                seo_result = response.text

                print("SEO generated successfully!")

                break

            except Exception as e:

                print(f"Gemini error: {e}")

                if attempt == max_retries - 1:
                    return jsonify({
                        "error": str(e)
                    }), 503

                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

        if not seo_result:
            return jsonify({
                "error": "Unable to generate SEO information."
            }), 500

        return jsonify({
            "seo": seo_result
        })

    except Exception as e:

        print("Application error:", e)

        return jsonify({
            "error": str(e)
        }), 500



# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)