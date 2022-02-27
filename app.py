from flask import Flask, render_template

app = Flask(__name__)

#variables to alter between local and production environments
local = '/'
prod = '/hello_flask.html'

@app.route(local)
def index():
    return render_template('index.html')




if (__name__ == "__main__"):
    app.run(debug=True)
