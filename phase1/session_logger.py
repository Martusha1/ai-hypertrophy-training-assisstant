import database

def show_all_programs():
    all_programs = database.get_programs()

    print("Please pick your program by its ID:")

    for num, program in all_programs:
        print(f"{num}. {program}")
    
    # add switch case for user pick based on num

def main():
    show_all_programs()

if __name__ == "__main__":
    main()