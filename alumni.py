class Alumni:
    def __init__(self, alumni_id, name, company):
        self.alumni_id = alumni_id
        self.name = name
        self.company = company

    def display(self):
        print("Alumni ID  :", self.alumni_id)
        print("Name       :", self.name)
        print("Company    :", self.company)
