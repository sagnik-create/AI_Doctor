from flask import Flask, render_template, request

app = Flask(__name__)

# Define some diseases and their associated symptoms
disease_symptoms = {
    'Flu': ['fever', 'cough', 'sore throat', 'runny nose'],
    'Cold': ['sneezing', 'stuffy nose', 'sore throat'],
    'Migraine': ['headache', 'nausea', 'sensitivity to light'],
    'COVID-19': ['fever', 'cough', 'difficulty breathing', 'loss of taste']
}

def diagnose(symptoms):
    possible_diseases = []
    for disease, disease_symptoms in disease_symptoms.items():
        if all(symptom in symptoms for symptom in disease_symptoms):
            possible_diseases.append(disease)
    return possible_diseases

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    if request.method == 'POST':
        symptoms_input = request.form.get('symptoms')
        symptoms = [s.strip().lower() for s in symptoms_input.split(',')]
        diagnosis = diagnose(symptoms)
    
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
