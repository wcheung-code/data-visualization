from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/prices', methods=['POST'])
def prices():
    tsymbol = request.form['tsymbol']
    r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker='+tsymbol+'&qopts.columns=open,close,adj_open,adj_close&api_key=Y2Zioiyb9r16QRthEeyU')
    json_object = r.json()
    datalist = list(json_object[datatable][data])
    return str(datalist)
    #return render_template('prices.html')
    #return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = vagrant:5000)
