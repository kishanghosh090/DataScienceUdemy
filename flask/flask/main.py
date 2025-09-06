from flask import Flask,render_template 
# render_template is used to render html pages

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"

@app.route("/home")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/form',methods=['GET','POST'])
def method_name():
    if method_name == 'POST':
        return "this is post method"
    else:
        return "this is get method"

if __name__ == "__main__":
    app.run(debug=True)