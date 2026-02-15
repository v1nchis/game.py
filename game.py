# esta en ingles porque mi teclado es 60% y es en ingles y me da pereza cambiarlo jijiji
# The Whisperer = Tells you wrong information, doesn't, if you stay still for a long time it appears behind you.
# The hall boy = A weird kid at the end of the hall, he doesn't atacks,  if you run to him,but if you stay still or walk slowly, you're cooked.
# The Broken DAMA = if you stare at her she will atack you, just don't get lost in her beauty
# Stalker = When lights go off, if you move it atacks, only move when the lights are on.
# The boneless = If you don't look at it directly it will atack you, just stare at that ugly mother fucker
# The mirror final boss = no matter what you do, you will die, it shows who you truly are "YO"
def print_Whisperer ():
    print("""
        .-.
       (o o)
       | O \
       |   | 
      /|   |\
     /_|___|_\
        /   \
       /_____\

    "The Whisperer"
""")
    
def print_hall_boy ():
    print("""
        (   )
       (  o o  )
        |   ^   |
        |  \___/  |
         \________/
          /  |  \
         /___|___\
            / \
           /___\

    "The Hall Boy"
""")
    
def print_The_Broken_DAMA ():
    print("""
        /\\
       /  \\
      |  X  X |
      |    ---   |
       \   ____   /
        \_________/
         /   |   \
        /____|____\
            / \
           /___\

    "The Broken Dama."
""")
    
def print_stalker ():
    print("""
         _______
        /       \
       |   O   O   |
       |     \___/     |
        \______/|\______/
              / | \
             /__|__\

    "The Stalker."
""")
    
def print_the_boneless ():
    print("""
        ______
       /      \
      |  0   0  |
      |    ___    |
       \__/     \__/
       /  /     \  \
      /__/         \__\

    "The Boneless."
""")
    
def print_the_mirror ():
    print("""
        ______________________
       |                      |
       |        ( ^_^ )       |
       |                      |
       |      YOU LOOK...     |
       |                      |
       |        (  o_o  )     |
       |        /  |   \      |
       |       /___|___\     |
       |______________________|

   ...
""")


def end_game():
    global name , hp , sanity
    print("\n---time to wake up---")
    
    print ("that's how" , name , "die!")
    print ( "-- wanna try again --" , name,"--")

print("Your last day")

name= str(input ("What's your name?: "))
aka = name[0].upper()

hp = 10
sanity = 10

def main_door (hp,sanity):
    print("You just woke up from a terrible dream\nBut you're not in your room\nIt seems a bit diferent\nYou have to choose a door")
    print("""
            ╔═════════╗             ╔═════════╗
            ║    1    ║             ║    2    ║
            ║  █████  ║             ║  █████  ║
            ║  █  ☠  █  ║             ║  █  👁  █  ║
            ║  █████  ║             ║  █████  ║
            ║    ▓▓    ║             ║    ▓▓    ║
            ╚════▓▓════╝             ╚════▓▓════╝

              choose wisely...
""")
    first_decision= int(input("What's your pick? -- First door (1) -- Second door (2) --: "))
    if first_decision == 1:
        hp -=0
        sanity -=0
        print(aka, "-- It's open --")
    elif first_decision == 2:
        hp -=0
        sanity -= 2
        print(aka,"-- Why is it closed? --")
        print(aka,"-- I'll open the first insted. --")
    return hp, sanity
hp , sanity = main_door(hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def first_door (hp,sanity):
    print(aka,"--  It's so dark --")
    print(aka,"--  What was that noise? --")
    print_Whisperer ()
    print("S -- Be carefull buddy,\n if you move before the lights turn on it's going to kill you. --")
    first_monster= int(input("What do you want to do?\n -- Stay still until lights turn on (1)--\n -- Run (2)--"))
    if first_monster == 1:
        hp *=0
        sanity *=0
        return end_game()

    elif first_monster == 2:
        hp -=0
        sanity -=0
        print(aka, "-- That was close! --")
    return hp, sanity
hp , sanity = first_door (hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def second_door (hp,sanity):
    print(aka, "--  Who is crying? -- ")
    print(aka, "--  Who is that little boy? -- ")
    print(aka, "--  Do you need help buddy? -- ")
    print_hall_boy ()  
    print("B -- crying,--")
    second_monster = int(input("Choose wisely...\n -- Stay still (1) --\n -- Walk slowly (2) --\n -- Run towards him (3 --)"))
    if second_monster ==1:
        hp *=0
        sanity *=0
        return end_game()
    elif second_monster ==2:
        hp -=10
        sanity -=10
        return end_game()
    elif second_monster ==3:
        hp -=0
        sanity -=0
        print(aka, "-- He just disapeared --")
    return hp, sanity
hp , sanity = second_door (hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def third_door (hp,sanity):
    print(aka, "--  What's that doll? --")
    print(aka, "it looks strange")
    print_The_Broken_DAMA ()    
    print("D -- staring. --")
    third_monster = int(input("What now?...\n-- Ignore it completely (1) --\n -- Grab it (2) -- \n -- Just look at it (3) --"))
    if third_monster ==1:
        hp -=0
        sanity -=0
        print(aka,"-- Hmm... that was interesting. --")
    elif third_monster ==2:
        hp *=0
        sanity *=0
        return end_game()
    elif third_monster ==3:
        hp *=0
        sanity *=0
        return end_game()
    return hp, sanity
hp , sanity = third_door (hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def fourth_door (hp,sanity):
    print(aka, "-- The lights went off suddenly --")
    print(aka, "-- The lights started flickering --")
    print(aka, "-- There's a fucking monster --")
    print_stalker ()  
    fourth_monster = int(input("What should you do?...\n -- Run (1) --\n -- Move when the lights are off (2) --\n -- Move only when the lights are on (3) --"))
    if fourth_monster ==1:
        hp *=0
        sanity *=0
        return end_game()
    elif fourth_monster ==2:
        hp *=0
        sanity *=0
        return end_game()
    elif fourth_monster ==3:
        hp -=0
        sanity -=0
        print(aka, "-- He looked like my chemistry teacher named Jesus, that was very unpleasant... --")
        return hp, sanity
hp , sanity = fourth_door (hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def fifth_door (hp,sanity):
    print(aka, "-- Holy shit!! --")
    print(aka,"-- It's an abomination!!!!! --")
    print_the_boneless ()
    fifth_monster = int(input("I'm tired of this shit!!! --\n -- Fight or die (1) --\n -- Run (2) --"))
    if fifth_monster ==1:
        hp -=9
        sanity -=9
        print (aka," -- AAAHHH --")
    elif fifth_monster ==2:
        hp *=0
        sanity *=0
        return end_game()
    return hp, sanity
hp , sanity = fifth_door(hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)

def last_door (hp,sanity):
    print(aka," -- I'm about to pass out. --")
    print(aka," -- That degenerate almost killed me... --")
    print(aka," -- That piece of shit dropped a key, What might it open? --")
    print(name, " -- OPPENED THE LAST DOOR AND... --")
    print(name, " -- Am I at the beggining again???? -- \n -- Does this fucking key open that second door?!??!! --")
    print("""
            ╔═════════╗             ╔═════════╗
            ║         ║             ║    2    ║
            ║         ║             ║  █████  ║
            ║           ║             ║  █  👁  █  ║
            ║         ║             ║  █████  ║
            ║          ║             ║    ▓▓    ║
            ╚════  ════╝             ╚════▓▓════╝

              ONLY ONE OPTION...
""")
    last_door = int(input(" -- Should I stay here and die (1) --\n -- Or open that fucking door (2) --"))
    if last_door ==1:
        hp *=0
        sanity *=0
        return end_game()
    elif last_door ==2:
        hp -=0
        sanity -=0
        print_the_mirror ()
        print(name," -- What is this nonsense, What have I become???!?!??! --")
        print(name," -- I AM A MONSTER -- ")
    return hp, sanity
hp , sanity = fifth_door(hp , sanity)
print(name, ", Your life is,", hp , "and your cordure is" , sanity,)
print (name, "--  yes you are a monster --")
    

