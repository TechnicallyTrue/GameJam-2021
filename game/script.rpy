# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = DynamicCharacter("namevar")
define c = Character("Dr. Whiskers")
define imagex = 0.6
define imagey = 0.6
define imagez = 0.75
define config.gl2 = True
define C1 = 0.0
define C2 = 0.0
define C3 = 0.0
define C4 = 0.0
define affection = 0
define C5 = "#FFFFFF"
# The game starts here.

label start:

    stop music fadeout 0.5

    $ renpy.music.set_volume(0.5)

    # Set custom pause menu
    $ _game_menu_screen = "pause_menu"

    # Clear the list of characters because apparently that persists between
    # games because of course why wouldn't it AHHHHHHHHHHHHHHHHHHHH
    $ chars = ["NULL"]

    # Set score to 0
    $ score = 0

    # Set the scene
    scene bg room
    show table

label tutorial:

    show cat behind table

    c "Hello, and welcome to the Cafe Gamophobia!"
    c "I'm Dr. Whiskers, and I've got a PhD in ~love~"
    c "And a minor in paleoanthropology."
    c "Over the course of your evening here, we're going to match you up with several potential suitors."
    c "They'll probably ask you some questions to make sure you're a compatible date."
    c "Make sure to answer nice and promptly - nothing worse than an awkward silence!"
    c "(Unless you're into that)"
    c "((No judgement here))"
    c "(((Ok a little bit of judgement)))"
    c "Try not to offend anyone too badly - if someone takes a real strong disliking to you, we might just have to boot you out."
    c "On the other hand, if someone takes a shine to you, they'll probably want to take you away themselves!"
    c "I guess if you were some kind of crazy person who wanted to be here for an I N F I N I T E length of time, you'd have to, I dunno, keep everyone sort of neutral towards you?"
    c "But that'd be weird, wouldn't it? This isn't a game, you know ;)"
    c "Alright! I'll leave you to it! Remember that you can hit the ESC key or right click to bring up the menu."
    c "But be warned - looking at the menu doesn't pause the ceaseless march of time!"
    c "There's no pausing ~loooooooooooooooooooooooooooooooove~!"
    c "Ok bye!"

    play music gameplay_final loop fadeout 1

label date_start:

    scene bg room
    show table

    $ char1 = random.choice(chars)

    if char1 == "NULL":
        $ char1 = Char()
        $ chars.append(char1)

    $ C1 = char1.hair_colour
    $ C2 = char1.eye_colour
    $ C3 = char1.shirt_colour_a
    $ C4 = char1.shirt_colour_b
    $ C5 = char1.skin_colour
    $ affection = char1.affection


    show expression char1.hair_back_fill as hair_back_fill behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C1)
    show expression char1.hair_back_lines as hair_back_lines behind table:
        zoom imagez xalign imagex yalign imagey
    show expression char1.back_shirt_colour_a as back_shirt_colour_a behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C3)
    show expression char1.back_shirt_colour_b as back_shirt_colour_b behind table:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C4)
    show expression char1.back_shirt_lines as back_shirt_lines behind table:
        zoom imagez xalign imagex yalign imagey
    #Draws back hair and body behind table
    show expression char1.body_colour_a_N as body_colour_a_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C3)
    show expression char1.body_colour_b_N as body_colour_b_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C4)
    show expression char1.body_colour_c_N as body_colour_c_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor TintMatrix(C5)
    show expression char1.body_lines_N as body_lines_N:
        zoom imagez xalign imagex yalign imagey
    #body drawn

    show expression char1.hair_front_fill as hair_front_fill1:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C1)
    #hair front fill 1
    show expression char1.eye_back as eye_back:
        zoom imagez xalign imagex yalign imagey
    show expression char1.eye_fill as eye_fill:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C2)
    show expression char1.eye_lines as eye_lines:
        zoom imagez xalign imagex yalign imagey
    show expression char1.eyebrow_colour_N as eyebrow_colour_N:
        zoom imagez xalign imagex yalign imagey
        matrixcolor HueMatrix(C1)
    show expression char1.eyebrow_lines_N as eyebrow_lines_N:
        zoom imagez xalign imagex yalign imagey
    show expression char1.mouth_closed_N as mouth_closed_N:
        zoom imagez xalign imagex yalign imagey
    #face drawn
    show expression char1.hair_front_fill as hair_front_fill2:
        zoom imagez xalign imagex yalign imagey
        alpha 0.5
        matrixcolor HueMatrix(C1)
    show expression char1.hair_front_lines as hair_front_lines:
        zoom imagez xalign imagex yalign imagey

    #affection meter
    if affection == -2:
        show affection_meter 6:
            zoom 0.7 xpos 875 ypos 425
    if affection == -1:
        show affection_meter 5:
            zoom 0.7 xpos 875 ypos 425
    if affection == 0:
        show affection_meter 4:
            zoom 0.7 xpos 875 ypos 425
    if affection == 1:
        show affection_meter 3:
            zoom 0.7 xpos 875 ypos 425
    if affection == 2:
        show affection_meter 2:
            zoom 0.7 xpos 875 ypos 425


    # Set information

    $ namevar = char1.name
    show screen info (char1.name, char1.facts)

    # Pick the question

    $ current_question = random.choice(random.choice(char1.facts).questions)
    $ pos_response = random.choice(pos_responses)
    $ neg_response = random.choice(neg_responses)
    $ pos_timeout_res = random.choice(pos_timeout)
    $ neg_timeout_res = random.choice(neg_timeout)

    # Set timer

    $ timeout = 4.0
    #$ timer_range = 2.5
    $ timeout_label = "out_of_time"
    #show screen countdown

    # Ask the question

    menu:
        a "[current_question.q_text]"

        "[current_question.good_answer]":
            hide mouth_closed_N
            hide body_colour_a_N
            hide body_colour_b_N
            hide body_colour_c_N
            hide body_lines_N

            $ affection += 1
            show expression char1.blush as blush:
                zoom imagez xalign imagex yalign imagey
                alpha 0.5
            show expression char1.body_colour_a_H as body_colour_a_H behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C3)
            show expression char1.mouth_open_N as mouth_open_N:
                zoom imagez xalign imagex yalign imagey
            show expression char1.body_colour_b_H as body_colour_b_H behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C4)
            show expression char1.body_colour_c_H as body_colour_c_H behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor TintMatrix(C5)
            show expression char1.body_lines_H as body_lines_H behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey


            if affection == -3:
                show affection_meter 7:
                    zoom 0.7 xpos 875 ypos 425
            if affection == -2:
                show affection_meter 6:
                    zoom 0.7 xpos 875 ypos 425
            if affection == -1:
                show affection_meter 5:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 0:
                show affection_meter 4:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 1:
                show affection_meter 3:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 2:
                show affection_meter 2:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 3:
                show affection_meter 1:
                    zoom 0.7 xpos 875 ypos 425

            #hide screen countdown
            a "[pos_response]"
            $ char1.affection += 1
                #affection meter

        "[current_question.bad_answer]":
            hide mouth_closed_N
            hide eyebrow_colour_N
            hide eyebrow_lines_N
            hide body_colour_a_N
            hide body_colour_b_N
            hide body_colour_c_N
            hide body_colour_a_H
            hide body_colour_b_H
            hide body_colour_c_H
            hide body_lines_N

            $ affection -= 1

            show expression char1.mouth_closed_A as mouth_closed_A:
                zoom imagez xalign imagex yalign imagey
            show expression char1.eyebrow_colour_A as eyebrow_colour_A behind hair_front_fill2:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C1)
            show expression char1.eyebrow_lines_A as eyebrow_lines_A behind hair_front_fill2:
                zoom imagez xalign imagex yalign imagey
            show expression char1.body_colour_a_A as body_colour_a_A behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C3)
            show expression char1.body_colour_b_A as body_colour_b_A behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C4)
            show expression char1.body_colour_c_A as body_colour_c_A behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey
                matrixcolor TintMatrix(C5)
            show expression char1.body_lines_A as body_lines_A behind hair_front_fill1:
                zoom imagez xalign imagex yalign imagey


            if affection == -3:
                show affection_meter 7:
                    zoom 0.7 xpos 875 ypos 425
            if affection == -2:
                show affection_meter 6:
                    zoom 0.7 xpos 875 ypos 425
            if affection == -1:
                show affection_meter 5:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 0:
                show affection_meter 4:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 1:
                show affection_meter 3:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 2:
                show affection_meter 2:
                    zoom 0.7 xpos 875 ypos 425
            if affection == 3:
                show affection_meter 1:
                    zoom 0.7 xpos 875 ypos 425

            #hide screen countdown
            a "[neg_response]"
            $ char1.affection -= 1

    #"Current affection: [char1.affection]"

label check_end_condition:

    if char1.affection <= -3:
        play music ending_final fadeout 1
        jump bad_game_over

    if char1.affection >= 3:
        play music ending_final fadeout 1
        jump good_game_over

    $ score += 1

    jump date_start

label out_of_time:

    $ res = random.randint(1,2)

    if res == 1:
        hide mouth_closed_N
        hide body_colour_a_N
        hide body_colour_b_N
        hide body_colour_c_N
        hide body_lines_N
        show expression char1.blush as blush:
            zoom imagez xalign imagex yalign imagey
            alpha 0.5
        show expression char1.body_colour_a_H as body_colour_a_H behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor HueMatrix(C3)
        show expression char1.mouth_open_N as mouth_open_N:
            zoom imagez xalign imagex yalign imagey
        show expression char1.body_colour_b_H as body_colour_b_H behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor HueMatrix(C4)
        show expression char1.body_colour_c_H as body_colour_c_H behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor TintMatrix(C5)
        show expression char1.body_lines_H as body_lines_H behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey

        $ affection += 1
        if affection == -3:
            show affection_meter 7:
                zoom 0.7 xpos 875 ypos 425
        if affection == -2:
            show affection_meter 6:
                zoom 0.7 xpos 875 ypos 425
        if affection == -1:
            show affection_meter 5:
                zoom 0.7 xpos 875 ypos 425
        if affection == 0:
            show affection_meter 4:
                zoom 0.7 xpos 875 ypos 425
        if affection == 1:
            show affection_meter 3:
                zoom 0.7 xpos 875 ypos 425
        if affection == 2:
            show affection_meter 2:
                zoom 0.7 xpos 875 ypos 425
        if affection == 3:
            show affection_meter 1:
                zoom 0.7 xpos 875 ypos 425

        a "[pos_timeout_res]"
        $ char1.affection += 1

    else:
        hide mouth_closed_N
        hide eyebrow_colour_N
        hide eyebrow_lines_N
        hide body_colour_a_N
        hide body_colour_b_N
        hide body_colour_c_N
        hide body_colour_a_H
        hide body_colour_b_H
        hide body_colour_c_H
        hide body_lines_N

        show expression char1.mouth_closed_A as mouth_closed_A:
            zoom imagez xalign imagex yalign imagey
        show expression char1.eyebrow_colour_A as eyebrow_colour_A behind hair_front_fill2:
            zoom imagez xalign imagex yalign imagey
            matrixcolor HueMatrix(C1)
        show expression char1.eyebrow_lines_A as eyebrow_lines_A behind hair_front_fill2:
            zoom imagez xalign imagex yalign imagey
        show expression char1.body_colour_a_A as body_colour_a_A behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor HueMatrix(C3)
        show expression char1.body_colour_b_A as body_colour_b_A behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor HueMatrix(C4)
        show expression char1.body_colour_c_A as body_colour_c_A behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
            matrixcolor TintMatrix(C5)
        show expression char1.body_lines_A as body_lines_A behind hair_front_fill1:
            zoom imagez xalign imagex yalign imagey
        $ affection -= 1
        if affection == -3:
            show affection_meter 7:
                zoom 0.7 xpos 900 ypos 425
        if affection == -2:
            show affection_meter 6:
                zoom 0.7 xpos 900 ypos 425
        if affection == -1:
            show affection_meter 5:
                zoom 0.7 xpos 900 ypos 425
        if affection == 0:
            show affection_meter 4:
                zoom 0.7 xpos 900 ypos 425
        if affection == 1:
            show affection_meter 3:
                zoom 0.7 xpos 900 ypos 425
        if affection == 2:
            show affection_meter 2:
                zoom 0.7 xpos 900 ypos 425
        if affection == 3:
            show affection_meter 1:
                zoom 0.7 xpos 900 ypos 425

        a "[neg_timeout_res]"
        $ char1.affection -= 1

    jump check_end_condition

label good_game_over:

    hide screen info

    a "Why don't we get out of here?"

    "The two of you leave and have a lovely, decidedly finite time together."

    jump ending

label bad_game_over:

    scene bg room
    show table

    show cat behind table

    c "Hi there! Sorry, but it seems you're not mixing well with some of the others here."
    c "Maybe try your luck another day."
    c "In the meantime, GET OUT! You're harshing the vibe!"

    "You are swiftly ejected from the premises."

    jump ending

label ending:

    "You lasted [score] rounds in Cafe Gamophobia."

    "THE END"

    return
