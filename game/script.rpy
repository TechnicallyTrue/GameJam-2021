﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = DynamicCharacter("namevar")
define imagex = 1.0
define imagey = 0.6
define imagez = 0.75
define config.gl2 = True
define C = 0.0

# The game starts here.

label start:

    # Set custom pause menu
    $ _game_menu_screen = "pause_menu"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room
    show table


label date_start:

    scene bg room
    show table

    $ char1 = random.choice(chars)

    if char1 == "NULL":
        $ char1 = Char()
        $ chars.append(char1)

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


    # Set information

    $ namevar = char1.name
    show screen info (char1.name, char1.facts)

    # Pick the question

    $ current_question = random.choice(random.choice(char1.facts).questions)

    # Set timer

    $ timeout = 4.0
    #$ timer_range = 2.5
    $ timeout_label = "out_of_time"
    #show screen countdown

    # Ask the question

    menu:
        a "[current_question.q_text]"

        "[current_question.good_answer]":

            #hide screen countdown
            a "Good! I like you more now."
            $ char1.affection += 1

        "[current_question.bad_answer]":

            #hide screen countdown
            a "Well that's a shame. I like you less now."
            $ char1.affection -= 1

    "Current affection: [char1.affection]"

label check_end_condition:

    if char1.affection <= -3 or char1.affection >= 3:
        jump game_over

    jump date_start

label out_of_time:

    $ res = random.randint(1,2)

    if res == 1:
        a "INSERT POSITIVE RESPONSE TO SILENCE"
        $ char1.affection += 1
    else:
        a "INSERT NEGATIVE RESPONSE TO SILENCE"
        $ char1.affection -= 1

    jump check_end_condition

label game_over:

    "GAME OVER"

    return
