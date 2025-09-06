from flask import Flask,render_template,request
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
    if request.method == 'POST':
        print(request.form.get('email'))
        print("this is post method")
        return "this is post method"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)