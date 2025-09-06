from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

# Variable rules
# jinja2 template
'''
    {{}} expression to print output in html
    {% %} control flow,loops
    {# #} comments
'''
@app.route('/success/<int:score>')
def success(score):
    # return "the person score is, "+ str(score)
    res = ""
    if score > 50:
        res = "pass"
    else:
        res = "fail"

    return render_template('result.html', result=res) 


@app.route('/successResult/<int:score>')
def successResult(score):
    # return "the person score is, "+ str(score)
    res = ""
    if score > 50:
        res = "pass"
    else:
        res = "fail"


    exp = {
        'score':score,
        'result':res
    }
    return render_template('result.html', exp=exp) 


@app.route('/home')
def home():
    # return "the person score is, "+ str(score)
    # res = ""
    # if score > 50:
    #     res = "pass"
    # else:
    #     res = "fail"

    return "<h1> this is home</h1>" 

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        print(request.form.get('email'))
        print("this is post method")
        return redirect(url_for('home'))
        # return f"this is post method {request.form.get('email')}"
    else:
        return render_template("index.html")
    





if __name__ == "__main__":
    app.run(debug=True)