from ast import Str
import math
import string


#write a program that will analyze data for a family. Input for each family consists of:
# The family last name   (string)
# Number of persons in the family     (integer)
# Annual Income      (double)
# Total debts         (double)

# Your program should interactively read these inputs (with appropriate prompt messages), perform calculations, then output the following:

# a) An appropriate header
# b) The family's last name, number of persons, income and debts
# c) Predicted family living expenses ($3000 times the family size)
# d) The monthly payments necessary to pay off the debt in one year
# e) The amount the family should save (family size time 2% of the (income-debt))

Last = input ("Enter your family last name: ")
NumPerson = input ("Number of persons in your family: ")
AnnInc= input ("Your Annual income: ")
debt = ("Enter your total debt: ")

print("\n NEO FBA ""Family Budget Assistance" "\n"" Review of your family budget:")
print (str (Last),"'s Family has, ",int (NumPerson)," members and their annual income is ", float (AnnInc), " and their toal debt is ", float (debt))
predict = float (3000) * int (NumPerson)
debtpay = float (debt) / float (12)
famsave = float (NumPerson) * (0.02 * (float (AnnInc)-float (debt)))
print ("Pay ", float (debtpay) ," per month in one year to pay off the Debt" )
print ("You also need to save " , float (famsave))
print ("\n Thank you! \n")
                              
                 