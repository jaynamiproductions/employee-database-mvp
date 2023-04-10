from flask import Blueprint, render_template as rt, request, flash, jsonify, send_file
from flask_login import login_required,current_user
from .models import Demographics, Certifications, Form, Clinical_edu, Emp_notes, Equipment_IT, Emp_health, Human_resources, Labor_relations, New_hires, Payroll, Timekeeping
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
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        hphone = request.form.get('hphone')
        cphone = request.form.get('cphone')
        wphone = request.form.get('wphone')
        wext = request.form.get('wext')
        dob = request.form.get('dob')
        emergencyname = request.form.get('emergencyname')
        emergencyphone = request.form.get('emergencyphone')
        emergencyrelation = request.form.get('emergencyrelation')

        full_demo = Demographics(
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
            city=city,
            state=state,
            zipcode=zipcode,
            hphone=hphone,
            cphone=cphone,
            wphone=wphone,
            wext=wext,
            dob=dob,
            emergencyname=emergencyname,
            emergencyphone=emergencyphone,
            emergencyrelation=emergencyrelation,
            user_id=current_user.id)
        
        field = Demographics.query.filter(Demographics.user_id==current_user.id).first()
        if field:
            db.session.delete(field)
            db.session.commit()
        db.session.add(full_demo)
        db.session.commit()
        flash('Information saved in database.',category='Success')

    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql1 = 'SELECT * FROM demographics WHERE user_id=' + str(current_user.id)
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
        ardms = request.form.get('ardms')
        arrt = request.form.get('arrt')
        bls = request.form.get('bls')
        cci = request.form.get('cci')
        school1 = request.form.get('school1')
        edu1 = request.form.get('edu1')
        major1 = request.form.get('major1')
        school2 = request.form.get('school2')
        edu2 = request.form.get('edu2')
        major2 = request.form.get('major2')
        nurse_asst = request.form.get('nurse_asst')
        nysnurse_asst = request.form.get('nysnurse_asst')
        rn = request.form.get('rn')
        nysrn = request.form.get('nysrn')
        doh = request.form.get('doh')
        pals = request.form.get('pals')
        radiographer = request.form.get('radiographer')
        visa = request.form.get('visa')
        misc = request.form.get('misc')

        full_cert = Certifications(
            acls_cert=acls,
            annual_trophon=trophon,
            ardms=ardms,
            arrt=arrt,
            bls=bls,
            cci=cci,
            school1=school1,
            edu1=edu1,
            major1=major1,
            school2=school2,
            edu2=edu2,
            major2=major2,
            nurse_asst=nurse_asst,
            nysnurse_asst=nysnurse_asst,
            rn=rn,
            nysrn=nysrn,
            doh=doh,
            pals=pals,
            radiographer=radiographer,
            visa=visa,
            misc=misc,
            user_id=current_user.id)

        field = Certifications.query.filter(Certifications.user_id==current_user.id).first()
        if field:
            db.session.delete(field)
            db.session.commit()
        db.session.add(full_cert)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql1 = 'SELECT * FROM certifications WHERE user_id=' + str(current_user.id)
    c.execute(sql1)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('certs.html',user=current_user,data=output[0])
    except:
        return rt('certs.html',user=current_user,data=output)
    
@views.route('/clinical-education', methods=['GET','POST'])
@login_required
def clinical_edu():
    if request.method == 'POST':
        rn_na_comp = request.form.get('rn_na_comp')
        rn_na_recert = request.form.get('rn_na_recert')
        rn_na_orien = request.form.get('rn_na_orien')
        linen = request.files['linen']
        pyxis = request.files['pyxis']
        misc = request.form.get('misc')

        full_clin = Clinical_edu(
            rn_na_comp=rn_na_comp,
            rn_na_recert=rn_na_recert,
            rn_na_orien=rn_na_orien,
            linen=linen.filename,linendata=linen.read(),
            pyxis=pyxis.filename,pyxisdata=pyxis.read(),
            misc=misc,
            user_id=current_user.id)
        
        row = Clinical_edu.query.filter(Clinical_edu.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full_clin)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM clinical_edu WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('clinical.html',user=current_user,data=output[0])
    except:
        return rt('clinical.html',user=current_user,data=output)
    

@views.route('/employee-notes', methods=['GET','POST'])
@login_required
def emp_notes():
    if request.method == 'POST':
        blood_don = request.files['blood_don']
        cancerscreen = request.files['cancerscreen']
        issuednote = request.files['issuednote']
        medical = request.files['medical']
        proofdeath = request.files['proofdeath']
        resignation = request.files['resignation']

        full_notes = Emp_notes(
            blood_don=blood_don.filename,blood_dondata=blood_don.read(),
            cancerscreen=cancerscreen.filename,cancerscreendata=cancerscreen.read(),
            issuednote=issuednote.filename,issuednotedata=issuednote.read(),
            medical=medical.filename,medicaldata=medical.read(),
            proofdeath=proofdeath.filename,proofdeathdata=proofdeath.read(),
            resignation=resignation.filename,resignationdata=resignation.read(),

            user_id = current_user.id)

        
        row = Emp_notes.query.filter(Emp_notes.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full_notes)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Emp_notes WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('emp_notes.html',user=current_user,data=output[0])
    except:
        return rt('emp_notes.html',user=current_user,data=output)
    
@views.route('/equipment&it', methods=['GET','POST'])
@login_required
def equipmentit():
    if request.method == 'POST':
        app_access = request.form.get('app_access')
        electronics = request.form.get('electronics')
        vpninfo = request.form.get('vpninfo')
        misc = request.form.get('misc')

        full_it = Equipment_IT(
            app_access=app_access,
            electronics=electronics,
            vpninfo=vpninfo,
            misc=misc,
            user_id = current_user.id)
        
        row = Equipment_IT.query.filter(Equipment_IT.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full_it)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Equipment_IT WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('equipment.html',user=current_user,data=output[0])
    except:
        return rt('equipment.html',user=current_user,data=output)
    

@views.route('/employee-health', methods=['GET','POST'])
@login_required
def health():
    if request.method == 'POST':
        health_assessment = request.form.get('assessment')
        covid = request.form.get('covid')
        n95 = request.form.get('n95')
        vaccine = request.form.get('vaccine')
        misc = request.form.get('misc')

        full = Emp_health(
            health_assessment=health_assessment,
            covid=covid,
            n95=n95,
            vaccination=vaccine,
            misc=misc,
            user_id = current_user.id)
        
        row = Emp_health.query.filter(Emp_health.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Emp_health WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('emp_health.html',user=current_user,data=output[0])
    except:
        return rt('emp_health.html',user=current_user,data=output)
    

@views.route('/human-resources', methods=['GET','POST'])
@login_required
def hr():
    if request.method == 'POST':
        attestation = request.form.get('attestation')
        dept = request.form.get('dept')
        ivcontrast = request.form.get('ivcontrast')
        lmsproof = request.form.get('lmsproof')
        eval = request.form.get('eval')
        program = request.form.get('program')
        trophon = request.form.get('trophon')
        awards = request.form.get('awards')
        orientation = request.form.get('orientation')
        leave = request.form.get('leave')
        expire = request.form.get('expire')
        desc = request.form.get('desc')
        checklist = request.form.get('checklist')
        charting = request.form.get('charting')
        appt = request.form.get('appt')
        status = request.form.get('status')
        misc = request.form.get('misc')

        full = Human_resources(
            attestation=attestation,
            dept_competency=dept,
            ivcontrast=ivcontrast,
            lmsproof=lmsproof,
            performance_eval=eval,
            performance_program=program,
            trophon=trophon,
            awards=awards,
            orientation=orientation,
            leave_letter=leave,
            expiration_notice=expire,
            description=desc,
            hospital_checklist=checklist,
            chartingnumber_request=charting,
            appt_packet=appt,
            status=status,
            misc=misc,
            user_id = current_user.id)
        
        row = Human_resources.query.filter(Human_resources.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Human_resources WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('hr.html',user=current_user,data=output[0])
    except:
        return rt('hr.html',user=current_user,data=output)
    
@views.route('/labor-relations', methods=['GET','POST'])
@login_required
def lr():
    if request.method == 'POST':
        memorandum = request.form.get('memorandum')
        term = request.form.get('term')
        drequest = request.form.get('drequest')
        dnotice = request.form.get('dnotice')
        nonrenewal = request.form.get('nonrenewal')
        re_appt = request.form.get('re_appt')
        misc = request.form.get('misc')

        full = Labor_relations(
            memorandum=memorandum,
            termination=term,
            disciplinerequest=drequest,
            disciplinenotice=dnotice,
            nonrenewal=nonrenewal,
            re_appt=re_appt,
            misc=misc,
            user_id = current_user.id)
        
        row = Labor_relations.query.filter(Labor_relations.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Labor_relations WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('labor.html',user=current_user,data=output[0])
    except:
        return rt('labor.html',user=current_user,data=output)

@views.route('/new-hires', methods=['GET','POST'])
@login_required
def newhires():
    if request.method == 'POST':
        resume = request.form.get('resume')
        offer = request.form.get('offer')
        acceptance = request.form.get('acceptance')
        reference = request.form.get('reference')
        internal = request.form.get('internal')
        interview = request.form.get('interview')
        requisition = request.form.get('requisition')
        misc = request.form.get('misc')

        full = New_hires(
            resume=resume,
            offer=offer,
            acceptance=acceptance,
            reference=reference,
            internal=internal,
            interview=interview,
            requisition=requisition,
            misc=misc,
            user_id = current_user.id)
        
        row = New_hires.query.filter(New_hires.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM New_hires WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('newhires.html',user=current_user,data=output[0])
    except:
        return rt('newhires.html',user=current_user,data=output)
    
@views.route('/payroll', methods=['GET','POST'])
@login_required
def payroll():
    if request.method == 'POST':
        change = request.form.get('change')
        salary = request.form.get('salary')
        misc = request.form.get('misc')

        full = Payroll(
            hospitalchange=change,
            salary=salary,
            misc=misc,

            user_id = current_user.id)
        
        row = Payroll.query.filter(Payroll.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Payroll WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('payroll.html',user=current_user,data=output[0])
    except:
        return rt('payroll.html',user=current_user,data=output)
    
@views.route('/timekeeping', methods=['GET','POST'])
@login_required
def time():
    if request.method == 'POST':
        accrual = request.form.get('accrual')
        disability = request.form.get('disability')
        injury = request.form.get('injury')
        kronos = request.form.get('kronos')
        overtime = request.form.get('overtime')
        sbmc = request.form.get('sbmc')
        wc = request.form.get('wc')
        misc = request.form.get('misc')

        full = Timekeeping(
            accrual=accrual,
            disability=disability,
            injury=injury,
            kronos=kronos,
            overtime=overtime,
            sbmc_agency=sbmc,
            wc=wc,
            misc=misc,
            user_id = current_user.id)
        
        row = Timekeeping.query.filter(Timekeeping.user_id==current_user.id).first()
        if row:
            db.session.delete(row)
            db.session.commit()
        db.session.add(full)
        db.session.commit()
        flash('Information saved in database.',category='Success')
    connect = sqlite3.connect('instance/database.db')
    c = connect.cursor()
    sql = 'SELECT * FROM Timekeeping WHERE user_id=' + str(current_user.id)
    c.execute(sql)
    output = c.fetchall()
    c.close()
    connect.close()
    try:
        if output[0]:
            return rt('timekeeping.html',user=current_user,data=output[0])
    except:
        return rt('timekeeping.html',user=current_user,data=output)

@views.route('/admin', methods=['GET','POST'])
@login_required
def admin(): # set admin users here
    if current_user.email == 'test@email.com':
        flash('Successfully accessed Admin page.',category='Success')
        connect = sqlite3.connect('instance/database.db')
        c = connect.cursor()


        sql5 = 'SELECT * FROM user u JOIN demographics d on u.id = d.user_id JOIN certifications c on u.id = c.user_id JOIN Clinical_Edu cl on u.id = cl.user_id JOIN Emp_notes n on u.id=n.user_id JOIN Equipment_IT it on u.id=it.user_id JOIN Emp_health h on u.id=h.user_id JOIN Human_resources hr on u.id=hr.user_id JOIN Labor_relations lr on u.id=lr.user_id JOIN New_hires nh on u.id=nh.user_id JOIN Payroll p on u.id=p.user_id JOIN Timekeeping t on u.id=t.user_id JOIN Form f on u.id=f.user_id'
        c.execute(sql5)
        total = c.fetchall()

        c.close()
        connect.close()
        return rt('admin2.html',user=current_user,total=total)
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

# for Forms
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

# for Clinical Education
@views.route('/linen_download/<upload_id>')
def linen_download(upload_id):
    upload = Clinical_edu.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.linendata), download_name=upload.linen,as_attachment=True)

@views.route('/pyxis_download/<upload_id>')
def pyxis_download(upload_id):
    upload = Clinical_edu.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.pyxisdata), download_name=upload.pyxis,as_attachment=True)

# for Doctor and Employee notes
@views.route('/blood_don_download/<upload_id>')
def blood_don_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.blood_dondata), download_name=upload.blood_don,as_attachment=True)

@views.route('/cancerscreen_download/<upload_id>')
def cancerscreen_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.cancerscreendata), download_name=upload.cancerscreen,as_attachment=True)

@views.route('/issuednote_download/<upload_id>')
def issuednote_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.issuednotedata), download_name=upload.issuednote,as_attachment=True)

@views.route('/medical_download/<upload_id>')
def medical_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.medicaldata), download_name=upload.medical,as_attachment=True)

@views.route('/proofdeath_download/<upload_id>')
def proofdeath_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.proofdeathdata), download_name=upload.proofdeath,as_attachment=True)

@views.route('/resignation_download/<upload_id>')
def resignation_download(upload_id):
    upload = Emp_notes.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.resignationdata), download_name=upload.resignation,as_attachment=True)



@views.route('/delete-field', methods=['POST']) 
def delete_note():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Demographics.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field2', methods=['POST'])
def delete_note2():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Certifications.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field3', methods=['POST'])
def delete_note3():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Clinical_edu.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field4', methods=['POST'])
def delete_note4():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Emp_notes.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field5', methods=['POST'])
def delete_note5():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Equipment_IT.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field6', methods=['POST'])
def delete_note6():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Emp_health.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field7', methods=['POST'])
def delete_note7():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Human_resources.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field8', methods=['POST'])
def delete_note8():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Labor_relations.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field9', methods=['POST'])
def delete_note9():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = New_hires.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})

@views.route('/delete-field10', methods=['POST'])
def delete_note10():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Payroll.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})


@views.route('/delete-field11', methods=['POST'])
def delete_note11():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Timekeeping.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})



@views.route('/delete-forms', methods=['POST'])
def delete_forms():
    field = json.loads(request.data)
    profileid = field['profileid']
    field = Form.query.get(profileid)
    if field:
        if field.user_id == current_user.id:
            db.session.delete(field)
            db.session.commit()
    return jsonify({})




