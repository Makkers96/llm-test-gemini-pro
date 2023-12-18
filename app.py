from flask import Flask, render_template, request, session
from main import run_llm
from IPython.display import display
from IPython.display import Markdown

app = Flask(__name__)
app.secret_key = "thisisasupersecretkey124"


@app.route("/", methods=["GET", "POST"])
def google_test():

    if 'llm_response' not in session:
        session['llm_response'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = run_llm(session['prompt'])

    return render_template("google_test.html",
                           llm_response=session['llm_response'],
                           )


@app.route("/markdown", methods=["GET", "POST"])
def google_test_markdown():

    if 'llm_response' not in session:
        session['llm_response'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = Markdown(run_llm(session['prompt']).text)

    return render_template("google_test.html",
                           llm_response=session['llm_response'],
                           )


if __name__ == "__main__":
    app.run()