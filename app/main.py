#import dependencies
from flask import Flask, render_template, request
from plotly import plotly, graph_objs
import requests
import json
from collections import OrderedDict
from random import randint

#create and configure flask app
app = Flask(__name__, static_url_path = "/static")
filename = "static/price_history.png"

#define route(s)
@app.route('/ticker/<interval>/<symbol>')
def createTicker(interval, symbol):

    #Get historical data for symbol (for 52 weeks)
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol="+symbol+"&apikey=0ZOBQU6TFH7M286O")
    dates = []
    price = []
    response_object = json.loads(response.content, object_pairs_hook=OrderedDict)
    counter = 0
    for week in response_object["Weekly Time Series"]:
        dates.append(week)
        price.append(response_object["Weekly Time Series"].get(week)["4. close"])
        counter = counter + 1
        if counter > 51:
            break;

    #Graph historical data for symbol
    price_history = graph_objs.Scatter(
        x = dates,
        y = price,
        name = symbol.upper(),
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 4
        )
    )
    data = [price_history]
    layout = dict(title = "1-Year Price History",
            xaxis = dict(title = "Date"),
            yaxis = dict(title = "$ Price")
    )
    fig = dict(data = data, layout = layout)

    #if we reach the limit of plotly requests for free tier, catch error 
    try:
        plotly.image.save_as(fig, filename = "app/" + filename)
    except:
	print "Graph unavailable at this time"
    
    #return template which gets real-time prices for symbol
    return render_template("ticker.html", symbol=symbol.upper(), interval=int(interval)*1000*60, graph=request.url_root + filename + "?" + str(randint(100000, 999999))) 

#run app on localhost:80
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int("80"))

