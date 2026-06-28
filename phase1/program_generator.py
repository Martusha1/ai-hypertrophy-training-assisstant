def get_name():
    while True:
        name = input("Please enter your name: ")
        if name.isdigit():
            print("Please use only letters. ")
        else: break
    return name

def get_age():
    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            age = int(age)
            if age > 0 and age <= 122:
                break
            else:
                print("Please enter a valid age. ")
        else:
            print("Please use only numbers. ")
    return age

def get_training_exp():
    while True:
        training_exp = input("Please select the number corresponding to your training experience: 1. Beginner, 2. Intermediate, 3. Advanced. ")
        if training_exp.isdigit():
            training_exp=int(training_exp)
            if training_exp in [1,2,3]:
                if training_exp == 1:
                    training_exp = "Beginner"
                elif training_exp == 2:
                    training_exp = "Intermediate"
                else:
                    training_exp = "Advanced"
                break
            else:
                print("Please select a number from 1 to 3 depending on your training experience. ")
        else:
            print("Please enter the number standing to your individual training experience. ")
    return training_exp

def get_training_days_per_week():
    while True:
        days = input("Please enter how many days per week you would like to train: ")
        if days.isdigit():
            days=int(days)
            if days >= 1 and days <= 7:
                break
            else:
                print("Please enter a valid number of days within a week. ")
        else:
            print("Please enter a valid number. ")
    return days
    
def get_session_length():
    while True:
        length = input("Please enter how many minutes per session you would like to train: ")
        if length.isdigit():
            length=int(length)
            if length >= 15 and length <= 360:
                break
            else:
                print("Please enter a valid session length. ")
        else:
            print("Please enter a number representing the amount of time you would like to train per session in minutes. ")
    return length

def get_available_equipment():
    while True:
        equipment=input("Please select what equipment you have available by choosing its corresponding number: 1. Full gym, 2. Dumbbells, 3. Barbell, 4. Bench, 5. Rack, 6. Resistance bands, 7. Nothing. ")
        if equipment.isdigit():
            equipment=int(equipment)
            if equipment in [1,2,3,4,5,6,7]:
                match equipment:
                    case 1:
                        equipment = "Full gym"
                        break
                    case 2:
                        equipment = "Dumbbells"
                        break
                    case 3:
                        equipment = "Barbell"
                        break
                    case 4:
                        equipment = "Bench"
                        break
                    case 5:
                        equipment = "Rack"
                        break
                    case 6:
                        equipment = "Resistance bands"
                        break
                    case 7:
                        equipment = "Nothing"
                        break
                    case _:
                        print("Error. Please try again. ")
            else:
                print("Please select a number from 1 to 7. ")
        else:
            print("Please select a number that correlates to your equipment. ")
    return equipment

def get_goal():
    while True:
        goal = input("Please select the number corresponding to your goal: 1. Maximum hypertrophy, 2. General fitness (based on muscle building). ")
        if goal.isdigit():
            goal=int(goal)
            if goal in [1,2]:
                if goal == 1:
                    goal = "Maximum hypertrophy"
                    break
                else:
                    goal = "General fitness (based on muscle building)"
                    break
            else:
                print("Please enter either 1 or 2 depending on your goal. ")
        else:
            print("Please use only a number. ")
    return goal

def get_user_profile():

    user = {"name": None, "age": None, "training experience": None,
            "training days per week": None, "session length": None,
            "available equipment": None, "goal": None}
    
    user["name"]=get_name()
    user["age"]=get_age()
    user["training experience"]=get_training_exp()
    user["training days per week"]=get_training_days_per_week()
    user["session length"]=get_session_length()
    user["available equipment"]=get_available_equipment()
    user["goal"]=get_goal()
    
    return user


def main():
    print(get_user_profile())

if __name__ == "__main__":
        main()

    

    
    

    


