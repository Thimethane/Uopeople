# This program has been enhanced to include additional words to fill in, 
# and it determines whether to use "a" or "an" before the user's input based on its first letter.

def get_article(word):
    """Determine whether to use 'a' or 'an' based on the first letter of the word."""
    if word[0].lower() in 'aeiou':
        return "an"
    else:
        return "a"

def main():
    # Prompt user for inputs
    adjective = input("Please enter an adjective: ")
    animal = input("Please enter an animal: ")
    verb1 = input("Please enter a verb: ")
    exclamation = input("Please enter an exclamation: ")
    verb2 = input("Please enter another verb: ")
    verb3 = input("Please enter a third verb: ")
    noun = input("Please enter a noun: ")
    place = input("Please enter a place: ")

    # Capitalize the exclamation
    exclamation = exclamation.capitalize()

    # Create the story with the user's words
    story = (
        f"The other day, I was really in trouble. It all started when I saw a very\n"
        f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
        f"I could think to do was to {verb2} over and over. Miraculously,\n"
        f"that caused it to stop, but not before it tried to {verb3}\n"
        f"right in front of my family. I couldn't believe it when I saw {get_article(noun)} {noun} in {place}!"
    )

    # Display the story
    print("\nYour story is:\n")
    print(story)

# Run the main function
if __name__ == "__main__":
    main()
