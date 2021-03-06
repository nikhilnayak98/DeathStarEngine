import json
import httplib2
import base64
from flask import jsonify
from models.models import *
from constants.constants import *

http = httplib2.Http()


def login_and_fetch_details(username, password):
    body = json.dumps({'username': username, 'password': password, 'MemberType': membertype})
    headers = {'Content-type': 'application/json'}
    response, login_content = http.request(URL + '/login', 'POST', headers=headers, body=body)

    if int(response['status']) == 200:
        login_data = json.loads(login_content)
        headers = {'Cookie': response['set-cookie']}
        student = Student()

        response, details_content = http.request(URL + '/studentinfo', 'POST', headers=headers)
        details_content = json.loads(details_content)
        details_content = json.dumps(details_content["detail"][0])
        details_content = json.loads(details_content)

        student.set_name(login_data["name"].lower().title())
        student.set_regno(details_content["enrollmentno"])
        student.set_gender(details_content["gender"])
        student.set_program(details_content["programdesc"])
        student.set_branch(details_content["branchdesc"])
        student.set_sec(details_content["sectioncode"])
        student.set_sem_number(details_content["stynumber"])
        student.set_phone(details_content["pcellno"])
        student.set_email(details_content["pemailid"])
        student.set_headers(headers)

        resp, image = http.request(URL + '/image/studentPhoto', 'GET', headers=headers)
        student.set_image(str(base64.b64encode(image).decode("utf-8")))
        return student
    else:
        return None


def fetch_attendance(student):
    resp, sem_content = http.request(URL + '/studentSemester/lov', 'POST', headers=student.get_headers(), body="")
    sem_content = json.loads(sem_content)
    reglov = sem_content['studentdata'][0]['REGISTRATIONID']
    body = json.dumps({'registerationid': reglov})
    response, attendance_content = http.request(URL + '/attendanceinfo', 'POST', headers=student.get_headers(), body=body)
    attendance = json.loads(attendance_content)
    attendance = json.dumps(attendance["griddata"])
    attendance = json.loads(attendance)
    attendance_objects = []
    subjects = 0
    for att in attendance:
        subjects = subjects + 1
        num_theory = 0
        den_theory = 0
        num_lab = 0
        den_lab = 0
        attendance_object = Attendance()
        attendance_object.set_subject(att['subject'])
        attendance_object.set_lab_att(att['Patt'])
        attendance_object.set_theory_att(att['Latt'])
        attendance_object.set_total_att(att['TotalAttandence'])
        attendance_object.last_updated_on(att['lastupdatedon'])
        if attendance_object.get_theory_att() != "Not Applicable":
            num_theory, den_theory = attendance_object.get_theory_att().split('/')
        if attendance_object.get_lab_att() != "Not Applicable":
            num_lab, den_lab = attendance_object.get_lab_att().split('/')
        if attendance_object.get_total_att() < 75:
            num_total = int(num_lab) + int(num_theory)
            den_total = int(den_lab) + int(den_theory)
            attendance_object.set_needed_sevenfive(3 * int(den_total) - 4 * int(num_total))
        else:
            attendance_object.set_needed_sevenfive(0)
        attendance_objects.append(attendance_object)
    attendance_json = []
    for subs in range(0, subjects):
        attendance_json.append(attendance_objects[subs].toJSON())

    return attendance_json
