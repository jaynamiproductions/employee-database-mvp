from flask import Blueprint, render_template as rt, request, flash, jsonify, send_file
from flask_login import login_required,current_user
from .models import Demo, Cert, Form
from . import db
import json
from io import BytesIO
import sqlite3


views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    return rt('home.html',user=current_user)

@views.route('/demographics',methods=['GET','POST'])
@login_required
def demo():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        maiden = request.form.get('maiden')
        sbid = request.form.get('sbid')
        position = request.form.get('position')
        linenum = request.form.get('linenum')
        dept = request.form.get('dept')
        ccnn = request.form.get('ccnn')
        salary = request.form.get('salary')
        appt = request.form.get('appt')
        hiredate = request.form.get('hiredate')
        apptdate = request.form.get('apptdate')
        supervisor = request.form.get('supervisor')
        sbemail = request.form.get('sbemail')
        home = request.form.get('home')




    
        field = Demo.query.filter(Demo.user_id==current_user.id).first()
        if field:
            db.session.delete(field)
            db.session.commit()
        full_demo = Demo(
            fname=fname,
            lname=lname,
            maiden=maiden,
            sbid=sbid,
            position=position,
            linenum=linenum,
            dept=dept,
            ccnn=ccnn,
            salary=salary,
            appt=appt,
            hiredate=hiredate,
            apptdate=apptdate,
            supervisor=supervisor,
            sbemail=sbemail,
            home=home,
            user_id=current_user.id)
        db.session.add(full_demo)
        db.session.commit()

        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql1 = 'SELECT * FROM demo WHERE user_id=' + str(current_user.id)
    c.execute(sql1)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('demo.html',user=current_user,data=output[0])
    except:
        return rt('demo.html',user=current_user,data=output)

@views.route('/certificates',methods=['GET','POST'])
@login_required
def cert():
    if request.method == 'POST':
        acls = request.form.get('acls')
        trophon = request.form.get('trophon')
        full_cert = Cert(acls_cert=acls,annual_trophon=trophon,user_id=current_user.id)

        field = Cert.query.filter(Cert.user_id==current_user.id).first()
        if field:
            db.session.delete(field)
            db.session.commit()

        db.session.add(full_cert)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql1 = 'SELECT * FROM cert WHERE user_id=' + str(current_user.id)
    c.execute(sql1)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('certs.html',user=current_user,data=output[0])
    except:
        return rt('certs.html',user=current_user,data=output)

@views.route('/admin', methods=['GET','POST'])
@login_required
def admin(): # set admin users here
    if current_user.email == 'jason1@gmail.com':
        flash('Successfully accessed Admin page.',category='Success')
        connect = sqlite3.connect('instance/database.db')
        c = connect.cursor()
        sql1 = 'SELECT * FROM demo'
        c.execute(sql1)
        output = c.fetchall()
        c.close()
        connect.close()
        return rt('admin2.html',user=current_user,data=output)
    else:
        flash('Admin page access denied.',category='Error')
        return rt('admin.html',user=current_user)
    

@views.route('/forms',methods=['GET','POST'])
@login_required
def form():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        file4 = request.files['file4']
        file5 = request.files['file5']
        file6 = request.files['file6']
        file7 = request.files['file7']
        if file1 == None:
            flash('Upload .',category='Success')


        full_form = Form(
            kronos=file1.filename,kronosdata=file1.read(),
            performance=file2.filename,performancedata=file2.read(),
            attestation=file3.filename,attestationdata=file3.read(),
            ivcontrast=file4.filename,ivcontrastdata=file4.read(),
            supportperform=file5.filename,supportperformdata=file5.read(),
            couns=file6.filename,counsdata=file6.read(),
            hybrid=file7.filename,hybriddata=file7.read(),
            user_id=current_user.id
            )

        field = Form.query.filter(Form.user_id==current_user.id).first()
        if field:
            db.session.delete(field)
            db.session.commit()

        db.session.add(full_form)
        db.session.commit()

        flash('Information saved in database.',category='Success')
    
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql1 = 'SELECT * FROM form WHERE user_id=' + str(current_user.id)
    c.execute(sql1)
    output = c.fetchall()
    c.close()
    connect.close()

    return rt('forms.html',user=current_user,data=output)


@views.route('/kronos_download/<upload_id>')
def kronos_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.kronosdata), download_name=upload.kronos,as_attachment=True)

@views.route('/performance_download/<upload_id>')
def performance_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.performancedata), download_name=upload.performance,as_attachment=True)

@views.route('/attestation_download/<upload_id>')
def attestation_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.attestationdata), download_name=upload.attestation,as_attachment=True)

@views.route('/ivcontrast_download/<upload_id>')
def ivcontrast_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.ivcontrastdata), download_name=upload.ivcontrast,as_attachment=True)

@views.route('/supportperform_download/<upload_id>')
def supportperform_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.supportperformdata), download_name=upload.supportperform,as_attachment=True)

@views.route('/couns_download/<upload_id>')
def coun_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.counsdata), download_name=upload.couns,as_attachment=True)

@views.route('/hybrid_download/<upload_id>')
def hybrid_download(upload_id):
    upload = Form.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.hybriddata), download_name=upload.hybrid,as_attachment=True)





@views.route('/delete-field', methods=['POST']) 
def delete_note():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Demo.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field2', methods=['POST'])
def delete_note2():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Cert.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field3', methods=['POST'])
def delete_note3():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Form.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})






