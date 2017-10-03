from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    #print request.headers
    #print request.method
    print request.args
    #print request.form
    #print request
    return render_template('form.html')

@app.route("/main")
def greeting():
    return render_template('greeting.html', username = request.args["username"], method = request.method )

if (__name__ == "__main__"):
    app.debug = True
    app.run()
