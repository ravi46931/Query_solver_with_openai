from flask import Flask, render_template, request
from openai_practice import (
    text_summarization,
    few_shot_prompting,
    custom_steps,
    description,
    sentiment,
)


app = Flask(__name__)
TASKS = ["Few Shot", "Text Summarization", "Custom Steps", "Description", "Sentiment"]


@app.route("/")
def index():
    return render_template("index.html", tasks=TASKS)


@app.route("/submit", methods=["POST"])
def submit():
    message = request.form["message"]
    task = request.form["task"]
    if task == "Text Summarization":
        answer = text_summarization(message)
    elif task == "Few Shot":
        answer = few_shot_prompting(message)
    elif task == "Custom Steps":
        subtask = request.form["subtask"]
        language = request.form["language"]
        output_type = request.form["output_type"]
        answer = custom_steps(message, subtask, language, output_type)
    elif task == "Description":
        answer = description(message)
    elif task == "Sentiment":
        answer = sentiment(message)
    return render_template("response.html", response=answer)


if __name__ == "__main__":
    app.run(debug=True)
