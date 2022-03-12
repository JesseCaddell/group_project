from flask import Flask, render_template, request, url_for, redirect, session
from test_list import test_list

app = Flask(__name__)
app.config.from_object('myapplication.default_settings')
app.config.from_envvar('MYAPPLICATION_SETTINGS')

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        queryterm = request.form["search"]
        session['passed_queryterm'] = queryterm
        return redirect(url_for("result", queryterm=queryterm))
    else:
        return render_template('submit.html')

@app.route("/result")
def result():
    result = test_list
    passed_queryterm = session.get('passed_queryterm', None)
    return render_template('result.html', result=result, passed_queryterm=passed_queryterm)


if __name__ == "__main__":
   
    app.run(debug=True)