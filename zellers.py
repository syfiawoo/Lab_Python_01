#f_name=raw_input("Enter your first name: ")
#l_name=raw_input("Enter your last name: ")
print "Enter your date of birth:"
A=input("Enter month as number from 1-12(March=1; February=12): ")
B=input("day of the month: ")
year=input("year of birth: ")
C=year%100
D=year/100
if A==11 or A==12:
    C=C-1    

W=(13*A-1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C-2*D
R=Z%7

if R<0:
    R=R+7 

Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']    
print "You were born on", Days[R]
