from flask import Flask, render_template, request, session
from main import run_llm, run_chat
import markdown

app = Flask(__name__)
app.secret_key = "thisisasupersecretkey124"


@app.route("/", methods=["GET", "POST"])
def google_test():

    if 'llm_response' not in session:
        session['llm_response'] = ""
    if 'chat_history' not in session:
        session['chat_history'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = run_llm(session['prompt'])
            session['llm_response'] = markdown.markdown(session['llm_response'])

            session['chat_history'] = run_chat(session['prompt'])

    return render_template("google_test.html",
                           llm_response=session['llm_response'],
                           chat_history=session['chat_history'],
                           )


@app.route("/markdown", methods=["GET", "POST"])
def google_test_markdown():

    if 'llm_response' not in session:
        session['llm_response'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = run_llm(session['prompt'])
            print(f"--------------------TEST TEST TEST ------------------------- /// llm response b4 markdown: {session['llm_response']}")
            session['llm_response'] = markdown.markdown(session['llm_response'])
            print(
                f"--------------------TEST TEST TEST ------------------------- /// llm response after markdown: {session['llm_response']}")

    return render_template("google_test_markdown.html",
                           llm_response=session['llm_response'],
                           )


@app.route("/html", methods=["GET", "POST"])
def html_test():

    if 'llm_response' not in session:
        session['llm_response'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = run_llm(session['prompt'])
            session['llm_response'] = markdown.markdown(session['llm_response'])

    return render_template("html_test.html",
                           llm_response=session['llm_response'],
                           )


if __name__ == "__main__":
    app.run()
