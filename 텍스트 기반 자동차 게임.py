started = False

while True:
    try:
        command = input(">").strip().replace(" ", "").lower()
        if command == "help":
            print("start - to start the car\n"
                  "stop - to stop the car\n"
                  "quit - to exit")
        elif command == "start":
            if started:
                print("Car is already started!")
            else:
                print("Car started...Ready to go!")
                started = True
        elif command == "stop":
            if not started:
                print("Car is already stopped")
            else:
                print("Car stopped.")
                started = False
        elif command == "quit":
            break
        else:
            print("I don't understand that...")

    except Exception as e:
        print("error", e)