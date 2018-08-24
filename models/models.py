import base64
import json


class Student:
    def toJSON(self):
        details_json = json.dumps(self, default=lambda o: o.__dict__)
        return json.loads(details_json)

    def set_headers(self, headers):
        self.headers = headers

    def set_regno(self, regno):
        self.regno = regno

    def set_name(self, name):
        self.name = name

    def set_sem_number(self, sem_number):
        self.sem_number = sem_number

    def set_program(self, program):
        self.program = program

    def set_branch(self, branch):
        self.branch = branch

    def set_sec(self, sec):
        self.sec = sec

    def set_image(self, image_string):
        self.image_string = image_string

    def set_phone(self, phone_num):
        self.phone_num = phone_num

    def set_gender(self, gender):
        self.gender = gender

    def set_email(self, email):
        self.email = email

    def get_headers(self):
        return self.headers

    def get_regno(self):
        return self.regno

    def get_name(self):
        return self.name

    def get_sem_number(self):
        return self.sem_number

    def get_program(self):
        return self.program

    def get_branch(self):
        return self.branch

    def get_sec(self):
        return self.sec

    def get_image(self):
        return self.image_string

    def get_phone(self):
        return self.phone_num

    def get_gender(self):
        return self.gender

    def get_email(self):
        return self.email


class Attendance:
    def toJSON(self):
        details_json = json.dumps(self, default=lambda o: o.__dict__)
        return json.loads(details_json)

    def set_subject(self, sub_name):
        self.sub_name = sub_name

    def set_theory_att(self, theory_att):
        self.theory_att = theory_att

    def set_lab_att(self, lab_att):
        self.lab_att = lab_att

    def set_total_att(self, total_att):
        self.total_att = total_att

    def last_updated_on(self, last_update):
        self.last_update = last_update

    def set_needed_sevenfive(self, sevenfive_days):
        self.sevenfive_days = sevenfive_days

    def get_subject(self):
        return self.sub_name

    def get_theory_att(self):
        return self.theory_att

    def get_lab_att(self):
        return self.lab_att

    def get_total_att(self):
        return self.total_att

    def get_last_updated_on(self):
        return self.last_update

    def get_needed_sevenfive(self):
        return self.sevenfive_days