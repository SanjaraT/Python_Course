print("CREATING A CLASS THAT TAKES NAMES & MARKS OF 3 SUBS AS ARG & A METHOD TO PRINT AVERAGE")

class Classroom:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def cal_avg(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
            avg = sum/3
        print(self.name,"Your average score is : ", avg)
    s1 = Classroom("Sanju",[99,85,88])
    s1.cal_avg()
        