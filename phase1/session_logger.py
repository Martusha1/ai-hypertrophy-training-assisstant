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

    for day in program["days"]:
        # print each day and muscles_targeted
        # ask the user to pick a day number
        # return the exercises list for that day


def main():
    show_programs()

if __name__ == "__main__":
    main()