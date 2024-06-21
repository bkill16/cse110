print()

#Welcome Message
print('Welcome to my adventure game. You will be presented with')
print('some scenarios. You will be provided with choices. Which')
print('choice you decide to enter will determine the course of')
print('the game. Be sure to type your answers exactly as they')
print('appear in all caps in the questions. No extra spaces.')
print('Have fun!!!')

print()

#KEEP WALKING or TURN AROUND
print("You're going for a stroll through the woods. You've been")
print("out for a while, and sunset is near. Do you KEEP WALKING")
choice_one = input("anyway, or do you want to TURN AROUND? ")

print()

#FRONT DOOR or BACK DOOR
if choice_one.upper() == 'KEEP WALKING':
    print("You've decided to carry on through the woods for a little")
    print("longer, despite the oncoming darkness.")
    print()
    print("You've now walked deeper into the forest, and night has fallen")
    print("You've pulled out a flashlight to help you see. After a while,")
    print("you stumble upon a path you've never seen before and decide to")
    print("travel down it. You discover an old, abandoned house. Curious,")
    print("you decide to go inside. You notice a FRONT DOOR and a BACK DOOR.")
    choice_two = input("Which door do you want to open? ")

    print()
    
    #LEAVE or KEEP EXPLORING
    if choice_two.upper() == 'FRONT DOOR':
        print("You decide to open the front door. As you walk in, a bucket of water that")
        print("has been rigged to the door falls on your head, covering your eyes and")
        print("drenching you with freezing water.")
        print()
        print("After being disoriented and flailing around for a few seconds, you manage to")
        print("get the bucket off of your head. Soaked and shivering, you start to explore")
        print("the house. You soon begin to realize that this old house isn't abandoned.")
        print("Someone has been living inside very recently. You notice a notebook on a table")
        print("with a list of names. Some are crossed out. Next to it, you see a handful of")
        print("bullets. You begin to feel unsafe. Do you want to LEAVE or KEEP EXPLORING the")
        choice_four = input("house? ")

        print()
        
        #FIGHT or RUN
        if choice_four.upper() == 'LEAVE':
            print("The notebook you found that appeared to be some kind of hit list really")
            print("freaked you out, so you hurry back out the front door. You start heading")
            print("back home and you move pretty fast, you don't want to run into whoever")
            print("lives in that old house. Eventually, you make it back to your house safely.")
            print()
            print("THE END. Thanks for playing :)")
        elif choice_four.upper() == 'KEEP EXPLORING':
            print("You feel a little uneasy, but you decide to keep looking around the house.")
            print("After a few minutes, you hear someone outside. You look out the window and")
            choice_five = input("see a man approaching. Do you want to FIGHT or RUN? ")

            print()

            #ENDING - FIGHT or RUN
            if choice_five.upper() == 'FIGHT':
                print("You've decided to fight your way out. You grab a frying pan from the kitchen")
                print("and hide in the hallway. The man walks in and sees that his bucket trap has")
                print("sprung. He walks in slowly, and pulls out his gun. He gets closer to you and")
                print("you prepare your swing. He gets to you and you swat him with the pan, knocking")
                print("the man to the ground, unconcious. You hurry out of the house and run back home.")
                print()
                print("THE END. Thanks for playing :)")
            elif choice_five.upper() == 'RUN':
                print("Scared, you take off running. The man sees you, draws his gun, and shoots you. He's")
                print("an excellent shot and you are dead.")
                print()
                print("THE END. Thanks for playing :)")
            else:
                print('ERROR. Please enter from the choices provided.')
        else:
            print('ERROR. Please enter from the choices provided.')

    #BACK DOOR      
    elif choice_two.upper() == 'BACK DOOR':
        print("In order to be secretive, you decide to sneak around to the back. You try")
        print("the door but it's locked. You notice a hatchet in a nearby pile of wood.")
        print("You grab it, and use it to tear through the door. As you walk inside, you")
        print("see that the interior of the old house is nothing short of spooky.")
        print()
        print("The back door leads into the garage. You step in and see an assortment of")
        print("weaponry. Guns, knives, swords, and others. You notice that some of the")
        print("blades are covered with blood. You notice another door in the garage, too")
        print("and you open it, revealing a dark stairway to a basement. Do you GO DOWN")
        choice_six = input("THE STAIRS or CLOSE THE DOOR? ")

        print()

        #GO DOWN THE STAIRS or CLOSE THE DOOR
        if choice_six.upper() == 'GO DOWN THE STAIRS':
            print("You decide to go down the stairs and check out the basement. You find")
            print("a light switch and turn it on. The light reveals a collection of freezers")
            choice_seven = input("and refrigerators. Do you want to OPEN them or LEAVE THEM ALONE? ")

            print()
            
            #OPEN or LEAVE THEM ALONE - ENDING
            if choice_seven.upper() == 'OPEN':
                print("Your curiosity gets the best of you and you decide to open one of the")
                print("freezers. Inside, you find a body. Yelping, you jump back. But what's")
                print("even scarier than the body is that as you jump back, you feel yourself")
                print("bump into something. Turns out, it's not a something, but a someone. And")
                print("he pushes you into the open freezer, closes it, and locks it, leaving you")
                print("there to freeze to death.")
                print()
                print("THE END. Thanks for playing :)")
            elif choice_seven.upper() == 'LEAVE THEM ALONE':
                print("The basement seems pretty spooky, so you decide to go back upstairs. You've")
                print("been out all night, and you don't want to stay in the creepy house or dark")
                print("forest any longer, so you leave the house and go back home.")
                print()
                print("THE END. Thanks for playing :)")
            else:
                print('ERROR. Please enter from the choices provided.')
        
        elif choice_six.upper() == 'CLOSE THE DOOR':
            print("You're scared of basements, so you decide to close the door. As you do so,")
            print("you feel a tap on your shoulder. You jump and turn around. There's a creepy")
            print("man standing behind you. With a smile on his face, he hits you over the head")
            print("with a baseball bat and you die.")
            print()
            print("THE END. Thanks for playing :)")
        else:
            print('ERROR. Please enter from the choices provided.')
    else:
        print('ERROR. Please enter from the choices provided.')

#SAY SOMETHING or QUIETLY FOLLOW or MIND YOUR OWN BUSINESS
elif choice_one.upper() == 'TURN AROUND':
        print("You've decided to call it a day before night falls, and")
        print("you start heading back home.")
        print()
        print("As you're making your way back home, you notice a strange man carrying a")
        print("large black bag over his shoulders. Do you want to SAY SOMETHING to the man,")
        choice_three = input("QUIETLY FOLLOW him, or MIND YOUR OWN BUSINESS? ")

        print()

        if choice_three.upper() == 'SAY SOMETHING':
            print('You decide to say something to the strange man. You call out, "Hey,' ' ' "what's")
            print('up?" This startles the man, and you see him pull out what you think is a gun.')
            choice_eight = input('Frightened, you take off running. Do you run HOME or go tell the POLICE? ')

            print()

            #HOME or POLICE
            if choice_eight.upper() == 'HOME':
                print("With the adrenaline rushing through you, you sprint your way back home. You open your")
                print("front door and slam it shut behind you, panting. Your mom starts yelling at you, but")
                print("you're so disoriented that you don't understand what she's saying. She's clearly upset")
                choice_nine = input("so do you APOLOGIZE or give your mom ATTITUDE? ")

                print()

                #APOLOGIZE or ATTITUDE - ENDING
                if choice_nine.upper() == 'APOLOGIZE':
                    print("You apologize to your mom, despite what you just experienced. She appreciates that")
                    print("and makes you cookies. Cookies make you feel better after almost dying.")
                    print()
                    print("THE END. Thanks for playing :)")
                elif choice_nine.upper() == 'ATTITUDE':
                    print("You didn't understand why your mom was mad at you. You'd almost been shot and she had")
                    print("the audacity to yell at you. Of course, she didn't know that you'd almost been killed,")
                    print("but you hit her with the 'tude anyways. She didn't like that, so she grounded you.")
                    print()
                    print("THE END: Thanks for playing :)")
            
            elif choice_eight.upper() == 'POLICE':
                print("A strange man with a large black bag just pulled a gun on you, so you figure the best")
                print("thing to do is to go to the police. You arrive at the station and tell them what happened")
                print("and they go to the forest. You read in the papers the next day that a man was arrested. He")
                print("was going to dump a body in the woods. You're now a hero who put a stop to a serial killer.")
                print()
                print("THE END. Thanks for playing :)")
            else: 
                print('ERROR. Please enter from the choices provided.')
        elif choice_three.upper() == 'QUIETLY FOLLOW':
            print("You decide to see what this strange man is up to, and you quietly follow him")
            print("through the darkening forest. Eventually, you arrive at a clearing, and the man")
            print("drops the bag. He pulls out a shovel and starts digging a hole. From the bag, he")
            print("pulls out a body, and he places it into the hole and covers it up. You're pretty")
            choice_ten = input("spooked, so do you LEAVE, or do you KEEP FOLLOWING him? ")

            print()

            #LEAVE or KEEP FOLLOWING
            if choice_ten.upper() == 'LEAVE':
                print("You decide to leave. You just watched a man dump a dead body, so you go to the")
                print("police. You tell them what you saw, and they investigate. They catch the guy, and")
                print("you're the reason they stopped a serial killer.")
                print()
                print("THE END. Thanks for playing :)")
            elif choice_ten.upper() == 'KEEP FOLLOWING':
                print("Some kind of courage has come over you, and you decide to keep following this creepy")
                print("guy. You follow him through the woods until finally, you arrive at an old, broken down")
                print("house. The man sits down on a log, and starts cleaning off his boots. You could catch him")
                choice_eleven = input("off guard and take him out. So do you ATTACK or KEEP YOUR DISTANCE? ")

                print()

                #ATTACK or KEEP YOUR DISTANCE - ENDING
                if choice_eleven.upper() == 'ATTACK':
                    print("You've decided to be a hero. You grab a really big stick and start to sneak up behind")
                    print("the killer. He doesn't hear you coming, and you wind up a mighty swing. The stick comes")
                    print("down on the man's head, and he dies. You call the police but they charge you for murder")
                    print("instead.")
                    print()
                    print("THE END. Thanks for playing :)")
                elif choice_eleven.upper() == 'KEEP YOUR DISTANCE':
                    print("You decide to stay back and watch. As you're creeping around, your foot lands on a twig.")
                    print("It makes a loud snap, and the man quickly turns towards the noise, sees you, draws his gun")
                    print("like he's in the wild west, and shoots you. He barries your body next to the other one.")
                    print()
                    print("THE END. Thanks for playing :)")
                else:
                    print('ERROR. Please enter from the choices provided.')
            else:
                print('ERROR. Please enter from the choices provided.')
        
        #MIND YOUR OWN BUSINESS - ENDING
        elif choice_three.upper() == 'MIND YOUR OWN BUSINESS':
            print("It's getting late and you don't want any trouble, so you choose to ignore the")
            print("man and keep making your way back home.")
        else:
            print('ERROR. Please enter from the choices provided.')

else: 
    print('ERROR. Please enter from the choices provided.')

print()


    