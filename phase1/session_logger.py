import database

def show_programs():
    all_programs = database.get_programs()

    for num, program in all_programs:
        print(f"{num}. {program}")

    program_ids = []
    for p in all_programs:
        program_ids.append(p[0])
    
    while True:
        chosen_program = input("Please pick your program by its ID:")
        try:
            chosen_program = int(chosen_program)
            if chosen_program in program_ids:
                return chosen_program
            else:
                print("Please pick the number corresponding to your chosen program!")
        except ValueError:
            print("Please pick the number corresponding to your chosen program!")

def day_selection():
    p_id = show_programs()
    program = database.get_program_day(p_id)

    all_days = []

    for day in program["days"]:
        print(f"Day {day["day"]}:")
        all_days.append(day["day"])
        for muscle in day["muscles_targeted"]:
            print(f"{muscle}")
    
    while True:
        chosen_day = input("Please pick the number of the day of choice.")
        if chosen_day.isdigit():
            chosen_day = int(chosen_day)
            if chosen_day in all_days:
                for day in program["days"]:
                    if day["day"] == chosen_day:
                        return day["exercises"]
            else:
                print("The day you entered is invalid.")
        else:
            print("Please enter a digit.")

def log_sets(workout_id, exercises):
    for ex in exercises:
        exercise_name = ex["name"]
        print(f"{ex["name"]}")
        for s in range(1,ex["sets"]+1): # +1 because endpoint excluded
            set_number = s
            while True:
                weight_kg = input(f"Weight for set {s}: ")
                try:
                    weight_kg = float(weight_kg)
                    if 0.0 < weight_kg < 2845.0:
                        break
                    else:
                        print("Please enter a valid weight in kg.")
                except ValueError:
                    print("Please use numbers.")
            while True:
                reps = input("Reps: ")
                if reps.isdigit():
                    reps = int(reps)
                    if 0 < reps < 100:
                        break
                    else:
                        print("Please enter a valid amount of reps")
                else:
                    print("Please use digits.")
            while True:
                rir = input("Reps in reserve: ")
                if rir.isdigit():
                    rir = int(rir)
                    if 0 < rir < 100:
                        break
                    else:
                        print("Please enter a valid amount of reps in reserve.")
                else:
                    print("Please use digits.")
            database.save_set(workout_id,exercise_name,set_number,reps,weight_kg,rir)

def main():
    show_programs()

if __name__ == "__main__":
    main()