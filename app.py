from curses import flash
from pyexpat import model
from tkinter import Scale
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

def new_func(__name__):
    app = Flask(__name__)
    file1 = pickle.load(open('model.pkl', 'rb'))
    return app

app = new_func(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='	Species should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    prediction = new_func1()

    output = prediction[0]
    return jsonify(output)

def new_func1():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    return prediction

def new_func2(__name__, app):
    if __name__ == "__main__":
        app.run(debug=True)

new_func2(__name__, app)


app1= flash(__name__)
file2= pickle.load(open("scale.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    output = new_func3()

    return render_template('index.html', prediction_text='	Species should be $ {}'.format(output))

def new_func3():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = Scale.predict(final_features)

    return new_func4(prediction)

def new_func4(prediction):
    output = round(prediction[0], 2)
    return output

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app1.run(debug=True)
