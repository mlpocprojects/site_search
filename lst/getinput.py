from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import pickle
import re
model = load_model(r'C:\Users\Admin\PycharmProjects\recommendation_system\nextword1.h5')
tokenizer = pickle.load(open(r'C:\Users\Admin\PycharmProjects\recommendation_system\tokenizer1.pkl', 'rb'))


# def Pred_word_fun(model, tokenizer, text):
#     df = pd.read_excel(r"C:\Users\Admin\Downloads\Sales-Dataset-2.xlsx")
#     Item_count = df["Item_Purchased"].value_counts()
#     df2 = pd.DataFrame(Item_count)
#     a = list(df['Item_Purchased'])
#
#     # Load the model and tokenizer

    # model = load_model(r'C:\Users\Admin\PycharmProjects\recommendation_system\nextword1.h5')
    # tokenizer = pickle.load(open(r'C:\Users\Admin\PycharmProjects\recommendation_system\tokenizer1.pkl', 'rb'))

def Predict_Next_Words(model, tokenizer, text):
    df = pd.read_excel(r"C:\Users\Admin\Downloads\Sales-Dataset-2.xlsx")
    Item_count = df["Item_Purchased"].value_counts()
    df2 = pd.DataFrame(Item_count)
    a = list(df['Item_Purchased'])
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ""

    for key, value in tokenizer.word_index.items():
        if value == preds:
            predicted_word = key
            break

        print(predicted_word)
    return predicted_word

    text = input("Enter your line: ")
    # next_word = Predict_Next_Words(model, tokenizer, text)
    # full_text = ''.join(text + " " + next_word)
    #
    # # def check_content():
    # l = []
    # pred_lst = []
    # pred_lst_count = []
    # for i in range(len(a)):
    #     if re.search(full_text.upper(), a[i].upper()):
    #         l.append(a[i])
    # brand = set(l)
    # for i in brand:
    #     pred_lst.append(i)
    #     pred_lst_count.append(df2[df2.index == i]["Item_Purchased"][0])
    # df_out = pd.DataFrame({"Items": pred_lst, "Counts": pred_lst_count})
    # print(df_out)


# Pred_word_fun('Boosah')





