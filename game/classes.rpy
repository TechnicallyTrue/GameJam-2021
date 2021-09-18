init python:
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
