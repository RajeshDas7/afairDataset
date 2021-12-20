from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    

    if request.method == 'POST':
        intcr1=1.0
        # occ_2=0.0
        # occ_3=0.0
        # occ_4=0.0
        # occ_5=0.0
        # occ_6=0.0
        # occ_husb_2=0.0
        # occ_husb_3=0.0
        # occ_husb_4=0.0
        # occ_husb_5=0.0
        # occ_husb_6=0.0
        # rate_marriage1=0.0
        # religious1=0.0
        # educ1=0.0
        age = float(request.form['age'])
        yrs_married = float(request.form['yrs_married'])
        children = float(request.form['children'])

       

        
        rate_marriage=request.form['rate_marriage']
        if(rate_marriage=='1'):
                rate_marriage1=1.0
                
        elif(rate_marriage=='2'):
                rate_marriage1=2.0
        elif(rate_marriage=='3'):
                rate_marriage1=3.0
        elif(rate_marriage=='4'):
                rate_marriage1=4.0
        elif(rate_marriage=='5'):
                rate_marriage1=5.0
        else:
            rate_marriage1=0.0


        religious=request.form['religious']
        if(religious=='1'):
                religious1=1.0
                
        elif(religious=='2'):
                religious1=2.0
        elif(religious=='3'):
                religious1=3.0
        elif(religious=='4'):
                religious1=4.0
        else:
                religious1=0.0
        

        educ=request.form['educ']
        if(educ=='9'):
                educ1=9.0
                
        elif(educ=='12'):
                educ1=12.0
        elif(educ=='14'):
                educ1=14.0
        elif(educ=='16'):
                educ1=16.0
        elif(educ=='17'):
                educ1=17.0
        elif(educ=='20'):
                educ1=20.0
        else:
                educ1=0.0

        occupation=request.form['occupation']
        if(occupation=='1'):
                occ_2=0.0
                occ_3=0.0
                occ_4=0.0
                occ_5=0.0
                occ_6=0.0
                
        elif(occupation=='2'):
                occ_2=1.0
                occ_3=0.0
                occ_4=0.0
                occ_5=0.0
                occ_6=0.0
        elif(occupation=='3'):
                occ_2=0.0
                occ_3=1.0
                occ_4=0.0
                occ_5=0.0
                occ_6=0.0
        elif(occupation=='4'):
                occ_2=0.0
                occ_3=0.0
                occ_4=1.0
                occ_5=0.0
                occ_6=0.0
        elif(occupation=='5'):
                occ_2=0.0
                occ_3=0.0
                occ_4=0.0
                occ_5=1.0
                occ_6=0.0
        elif(occupation=='6'):
                occ_2=0.0
                occ_3=0.0
                occ_4=0.0
                occ_5=0.0
                occ_6=1.0
        else:
                occ_2=0.0
                occ_3=0.0
                occ_4=0.0
                occ_5=0.0
                occ_6=0.0
        
        


        occupation_husb=request.form['occupation_husb']
        if(occupation_husb=='1'):

            occ_husb_2=0.0
            occ_husb_3=0.0
            occ_husb_4=0.0
            occ_husb_5=0.0
            occ_husb_6=0.0
                
        elif(occupation_husb=='2'):
            occ_husb_2=1.0
            occ_husb_3=0.0
            occ_husb_4=0.0
            occ_husb_5=0.0
            occ_husb_6=0.0
        elif(occupation_husb=='3'):
            occ_husb_2=0.0
            occ_husb_3=1.0
            occ_husb_4=0.0
            occ_husb_5=0.0
            occ_husb_6=0.0
        elif(occupation_husb=='4'):
            occ_husb_2=0.0
            occ_husb_3=0.0
            occ_husb_4=1.0
            occ_husb_5=0.0
            occ_husb_6=0.0
        elif(occupation_husb=='5'):
            occ_husb_2=0.0
            occ_husb_3=0.0
            occ_husb_4=0.0
            occ_husb_5=1.0
            occ_husb_6=0.0
        elif(occupation_husb=='6'):
            occ_husb_2=0.0
            occ_husb_3=0.0
            occ_husb_4=0.0
            occ_husb_5=0.0
            occ_husb_6=1.0
        else:
            occ_husb_2=0.0
            occ_husb_3=0.0
            occ_husb_4=0.0
            occ_husb_5=0.0
            occ_husb_6=0.0
            


        
        

        
        
        try:
        
            
            prediction=model.predict([[intcr1,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage1,age,yrs_married,children,religious1,educ1]])
        #     prediction_val=[intcr1,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage1,age,yrs_married,children,religious1,educ1]    
        
        #     prediction_text=prediction[0]
        #     return render_template('index.html')
            
        #     result=True
        #     if int(prediction[0])==0:
        #         result=False
        #     else:
        #         pass
        

            if int(prediction[0])<1:
                return render_template('index.html',prediction_text="Affair=True")
            else:
                return render_template('index.html',prediction_text="Affair=False")
        except Exception as e:
            pass

            
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
