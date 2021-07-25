import flask
from flask import request
app = flask.Flask(__name__)


from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1> API server is running </h1>'


# pridict page route
@app.route('/predict')
def predict():
    import joblib
    model = joblib.load('marriage_age_predict_model.ml')
    age_predict = model.predict([[1, 15, 2, 35, 6, 5]])
    return str(age_predict)


app.run(debug=True)