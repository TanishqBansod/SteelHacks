from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Google Generative AI with your API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


@app.route("/")
def forum():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def Tutor():
    user_input = request.form["user_input"]  # Get input from the form

    # Create the model with the provided configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [user_input],
            }
        ]
    )

    response = chat_session.send_message(user_input)

    return render_template(
        "index.html", result=response.text
    )  # Pass the response back to the template


if __name__ == "__main__":
    app.run(debug=True)
