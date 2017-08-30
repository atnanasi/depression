from flask import Flask, render_template, request, redirect, url_for

app = Flask("depression")

@app.route('/')
def index():
    return render_template('index.html')

def run():
    app.run(host='0.0.0.0')