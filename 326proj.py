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

# Example usage
'''if __name__ == "__main__":
    gpa_calculator = Gpa()
    gpa_calculator.add_course("INST326", 92, 3)
    gpa_calculator.add_course("INST311", 85, 3)
    gpa_calculator.add_course("INST201", 97, 3)

    final_gpa = gpa_calculator.calculate_gpa()
    print(f"\nCumulative GPA: {final_gpa}")'''
    
class Schedule:
    """
    Displays what days of the week the course meets, at what time, where, and when the final exams are.

    Attributes
    ------------
    class_times:
    hall:
    exam_dates:
    #if making this a list with imbedded lists is easier go for that
    
    Returns
    -------------
    """
    
    def __init__(self, class_times, hall, exam_dates):
        pass

class Course_details:
    """
    This displays the details of the course.
    
    Attributes
    -----------
    class_times:
    hall:
    exam_dates:
     #if making this a list with imbedded lists is easier go for that
    
    Returns
    --------
    """
    
    def __init__(self, professor, students, ta):
        pass
    
class Assignment_tracker:
    """
    This stores all the assignments for a course, their due dates, the weight of each assignment, and the grade received. 
    
    Attributes
    -----------
    professor:
    students:
    ta:
    #if making this a list with imbedded lists is easier go for that
    
    Returns
    --------

    """
    
    def __init__(self, assignment, due_date, grade, weight):
        pass