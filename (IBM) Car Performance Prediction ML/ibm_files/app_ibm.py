from flask import Flask,redirect,url_for,render_template,request
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Vw0gV1mwrT57bL3ClqgE7ERRcTN0hd0hYiPEULA96Nuo"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app=Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")
    
@app.route('/predict',methods =['POST','GET'])
def predict():
    if request.method == 'POST':
       #model = pickle.load(open('Car_Performance_Prediction_Model.pkl','rb'))
    
        cyl = request.form['cyl']
        dis = request.form['dis']
        hp = request.form['hp']
        w = request.form['w']
        a = request.form['a']
        my = request.form['my']
        
        arr=[[cyl,dis,hp,w,a,my]]
        
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        
        payload_scoring = {"input_data": [{"fields": ['cylinders','displacement','horsepower','weight','acceleration','model year'], "values": arr}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5c594f5c-896e-401c-9804-3e6b0566c32c/predictions?version=2022-03-07', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        #print("Scoring response")
        #print(response_scoring.json())

        op = response_scoring.json()
        pred = op['predictions'][0]['values'][0][0]
        pred = float("{:.2f}".format(pred))
        #print(pred)
		
        #p=model.predict(arr)
       
        return render_template("predict.html",data=pred)
    

if __name__ == '__main__':
    app.run(debug=True)