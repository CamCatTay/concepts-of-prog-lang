class Course:
    # initialize attributes for a new course object
    # so that other methods can access these variables
    def __init__(self, name, number, section, term, year, num_students):
        self.name = name or None
        self.number = number or None
        self.section = section or None
        self.term = term or None
        self.year = year or None
        self.num_students = num_students or None

    # setters
    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def set_section(self, section):
        self.section = section

    def set_term(self, term):
        self.term = term

    def set_year(self, year):
        self.year = year

    def set_num_students(self, num_of_students):
        self.num_students = num_of_students

    # print attributes
    def print_name(self):
        print(f"Course Name: {self.name}")

    def print_number(self):
        print(f"Course Number: {self.number}")

    def print_section(self):
        print(f"Section: {self.section}")

    def print_term(self):
        print(f"Term: {self.term}")

    def print_year(self):
        print(f"Year: {self.year}")

    def print_num_students(self):
        print(f"Number of Students: {self.num_students}")

    # print all attributes
    def print_all_details(self):
        print(f"Course {self.name} Attributes:")
        self.print_number()
        self.print_section()
        self.print_term()
        self.print_year()
        self.print_num_students()

def main():
    # contains course objects (course_number : course_object)
    courses = {}

    # users selected choice after menu prompt
    choice = ""

    while choice != "4":
        print("\nCourse Menu")
        print("1. Add a New Course")
        print("2. Change a Course Attribute")
        print("3. Display All Courses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        print("\n")

        if choice == "1":
            # request data from input
            name = input("Enter Course Name: ")
            num = input("Enter Course Number: ")
            sec = input("Enter Section: ")
            term = input("Enter Term: ")
            year = input("Enter Year: ")
            students = input("Enter Number of Students: ")

            # create course object and store it in courses using its number as a key
            new_course = Course(name, num, sec, term, year, students)
            courses[num] = new_course
            print(f"Course {num} added successfully!")

        elif choice == "2":
            # identify which course to modify
            num = input("Enter the Course Number you wish to modify: ")
            if num in courses:
                print("\nWhich attribute would you like to change?")
                print("a. Name")
                print("b. Number")
                print("c. Section")
                print("d. Term")
                print("e. Year")
                print("f. Number of Students")

                sub_choice = input("Enter your choice (a-f): ").lower()
                new_val = input("Enter the new value: ")

                # invoke specific setter based on user selection
                if sub_choice == "a":
                    courses[num].set_name(new_val)
                elif sub_choice == "b":
                    # update the dictionary key if the course number changes
                    courses[new_val] = courses.pop(num)
                    courses[new_val].set_number(new_val)
                elif sub_choice == "c":
                    courses[num].set_section(new_val)
                elif sub_choice == "d":
                    courses[num].set_term(new_val)
                elif sub_choice == "e":
                    courses[num].set_year(new_val)
                elif sub_choice == "f":
                    courses[num].set_num_students(new_val)
                else:
                    print("Invalid attribute selection.")

                print("Attribute updated.")
            else:
                print("Course not found.")

        elif choice == "3":
            if not courses:
                print("No courses in the system.")
            else:
                # invoke print method for every course in the collection
                for course_key in courses:
                    courses[course_key].print_all_details()
                    print("\n")

        elif choice == "4":
            print("Exiting program.")

        else:
            print("Invalid choice, please try again.")

# initialize main
main()