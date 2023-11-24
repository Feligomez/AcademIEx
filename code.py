
class Course:
    def __init__(self, name, subject, duration):
        self.name = name
        self.subject = subject
        self.duration = duration

class Student:
    def __init__(self, name, age, degree, year):
        self.name = name
        self.age = age
        self.degree = degree
        self.year = year
        self.marks = {}
        self.goals = {}

    def add_mark(self, subject, mark, goal):
        self.marks[subject] = mark
        self.goals[subject] = goal

    def calculate_mean_mark(self):
        return sum(self.marks.values()) / len(self.marks) if len(self.marks) > 0 else 0

    def calculate_mean_goal(self):
        return sum(self.goals.values()) / len(self.goals) if len(self.goals) > 0 else 0

def calculate_priority(student, subject):
    if subject not in student.marks or subject not in student.goals:
        return 0, 0

    difference = student.marks[subject] - student.goals[subject]

    if student.marks[subject] < 5:
        return 10, difference
    elif difference < -5:
        return 9, difference
    elif difference < -4:
        return 8, difference
    elif difference < -3:
        return 7, difference
    elif difference < -2:
        return 6, difference
    elif difference < -1:
        return 5, difference
    elif difference < 0:
        return 4, difference
    else:
        return 2, difference

def recommend_courses(student, all_courses, weeks_remaining):
    recommended_courses = {}

    for course in all_courses:
        if course.duration <= weeks_remaining:
            priority_score, difference = calculate_priority(student, course.subject)
            if priority_score > 0:
                if course.subject not in recommended_courses:
                    recommended_courses[course.subject] = {"status": "", "courses": [], "priority": 0, "difference": 0}
                recommended_courses[course.subject]["courses"].append((course, priority_score, difference))
                recommended_courses[course.subject]["priority"] = max(
                    recommended_courses[course.subject]["priority"], priority_score)
                recommended_courses[course.subject]["difference"] = max(
                    recommended_courses[course.subject]["difference"], difference)

    sorted_subjects = sorted(recommended_courses.keys(), key=lambda x: recommended_courses[x]["priority"], reverse=True)

    for subject in recommended_courses:
        courses_list = recommended_courses[subject]["courses"]
        n = len(courses_list)

        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if courses_list[j][1] < courses_list[min_index][1]:
                    min_index = j

            courses_list[i], courses_list[min_index] = courses_list[min_index], courses_list[i]

    return {subject: {"status": recommended_courses[subject]["status"],
                      "courses": [course[0] for course in recommended_courses[subject]["courses"]],
                      "priority": recommended_courses[subject]["priority"],
                      "difference": recommended_courses[subject]["difference"]} for subject in sorted_subjects}

def get_student_details():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    degree = input("Enter student's degree: ")
    year = input("Enter student's university year: ")

    student = Student(name, age, degree, year)

    for course in set(course.subject for course in courses):
        mark = int(input(f"Enter {course} mark for {name}: "))
        goal = int(input(f"Enter {course} goal for {name}: "))
        student.add_mark(course, mark, goal)

    return student

def display_recommendations(student, weeks_remaining):
    recommended_courses = recommend_courses(student, courses, weeks_remaining)

    print(f"\nRecommended courses for {student.name}:")
    for subject in recommended_courses:
        print(" ")
        priority_score, difference = calculate_priority(student, subject)
        status = "Failed" if student.marks.get(subject, 0) < 5 else "Below Goal" if difference < 0 else "On Track"

        print(f"{subject.capitalize()} — {status} - Difference from Goal: {difference}")

        if recommended_courses[subject]["courses"]:
            sorted_courses = sorted(recommended_courses[subject]["courses"], key=lambda course: abs(
                student.goals[subject] - student.marks.get(subject, 0)), reverse=True)

            print("\nAvailable Courses:")
            for course in sorted_courses:
                print(f"  {course.name} — (Estimated time for completion: {course.duration} weeks)")
            print("\n————————————————————————————————————")

def display_profile(student):
    print(f"\nStudent Profile for {student.name}:")
    print(f"  Name: {student.name}")
    print(f"  Age: {student.age}")
    print(f"  Degree: {student.degree}")
    print(f"  University Year: {student.year}")

    mean_mark = student.calculate_mean_mark()
    mean_goal = student.calculate_mean_goal()

    print(f"\nSubject Marks:")
    for subject in student.marks:
        status = "Failed" if student.marks[subject] < 5 else "Below Goal" if student.marks[subject] < student.goals[
            subject] else "On Track"
        print(
            f"  {subject.capitalize()}: Mark: {student.marks[subject]}, Goal: {student.goals[subject]} — {status}")

    print(f"\nMean Mark: {mean_mark:.2f}")
    print(f"Mean Goal: {mean_goal:.2f}")
    print("Performance: ", end="")
    if 1.1 * mean_mark < mean_goal:
        print("Far Below Expectations")
    elif mean_mark > mean_goal * 1.5:
        print("Far Above Expectations")
    else:
        print("On Track")

def change_marks_goals(student):
    subject = input("Enter the subject for which you want to change marks and goals: ")
    if subject in student.marks and subject in student.goals:
        new_mark = int(input(f"Enter new mark for {subject}: "))
        new_goal = int(input(f"Enter new goal for {subject}: "))
        student.marks[subject] = new_mark
        student.goals[subject] = new_goal
        print(f"Marks and goals updated for {subject}.")
    else:
        print(f"You haven't entered marks and goals for {subject} yet.")

# Sample courses (duration in weeks)
courses = [
    Course("QuizletTech1", "Technology", 1),
    Course("QuizletTech2", "Technology", 1),
    Course("TechLab1", "Technology", 2),
    Course("TechLab2", "Technology", 2),
    Course("Udemy's Flutterflow Course", "Technology", 2),
    Course("TechProject2", "Technology", 4),
    Course("YouTubeMath1", "Math", 2),
    Course("YouTubeMath2", "Math", 2),
    Course("QuizletMkt1", "Marketing Management", 1),
    Course("QuizletMkt2", "Marketing Management", 1),
    Course("BookMkt", "Marketing Management", 2),
    Course("KhanAcademyMkt2", "Marketing Management", 3),
    Course("KhanAcademyMkt1", "Marketing Management", 3),
    Course("KhanAcademyMkt2", "Marketing Management", 3),
    Course("AdvancedBookMkt", "Marketing Management", 4),
    Course("AdvancedYouTubeStat", "Statistics", 4),
    Course("Data Structures & Algorithms Playlist by CS Dojo (Youtube)", "Algorithms & Data Structures", 2),
    Course("Algorithms and Data Structures Tutorial by freeCodeCamp.org (Youtube)", "Algorithms & Data Structures", 1),
    Course("Coursera", "Algorithms & Data Structures", 3),
    Course("Ted Talks", "Building Powerful Relationships", 1),
    Course("Mind map practice", "Building Powerful Relationships", 1),
    Course("YouTubeProg1", "Programming for Data Management & Analysis", 3),
    Course("YouTubeProg2", "Programming for Data Management & Analysis", 3),
]

# Sample student
student1 = get_student_details()

# Input weeks
weeks_remaining = int(input("Enter the number of weeks remaining until final exams: "))

# Interactive menu
while True:
    print("\nChoose an option:")
    print("1. Recommendations")
    print("2. Display Profile")
    print("3. Change Marks and Goals")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        display_recommendations(student1, weeks_remaining)
    elif choice == '2':
        display_profile(student1)
    elif choice == '3':
        change_marks_goals(student1)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")




