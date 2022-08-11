# app.py
from flask import Flask, Response, render_template, request, jsonify
from radix.getdata import load_data
from lst.getinput import Predict_Next_Words
from autocomplete.autofill import autocompletion
import json
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import re
import pandas as pd
from wtforms import *


app = Flask(__name__,template_folder='templates')

df = pd.read_excel("../input/sales-dataset/Sales-Dataset-2.xlsx")
Item_count = df["Item_Purchased"].value_counts()
df2 = pd.DataFrame(Item_count)
a = list(df['Item_Purchased'])
# Load the model and tokenizer

model = load_model('nextword1.h5')
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

class SearchForm(Form):
    autocomp = TextAreaField('Search', id='autocomplete')




#Radix
@app.route('/_autocomplete')
def autocomplete():
    query = request.args.get("q", '')
    output = load_data(filepath=r'C:\Projects\treeview\item_counts.csv', n=5, name_value=query)
    main_output = pd.DataFrame({"Item_names ": output[0], "count" : output [1]})
    # main_output.to_html(header=True,table_id=table)
    return render_template(matching_results=main_output)

#lst
@app.route('/lstm')
def recommend():
    data = request.args.get("q",'')
    next_word = Predict_Next_Words(model, tokenizer, data)
    full_text = ''.join(data + " " + next_word)

    # def check_content():
    l = []
    pred_lst = []
    pred_lst_count = []
    for i in range(len(a)):
        if re.search(full_text.upper(), a[i].upper()):
            l.append(a[i])
    brand = set(l)
    for i in brand:
        pred_lst.append(i)
        pred_lst_count.append(df2[df2.index == i]["Item_Purchased"][0])
    df_out = pd.DataFrame({"Items": pred_lst, "Counts": pred_lst_count})
    return df_out

#autocomplete
@app.route('/fill')
def fast():
    input = request.args.get("q", '')
    out = autocompletion(input)
    return out



@app.route('/', methods=['GET'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)