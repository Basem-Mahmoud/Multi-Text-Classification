from flask import Flask, request, render_template,jsonify
from flask_restful import Api, Resource, reqparse
from joblib import dump, load

app = Flask(__name__,template_folder='template')
api = Api(app)
def Model(text1):
    model = load('svm_model.joblib')
    pred_industry = model.predict([text1])
    return pred_industry
 
@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/prediction', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    pred = Model(text1)
    result = {
        "prediction": pred
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

app.run()