from flask import Flask, redirect, url_for, render_template, request
import requests
import sys
import trainer as tr
import webbrowser
import pandas
import main
import time
app = Flask(__name__)
result = ""

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == "POST":
        url = request.form['url']
        r = requests.get(url)
        a_url = r.url
        print(r.url)
        main.process_test_url(a_url, 'test_features.csv')
        return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
        a = str(return_ans).split()
        print("-----")
        print("return_ans:",return_ans)
        print("-----")
        if int(a[1]) == 0:
            result = "The URL : " +a_url+ " is safe to visit"
            return render_template("index.html", prediction1 = result)
        elif int(a[1]) == 1:
            result = "The URL : " +a_url+ " is Malicious"
            return render_template("index.html", prediction2 = result)
        else:
            result = "The URL : " +a_url+ " is Malware"
            return render_template("index.html", prediction3 = result)
        #return render_template("index.html", prediction = result)



if __name__ == "__main__":
    app.run(debug=False)
