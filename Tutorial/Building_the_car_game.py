command=""
while True:
    command= input("> ").lower()
    if command.lower() == "start":
        print("The Car has started....")
    elif command.lower() == "stop":
        print("THe Car has stopped...")
    elif command.lower() == "help":
        print("""start - car waill start
stop - car will stop
quit - the game will quit""" )
    elif command.lower() == "quit":
        break
    else:
        print("I dont understand")
