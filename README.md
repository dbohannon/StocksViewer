# StocksViewer
Lightweight Flask web application used to retrieve and graph real-time stock price data. This application is used to demonstrate the debugger RCE vulnerability in early versions of Werkzeug.

### To run on a *nix system:
```
pip install -r requirements.txt 
sudo python app/main.py 
```

### To access:
Navigate to http://<ip_or_domain>/ticker/<refresh_time_minutes>/<stock_symbol>
For example, http://localhost/ticker/5/aapl

### To get RCE:
...you'll have to do some research and hacking of your own!
