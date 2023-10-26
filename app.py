from flask import *
import numpy as np
import pandas as pd
import pickle
import jsonify

app = Flask(__name__)

model = pickle.load(open('adaboost.pkl','rb'))

# with open('models/adaboost.pkl', 'rb') as file:
#     model = pickle.load(file)


# Sample model prediction function (you would use your actual model)
def predict_mh_condition(age, gender, family_history, benefits, care_options, anonymity, leave, work_interfere, seek_help):
    # Example: A simple condition where if benefits are 0 (No), it predicts "Good Mental Health"
    return 1 if benefits == 0 else 0

def convert_benefits(value):
    if value == 0:
        return 'No'
    elif value == 1:
        return 'Yes'
    else:
        return "Don't Know"

def convert_family_history(value):
    if value == 0:
        return 'No'
    elif value == 1:
        return 'Yes'

@app.route('/')
def home():
    return render_template('index.html', results="")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            Age = float(request.form['Age'])
            Gender = int(request.form['Gender'])
            family_history = int(request.form['family_history'])
            benefits = int(request.form['benefits'])
            care_options = int(request.form['care_options'])
            anonymity = int(request.form['anonymity'])
            leave = int(request.form['leave'])
            work_interfere = int(request.form['work_interfere'])
            seek_help = int(request.form['seek_help'])

            prediction = predict_mh_condition(Age, Gender, family_history, benefits, care_options, anonymity, leave, work_interfere, seek_help)

            benefits_label = convert_benefits(benefits)
            family_history_label = convert_family_history(family_history)

            if prediction == 1:
                result = f"Based on your inputs, it appears that you have good mental health."
            else:
                result = f"Based on your inputs, you may want to seek help for your mental health."
        except ValueError as e:
            result = f"Error: {str(e)}"

        return render_template('index.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)
