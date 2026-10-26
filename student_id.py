def main():
    name = input("Full Name: ")
    try:
        enrollment_year = int(input("Enrollment Year: "))
        initials = get_initials(name)
        stud_id = generate_id(initials, enrollment_year)
        print(f"Your student ID is: {stud_id}")
    except ValueError:
        pass


def get_initials(name):
    first, last = name.upper().split()
    first = first[0]
    last = last[0]
    initials = first + "." + last + "."
    return initials


def generate_id(initials, enrollment_year):
    year = enrollment_year % 100
    stud_id = f"MKSU/{initials}/{year}"
    return stud_id


if __name__ == "__main__":
    main()
