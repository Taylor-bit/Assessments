from military_recruits import MilitaryRecruits

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Recruits\n2. View Individual Recruit <first_name><last_name><birthdate>\n3. Add a Recruit\n4. Quit\n")

    if mode == '1':
            MilitaryRecruits().list_recruits()
    elif mode == '2':
        first_name = input('Enter recruit first name: \n')
        last_name = input('Enter recruit last name: \n')
        birthdate = input('Enter recruit birthdate: \n')
        recruit_string = str(MilitaryRecruits().find_recruit(first_name, last_name, birthdate))
        print(recruit_string)
    elif mode == '3':
        military_recruit_data = { }
        military_recruit_data['recruit_id']         = input('Enter recruit ID:\n')
        military_recruit_data['first_name']         = input('Enter recruit first name:\n')
        military_recruit_data['last_name']          = input('Enter recruit last name: \n')
        military_recruit_data['branch_of_service']  = input('Enter recruit branch of service: \n')
        military_recruit_data['birthdate']          = input('Enter recruit birthdate: \n')
        military_recruit_data['education_level']    = input('Enter recruit education level: \n')
        military_recruit_data['pay_grade']          = input('Enter recruit pay grade: \n')
        military_recruit_data['closest_relative']   = input('Enter recruit closest relative: \n')
        MilitaryRecruits().add_recruit(military_recruit_data)
    elif mode == '4':
        break