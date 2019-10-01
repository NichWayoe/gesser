import random
hidden=random.randint(0,100)
print(hidden)
guess1 = int(input("Guess the number "))
count=1
d=abs(hidden - guess1 )
if hidden==guess1:
  print("You are correct! You got it after " + str(count)+" guess")
else:
  if d  >0 and d<10:
   print("You are hot!")
  elif d>10 and d<20:
    print("You are warm!")
  elif d>20:
    print("You are cold!")
  guess=int(input("Guess the number "))
  a=guess
  count+=1
  while guess!=hidden:
    d=abs(hidden - a )
    if d<10 and a<guess1 :
      print("You are getting warmer!")
      print("You are red hot!")
    elif d<10 and a>guess1:
      print("You are getting colder!")
      print("you are red hot!")
    elif d>10 and d<20 and a<guess1:
      print("You are getting warmer!")
      print("You are warm!")
    elif d>10 and d<20 and a>guess1:
      print("You are getting colder")
      print("You are warm!")
    elif d>20 and a>guess1:
      print("You are getting colder")
      print("You are cold!")
    elif d>20 and a<guess1:
      print("You are getting warmer!")
      print("You are cold!")
      a=guess
    guess=int(input("Guess the number "))
    count+=1
  print("You are correct! You got it after " + str(count)+" guesses")
