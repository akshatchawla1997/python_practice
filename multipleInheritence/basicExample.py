class Father:
    def skills(self):
        print("I love Gardening")

class Mother:
    def skills(self):
        print("I love Cooking")

class Child( Mother, Father):
    def skills(self):
        super(Child, self).skills()  # Call the skills method in Father
        super(Mother, self).skills()  # Call the skills method in Mother
        print("I love Sports")

child = Child()
child.skills()
