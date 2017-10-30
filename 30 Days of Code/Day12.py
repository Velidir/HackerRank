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
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(scores)/len(scores)
        if 90 <= average and average <= 100:
            return "O"
        elif 80 <= average and average < 90:
            return "E"
        elif 70 <= average and average < 80:
            return "A"
        elif 55 <= average and average < 70:
            return "P"
        elif 40 <= average and average < 50:
            return "D"
        else:
            return "T"