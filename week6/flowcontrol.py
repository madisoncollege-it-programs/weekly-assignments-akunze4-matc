#!/usr/bin/env python3

#Author: Alex Kunze for Door 3
#Purpose messing with IF statements

print("""You enter a dark room with two doors. 
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")
elif door == "3":
    print("You see Kermit the Frog standing in the back of the room. What do you do?")

    print("""
    1. Scream at the top of your lungs.
    2. Do nothing.
    3. Start running for one of the doors.
    """)

    what = input("> ")
    if what == "1":
        print("You instantly become petrified into stone.")
    elif what == "2":
        print("""
        Kermit continues to stare into your soul, and you begin to slowly petrify.

        1. Try to slowly break out of the petrification trance.
        2. Give in to the trance, and slowly become a stone figure of yourself.
        """)
        whut = input("> ")
        if whut == "1":
            print("""
        Kermit vanishes into thin air.

        1. Look around yourself doing a 360, to make sure this cursed frog isn't in your localized radious of sight.
        2. Do absolutely nothing, and hope that this is but a meer dream.
        """)
            whot = input("> ")
            if whot == "1":
                print("""
                To your delight the cursed frog is nowhere in your peripheral vision.
                
                1. Slowly walk towards the door from which you first arrived.
                2. Run towards the door from which your first arrived.
                """)
                whvt = input("> ")
                if whvt == "1":
                    print("""
                    Out of sheer luck, you make it out alive, and never return.

                    1. Slowly walk home.
                    2. Find a bus to take you home.
                            """)
                    duck = input("> ")
                    if duck == "1":
                        print("You make it home safely.")
                    elif duck == "2":
                        print("The bus falls into a giant sink hole in the middle, and you my good sir then realise that you will never see the surface again.")
                    else:
                        print("A giant bear comes out of nowhere at murders you.")
                else:
                    print("The ground below you vanishes into thin air, and you fall into complete darkness, never to be able to escape.")
            else:
                print("You die from a major panic attack")
        else:
            print("You become a stone figure, but retain your self awareness. You begin to see complete darkness.")
    elif what == "3":
        print("""
    Kermit senses your fear, and starts dashing towards you with a knife, and because you are
    just a meer human, he catches up to you, and ends your life with a single slash of his knife.""")
    else:
        print("Kermit slowly starts walking towards you, p.s. you didn't choose a valid number")


else:
    print("You did not select a door??? Good Call :)")

