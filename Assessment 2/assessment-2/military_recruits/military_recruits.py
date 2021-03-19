# Create class Recruit
    # class attribute of my_path = os.path.abspath(os.path.dirname(__file__))
    # path = os.path.join(my_path, "../military_recruits.csv")
        # Initialize Recruits with columns in csv
    
    # Create dunder string method to format list output in Recruit
    # Create @classmethod to read and write to csv file
    # Create a method to save changes to the file
             

# Create method to list recruits in this format: Recruit 1: Jon Smith, born 01/01/1990, Marines. 
# Jon finished College and is being paid at the O-1 pay grade. Their closest relative is named Tom Smith.

# Create method with input statement to add new recruits to the csv file (append)
    # Make sure it has access to save_to_file method

# Create method find_recruit that compares user input of first_name, last_name and birthdate 
    # Returns the proper recruit information 
    # If no matches found, return "Recruit does not exist"

# In runner file create while loop for True with options to 
    # Look up all recruits
    # Look up individual recruits
    # Add a new recruit 
import csv
import os
from recruits import Recruit

class MilitaryRecruits:
    
    def __init__(self):
        self.recruits = Recruit.objects()

    def add_recruit(self, input):
        new_recruit = Recruit(**input)
        self.recruits.append(new_recruit)
        new_recruit.save_to_file()

    def find_recruit(self, first_name, last_name, birthdate):
        for recruit in self.recruits:
            if recruit.first_name == first_name and recruit.last_name == last_name and recruit.birthdate == birthdate:
                return recruit
        return "Recruit does not exist."

    def list_recruits(self):
        print('\n')
        for recruit in self.recruits:
            print(f"Recruit {recruit.recruit_id}: {recruit.first_name} {recruit.last_name}, born {recruit.birthdate}, {recruit.branch_of_service}. {recruit.first_name} finished {recruit.education_level} and is at the {recruit.pay_grade}. Their closest relative is name {recruit.closest_relative}.")

