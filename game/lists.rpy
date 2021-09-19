init python:
    facts = [
        Fact("Likes cats", [
            Question("Are you a cat person or a dog person?", "Cat person",
                    "Dog person"),
            Question("Do you think cats are secretly evil?", "No", "Yes"),
            Question("Would you be open to adopting a cat?", "Yes", "No")
        ]),
        Fact("Likes chess", [
            Question("Do you play chess?", "Yes", "No"),
            Question("Do you know which chess piece moves only in a straight line?",
            "Rook", "Knight"),
            Question("What's your favourite chess move?", "The Dutch Attack",
            "The Slam Dunk")
        ]),
        Fact("Has respiratory problems", [
            Question("Do you smoke?", "No", "Yes"),
            Question("Do you think I should have to wear a facemask?", "No", "Yes"),
            Question("Is your place well-ventilated?", "Yes", "No")
        ])
    ]

    names = ["Aiden", "Alex", "Sam", "Pat", "Kelly", "Kris"]
