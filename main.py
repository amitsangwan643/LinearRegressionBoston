#import liberaries
import pickle
from flask import Flask , request,render_template,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/prediction",methods=["POST"])
def predict_price():
    if request.method=="POST":
        try:
            RAD = float(request.form["RAD"])
            DIS = float(request.form["DIS"])
            RM = float(request.form["RM"])
            B = float(request.form["B"])
            CHAS = float(request.form["CHAS"])
            PTRATIO = float(request.form["PTRATIO"])
            LSTAT = float(request.form["LSTAT"])
        except :
            print("Please give values correctly")
        try:
            model=pickle.load(open("linearregmodel.pickle","rb"))
            value=model.predict([[RAD,DIS,RM,B,CHAS,PTRATIO,LSTAT]])
            print("price of house is : ",round(value[0],3),"k $")
        except:
            print("Problem occured during value prediction")
    return render_template("houseprice.html",result=round(value[0],3))


if __name__=="__main__":
    app.run(debug=True)