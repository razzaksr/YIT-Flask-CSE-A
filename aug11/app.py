from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

customers = [
    {"weight":87,"height":170.67,"age":20,"gender":"female"},
    {"weight":92.21,"height":180.987,"age":33,"gender":"female"},
    {"weight":55,"height":170,"age":21,"gender":"male"},
    {"weight":45.89,"height":150,"age":19,"gender":"male"}
]

@app.route("/view",methods=["GET"])
def viewTable(): return render_template('view.html',data=customers)

@app.route("/findbmr",methods=["GET","POST"])
def calculateBmr():
    if request.method == "GET": return render_template('index.html')
    else:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        if gender == "male": bmr = 10*weight+6.25*height-5*age+5
        else: bmr = 10*weight+6.25*height-5*age-161
        return render_template('index.html',calculated=bmr)
        
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message":"Welcome to Python Flask"})

if __name__ == "__main__":
    app.run('localhost',9999)