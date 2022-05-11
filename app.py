from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__, template_folder='template')
model_name = open('svm_model.pkl','rb')
svm_model=pickle.load(model_name)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/send', methods=['GET','POST'])
def predict():
    if request.method == "POST" :
    
        Gender = request.form['gender']
        ssc_p = request.form['ssc_p']
        hsc_p = request.form['hsc_p']
        hsc_s = request.form['hsc_s1']
        degree_p = request.form['degree_p']
        degree_t = request.form['degree_t1']
        workex = request.form['workex1']
        etest_p = request.form['etest_p']
        specialisation = request.form['specialisation1']
        mba_p = request.form['mba_p']
       
        
        if Gender == 'M':
            gender = 0
        else:
            gender = 1
    
        
        if degree_t == 'Sci&Tech':
            degree_t1 = 2
        elif degree_t == 'Comm&Mgmt':
            degree_t1 = 0
        else:
            degree_t1 = 1 
    
        if workex == 'Yes':
            workex1 = 1
        else:
            workex1 = 0
        
        if hsc_s == 'Commerce':
            hsc_s1 = 1
        elif hsc_s == 'Science':
            hsc_s1 = 2
        else:
            hsc_s1 = 0
        
        if specialisation == 'Mkt&HR':
            specialisation1 = 1
        else:
            specialisation1 = 0
    
        Pred_args=[gender,ssc_p,hsc_p,hsc_s1,degree_p,degree_t1,workex1,etest_p,specialisation1,mba_p]
        pred_args=np.array(Pred_args)
        pred_args=pred_args.reshape(1,-1)
        
        y_pred=svm_model.predict(pred_args)
        y_pred=y_pred[0]
        if y_pred == 0:
            return render_template('show.html',res="Work Hard!!! Chances are less") 
        else:
            return render_template('show.html',res=" You are Doing well!! You Will Get placements")
    
    
    


if __name__ == '__main__':
    app.run()