print("This is a story about someone that just recently got immagrated in the Netherlands and went to the Media College in Amsterdam")
print("Can you tell me what your name is?")

username = input("")
print("So your name is " + username)

print("Imagine you live in Syria, you tried to have a good day, but then suddenly you have to immegrate to somewhere you are not familiar to")
print("So after you managed to get out of Syria, how would you go to a different country?")

answer = input("If you want to go with the boat type boat and if you want to go with a plane you type plane ") 
if answer == "plane": 
    print("it seems you don't have any money to go on a plane so you decide to walk out of the country...")
    print("Where do you want to walk?")
    answer3 = input("If you want to go north, type north, if you want to walk south type south")
    if answer3 == "north":
         print("You walked up north, but then something happened, you saw from a far fighter jets coming right at you, they shoot at you, but you evaded the bullets and hid behind a rock")
         print("What would you do?")
         answer4 = input("if you want to run from those jets type run, if you want to wait type wait")
         if answer4 == "run":
               print("You ran from the fighter jets, but the fighter jets moved towards your direction yet agian and shot you down")
               print("GAME OVER")
         elif answer4 == "wait":
               print("You waited behind the rock until the fighter jets to pass, they turned around and tried to find more people who try to cross the boarder to Turkey...")
               print("So you try to make up a plan, you could rush in towards the border, risking your own life, or you could cross the border very sneaky...")
    elif answer3 == "south":
         print("You walked down south and came to a village full of terrorist of ISIS, they spot you and begin to fire, you were hit by a few bullets and that is how you met your end")
         print("GAME OVER")
    else:
         print("Please enter north or south")
elif answer == "boat": 
    print("So you ask to somebody if they know a guy that can immegrate you into a other country...") 
    print("Which country do you want to immegrate? Netherlands or France?")
    answer2 = input("")
    if answer2 == "Netherlands":
       print("You went inside of the boat with other people, you were scared just like the rest of the people inside of the boat, but after a few minutes, the boat started to get of shores and ride to the Netherlands, the journey towards The Netherlands went smoothly, but only because you had your own passport with you, So you then arrive in a city named Rotterdam that is located in the " + answer2)
       print("Every single thing is new for you, you don't speak their language, but you can speak a bit english.")
       print("You went around and asked people where you could be helped, the people were mostly not nice, they pushed you around like you were nothing...")
       print("Some of the people were nice and tried to guide you to the city hall where you should be registered as a immagrate...")
       print("You finally arrived the city hall from Rotterdam and went inside, alot of people looked at you, but they then all resumed what they were doing.")
       print("You walked towards the reception of the city hall, a woman said to you: 'Sir/Ma'am, do you have a reservation or do you have other reasons to go here...'")
    answer5 = input("What do you want to say?, type immagrant if you want to say that you just arrived as a legal immagrant but still have no home, type plead if you want to plead to talk with the mayor to have a home to live in temporary...")
    if answer5 == "immagrant":
           print("You said that you were an legal immagrant and you were looking for a temporary home until the war in Syria is over, the woman behind the counter told towards you if you had a passport proving you are a legal immagrant, you gave her your passport, she picked it up and looked inside of it.")
           print("She looked at you once more and gave you the passport back, she told that you need to pick an number from the desk and wait until your number has been picked...")
           print("So you took a number and went to the waiting room, you waited for 15 minutes until your number has been picked...")
           print("You went to the desk with your number above it, there was one chair near the counter, so you sat down.")
           print("A guy was behind a glass and told you why you were here, you told him you were a legal immagrant and you searched for a temporary home until the war in Syria was over...")
           print("The man behind the glass, looked at you and told if you had a passport, you gave him your passport as proof, then the man behind the glass looked at you briefly and said: ")
           print("Alright, it seems that you were here going to stay until the war in Syria is over? am I correct?")
           print("You said yes, and the man behind the glass looked towards you, then he looked agian towards your passport...")
    elif answer5 == "plead":
           print("You said and pleaded to the receptionist, that you wanted to stay in the Netherlands to build a normal life, but the receptionist said that you could but you need to wait for a long time...")
           print("")
    elif answer2 == "France":
       print("You arrived at a city surrounded by everything new ")
    else: 
       print("Please enter Netherlands or France...")
else: 
    print("Please enter plane or a boat...")
