# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = DynamicCharacter("namevar")
define c = Character("Dr. Whiskers")
define imagex = 1.0
define imagey = 0.6
define imagez = 0.75
define config.gl2 = True
define C = 0.0

# The game starts here.

label start:

    # Set custom pause menu
    $ _game_menu_screen = "pause_menu"

    # Clear the list of characters because apparently that persists between
    # games because of course why wouldn't it AHHHHHHHHHHHHHHHHHHHH
    $ chars = ["NULL"]

    # Set the scene
    scene bg room
    show table

label tutorial:

    show cat neutral behind table

    c "Hello, and welcome to GAME NAME!"
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
            show expression char1.blush as blush:
                zoom imagez xalign imagex yalign imagey
                alpha 0.5
            #hide screen countdown
            a "Good! I like you more now."
            $ char1.affection += 1

        "[current_question.bad_answer]":
            hide mouth_closed_N
            hide eyebrow_colour_N
            hide eyebrow_lines_N
            show expression char1.mouth_closed_A as mouth_closed_A:
                zoom imagez xalign imagex yalign imagey
            show expression char1.eyebrow_colour_A as eyebrow_colour_A behind hair_front_fill2:
                zoom imagez xalign imagex yalign imagey
                matrixcolor HueMatrix(C)
            show expression char1.eyebrow_lines_A as eyebrow_lines_A behind hair_front_fill2:
                zoom imagez xalign imagex yalign imagey

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
