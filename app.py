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
from datetime import datetime
from bokeh.plotting import figure, output_file, show

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
    
    def dateToInt(string):
        datetime_object = datetime.strptime(string, '%Y-%m-%d')
        answer = datetime.today() - datetime_object
        return -answer.days
    
    dates = map(dateToInt, datess)
    
    p1 = figure(title="Data from Quandle WIKI set", x_axis_label='Dates', y_axis_label='Prices')

#plot = figure(title='Data from Quandle WIKI set',
      #        x_axis_label='date',
       #       x_axis_type='datetime')

# add a line renderer with legend and line thickness
    p1.line(dates, openprices, legend="Open Prices", line_width=2)

# show the results
    plot = show(p1)
    
    return render_template('prices.html', graph = plot, date = dates, date2 = datess, openList=openprices, closeList=closeprices, adjopenList= adjopenprices, adjcloseList = adjcloseprices ) #insert attributes here if needed




if __name__ == '__main__':
    app.run(port=33507)