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

import numpy as np
from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components 



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

    
    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    plot = figure(title="Data from Quandle WIKI set", x_axis_label='Date', x_axis_type='datetime', y_axis_label='Price')

    def datetime(x):
        return np.array(x, dtype=np.datetime64)

    # add a line renderer with legend and line thickness
    plot.line(datetime(datess), openprices, legend="Temp.", line_width=2)


    script, div = components(plot)
    return render_template('graph.html', script=script, div=div)
    # show the results


if __name__ == '__main__':
    app.run(port=33507)