from flask import Flask, jsonify,request
import json
import random
import tensorflow as tf
import numpy as np
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer 
nltk.download("punkt")
nltk.download('wordnet')
nltk.download('omw-1.4')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)


__data = None
__listdata = None


@app.route("/")
def index():
    global __data
    with open("./artifacts/organ_wikipedia.txt",'r') as f:
        __data = f.readlines()
    __listdata = []
    for line in __data:
        for item in line.strip().split():
            __listdata.append(item)
    print(__listdata)
    pass

@app.route("/get_response",methods=['GET','POST'])
def get_response():
    user_response = request.form['user_text']
    bot_response = get_bot_response(user_response)
    response = jsonify({
            'bot_response':bot_response
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

def get_bot_response(input):
    global __data
    global __listdata

     #Append the query to the sentences list
    __listdata.append(input)
    #Create the sentences vector based on the list
    vectorizer = TfidfVectorizer()
    sentences_vectors = vectorizer.fit_transform(__listdata)
    
    #Measure the cosine similarity and take the second closest index because the first index is the user query
    vector_values = cosine_similarity(sentences_vectors[-1], sentences_vectors)
    answer = __listdata[vector_values.argsort()[0][-2]]
    #Final check to make sure there are result present. If all the result are 0, means the text input by us are not captured in the corpus
    input_check = vector_values.flatten()
    input_check.sort()
    
    if input_check[-2] == 0:
        return "Any other debt-o's?"
    else: 
        return answer


if __name__ =="__main__":
    # load_artifacts()
    app.run()