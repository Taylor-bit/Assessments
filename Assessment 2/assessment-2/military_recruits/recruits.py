import csv
import os

class Recruit:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "military_recruits.csv")

    def __init__(self, recruit_id, first_name, last_name, branch_of_service, birthdate, education_level, pay_grade, closest_relative):
        self.recruit_id = recruit_id
        self.first_name = first_name
        self.last_name = last_name
        self.branch_of_service = branch_of_service
        self.birthdate = birthdate
        self.education_level = education_level
        self.pay_grade = pay_grade
        self.closest_relative = closest_relative

    def __str__(self):
        return f"Recruit {self.recruit_id}: {self.first_name} {self.last_name}, born {self.birthdate}, {self.branch_of_service}. {self.first_name} finished {self.education_level} and is at the {self.pay_grade}. Their closest relative is name {self.closest_relative}."

    @classmethod
    def objects(cls):
        recruits = []

        with open(Recruit.path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recruits.append(Recruit(**dict(row)))
        return recruits

    def save_to_file(self):
        with open(Recruit.path, 'a') as csvfile:
            csvfile.write(f"{self.recruit_id},{self.first_name},{self.last_name},{self.branch_of_service},{self.birthdate},{self.education_level},{self.pay_grade},{self.closest_relative}")