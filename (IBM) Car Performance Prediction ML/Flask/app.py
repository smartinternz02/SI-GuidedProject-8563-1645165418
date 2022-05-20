from flask import Flask,redirect,url_for,render_template,request
import pickle
app=Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")
    
@app.route('/predict',methods =['POST','GET'])
def predict():
    if request.method == 'POST':
        model = pickle.load(open('Car_Performance_Prediction_Model.pkl','rb'))
    
        cyl = request.form['cyl']
        dis = request.form['dis']
        hp = request.form['hp']
        w = request.form['w']
        a = request.form['a']
        my = request.form['my']
        
        arr=[[cyl,dis,hp,w,a,my]]
        
        p=model.predict(arr)
        
        p=p[0]
        
        p = float("{:.2f}".format(p))
        
        return render_template("predict.html",data=p)
    

if __name__ == '__main__':
    app.run(debug=True)