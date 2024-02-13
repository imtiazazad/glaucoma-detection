from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)
model = None
model_file_path = r'C:\Users\Zahid Hasan\OneDrive\Desktop\dengu\dengu_model.sav'

try:
    with open(model_file_path, 'rb') as file:
        model = pickle.load(file)
except EOFError:
    print("The file is empty or does not exist. Please make sure the file exists and has data in it.")
except Exception as e:
    print(f"An error occurred: {e}")  
else:
    # code that uses the model only if it was successfully loaded
    print(model)

@app.route('/', methods=['GET'])
def Page():
    return render_template('index.html')
@app.route('/home', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        V1 = float(request.form['Age'])
        V2 = int(request.form['Sex'])
        V3 = int(request.form['Total_Days_with_symthoms'])
        V4 = float(request.form['Current_Body_Temperature'])
        V5 = int(request.form['Severe_Headache'])
        V6 = int(request.form['Pain_Behind_the_Eyes'])
        V7 = int(request.form['Joint_and_Muscle_Aches'])
        V8 = int(request.form['Metallic_Taste_in_the_Mouth'])
        V9 = int(request.form['Appetite_Loss'])
        V10 = int(request.form['Abdominal_Pain'])
        V11 = int(request.form['Nausea_Vomiting'])
        V12 = int(request.form['Diarrhoea'])
        V13 = float(request.form['Hemoglobin (g/dL)'])
        V14 = float(request.form['WBC(cmm)'])
        V15 = float(request.form['Hematocrit(HCT)%'])
        V16 = float(request.form['MCV(fl)'])
        V17 = float(request.form['MCH(pg)'])
        V18 = float(request.form['MCHC(g/dL)'])
        V19 = float(request.form['RBC(million/cmm)'])
        V20 = float(request.form['Neutrophil(%)'])
        V21 = float(request.form['Lymphocyte(%)'])
        V22 = float(request.form['Monocyte(%)'])
        V23 = float(request.form['Eosinophil(%)'])
     
        V24_str = request.form['Platelet(cmm)']

        # Convert 'Platelet (cmm)' to numeric, handle non-numeric values
        try:
            V24_str = float(V24_str.replace(',', ''))  # Remove commas if present
        except ValueError:
            return "Invalid Platelet value. Please check your input."

        # ... (your existing code)

        # Make sure the 'model' variable is accessible
        if model is not None:
            values = np.array([[V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23,V24_str]])
            prediction = model.predict(values)
            prediction = round(prediction[0], 2)
            if prediction == 0:
                prediction_text = 'POSITIVE'
            else:
                prediction_text = 'NEGATIVE'

            return render_template('dashboard.html', prediction_text=prediction_text)
        else:
            return "Model not loaded. Please check the model file."

@app.route('/dashboard', methods=['GET', 'POST']) 
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
