def get_name():
    while True:
        name = input("Please enter your name: ")
        if name.isdigit():
            print("Please use only letters.")
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
                print("Please enter a valid age.")
        else:
            print("Please use only numbers.")
    return age

def get_training_exp():
    while True:
        training_exp = input("Please select the number corresponding to your training experience: 1. Beginner, 2. Intermediate, 3. Advanced")
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
                print("Please select a number from 1 to 3 depending on your training experience.")
        else:
            print("Please enter the number standing to your individual training experience.")
    return training_exp

def get_user_profile():

    user = {"name": None, "age": None, "training experience": None,
            "training days per week": None, "session length": None,
            "available equipment": None, "goal": None, "injury history": None}
    
    return user
    
    

    
    

    


