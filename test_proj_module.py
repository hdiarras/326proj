import unittest
from proj326 import Gpa, Schedule, CourseDetails, AssignmentTracker

class GpaTest(unittest.testCase):
   
    def test_gpa_percent(self):
        gpa = Gpa()
        self.assertEqual(gpa.gpa_percent(95),4.0)
        self.assertEqual(gpa.gpa_percent(88), 3.3) #misspelled percent, error
        self.assertEqual(gpa.gpa_percent(72), 1.7)
        self.assertEqual(gpa.gpa_percent(50), 0.0)
      
    def test_gpa_calculator(self):
        gpa = Gpa()
        gpa.add_course("INST326", 89, 3)
        gpa.add_course("INST311", 95, 3)
        result = gpa.calculate_gpa()
        self.assertAlmostEqual(result, 3.2, places=2)
        
        
class ScheduleTest(unittest.TestCase):
    
    def test_schedule(self):
        schedule = Schedule()
        schedule.add_course_schedule("INST326", "MWF", "12:00PM", "HBK 0226", "12/09")
        self.assertEqual(schedule.get_schedule("INST326"), ["MWF", "12:00PM", "HBK 0226", "12/09" ])
        
        
class CourseDetailTest(unittest.TestCase):
    
    def test_course_details(self):
        cd = CourseDetails()
        cd.add_prof("Prof. Cruz")
        cd.add_ta("Jian")
        cd.add_student("Student A")
        self.assertEqual(cd.get_details()['professor'], "Prof. Cruz")
        self.assertIn("Jian", cd.get_details()['TAs'])
        
        
class AssignmentTrackerTest(unittest.TestCase):
    def test_assignment_tracker(self):
        tracker = AssignmentTracker()
        tracker.add_assignment("HW1","2024-10-24, 95, 0.1")
        
if __name__ == "__main__": #forgot =, error
    unittest.main()
        