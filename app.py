#from flask import Flask, render_template, request, redirect
#import requests

#app = Flask(__name__)

#@app.route('/prices', methods=['POST'])
#def prices():
#    tsymbol1 = request.form['tsymbol']
#    r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker='+tsymbol1+'&qopts.columns=open,close,adj_open,adj_close&api_key=Y2Zioiyb9r16QRthEeyU')
#    json_object = r.json()
#    datalist = list(json_object[datatable][data])
#    return str(datalist)
    #return render_template('prices.html')
    #return redirect('/index')

#@app.route('/index')
#def index():
#    return render_template('index.html')

#if __name__ == '__main__':
#    app.run(host = '0.0.0.0', port = 33507)


from flask import Flask, render_template, request, redirect
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prices', methods=['POST'])
def prices():
    tsymbol1 = request.form['tsymbol']
    r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker='+tsymbol1+'&qopts.columns=date,open,close,adj_open,adj_close&api_key=Y2Zioiyb9r16QRthEeyU')
    json_object = r.json()
    datalist = json_object['datatable']['data']
    #return render_template('prices.html')
    #return redirect('/index')
    df = pd.DataFrame(datalist)
    datess = df[df.columns[0]].tolist()
    openprices = df[df.columns[1]].tolist()
    closeprices = df[df.columns[2]].tolist()
    adjopenprices = df[df.columns[3]].tolist()
    adjcloseprices = df[df.columns[4]].tolist()
    
    return render_template('prices.html', date = datess, openList=openprices, closeList=closeprices, adjopenList= adjopenprices, adjcloseList = adjcloseprices ) #insert attributes here if needed




if __name__ == '__main__':
    app.run(port=33507)