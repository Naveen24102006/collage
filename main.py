from Student import Student
from Faculty import Faculty
from Course import Course
from Fees import Fees
from Alumni import Alumni


print("======================================")
print("       COLLEGE MANAGEMENT SYSTEM")
print("======================================")

print("\n--- STUDENT DETAILS ---")
student = Student(101, "Naveen", "Software Engineering")
student.display()

print("\n--- FACULTY DETAILS ---")
faculty = Faculty(201, "Dr. Kumar", "Computer Science")
faculty.display()

print("\n--- COURSE DETAILS ---")
course = Course(301, "Software Engineering", "5 Years")
course.display()

print("\n--- FEES DETAILS ---")
fees = Fees(101, 75000, "Paid")
fees.display()

print("\n--- ALUMNI DETAILS ---")
alumni = Alumni(401, "Rahul", "Infosys")
alumni.display()

print("\n======================================")
print("     APPLICATION RUNNING SUCCESSFULLY")
print("======================================")
