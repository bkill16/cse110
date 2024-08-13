print("\nYou went for a late night jog through the park. As you're running, you")
print('notice an old, dirty homeless man sitting on a bench underneath a')
print('streetlight.\n')

print('What will you do?')

print('\nIGNORE the man and keep running.')
print('STOP and say hello.')

scenario_one = input('Enter your choice: ')

if scenario_one.lower() == 'ignore':
    print('\nYou decide to ignore the creepy homeless man and continue your jog')
    print("through the dark park. As you continue running, you can't help but")
    print('feel as though someone is watching you. You take a quick glance over')
    print('your shoulder, and notice a tall man jogging behind you.\n')

    print('What will you do?')

    print('\nCONTINUE your jog.')
    print('TURN AROUND and go home.')
    print('SLOW down and let the man pass.')

    scenario_two = input('Enter your choice: ')

    if scenario_two.lower() == 'continue':
        print('\nYou continue running, convincing yourself that you are just')
        print('being paranoid. You jog a few minutes more, taking turns down')
        print('several different paths, but the man is still following close')
        print('behind.\n')

        print('What will you do?')

        print('\nCONFRONT the man.')
        print('SPRINT ahead and hide somewhere.')

        scenario_four = input('Enter your choice: ')

        if scenario_four.lower() == 'confront':
            print('\nYou decide to confront the man and ask him why he is')
            print('following you. He apologizes for coming off as a threat,')
            print('and says he was just trying to keep you safe, as the park')
            print('is very dangerous at night. You apologize for confronting')
            print('him and you jog together back to your apartment. He asks for')
            print('your number, you two go on a date and eventually get married.\n')

            print('THE END.\n')
        
        elif scenario_four.lower() == 'sprint':
            print('\nYou are afraid of the man following you, and take off in a sprint')
            print('in an effort to escape him. You get ahead, and hide behind a large tree.')
            print('after a few minutes, you think you are safe, and step out. You get')
            print('back on the trail, and suddenly, the man walks out from behind a structure.')
            print('He knew you were there the whole time. He grabs you and kills you.\n')

            print('THE END.\n')

        else:
            print('\nError. Invalid input. Please enter a valid choice.\n')

    elif scenario_two.lower() == 'turn around':
        print('\nYou decide that you have had enough creepiness for one night')
        print('and turn around and start heading back home. You jog past the')
        print('man, keeping a wide distance. On your way back to your apartment,')
        print('you are hit by a car and pass away in the ambulance.\n')

        print('THE END.\n')

    elif scenario_two.lower() == 'slow':
        print('\nYou decide to slow down and let the man pass you. You can hear')
        print('his footsteps getting closer and closer. As he passes you, you take')
        print('a quick glance, and notice that he is Kevin Durant.\n')

        print('What will you do?')

        print('\nLet him PASS in peace.')
        print('ASK him for an autograph.')

        scenario_five = input('Enter your choice: ')

        if scenario_five.lower() == 'pass':
            print('\nAs Kevin Durant jogs past you, he gives you a friendly smile and')
            print('nod. You see him again later in your run, and he acknowleges how cool')
            print('you are for leaving him alone. He offers an autograph and a picture, and')
            print('you get to brag to everyone that you met KD.\n')

            print('THE END.\n')

        elif scenario_five.lower() == 'ask':
            print('\nYou freak out. You cannot believe that THE Kevin Durant is jogging right')
            print('next to you. You get excited and start screaming at him like a deranged fangirl.')
            print('You beg him to sign your shirt and take a picture. KD is annoyed and just wants to')
            print('be left alone. He yells at you and tell you to go away. Shocked, you stop in the')
            print('middle of the trail, confused as to why someone would be so mean to you. As you stand')
            print('there, bewildered, a bear runs out from the trees and mauls you. You die a violent death.\n')

            print('THE END.\n')

        else:
            print('\nError. Invalid input. Please enter a valid choice.\n')

    else:
        print('\nError. Invalid input. Please enter a valid choice.\n')

elif scenario_one.lower() == 'stop':
    print('\nYou decide to stop and say hello to the man. It is a cold night,')
    print('and you notice that the man does not have anything to help him')
    print('stay warm. You sit and talk with him for a few minutes.\n')

    print('What will you do?')

    print('\nGET UP and continue your run.')
    print('HELP the man.')

    scenario_three = input('Enter your choice: ')

    if scenario_three.lower() == 'get up':
        print('\nAfter talking with the man for a while and learning more about')
        print('his sad situation, you decide that it is getting late and you had')
        print('better head home. On your way home, you see a billboard about being')
        print('charitable and compassionate. You regret not helping the man, so you')
        print('turn around and head back to the park. When you get there, the man is')
        print('gone. You jog back home with a lot on your mind, feeling bad about not')
        print('helping the man. On your way home, you are hit by a car and die instantly.\n')

        print('THE END.\n')

    elif scenario_three.lower() == 'help':
        print('\nAs you are sitting with the man, you pull some change from your wallet.')
        print('You give the man some money, and also give him the jacket from off your')
        print('back. The man is grateful, but you want to do more for him.\n')

        print('What will you do?')

        print('\nTake the man to get some FOOD.')
        print('Take the man to the nearest SHELTER.')

        scenario_six = input('Enter your choice: ')

        if scenario_six.lower() == 'food':
            print('\nYou and the homeless man walk to a nearby restaraunt. You order him')
            print('anything he wants. You two chat for a nice long while. You discover that')
            print('he is a billionaire. He is grateful for your kindess and leaves you all')
            print('of his riches in his will. You become insanely wealthy.\n')

            print('THE END.\n')

        elif scenario_six.lower() == 'shelter':
            print('\nYou take the homeless man to a nearby shelter. He thanks you, and you')
            print('go your separate ways. On your way home, you get hit by a car. You are')
            print('left paralyzed from the waist down. You lose your job, and end up homeless.')
            print('You are reuninted with your old friend in the homeless shelter.\n')

            print('THE END.\n')

        else:
            print('\nError. Invalid input. Please enter a valid choice.\n')

    else:
        print('\nError. Invalid input. Please enter a valid choice.\n')

else:
    print('\nError. Invalid input. Please enter a valid choice.\n')