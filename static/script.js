const generateBtn = document.getElementById("generateBtn");
const copyBtn = document.getElementById("copyBtn");

const topicInput = document.getElementById("topic");
const toneInput = document.getElementById("tone");
const lengthInput = document.getElementById("length");

const articleOutput = document.getElementById("articleOutput");
const loading = document.getElementById("loading");


// Generate Article
generateBtn.addEventListener("click", async () => {

    const topic = topicInput.value.trim();
    const tone = toneInput.value;
    const length = lengthInput.value;

    // Validate topic
    if (!topic) {
        alert("Please enter an article topic.");
        topicInput.focus();
        return;
    }

    // Show loading state
    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";

    loading.classList.remove("hidden");

    articleOutput.innerHTML = "";


    try {

        const response = await fetch("/generate", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                topic: topic,
                tone: tone,
                length: length
            })
        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }


        // Display generated article
        articleOutput.textContent = data.article;


    } catch (error) {

        articleOutput.innerHTML = `
            <p class="error">
                ❌ ${error.message}
            </p>
        `;

    } finally {

        // Hide loading state
        loading.classList.add("hidden");

        generateBtn.disabled = false;
        generateBtn.textContent = "Generate Article";
    }

});


// Copy Article
copyBtn.addEventListener("click", async () => {

    const article = articleOutput.textContent.trim();

    if (!article || article === "Your AI-generated article will appear here.") {
        alert("There is no article to copy.");
        return;
    }

    try {

        await navigator.clipboard.writeText(article);

        copyBtn.textContent = "✅ Copied!";

        setTimeout(() => {
            copyBtn.textContent = "📋 Copy";
        }, 2000);

    } catch (error) {

        alert("Unable to copy the article.");

    }

});

// Improve Article

const improveBtn = document.getElementById("improveBtn");
const improveType = document.getElementById("improveType");


improveBtn.addEventListener("click", async () => {

    const article = articleOutput.textContent.trim();
    const improvement = improveType.value;

    if (!article || article === "Your AI-generated article will appear here.") {
        alert("Please generate an article first.");
        return;
    }

    improveBtn.disabled = true;
    improveBtn.textContent = "Improving...";

    loading.classList.remove("hidden");
    loading.textContent = "AI is improving your article...";


    try {

        const response = await fetch("/improve", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                article: article,
                improve_type: improvement
            })
        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(
                data.error || "Unable to improve article."
            );
        }


        articleOutput.textContent = data.article;


    } catch (error) {

        articleOutput.innerHTML = `
            <p class="error">
                ❌ ${error.message}
            </p>
        `;

    } finally {

        loading.classList.add("hidden");
        loading.textContent = "Generating your article...";

        improveBtn.disabled = false;
        improveBtn.textContent = "✨ Improve Article";
    }

});

// ==========================================
// SEO ASSISTANT
// ==========================================

const seoBtn = document.getElementById("seoBtn");
const seoOutput = document.getElementById("seoOutput");


seoBtn.addEventListener("click", async () => {

    const article = articleOutput.textContent.trim();


    // Check article
    if (
        !article ||
        article === "Your AI-generated article will appear here."
    ) {

        alert("Please generate an article first.");
        return;
    }


    // Button loading state
    seoBtn.disabled = true;
    seoBtn.textContent = "Generating SEO...";

    seoOutput.classList.remove("hidden");

    seoOutput.textContent = "🔍 AI is analyzing your article...";


    try {

        const response = await fetch("/seo", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                article: article
            })
        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Unable to generate SEO information."
            );
        }


        // Display SEO result
        seoOutput.textContent = data.seo;


    } catch (error) {

        seoOutput.textContent =
            `❌ ${error.message}`;

    } finally {

        seoBtn.disabled = false;
        seoBtn.textContent = "🔍 Generate SEO";

    }

});