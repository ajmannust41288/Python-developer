class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
 def __init__(self, fname, lname,batch,degreename,universityname,startyear,
              year,marks,totalmark,cgpa,totalcgp,crdhour,totalhr):
     super().__init__( fname, lname)
     self.university=universityname
     self.batch=batch
     self.degreename=degreename
     self.graduationstarting=startyear
     self.graduationyear=year
     self.scores=marks
     self.Totalmarks=totalmark
     self.Cgpa=cgpa
     self.totalcgpa=totalcgp
     self.credithour=crdhour
     self.totalcredithr=totalhr
 def welcome(self):
         print("\t \t \t \t \t \t Welcome TO ",self.university )
 def Engineering(self):
     print("\n Graduation Batch : ", self.batch, "\n Graduation Degree  Title : ",
           self.degreename)
 def Graduationperiod(self):
     print("\n Staring Graduation  ",self.graduationstarting,"\n Graduation End year ",
               self.graduationyear)
 def computerEng(self):
     print("\n \n Welcome to Result OF Your Degree : ","\n First name is: ",self.firstname,"\n  last name is : ",
           self.lastname,"\n scores  :",
           self.scores,"\n totalmarks",self.Totalmarks,"\n CGPA is :",self.Cgpa
           ,"\n Total cgpa",self.totalcgpa,"\n total credit hours completed are : ",
           self.credithour,"\n total credit hour in semester: ",self.totalcredithr)
x=Student("Zeeshan","khan","DE-40","Computer Engineering","NUST",2018,2022,990,1100,3.5,4,138,140)
x.welcome()
x.Engineering()
x.Graduationperiod()
x.computerEng()
