from flask import Flask, render_template, request, url_for, redirect, session
from test_list import test_list

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/submit")
def submit():
        return render_template('submit.html')


@app.route('/addquery', methods=["POST", "GET"])
def new_query():
    if request.method == "POST":
        query = request.form['search']
        result = test_list
        new_list = []

        
        if query in result:
            new_list.append(query)
            
                
        
        else:
            new_list = ["search invalid"]

        

        return render_template("result.html", query=query, new_list=new_list )




if __name__ == "__main__":

    app.run(debug=True)
