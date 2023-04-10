from . import db
from flask_login import UserMixin
import datetime

class Demographics(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    maiden = db.Column(db.String(50))
    sbid = db.Column(db.Integer)
    position = db.Column(db.String(50))
    linenum = db.Column(db.Integer)
    dept = db.Column(db.String(50))
    ccnn = db.Column(db.String(50))
    salary = db.Column(db.String(50))
    appt = db.Column(db.String(50))
    hiredate = db.Column(db.String(50))
    apptdate = db.Column(db.String(50))
    supervisor = db.Column(db.String(50))
    sbemail = db.Column(db.String(50))
    home = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.String(50))
    hphone = db.Column(db.String(50))
    cphone = db.Column(db.String(50))
    wphone = db.Column(db.String(50))
    wext = db.Column(db.String(50))
    dob = db.Column(db.String(50))
    emergencyname = db.Column(db.String(50))
    emergencyphone = db.Column(db.String(50))
    emergencyrelation = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Certifications(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    acls_cert = db.Column(db.String(50))
    annual_trophon = db.Column(db.String(50))
    ardms = db.Column(db.String(50))
    arrt = db.Column(db.String(50))
    bls = db.Column(db.String(50))
    cci = db.Column(db.String(50))
    school1 = db.Column(db.String(50))
    edu1 = db.Column(db.String(50))
    major1 = db.Column(db.String(50))
    school2 = db.Column(db.String(50))
    edu2 = db.Column(db.String(50))
    major2 = db.Column(db.String(50))
    nurse_asst = db.Column(db.String(50))
    nysnurse_asst = db.Column(db.String(50))
    rn = db.Column(db.String(50))
    nysrn = db.Column(db.String(50))
    doh = db.Column(db.String(50))
    pals = db.Column(db.String(50))
    radiographer = db.Column(db.String(50))
    visa = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Clinical_edu(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rn_na_comp = db.Column(db.String(50))
    rn_na_recert = db.Column(db.String(50))
    rn_na_orien = db.Column(db.String(50))
    linen = db.Column(db.String(50))
    linendata = db.Column(db.LargeBinary)
    pyxis = db.Column(db.String(50))
    pyxisdata = db.Column(db.LargeBinary)
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Emp_notes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    blood_don = db.Column(db.String(50))
    blood_dondata = db.Column(db.LargeBinary)
    cancerscreen = db.Column(db.String(50))
    cancerscreendata = db.Column(db.LargeBinary)
    issuednote = db.Column(db.String(50))
    issuednotedata = db.Column(db.LargeBinary)
    medical = db.Column(db.String(50))
    medicaldata = db.Column(db.LargeBinary)
    proofdeath = db.Column(db.String(50))
    proofdeathdata = db.Column(db.LargeBinary)
    resignation = db.Column(db.String(50))
    resignationdata = db.Column(db.LargeBinary)
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Equipment_IT(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    app_access = db.Column(db.String(50))
    electronics = db.Column(db.String(50))
    vpninfo = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Emp_health(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    health_assessment = db.Column(db.String(50))
    covid = db.Column(db.String(50))
    n95 = db.Column(db.String(50))
    vaccination = db.Column(db.String(50))
    vaccinationdata = db.Column(db.LargeBinary)
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Human_resources(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    attestation = db.Column(db.String(50))
    dept_competency = db.Column(db.String(50))
    ivcontrast = db.Column(db.String(50))
    lmsproof = db.Column(db.String(50))
    performance_eval = db.Column(db.String(50))
    performance_program = db.Column(db.String(50))
    trophon = db.Column(db.String(50))
    awards = db.Column(db.String(50))
    orientation = db.Column(db.String(50))
    leave_letter = db.Column(db.String(50))
    expiration_notice = db.Column(db.String(50))
    description = db.Column(db.String(50))
    hospital_checklist = db.Column(db.String(50))
    chartingnumber_request = db.Column(db.String(50))
    appt_packet = db.Column(db.String(50))
    status = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Labor_relations(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    memorandum = db.Column(db.String(50))
    termination = db.Column(db.String(50))
    disciplinerequest = db.Column(db.String(50))
    disciplinenotice = db.Column(db.String(50))
    nonrenewal = db.Column(db.String(50))
    re_appt = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class New_hires(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    resume = db.Column(db.String(50))
    offer = db.Column(db.String(50))
    acceptance = db.Column(db.String(50))
    reference = db.Column(db.String(50))
    internal = db.Column(db.String(50))
    interview = db.Column(db.String(50))
    requisition = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Payroll(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    hospitalchange = db.Column(db.String(50))
    salary = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Timekeeping(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    accrual = db.Column(db.String(50))
    disability = db.Column(db.String(50))
    injurt = db.Column(db.String(50))
    kronos = db.Column(db.String(50))
    overtime = db.Column(db.String(50))
    sbmc_agency = db.Column(db.String(50))
    wc = db.Column(db.String(50))
    misc = db.Column(db.String(50))
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Form(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    kronos = db.Column(db.String(50))
    kronosdata = db.Column(db.LargeBinary)
    performance = db.Column(db.String(50))
    performancedata = db.Column(db.LargeBinary)
    attestation = db.Column(db.String(50))
    attestationdata = db.Column(db.LargeBinary)
    ivcontrast = db.Column(db.String(50))
    ivcontrastdata = db.Column(db.LargeBinary)
    supportperform = db.Column(db.String(50))
    supportperformdata = db.Column(db.LargeBinary)
    couns = db.Column(db.String(50))
    counsdata = db.Column(db.LargeBinary)
    hybrid = db.Column(db.String(50))
    hybriddata = db.Column(db.LargeBinary)
    update = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    demo_info = db.relationship('Demographics')
    cert_info = db.relationship('Certifications')
    clinical_info = db.relationship('Clinical_edu')
    emp_notes_info = db.relationship('Emp_notes')
    equipment_it = db.relationship('Equipment_IT')
    emp_health = db.relationship('Emp_health')
    hr = db.relationship('Human_resources')
    lr = db.relationship('Labor_relations')
    newhires = db.relationship('New_hires')
    payroll_info = db.relationship('Payroll')
    timekeeping_info = db.relationship('Timekeeping')
    form_info = db.relationship('Form')


