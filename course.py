class Course:
    def __init__(self, course_id, course_name, duration):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration

    def display(self):
        print("Course ID  :", self.course_id)
        print("Course     :", self.course_name)
        print("Duration   :", self.duration)
