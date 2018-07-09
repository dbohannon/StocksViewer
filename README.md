# StocksViewer
Lightweight Flask web application used to retrieve and graph real-time stock price data. This application is used to demonstrate the debugger RCE vulnerability in early versions of Werkzeug.

## Setup

### Run on *nix system:
```bash
pip install -r requirements.txt 
sudo python app/main.py 
```

### Docker
```bash
# build
docker build -t stocksviewer:latest .
# run
docker run -d -p 80:80 stocksviewer
```

### To access:

Navigate to `http://<ip_or_domain>/ticker/<refresh_time_minutes>/<stock_symbol>`

For example, http://localhost/ticker/5/aapl

### To get RCE:
...you'll have to do some research and hacking of your own!
