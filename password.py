#import package

from lib2to3.pygram import Symbols
import random
import string


print("ITS KIASH TO GENERATE THE PASSWORD")

length=int(input("Enter the length of the password: "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbol=string.punctuation

all=lower+upper+num+symbol

password=random.sample(all,length)

temp="".join(password)

print(temp)


print("PASSSWORD WORKS SUCCESSFUL")