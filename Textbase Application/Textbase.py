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
               answer9 == input("type rush to rush towards the border, or type sneaky to sneak towards the border")
               if answer9 == "rush":
                  print("You tried to rush towards the border, the pilot from the fighterjet saw you, he shoots once more to kill you, you ran and ran, but then you got hit in your foot")
                  print("You fell and the fighterjet flew away and tried to prepare for another attack to kill you, you stand up and tried to limp towards the rock you hid in")
                  print("but it was already to late, the fighterjet was prepared and shot you, you were killed in the process")
                  print("GAME OVER")
               elif answer9 == "sneak":
                  print("You tried to sneak towards the border, it seems that the fighterjet didn't even notice you")
                  print("The fighterjet goes away and you still tried to go towards the border sneaky, then you saw next to you a few people running away from something. ")
                  print("You then looked behind them, it was a army car with guns aiming right at them, then a bomb went off, it's a minefield what they came across, you looked around if there was no landmines around you")
                  print("After dustsmoke faded you still saw the people running away, but the army car is destroyed and on fire.")
                  print("You could rush towards the minefield to the border or sneak further towards the border, what will you do?")
                  answer10 == input("type minefield to run towards the minefield and take your chances, or type sneak to sneak further towards the border")
                  if answer10 == "minefield":
                     print("You stood up and ran towards the group of people in the minefield a few explosions came from behind, while you were running, you catched up with the group of people")
                     print("They saw you too, the people running towards the border was your neighbour and a few other families, the neighbour said to you: Good to see you while he was running with you...")
                     print("Then behind you heard a few shots in the distance, ISIS is trying to kill you from the border off, a few people fell and were killed")
                     print("Your neigbour said towards you: Why does it always have to be ISIS and ran even harder with some zigzags on the way so he won't even get shot, you did the same as the neighbour.")
                     print("Then you saw the border, a brick wall blocking you from entering Turkey, you were worried that you would get killed, then a familiar sound came, the fighterjet you fled from came, now you were really scared for your life")
                     print("but the Figherjet didn't even shot you, it began to shoot ISIS, you looked behind in amazement, then somebody from the border said to the group (including you) that you needed to come towards them, when you arrived you saw still your neighbour running towards you.")
                     print("but then you saw your neighbour got shot in the head, you were the only left alive. ")
                     print("The person took you in and told if you were okay, he then told you that you did a stupid action but a brave one.")
                     print("You were then surrounded by police, you were taken towards a camp so you could regain your strength.")
                     print("After a few days somebody came towards you and told you had a choice, or you could work for the army to help the people in need, or you could get an appartment and get some work")
                     print("What would you choose?")
                     answer11 == input("type army to help the other people or type work to get a normal life")
                     if answer11 == "army":
                        print("You told the man you wanted to help the other people in need, he told you it was a wise decision and took you with him, a few months go forth and you helped alot of people gaining their strength and giving them healthcare")
                        print("The people respected you and had alot of great interactions with other people, ending this story completly")
                        print("THE END, you got the A Runner of a Soldier ENDING")
                     elif answer11 == "work": 
                        print("You told the man that you wanted to live a normal life agian, the man was a bit dissapointed but he couldn't blame you")
                        print("You were given an appartment and a job so you could get a normal life, but after a few months, a airstrike came around, destroying a building near your appartment")
                        print("Then you heard yet another airstrike coming but this time striking the building you were living in, killing you instantly")
                        print("You got the Tragic Ending")
                  elif answer10 == "sneak":
                     print("You shrugged and went further with sneaking with the rocks, after a few minutes you heard a few shots next to you, you looked sneakly next to the rock")
                     print("It was ISIS, they were shooting at the group, a few people were shot and killed")
                     print("Then one of the members of ISIS spotted you behind the rock, they captured you and killed you in cold blood.")
                     print("GAME OVER")
                  else:
                     print("please type minefield or sneak to continue")
               else:
                  print("please type rush or sneak")
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
           print("He then looks towards his computer and then told you: it seems one of your family lives around Amsterdam, so maybe you can live there for the time being")
           print("So you ask if you were in the clear and could live in the Netherlands, the man behind the glass sighed and said towards you: you first have to get a test if you are suitable to live here, but that can take around 3 months")
           print("You were a bit afraid, so you then ask to the man behind the glass if you could call the family member, the man behind the glass agrees and gives you the number, you called them up and you explained to your family member how you got in the Netherlands and if they could pick him up and live with them for a while")
           print("They agreed and they picked you up, they were happy to see you after the war in Syria got worse, they even thought you were dead.")
           print("3 months later you finally got the test results back if you could stay in the Netherlands or not, the results were positive and after a few days you thought of going back to school and having a part time job to earn some money.")
           print("And that is how you got into the MediaCollege Amsterdam, you liked the program and became friends with the students.")
           print("The End, Got the Media College Ending....")
       elif answer5 == "plead":
           print("You said and pleaded to the receptionist, that you wanted to stay in the Netherlands to build a normal life, but the receptionist said that you could but you need to wait for a long time...")
           print("You became angry and told the receptionist that you are a legal immegrant and that you demanded to have a normal life here, everyone stared at you, security came and threw you out...")
           print("You tried and tried to get in but failed, the cops were called and you were arrested for harrassing the receptionist and for almost destroying property...")
           print("You were send back towards your country and you failed your mission to have a normal life inside of this country")
           print("GAME OVER")
    elif answer2 == "France":
       print("You arrived at a city surrounded by everything new and there were alot of people around the area, there even was a few france police forces around the large group, all of you were escorded and putted into a camp with a little tent, a sleeping bag, food and a mattress, good enough to survive around here...")
       print("You were satisfied, but there was alot of noise around you, that was the only problem what you got, but it was to be expected...")
       print("Maybe I should go north, maybe find something good, or maybe I should stay here for a bit, maybe waiting will pay off and sooner or later I will get a good home...")
       print("So what do I decide, do I go north and try to find a home somewhere, or should I wait until I get a home and my long wait will be paid off...")
       answer6 = input("What should I choose, type North to go North, type stay to stay at this camp")
       if answer6 == "North":
              print("You told a guard guarding the place that you wanted to go and try to find somewhere to stay in the north, the Guard let's you go and you walked north")
              print("Before you went out, the guard gave you a bottle of water, so you don't get thirsty on the way and wishes you a wonderfull journey, you walked around a forest and the mountains...")
              print("It became colder and more colder, the more you climbed the mountain of the Alphs")
              print("You saw a cabin in the distance, you saw no light shining inside of the cabin...")
              print("What would you do?")
              answer7 = input("What would you choose, type cabin if you want to go in or type walk to not go into the cabin...")
              if answer7 == "cabin":
                 print("You walked towards the cabin, but still, there was no light. You knocked on the door")
                 print("No answer, you looked around the door and saw a doorbel, you pushed on it")
                 print("a creepy sound came out of the doorbel, it tingles through your spine, but still no answer...")
                 print("You gain a creepy vibe because of the cabin, but you tried to open the door, it wasn't even locked...")
                 print("You went inside because of the cold, you shouted is there anyone there?")
                 print("but you didn't hear anybody back, you looked around the cabin and tried to find somebody, there was nobody there, you locked the door and tried to get some sleep")
                 print("40 minutes after you were sleeping, you are hearing someone breathing near your ear, you woke up, there was nobody there, you looked around, but didn't find anyone...")
                 print("You became a bit paranoid and tried to get the lights on, but there was no power inside of the cabin")
                 print("You then heard someone behind you breathing in you ear, you looked next to you and you saw a man, smiling next to you, you were shocked and said to the man that you were trying to find somewhere to sleep")
                 print("The man didn't say anything, you were a bit freaked out, he picked up a knife and tries to attack you")
                 print("you dodged and kicked him agianst the wall, he grunted and tried to get up")
                 print("You ran towards the door and tried to open the door, it was locked...")
                 print("What do you do")
                 answer8 = input("type knife to get a knife, type smack if you want to smack the killer with a chair")
                 if answer8 == "knife":
                    print("You ran towards the kitchen but the killer was already there...")
                    print("the killer had a knife inside of his hands, he launched at you and stabbed you")
                    print("You tried to push him off, but he was to strong to push him off, he stabbed and stabbed you until you are dead")
                    print("GAME OVER")   
                 elif answer8 == "smack": 
                    print("You took a chair located near the living room, you took it and smacked the killer with it on the head.")
                    print("He passed out after the smack and you tied him up, you went towards a phone and tried to call the police what happened")
                    print("The police came after 2 hours, you told them what happened, the police cuffed the guy and put him away in prison")
                    print("it was later been revealed that the home was from an elderly couple who have been murdered and never have been found")
                    print("They found the two bodies inside of the basement, both of them were found as skeletons, the person who killed them got life in prison")
                    print("as a thank you, the family of the elderly couple gave you the cabin to live in, later you got a job and a happy life")
                    print("The end, got the Horror Slasher  Detective Ending")
                 else:
                    print("Please type knife or smack to continue the story")      
              elif answer7 == "walk":
                 print("You walked past the cabin, the longer you walked the colder it became, you could not feel you feet")
                 print("You slowly became more tired, you really wanted to sleep inside of the snow, but you try not to do that because of the cold")
                 print("But after a few minutes, you fell on the ground and died of hypothermia")
                 print("GAME OVER")
       elif answer6 =="Stay":
              print("You stayed inside of the camp")
              print("It became colder and colder, you realised winter was coming, but you resisted the cold...")
              print("You went towards your tent to warm up a bit with your own sleeping bag.")
              print("a few months later you saw alot of people getting dropped off and the camp is getting bigger and bigger, you grew a bit concerned, because what if later there was no place for you to sleep.")
              print("Then a few guards came towards you, they told you could live in France and gave your passport back with a French permission to live there")
              print("You thanked the guards and you were given a backpack and a little appartment inside of the city of Paris.")
              print("You have a good life and of course went back to school near Paris. You worked at a store part time to earn some money, you are living a happy life and nobody is stopping you")
              print("THE END, You have the Life in Paris Ending")
    else: 
       print("Please enter Netherlands or France...")
else: 
    print("Please enter plane or a boat...")