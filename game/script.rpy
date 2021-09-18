# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = DynamicCharacter("namevar")

# python:
#     facts = [
#         Fact("Likes cats"), [
#             Question("Are you a cat person or a dog person?", "Cat person",
#                     "Dog person"),
#             Question("Do you think cats are secretly evil?", "No", "Yes"),
#             Question("Would you be open to adopting a cat?", "Yes", "No")
#         ]
#     ]



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show table

    $ namevar = "Man with Covid"

    show cat neutral behind table

    show screen info ("Testy test", ["A", "B", "C"])

    # These display lines of dialogue.

    a "Hello. This is placeholder dialogue."

    a "I EXIS T ONLY TO KILL I EX IST ON LY TO KIL L I EX IS T ONLY T O KILL I EX IST ONLY T O KILL I EXIS T ONLY TO KI LL"

    menu:
        "That seems bad.":

            a "I do not care."

        "Great! I crave death.":

            a "Well that works out for both of us."

            $ namevar = "Old Character"

    "The cat murders you."

    define b = Character("New Character")

    b "Hello! Oh, am I interrupting something?"

    a "Not really, no."

    # This ends the game.

    return
