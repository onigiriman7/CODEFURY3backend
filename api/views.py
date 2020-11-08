from flask import Blueprint,jsonify,request,Response,redirect,render_template,url_for
from werkzeug.utils import secure_filename
from . import db
from .models import FileMaker1,LabourData
import pickle
from translate import Translator
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
classifier = pickle.load(open('classifer.model', 'rb'))
count_vect = pickle.load(open('vec_file.pkl', 'rb'))
trans = Translator(from_lang="Kannada", to_lang="English")

def predict(string):
    predstr = string
    length = 5
    str_error = False

    
    try:
        translated = trans.translate(predstr)
        # predstr = str(f'{t.text}')
        
        return classifier.predict(count_vect.transform([translated]))[0]
        str_error = True
    except AttributeError:
        pass

main = Blueprint("main", __name__)
@main.route('/')
def home():
    return render_template('home.html')

@main.route("/labourData")
def labourData():
    data_list = LabourData.query.all()
    workers = []
    for worker in data_list:
        workers.append({"id":worker.id,"name":worker.name, "village": worker.village, "work_exp": worker.work_exp, "aadhar_id": worker.aadhar_id, "skills": worker.skill})
    return jsonify({"workers": workers})

@main.route("/formSubmission",methods=["POST","GET"])
def formSubmission():
    MLskill = predict(request.form.get("work_exp"))
    if request.form:
        labour = LabourData(name=request.form.get("name"),village=request.form.get("village"),work_exp=request.form.get("work_exp"),aadhar_id=request.form.get("aadhar_id"),skill=MLskill)
        db.session.add(labour)
        db.session.commit()
    currentLab = LabourData.query.filter_by(aadhar_id=request.form.get("aadhar_id")).first()
    print(currentLab)
    return render_template('form.html', skill = MLskill, name=request.form.get("name"))

@main.route('/deleteAllData')
def remove():
    db.session.query(LabourData).delete()
    db.session.commit() 
    return "All entries deleted", 200