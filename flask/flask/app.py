from flask import Flask

app = Flask(__name__) # it creates an interface the flask class, which will be your WSGI application

@app.route('/')
def method_name():
    return "welcome to this flask course"




if __name__ == "__main__":
    app.run(debug=True)


