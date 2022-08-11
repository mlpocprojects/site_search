import pandas as pd
import numpy as np
from fast_autocomplete import autocomplete_factory
import json
import flask


def autocompletion(letters):
    sales_data = pd.read_csv("word_cnt.csv")

    brandname_list = list(sales_data['Item_Name'])
    brandname_split_list = list(list(sales_data['Item_Name'].str.split()))
    item_count_list = list(sales_data['Count'])

    brandname_count_dict = {}
    for i in range(len(brandname_list)):
        brandname_count_dict.update({f'{brandname_list[i]}': [
            {"make": brandname_split_list[i][0], "model": brandname_split_list[i][1]},
            f'{(" ".join(brandname_split_list[i][0:2]))}', int(item_count_list[i])]})
    with open("input_data.json", "w") as fp:
        json.dump(brandname_count_dict, fp)

    content_files = {
        'words': {
            'filepath': 'input_data.json',
            'compress': True  # means compress the graph data in memory
        }
    }

    autocomplete_with_count = autocomplete_factory(content_files=content_files)
    result_list = autocomplete_with_count.search(word=letters, max_cost=14, size=25)
    result = []
    for i in range(len(result_list)):
        print(result_list[i][0], sales_data[sales_data['Item_Name'] == result_list[i][0]]['Count'].item())
        result.append([result_list[i][0], sales_data[sales_data['Item_Name'] == result_list[i][0]]['Count'].item()])

    result

    return result