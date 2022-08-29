# from crypt import methods
import pickle
# import api.service 1.urls as service_1

import random
# import api.service 2.urls as service 2 
# import api.servite 3.urls as service 3
#import flask
from flask import redirect,Flask,render_template,request,app
from flask import app
app=Flask(__name__)
lr=pickle.load(open('lr.pkl','rb'))
print(1)
@app.route('/',methods=['GET','POST'])
def index():
    print('ijdtngdi')
    return render_template('template/index.html')
print("render_template('index.html')")
@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
      prediction=lr.predict([[request.form.get('area'),request.form.get('bedrooms')
      ,request.form.get('bathrooms'),request.form.get('stories'),request.form.get('mainroad'),
      request.form.get('guestroom'),request.form.get('basement'),
      request.form.get('hotwatering'),request.form.get('airconditioning'),request.form.get('parking')
      ,request.form.get('prefare'),request.form.get('furnishingstatus')]])
      output=round(prediction[0],2)
      return render_template('index.html',prediction_text='total house price is {output}/-')
      print('hello')
    except:
      print('try hello')
      return render_template('index.html',prediction_text='something went wrong')

if __name__=='main':
    app.run(use_evalex=False)
print(9)
