from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


classifier = pickle.load(open('score.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        grescore = int(request.form['grescore'])
        toeflscore = int(request.form['toeflscore'])
        rating = request.form['rating']
        SOP = float(request.form['sop'])
        LOR = float(request.form['lor'])
        CGPA = float(request.form['cgpa'])
        Research = request.form['Research']
        if Research == 'yes':
            Research = 1
        else:
            Research = 0

        prediction = classifier.predict([[grescore, toeflscore, rating, SOP, LOR, CGPA,
                                     Research]])
        output = prediction[0] * 100

        if output > 0:
            return render_template('index.html', prediction_text="The chance of getting an Admit is "+format(round(output))+" Percentage")
        else:
            return render_template('index.html', prediction_text="Please try Again")






if __name__ == "__main__":
    app.run(debug=True)
