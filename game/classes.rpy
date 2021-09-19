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
            # self.face = random.choice(faces)  <--  this is the easiest way to randomly
            # self.body = random.choice(bodies)      select something from a list
            # self.hair_front = random.choice(hair_fronts)
            # self.hair_back = random.choice(hair_backs)
            # self.hair_colours = random.choice(hair_colours)
            # self.eye_colour = random.choice(eye_colours)
            self.eye_colour = "eyes_colour_2 b.png"
            self.facts = random.sample(facts, 3)
            self.name = random.choice(names)
            self.affection = 0
