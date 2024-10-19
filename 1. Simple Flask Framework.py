from flask import Flask
'''
It create as instance of the Flask class,
which will be our WSGI(Web server Gateway Instance) applicetion.
'''
## create the flask instance
# WSGI Applicetion
app = Flask(__name__)
@app.route(rule='/')
def welcome():
    return "Welcome to my world, This is my first project with flask"

@app.route(rule='/second')
def second():
    return "This is our second page"

if __name__ == "__main__":
    app.run(debug=True)
