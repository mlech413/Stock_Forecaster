# API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, request, render_template, jsonify
import yfinance as yf
import numpy as np
import pickle
print(f"pickle version: {pickle.format_version}")

app = Flask(__name__)
# port = int(os.getenv('PORT'))

# Load the model
model = pickle.load(open('./model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    # # symbol = request.args.get('symbol', default="^VIX")
    # user_entered_index_value = ""
    # # Get the VIX current value
    # quote = yf.Ticker('^VIX')
    # vix_info = quote.info
    # vix_close = vix_info['previousClose']
    # quote = yf.Ticker('%5EGSPC')
    # sp500_info = quote.info
    # print("VIX previous close: ", vix_info['previousClose'])
    # print("VIX 52-week high ", vix_info['fiftyTwoWeekHigh'])
    # print("VIX 52-week low: ", vix_info['fiftyTwoWeekLow'])
    # print("S&P500 previous close: ", sp500_info['previousClose'])
    # print("S&P500 52-week high ", sp500_info['fiftyTwoWeekHigh'])
    # print("S&P500 52-week low: ", sp500_info['fiftyTwoWeekLow'])
    # # Make a prediction using the model
    # prediction = model.predict([[vix_info['previousClose']]])
    # # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
    # prediction_based_on_last_close = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
    # return render_template("index.html", prediction_based_on_last_close=prediction_based_on_last_close, vix_close=vix_close, user_entered_index_value=user_entered_index_value)
    
    print("Hello")
    return render_template("index.html")


# @app.route('/predict',methods=['GET', 'POST'])
# def predict():
#     # Get the data from the POST request.
#     if request.method == "POST":
#         # Get the VIX current value
#         quote = yf.Ticker('^VIX')
#         vix_info = quote.info
#         vix_close = vix_info['previousClose']
#         quote = yf.Ticker('%5EGSPC')
#         sp500_info = quote.info
#         print("VIX previous close: ", vix_info['previousClose'])
#         print("VIX 52-week high ", vix_info['fiftyTwoWeekHigh'])
#         print("VIX 52-week low: ", vix_info['fiftyTwoWeekLow'])
#         print("S&P500 previous close: ", sp500_info['previousClose'])
#         print("S&P500 52-week high ", sp500_info['fiftyTwoWeekHigh'])
#         print("S&P500 52-week low: ", sp500_info['fiftyTwoWeekLow'])
#         # Print out user-entered value
#         print("User entered index_value: ", request.form['index_value'])
#         data = float(request.form['index_value'])
#         # Print out data value from model
#         print("Model data: ", model.predict([[data]]))
#         # Make a prediction using the model
#         prediction = model.predict([[vix_info['previousClose']]])
#         # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
#         prediction_based_on_last_close = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
#         # Make a prediction using the model
#         prediction = model.predict([[data]])
#         # Multiple by 100, round, convert to string, remove leading & trailing [] array brackets, add % sign
#         user_model_output = str(np.round(prediction[0]*100, 2))[1:][:-1]+"%"
#         # return render_template("index.html", model_output=model_output, vix_close=vix_close)
#         return render_template("index.html", vix_close=vix_close, prediction_based_on_last_close=prediction_based_on_last_close, user_entered_index_value=data, user_model_output=user_model_output )

    

# @app.route("/quote")
# def display_quote():

#     symbol = request.args.get('symbol', default="^VIX")

#     quote = yf.Ticker(symbol)
#     print(quote.info['regularMarketPreviousClose'])
#     return quote.info


# @app.route("/history")
# def display_history():

#     symbol = request.args.get('symbol', default="^VIX")
#     period = request.args.get('period', default="1y")
#     interval = request.args.get('interval', default="1d")        
#     quote = yf.Ticker(symbol)   
#     hist = quote.history(period=period, interval=interval)["Close"]
#     # hist = quote.history(period=period, interval=interval)
#     for i in hist:
#         print(i)
#     # datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
#     data = hist.to_json()
#     return data


if __name__ == '__main__':
    app.run(debug=True)
