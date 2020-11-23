from flask import Flask,render_template,request,make_response,jsonify

app = Flask(__name__)

@app.route('/',methods=['POST'])
def add():
    a=request.form['a']
    b=request.form['b']
    c=a+b
    return{'result':c}

if __name__ == "__main__":
    app.run(debug=True)