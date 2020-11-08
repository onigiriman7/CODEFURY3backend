from . import db
class FileMaker1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_name = db.Column(db.String(50))
    img = db.Column(db.String(50), unique=True)
    mimetype = db.Column(db.String(500))

class LabourData1(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    village = db.Column(db.String(50))
    work_exp = db.Column(db.String(1000))
    aadhar_id = db.Column(db.String(50))
    skill = db.Column(db.String(200))

class LabourData(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    village = db.Column(db.String(50))
    work_exp = db.Column(db.String(1000))
    aadhar_id = db.Column(db.String(50))
    skill = db.Column(db.String(200))