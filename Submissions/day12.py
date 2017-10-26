class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        if len(self.scores) == 1:
            avg = self.scores
        else:
            avg = sum(self.scores) / len(self.scores)
        
        if avg < 40:
            return "T"
        elif 40 <= avg < 55:
            return "D"
        elif 55 <= avg < 70:
            return "P"
        elif 70 <= avg < 80:
            return "A"
        elif 80 <= avg < 90:
            return "E"
        elif 90 <= avg <= 100:
            return "O"
        else:
            return "N/A"
    