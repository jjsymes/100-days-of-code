print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input("Press any key to continue...")
print('''
                        ,sdPBbs.
                      ,d$$$$$$$$b.
                     d$P'`Y'`Y'`?$b
                    d'    `  '  \ `b
                   /    |        \  \\
                  /    / \       |   \
             _,--'        |      \    |
           /' _/          \   |        \\
        _/' /'             |   \        `-.__
    __/'       ,-'    /    |    |     \      `--...__
  /'          /      |    / \     \     `-.           `\\
 /    /;;,,__-'      /   /    \            \            `-.
/    |;;;;;;;\                                             \\
''')
print("The first obstacle in your way is a great mountain.")
user_input = input("Do you go over, round or through the mountain? ").lower()
if user_input == "over":
    print('''
*******************************************************************************
                       ``==
                        )  `==
                         )    `==
                         )       `=
                         )         }
                        )         ,|
                       )      , == |
                      )    ,==     |            ,----
                     )  ,==        |           ,     `~~~~\\
                    ),==           `         ,   `--------
                     `)             \       ,   /
             _____      )            \    ,    /
             ` ._ `      )      ______\_,     ,
                  \ \    ,)----'             /
                   \ \__/      ____        ,=
                    `     ,_.--    --- -==`
                     `---'
*******************************************************************************
    ''')
    print("You go over the mountain")
    user_input = input("A dragon appears, do you fight or run? ").lower()
    if user_input == "fight":
        print("You fight the dragon")
        print("You are completely outmached. As you prepare to fire an arrow, you are engulfed in scorching dragon fire and burnt to a crisp.")
        print("The End")
        exit()
    elif user_input == "run":
        print("You are not prepared for this fight. You decide to run!")
        print("Luckily you were not spotted. You run for miles and before you knew it, you were over the mountain.")
    else:
        print("You panic. The dragon spotted you and swoops down towards you, but before it reaches you, you take your own life by jumping off a large cliff. As you fall you wonder why you even bothered to embark on this adventure.")
        print("The End")
        exit()

elif user_input == "round":
    print("You go round the mountain")
    user_input = input("A legion of Orcs! Do you hide behind a tree, or in the long grass? (type grass or tree) ").lower()
    if user_input == "grass":
        print("You dive into the tall grass")
        print("As you patiently wait, the marching steps for the legion become ever louder, until an orc steps on your head. The impact of the step knocks you out. You are a dead man.")
        print("The End")
        exit()
    elif user_input == "tree":
        print("You hide behind a tree at the edge of a forest")
        print("You patiently wait as the legion marches past. The coast is now clear and continue along your journey.")
    else:
        print("You decide that this adventure was too much for you, turn around, and go back home.")
        print("The End")
        exit()
elif user_input == "through":
    print('''
             ,      ,
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\\
  jgs /       '----'       \\
    ''')
    print("You go through the mountain")
    user_input = input("A couple of Goblins have spotted you! Do you hunt them down, or let them run off? (type hunt or ignore)").lower()
    if user_input == "hunt":
        print("You hunt them down")
        print("They are too slow for you and you slay them with your sword.")
        print("Not before too long you see the light at the end of the tunnel. The other side of the mountain approaches, and you make it out alive.")
    elif user_input == "ignore":
        print("You ignore them and hope for the best")
        print("As you go further through the mountain tunnel, you start to think you will make it through alive. You eventually see a light in the distance... the other side of the mountain! You make a run for the exit, then suddenly, a goblin arrow pierces your skull.")
        print("The End")
        exit()
    else:
        print("You were not ready for this adventure. You curl up into a ball and cry, and hope the goblins don't come back. When you finally decide to continue, you get lost in the labyrinth of the caves. Your torch eventually goes out and you are trapped in complete darkness. You try to find an exit, but drop after many hours drop in exhaustion. In your sleep you are slain by the goblins you encountered earlier.")
        print("The End")
        exit()
else:
    print("You do not do anything. You stand still for hours despite your hunger, thirst or tiredness. As the hours go by you lose your energy, until you finally drop dead.")
    print("The End")
    exit()

user_input = input("You get to a river. Do you swim or wait for a ferry? (swim or wait) ").lower()

if user_input == "swim":
    print("You swim, but half way you lose your stamina. With every stroke you start to drown. Eventually you cannot stay above the surface of the water and suffocate. Your dead body floats downstream.")
    print("The End")
    exit()
elif user_input == "wait":
    print("You wait for a ferry")
    print("Eventually a fellow adventurer comes to your side of the bank on the ferry. You ride the ferry to the other side")
else:
    print("You do not do anything. You stand still for hours despite your hunger, thirst or tiredness. As the hours go by you lose your energy, until you finally drop dead.")
    print("The End")
    exit()

print('''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \\
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
''')
print("You follow your treasure map and think you have found the spot. You look up from your map to find a small abandoned shack. You go inside to find it is empty with a basement. You walk downstairs to find lots of coloured doors. The treasure must be in one of them.")
user_input = input("Which coloured door do you choose? ").lower()

if user_input == "red":
    print("You open the red door and flames engulf you. You are burnt alive.")
    print("The End")
    exit()
elif user_input == "blue":
    print("You open the blue door and are instantly grabbed by the hand of a huge beast. You are eaten alive.")
    print("The End")
    exit()
elif user_input == "yellow":
    print("You open the yellow door to find a chest at the centre of a small room. You open the chest to find the treasure. You are now rich beyond your wildest dreams!")
    print("The End")
    exit()
else:
    print(f"You open the {user_input} door.")
    print(f"The excitement of what lies on the other side is too much! As you reach for the handle of the {user_input} door, you feel a pain in your chest and lose all energy. You eventually black out and drop dead. You never find out what was on the other side of that door.")
    print("The End")
    exit()