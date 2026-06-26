def get_user_profile():
    user={}

    exp=["Beginner","Intermediate","Advanced"]
    equipment=["Full gym", "Dumbbells only", "Barbell and Rack", "Bench", "Nothing"]
    goal=["Hypertrophy", "Strength", "Recomposition"]

    schema = {"name": str, "training experience": list,
            "training days per week": int, "session length": int,
            "available equipment": list, "goal": list}
    
    for key, expected_type in schema:
        while True:
            value = input(f"Enter {key}: ")
            try:
                user[key]=expected_type(value)
                break
            except ValueError:
                print("Invalid input. Please enter letters.")

    
    

    


