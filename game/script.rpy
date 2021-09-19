# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = DynamicCharacter("namevar")
define imagex = 1.0
define imagey = 0.6
define imagez = 0.75
define config.gl2 = True
define C = 0.0
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

    $ char1 = Char()
    $ C = char1.hair_colour
    show expression char1.hair_back_fill as hair_back_fill behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    show expression char1.hair_back_lines as hair_back_lines behind table:
        zoom imagez xalign imagex yalign imagey
    $ C = char1.shirt_colour_a
    show expression char1.back_shirt_colour_a as back_shirt_colour_a behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    $ C = char1.shirt_colour_b
    show expression char1.back_shirt_colour_b as back_shirt_colour_b behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    show expression char1.back_shirt_lines as back_shirt_lines behind table:
        zoom imagez xalign imagex yalign imagey
    #Draws back hair and body behind table
    $ C = char1.shirt_colour_a
    show expression char1.body_colour_a_N as body_colour_a_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    $ C = char1.shirt_colour_b
    show expression char1.body_colour_b_N as body_colour_b_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    show expression char1.body_colour_c_N as body_colour_c_N:
        zoom imagez xalign imagex yalign imagey
    show expression char1.body_lines_N as body_lines_N:
        zoom imagez xalign imagex yalign imagey
    #body drawn

    show expression char1.hair_front_fill as hair_front_fill1:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    #hair front fill 1
    show expression char1.eye_back as eye_back:
        zoom imagez xalign imagex yalign imagey
    $ C = char1.eye_colour
    show expression char1.eye_fill as eye_fill:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    show expression char1.eye_lines as eye_lines:
        zoom imagez xalign imagex yalign imagey
    $ C = char1.hair_colour
    show expression char1.eyebrow_colour_N as eyebrow_colour_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C)
    show expression char1.eyebrow_lines_N as eyebrow_lines_N:
        zoom imagez xalign imagex yalign imagey
    show expression char1.mouth_closed_N as mouth_closed_N:
            zoom imagez xalign imagex yalign imagey
    #face drawn
    show expression char1.hair_front_fill as hair_front_fill2:
        zoom imagez xalign imagex yalign imagey
        alpha 0.5
        matrixcolor HueMatrix(C)
    show expression char1.hair_front_lines as hair_front_lines:
        zoom imagez xalign imagex yalign imagey




    $ namevar = "Man with Covid"

    #show cat neutral behind table

    show screen info (char1.name, char1.facts)

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
