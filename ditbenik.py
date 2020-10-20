print("Hello you, Ik ben Dirk ten Have")
print("Kunt u mij vertellen wie u bent?")

username = input("")
print("Mijn naam is " + username)

import datetime
x = datetime.datetime.now()

print(x)

answer = input("Enter yes or no: ") 
if answer == "yes": 
    print("Pizza Time") 
    print("Would you like to play a game?")
    answer2 = input("Enter yes or no: ")
    if answer2 == "yes":
      print("Ok, let's play Among us")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is", answer3)
    elif answer2 == "no":
      print("Fuck you, we are playing Among us!")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is", answer3)
    else:
      print("well darn that's not a answer, let's play Among us")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is", answer3)
      
elif answer == "no": 
     print("Stares Motherfuckerly") 
     print("Would you like to play a game?")
     answer2 = input("Enter yes or no: ")
     if answer2 == "yes":
        print("Ok, let's play Among us")
        print("What is your name?")
        answer3 = input("Enter your name...")
        print("So your name in Among us is ", answer3)
     elif answer2 == "no":
          print("Fuck you, we are playing Among us!")
          print("What is your name?")
          answer3 = input("Enter your name...")
          print("So your name in Among us is ", answer3)
     else:
          print("well darn that's not a answer, let's play Among us")
          print("What is your name?")
          answer3 = input("Enter your name...")
          print("So your name in Among us is", answer3)
     
else: 
    print("Stares Motherfuckerly")
    print("Would you like to play a game?")
    answer2 = input("Enter yes or no: ")
    if answer2 == "yes":
      print("Ok, let's play Among us")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is ", answer3)
      
    elif answer2 == "no":
      print("Fuck you, we are playing Among us!")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is ", answer3)
    else:
      print("Why aren't you typing yes or no?")
      print("What is your name?")
      answer3 = input("Enter your name...")
      print("So your name in Among us is ", answer3)
