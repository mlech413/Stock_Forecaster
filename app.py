# API of ML model using Flask

# This code takes API data while POST request an performs the prediction using loaded model and returns the results.

# Import libraries
from flask import Flask, request, render_template 
import yfinance as yf
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model.pkl','rb'))


# Home route
@app.route('/',methods=['GET'])
def home():
    print("HOME")
    # symbol = request.args.get('symbol', default="^VIX")
    user_entered_index_value = ""
    # Get the VIX current value
    quote = yf.Ticker('^VIX')
    vix_info = quote.info
    quote = yf.Ticker('^GSPC')
    sp500_info = quote.info 
    # Format commas and rounding for display on page
    vix_info['fiftyDayAverage'] = (round(vix_info['fiftyDayAverage'],2))
    vix_info['twoHundredDayAverage'] = (round(vix_info['twoHundredDayAverage'],2))
    sp500_info['previousClose'] = ('{:,}'.format(round(sp500_info['previousClose'],2)))
    sp500_info['fiftyTwoWeekHigh'] = ('{:,}'.format(round(sp500_info['fiftyTwoWeekHigh'],2)))
    sp500_info['fiftyTwoWeekLow'] = ('{:,}'.format(round(sp500_info['fiftyTwoWeekLow'],2)))
    sp500_info['fiftyDayAverage'] = ('{:,}'.format(round(sp500_info['fiftyDayAverage'],2)))
    sp500_info['twoHundredDayAverage'] = ('{:,}'.format(round(sp500_info['twoHundredDayAverage'],2)))
    # Make a prediction using the model for the current vix value from the api
    prediction = model.predict([[vix_info['previousClose']]])
    # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
    prediction_based_on_last_close = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
    return render_template("index.html", prediction_based_on_last_close=prediction_based_on_last_close, user_entered_index_value=user_entered_index_value, vix_info=vix_info, sp500_info=sp500_info)


# Predict route
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    print("PREDICT")
    # Get the data from the POST request.
    if request.method == "POST":
        # Get the VIX current value
        quote = yf.Ticker('^VIX')
        vix_info = quote.info
        quote = yf.Ticker('^GSPC')
        sp500_info = quote.info
        # Format commas and rounding for display on page
        vix_info['fiftyDayAverage'] = (round(vix_info['fiftyDayAverage'],2))
        vix_info['twoHundredDayAverage'] = (round(vix_info['twoHundredDayAverage'],2))
        sp500_info['previousClose'] = ('{:,}'.format(round(sp500_info['previousClose'],2)))
        sp500_info['fiftyTwoWeekHigh'] = ('{:,}'.format(round(sp500_info['fiftyTwoWeekHigh'],2)))
        sp500_info['fiftyTwoWeekLow'] = ('{:,}'.format(round(sp500_info['fiftyTwoWeekLow'],2)))
        sp500_info['fiftyDayAverage'] = ('{:,}'.format(round(sp500_info['fiftyDayAverage'],2)))
        sp500_info['twoHundredDayAverage'] = ('{:,}'.format(round(sp500_info['twoHundredDayAverage'],2)))
        # Print out user-entered value
        print("User entered index_value: ", request.form['index_value'])
        # If user hit the enter button without entering a value, replace with zero so the model doesn't error out
        if request.form['index_value'] == "":
            data = 0
        else:
            data = float(request.form['index_value'])
        # Print out data value from model
        print("Model data: ", model.predict([[data]]))
        # Make a prediction using the model for the current vix value from the api
        prediction = model.predict([[vix_info['previousClose']]])
        # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
        prediction_based_on_last_close = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
        # Make a prediction using the model for the USER ENTERED VALUE
        prediction = model.predict([[data]])
        # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
        user_model_output = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
        # return render_template("index.html", model_output=model_output, vix_close=vix_close)
        return render_template("index.html", prediction_based_on_last_close=prediction_based_on_last_close, user_entered_index_value=data, user_model_output=user_model_output, vix_info=vix_info, sp500_info=sp500_info )


# Models route
@app.route('/models',methods=['GET', 'POST'])
def models():
    print("MODELS route")
    return render_template("models.html")


if __name__ == '__main__':
    app.run(debug=True)
