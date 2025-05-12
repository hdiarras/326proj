"""
Final Project for INST326
Author: Nahum, Hawa, Komal, Zara
Date: 12/10/2023
Description: This code provides a GPA calculator, course schedule, course details, and assignment tracker for students.
"""

class Gpa:
    """
    Calculates GPA based on the UMD grading scale.

    Attributes:
        courses: list of tuples format (course_name, percentage_grade, credits).
    """

    def __init__(self):
        #initialize the list of courses
        self.courses = []

    def add_course(self, course_name, percentage, credits):
        """
        Add course with grade & credit value.

        Args:
            course_name: name of the course.
            percentage: grade % for course.
            credits: num of credits course is worth.
        """
        self.courses.append((course_name, percentage, credits))

    def percentage_to_gpa(self, percent):
        """
        Converts % to a GPA value using the UMD GPA scale.

        Args:
            percent: The % grade.

        Returns:
            float: The GPA equivalent.
        """
        if percent >= 97:
            return 4.0
        elif percent >= 93:
            return 4.0
        elif percent >= 90:
            return 3.7
        elif percent >= 87:
            return 3.3
        elif percent >= 83:
            return 3.0
        elif percent >= 80:
            return 2.7
        elif percent >= 77:
            return 2.3
        elif percent >= 73:
            return 2.0
        elif percent >= 70:
            return 1.7
        elif percent >= 67:
            return 1.3
        elif percent >= 63:
            return 1.0
        elif percent >= 60:
            return 0.7
        else:
            return 0.0

    def calculate_gpa(self):
        """
        Calculates cumulative GPA from all added courses.

        Returns:
            float: The cumulative GPA rounded to 3 decimal places.
        """
        total_quality_points = 0
        total_credits = 0

        for course_name, percent, credits in self.courses:
            gpa = self.percentage_to_gpa(percent)
            quality_points = gpa * credits
            total_quality_points += quality_points
            total_credits += credits
            print(f"{course_name}: {percent}% -> GPA {gpa} ({credits} credits)")

        if total_credits == 0:
            return 0.0  # Avoid division by zero
        return round(total_quality_points / total_credits, 3)
    
class Schedule:
    """
    Displays course meeting times, location, and final exam dates.

    Attributes:
        schedule (dict): Dictionary with course code as key and list of [days, time, hall, exam date] as value.
    """
    def __init__(self):
        self.schedule = {}

    def add_course_schedule(self, course_code, days, time, hall, exam_date):
        self.schedule[course_code] = [days, time, hall, exam_date]

    def get_schedule(self, course_code):
        return self.schedule.get(course_code, "Course not found")


class CourseDetails:
    """
    Displays professor, TAs, and student names.

    Attributes:
        details: Keys are 'professor', 'TAs', and 'students'
    """
    def __init__(self):
        self.details = {
            'professor': None,
            'TAs': [],
            'students': []
            }

    def set_professor(self, name):
        self.details['professor'] = name

    def add_ta(self, name):
        self.details['TAs'].append(name)

    def add_student(self, name):
        self.details['students'].append(name)

    def get_details(self):
        return self.details


class AssignmentTracker:
    """
    Tracks assignments, due dates, grades, and weights.

    Attributes:
        assignments: List of tuples in format (name, due_date, grade, weight)
    """
    def __init__(self):
        self.assignments = []

    def add_assignment(self, name, due_date, grade, weight):
        self.assignments.append((name, due_date, grade, weight))

    def get_assignments(self):
        return self.assignments

    def get_assignment_by_name(self, name):
        for assignment in self.assignments:
            if assignment[0] == name:
                return assignment
        return "Assignment not found"

# Test the Gpa class
if __name__ == "__main__":
    gpa_calc = Gpa()
    
    # Add some test courses
    gpa_calc.add_course("INST311", 95, 3)
    gpa_calc.add_course("INST327", 88, 3)
    gpa_calc.add_course("PLSC205", 76, 4)

    # Print out the GPA for each course
    for course, percentage, credits in gpa_calc.courses:
        gpa = gpa_calc.percentage_to_gpa(percentage)
        print(f"{course}: {percentage}% -> GPA: {gpa} ({credits} credits)")