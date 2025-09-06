from flask import Flask,request,render_template

app = Flask(__name__)

# Variable rules
@app.route('/success/<int:score>')
def success(score):
    # return "the person score is, "+ str(score)
    res = ""
    if score > 50:
        res = "pass"
    else:
        res = "fail"

    return render_template('result.html', result=res)                
@app.route('/route_name')
def method_name():
    pass





if __name__ == "__main__":
    app.run(debug=True)