def house(firstroom):
    if firstroom=="kitchen":
        secondroom=input("There is long counter with dirty dishes everywhwere. off to one side there is as you'd except , a refrigirator. you may open the 'refrigirator or look in the 'cabinet' \n > ")
        if secondroom=="cabinet":
            print("hmm this one is a wrong cabinet")
        elif secondroom=="refrigirator":
            food=input("Inside the refrigirator you see the food and stuff. It looks pretty nasty. Would you like to eat some of the food(yes/no)?\n> ")
            if food=="no":
                print("Yoi die of starvation...eventually")
            elif food=="yes":
                print("you can enjoy these foods..")
    if firstroom=="upstairs":
        secondroom=input("oh its looks like a cabinet (open/not)?")  
        if secondroom=="open":
            food=input("there is a large book collection in here..(read/leave)?")
            if food=="read":
                print("WOW!..I think i can read some of these books..")
            elif food=="leave":
                print("Hmm..its looks like a boring books")
        if secondroom=="not":
            food=input("ok then i shall go to the next room..(next)")
            if food=="next":
                print("Hmm..i again came to the same place")
        
print("WELCOME TO MITCHELL'S TINY ADVENTURE!")
firstroom=input("You are in a creepy house! Would you like to  go 'upstairs' or into the 'kitchen ?\n> '")
check=house(firstroom)
        
        




