init python:

    import random

    faces = []


    class Question:
        def __init__(self, q_text, good_answer, bad_answer):
            self.q_text = q_text
            self.good_answer = good_answer
            self.bad_answer = bad_answer

    class Fact:
        def __init__(self, f_text, questions):
            self.f_text = f_text
            self.questions = questions

    # class CharacterBio:
    #     def __init__(body, face, hair, name, affection, facts):
    #         self.body = body
    #         self.face = face
    #         self.hair = hair
    #         self.name = name
    #         self.affection = affection
    #         self.facts = facts

    # class Lists:
    #     facts = [
    #         Fact("Likes cats", [
    #             Question("Are you a cat person or a dog person?", "Cat person",
    #                     "Dog person"),
    #             Question("Do you think cats are secretly evil?", "No", "Yes"),
    #             Question("Would you be open to adopting a cat?", "Yes", "No")
    #         ])
    #     ]

    # class Char:
    #     def __init__(self):
    #         face = 0;
    #         body = 0;
    #         hairFront = 0;
    #         hairBack = 0;
    #         hairColour = 0;
    #         eyeColour = 0;
    #         expression = 0;
    #         character_sprites = []
    #         backHairColour = Image()
    #         backHairLines = Image()
    #
    #     def set(self):
    #         face = renpy.random.randint(1,2)
    #         body = renpy.random.randint(1,2)
    #         hairFront = renpy.random.randint(1,2)
    #         hairBack = renpy.random.randint(1,2)
    #         if(hairBack == 1):
    #             backHairColour = Image("back hair colour 1")
    #             backHairLines = Image("back hair lines 1")
    #
    #         if(hairBack == 2):
    #             backHairColour = Image("back hair colour 2")
    #             backHairLines = Image("back hair lines 2")

    class Char:
        def __init__(self):
            self.face = random.choice(faces)
            if self.face == "face 1":
                self.eyebrow_colour_N = "eyebrows_colour neut.png"
                self.eyebrow_lines_N = "eyebrows_lines_1 neut.png"
                self.eyebrow_colour_A = "eyebrows_colour angry.png"
                self.eyebrow_lines_A = "eyebrows_lines_1 angry.png"
            if self.face == "face 2":
                self.eyebrow_colour_N = "eyebrows_colour neut.png"
                self.eyebrow_lines_N = "eyebrows_lines_2 neut.png"
                self.eyebrow_colour_A = "eyebrows_colour angry.png"
                self.eyebrow_lines_A = "eyebrows_lines_2 angry.png"
            self.body = random.choice(bodies)
            if self.body == "body 1":
                self.back_shirt_colour_a = "back_shirt_colour_a_1.png"
                self.back_shirt_colour_b = "back_shirt_colour_b_1.png"
                self.back_shirt_lines = "back_shirt_lines_1.png"
                self.body_colour_a_N = "body_colour_a_1 neut.png"
                #self.body_colour_a_A = "back_shirt_lines_1.png"
                #self.body_colour_a_H = "back_shirt_lines_1.png"
                self.body_colour_b_N = "body_colour_b_1 neut.png"
                self.body_colour_c_N = "body_colour_c_1 neut.png"
                self.body_lines_N= "body_lines_1 neut.png"
            if self.body == "body 2":
                self.back_shirt_colour_a = "back_shirt_colour_a_2.png"
                self.back_shirt_colour_b = "back_shirt_colour_b_2.png"
                self.back_shirt_lines = "back_shirt_lines_2.png"
                self.body_colour_a_N = "body_colour_a_2 neut.png"
                #self.body_colour_a_A = "back_shirt_lines_1.png"
                #self.body_colour_a_H = "back_shirt_lines_1.png"
                self.body_colour_b_N = "body_colour_b_2 neut.png"
                self.body_colour_c_N = "body_colour_c_2 neut.png"
                self.body_lines_N= "body_lines_2 neut.png"
            if self.body == "body 3":
                self.back_shirt_colour_a = "back_shirt_colour_a_3.png"
                self.back_shirt_colour_b = "empty.png"
                self.back_shirt_lines = "back_shirt_lines_3.png"
                self.body_colour_a_N = "body_colour_a_3 neut.png"
                #self.body_colour_a_A = "back_shirt_lines_1.png"
                #self.body_colour_a_H = "back_shirt_lines_1.png"
                self.body_colour_b_N = "body_colour_b_3 neut.png"
                self.body_colour_c_N = "body_colour_c_3 neut.png"
                self.body_lines_N= "body_lines_3 neut.png"

            self.hair_back = random.choice(hair_backs)
            if self.hair_back == "back hair type 1":
                self.hair_back_fill = "back_hair_colour_1.png"
                self.hair_back_lines = "back_hair_lines_1.png"
            if self.hair_back == "back hair type 2":
                self.hair_back_fill = "back_hair_colour_2.png"
                self.hair_back_lines = "back_hair_lines_2.png"
            if self.hair_back == "back hair type 3":
                self.hair_back_fill = "back_hair_colour_3.png"
                self.hair_back_lines = "back_hair_lines_3.png"
            if self.hair_back == "back hair type 4":
                self.hair_back_fill = "back_hair_colour_4.png"
                self.hair_back_lines = "back_hair_lines_4.png"
            if self.hair_back == "back hair type 5":
                self.hair_back_fill = "back_hair_colour_5.png"
                self.hair_back_lines = "back_hair_lines_5.png"
            self.eye_type = random.choice(eye_types)
            if self.eye_type == "eye type 1":
                self.eye_back = "eyes_under_1 a.png"
                self.eye_fill = "eyes_colour_1 a.png"
                self.eye_lines = "eyes_lines_1 a.png"
            if self.eye_type == "eye type 2":
                self.eye_back = "eyes_under_2 a.png"
                self.eye_fill = "eyes_colour_2 a.png"
                self.eye_lines = "eyes_lines_2 a.png"
            self.hair_front = random.choice(hair_fronts)
            if self.hair_front == "front hair type 1":
                self.hair_front_fill = "hair_colour_1.png"
                self.hair_front_lines = "hair_lines_1.png"
            if self.hair_front == "front hair type 2":
                self.hair_front_fill = "hair_colour_2.png"
                self.hair_front_lines = "hair_lines_2.png"
            if self.hair_front == "front hair type 3":
                self.hair_front_fill = "hair_colour_3.png"
                self.hair_front_lines = "hair_lines_3.png"
            if self.hair_front == "front hair type 4":
                self.hair_front_fill = "hair_colour_4.png"
                self.hair_front_lines = "hair_lines_4.png"
            if self.hair_front == "front hair type 5":
                self.hair_front_fill = "hair_colour_5.png"
                self.hair_front_lines = "hair_lines_5.png"

            self.hair_colour = renpy.random.randint(0, 360)
            self.eye_colour = renpy.random.randint(0, 360)
            self.shirt_colour_a = renpy.random.randint(0, 360)
            self.shirt_colour_b = renpy.random.randint(0, 360)


            self.mouth_closed_N = "mouth a_neut.png"
            self.mouth_open_N = "mouth b_neut.png"
            self.mouth_closed_A = "mouth a_angry.png"
            self.mouth_open_A = "mouth b_angry.png"
            self.blush = "blush.png"

            self.facts = random.sample(facts, 3)
            self.name = random.choice(names)
            self.affection = 0
