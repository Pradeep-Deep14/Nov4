(5>10==False)


#1. Python evaluates expressions from left to right.

#2. The > operator has lower precedence than the == operator.

#3. Therefore, the expression 5 > 10 == False is evaluated as follows: 

#👉Evaluate 5 > 10. This results in the value False.
#👉 Evaluate False == False. This results in the value True.
#👉 Apply the == operator to the values False and True. This results in the value False.

#In other words, the expression (5 > 10 == False) is equivalent to the expression False == True,
#  which evaluates to False