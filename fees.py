class Fees:
    def __init__(self, student_id, amount, status):
        self.student_id = student_id
        self.amount = amount
        self.status = status

    def display(self):
        print("Student ID :", self.student_id)
        print("Fee Amount :", self.amount)
        print("Status     :", self.status)
