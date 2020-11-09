from flask import Flask, render_template, request
from time import sleep
import pickle
from translate import Translator
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

count_vect = CountVectorizer()

classifier = pickle.load(open('classifer.model', 'rb'))
count_vect = pickle.load(open('vec_file.pkl', 'rb'))
trans = Translator(from_lang="Kannada", to_lang="English")

df1 = pd.read_csv("opening.csv")


def predict(string):
    predstr = string
    try:
        value = str(classifier.predict(count_vect.transform([string]))[0])
        return value
        # return "Your field of work seems to be in the "+str(value)+" category"
    except AttributeError:
        pass


def dispfun(val):
    df2 = pd.read_csv("opening.csv")
    df2 = df2.loc[df2['work'] == val.capitalize()]
    df2 = df2.sort_values('monthly pay', ascending=False)
    companies = df2[['name', 'area', 'monthly pay']].values.tolist()
    prstmt = "The openings for "+val+" category are\n""'"+companies[0][0]+"' in "+companies[0][1]+" with "+str(companies[0][2])+" per month;\n"+"'"+companies[1][0]+"' in "+companies[1][1]+" with "+str(companies[1][2])+" per month;\n"+"'"+companies[2][0]+"' in "+companies[2][1]+" with "+str(companies[2][2])+" per month."
    return prstmt
app = Flask(__name__)
application = app
@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    sleep(0.5)
    if userText in ['bye', 'goodbye', 'thanks bye', 'thanks, bye', 'thank you, bye', 'thank you, goodbye', 'thanks', 'thank you']:
        return str("Have a nice day")
        exit()
    elif userText in ["Hi", "hi", "hello", "hey", "helloo", "hellooo", "good morining",  "gmorning",  "good morning", "morning", "good day", "good afternoon", "good evening", "greetings"]:
        return str("Greetings! How can I help you today?")
    else:
        predval = predict(str(userText))
        companies = dispfun(predval)
        return companies
     
if __name__ == "__main__":    
   app.run()
