# The Forest of Secrets - A Text-based Adventure Game with Exit and Go Back Options
# This program is a simple text-based adventure game where the player navigates through a forest
# with multiple paths, challenges, and outcomes based on their choices.
# 
# Creativity Beyond Expectations:
# - Multiple retry prompts for invalid inputs.
# - "EXIT" option to end the game anytime.
# - "BACK" option to go to the previous step and retry decisions.
# - Case-insensitive input processing.
# - Enhanced game complexity with various outcomes based on choices.
# - Clear comments and exception handling across all game levels.


def forest_adventure():
    """
    This function runs the main game loop of The Forest of Secrets. 
    Players can progress, retry, exit, or go back to previous steps during the game.
    """
    
    print("Welcome to *The Forest of Secrets*! You are a brave explorer venturing into an ancient and mystical forest.")
    print("Legend says that deep within the forest, there is a hidden treasure, but it is guarded by strange creatures and magic.")

    # A stack to keep track of the player's previous choices for the "go back" feature
    choice_stack = []

    # Helper function to manage the "go back" option
    def go_back():
        if choice_stack:
            return choice_stack.pop()
        else:
            print("You are already at the start of the game!")
            return None

    # Helper function to offer retry or exit after game over or win
    def retry_or_exit():
        while True:
            print("\nWould you like to RESTART the game or EXIT?")
            user_choice = input().lower()
            if user_choice == "restart":
                print("\nRestarting the game...\n")
                return True  # Return True to indicate restarting
            elif user_choice == "exit":
                print("Thank you for playing! Goodbye!")
                return False  # Return False to indicate exiting
            else:
                print("Invalid input. Please choose 'RESTART' or 'EXIT'.")
    
    while True:  # Main loop that allows restarting the game
        # First level choice
        while True:
            print("\nYou walk deeper into the forest and come across a fork in the path.")
            print("Do you choose to go LEFT, RIGHT, or STRAIGHT? (Type 'EXIT' to quit or 'BACK' to go back)")
            choice1 = input().lower()

            if choice1 == "exit":
                print("Exiting the game. Thank you for playing!")
                return
            elif choice1 == "back":
                previous_choice = go_back()
                if previous_choice:
                    choice1 = previous_choice
                    break
            elif choice1 in ["left", "right", "straight"]:
                choice_stack.append(choice1)
                break
            else:
                print("Invalid choice. Please choose LEFT, RIGHT, STRAIGHT, EXIT, or BACK.")

        # Second level depending on the first choice
        if choice1 == "left":
            while True:
                print("\nYou decide to go left. The path is narrow and overgrown with vines. Suddenly, you hear a rustling noise.")
                print("Do you INVESTIGATE the noise or KEEP WALKING? (Type 'EXIT' to quit or 'BACK' to go back)")
                choice2 = input().lower()

                if choice2 == "exit":
                    print("Exiting the game. Thank you for playing!")
                    return
                elif choice2 == "back":
                    previous_choice = go_back()
                    if previous_choice:
                        choice1 = previous_choice
                        break
                elif choice2 in ["investigate", "keep walking"]:
                    choice_stack.append(choice2)
                    break
                else:
                    print("Invalid choice. Please choose INVESTIGATE, KEEP WALKING, EXIT, or BACK.")

            if choice2 == "investigate":
                while True:
                    print("\nYou cautiously move toward the sound and find a wounded deer. It looks at you with pleading eyes.")
                    print("Do you HELP the deer or WALK AWAY? (Type 'EXIT' to quit or 'BACK' to go back)")
                    choice3 = input().lower()

                    if choice3 == "exit":
                        print("Exiting the game. Thank you for playing!")
                        return
                    elif choice3 == "back":
                        previous_choice = go_back()
                        if previous_choice:
                            choice2 = previous_choice
                            break
                    elif choice3 in ["help", "walk away"]:
                        choice_stack.append(choice3)
                        break
                    else:
                        print("Invalid choice. Please choose HELP, WALK AWAY, EXIT, or BACK.")

                if choice3 == "help":
                    print("\nYou tend to the deer's wounds, and as you do, it transforms into a magical creature!")
                    print("The creature grants you safe passage through the forest and leads you to the hidden treasure. You win!")
                    if retry_or_exit():
                        continue
                    else:
                        return
                elif choice3 == "walk away":
                    print("\nYou leave the deer and continue walking. Unfortunately, the path becomes too treacherous, and you get lost.")
                    print("After hours of wandering, you realize you should have helped the deer. Game over.")
                    if retry_or_exit():
                        continue
                    else:
                        return

            elif choice2 == "keep walking":
                while True:
                    print("\nYou ignore the noise and keep walking. As you continue, you find yourself surrounded by thick fog.")
                    print("Suddenly, a shadowy figure emerges. Do you RUN or STAND YOUR GROUND? (Type 'EXIT' to quit or 'BACK' to go back)")
                    choice3 = input().lower()

                    if choice3 == "exit":
                        print("Exiting the game. Thank you for playing!")
                        return
                    elif choice3 == "back":
                        previous_choice = go_back()
                        if previous_choice:
                            choice2 = previous_choice
                            break
                    elif choice3 in ["run", "stand your ground"]:
                        choice_stack.append(choice3)
                        break
                    else:
                        print("Invalid choice. Please choose RUN, STAND YOUR GROUND, EXIT, or BACK.")

                if choice3 == "run":
                    print("\nYou run as fast as you can, but the figure follows you. You trip on a root and are captured. Game over.")
                    if retry_or_exit():
                        continue
                    else:
                        return
                elif choice3 == "stand your ground":
                    print("\nYou face the figure bravely, and it turns out to be a friendly forest guardian.")
                    print("Impressed by your courage, the guardian shows you a secret passage to the treasure. You win!")
                    if retry_or_exit():
                        continue
                    else:
                        return

        elif choice1 == "right":
            while True:
                print("\nYou turn right and find yourself at the edge of a river. The water is fast and deep.")
                print("Do you SWIM across or BUILD a raft? (Type 'EXIT' to quit or 'BACK' to go back)")
                choice2 = input().lower()

                if choice2 == "exit":
                    print("Exiting the game. Thank you for playing!")
                    return
                elif choice2 == "back":
                    previous_choice = go_back()
                    if previous_choice:
                        choice1 = previous_choice
                        break
                elif choice2 in ["swim", "build"]:
                    choice_stack.append(choice2)
                    break
                else:
                    print("Invalid choice. Please choose SWIM, BUILD, EXIT, or BACK.")

            if choice2 == "swim":
                print("\nYou dive into the water, but the current is too strong! You're swept away and drown. Game over.")
                if retry_or_exit():
                    continue
                else:
                    return
            elif choice2 == "build":
                while True:
                    print("\nYou gather some logs and vines to build a raft. As you sail across, a river monster appears!")
                    print("Do you FIGHT the monster or ESCAPE? (Type 'EXIT' to quit or 'BACK' to go back)")
                    choice3 = input().lower()

                    if choice3 == "exit":
                        print("Exiting the game. Thank you for playing!")
                        return
                    elif choice3 == "back":
                        previous_choice = go_back()
                        if previous_choice:
                            choice2 = previous_choice
                            break
                    elif choice3 in ["fight", "escape"]:
                        choice_stack.append(choice3)
                        break
                    else:
                        print("Invalid choice. Please choose FIGHT, ESCAPE, EXIT, or BACK.")

                if choice3 == "fight":
                    print("\nYou grab a stick and bravely face the monster. With clever moves, you defeat it and reach the shore safely.")
                    print("The treasure is just beyond the trees. You win!")
                    if retry_or_exit():
                        continue
                    else:
                        return
                elif choice3 == "escape":
                    print("\nYou try to paddle faster to escape, but the monster overturns your raft. You sink into the depths. Game over.")
                    if retry_or_exit():
                        continue
                    else:
                        return

        elif choice1 == "straight":
            while True:
                print("\nYou walk straight and find an ancient temple hidden within the forest.")
                print("The temple has two doors: one marked with a SUN symbol and the other with a MOON symbol.")
                print("Do you enter the SUN door or the MOON door? (Type 'EXIT' to quit or 'BACK' to go back)")
                choice2 = input().lower()

                if choice2 == "exit":
                    print("Exiting the game. Thank you for playing!")
                    return
                elif choice2 == "back":
                    previous_choice = go_back()
                    if previous_choice:
                        choice1 = previous_choice
                        break
                elif choice2 in ["sun", "moon"]:
                    choice_stack.append(choice2)
                    break
                else:
                    print("Invalid choice. Please choose SUN, MOON, EXIT, or BACK.")

            if choice2 == "sun":
                while True:
                    print("\nYou open the SUN door and step into a room filled with bright light.")
                    print("A riddle is inscribed on the wall: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.'")
                    print("Do you ANSWER the riddle or LEAVE the room? (Type 'EXIT' to quit or 'BACK' to go back)")
                    choice3 = input().lower()

                    if choice3 == "exit":
                        print("Exiting the game. Thank you for playing!")
                        return
                    elif choice3 == "back":
                        previous_choice = go_back()
                        if previous_choice:
                            choice2 = previous_choice
                            break
                    elif choice3 in ["answer", "leave"]:
                        choice_stack.append(choice3)
                        break
                    else:
                        print("Invalid choice. Please choose ANSWER, LEAVE, EXIT, or BACK.")

                if choice3 == "answer":
                    print("\nYou answer the riddle: 'An echo.' The room fills with a golden glow, and a hidden door opens, revealing the treasure. You win!")
                    if retry_or_exit():
                        continue
                    else:
                        return
                elif choice3 == "leave":
                    print("\nYou decide to leave the room. As you step back into the forest, the door closes behind you. You are lost forever. Game over.")
                    if retry_or_exit():
                        continue
                    else:
                        return

            elif choice2 == "moon":
                print("\nYou open the MOON door and step into a dark room. As you proceed, the floor gives way beneath you, and you fall into a pit. Game over.")
                if retry_or_exit():
                    continue
                else:
                    return

# Start the game
forest_adventure()
