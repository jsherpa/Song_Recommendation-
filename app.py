from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from functions import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def render_classifier():
    return render_template('classifier.html')

@app.route('/', methods = ['POST'])
def predict():
    text = request.form.get('text')
    # print(list(model_df.index))
    results = get_rec(text,model_df)
    res = [results,text]
    if results == None:
        return render_template('nope.html', variable = res)
    if results != None:
        return render_template('twss.html', variable = res)

if __name__ == '__main__':
    app.run()
