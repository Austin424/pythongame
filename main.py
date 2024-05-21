run = True
menu = True
play = False
rules = False

# (# = choice input)
#  (> = empty input)

while run:
    while menu:
        print('1. NEW GAME')
        print('2. LOAD GAME')
        print('3. RULES')
        print('4. QUIT GAME')

        if rules:
            print("Here are some rules.")
            rules = False
            choice = input("# ")
            input("> ")
        else:
            choice = input("# ") 


        if choice =="1":
            name = input("# What's your name, hero? ")
            menu = False
            play = True
        elif choice =="2":
            pass
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play: 
        print(name)

        dest = input("# ")

        if dest - "0":
            play = False
            menu = True