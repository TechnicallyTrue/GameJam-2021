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
        ]),
        Fact("Eats snails", [
            Question("Do like eating snails?", "No", "Yes"),
            Question("Do you believe in parasites?", "No", "Yes"),
            Question("How much do you like garlic?", "Not at all", "Lots!")
        ]),
        Fact("Believes COVID exists", [
            Question("Do you believe the flu exists?", "No", "Yes"),
            Question("Should I have washed my hands?",
            "Never. Your beautiful hands could never be washed",
            "Disgusting! Get away with your uncleanliness"),
            Question("Does it gross you out that I'm coughing into your open mouth?",
            "Definitely not. That's how I roll", "D:")
        ]),
        Fact("Likes reading", [
            Question("Do you have any favourite books?", "No", "So many!"),
            Question("Do you read the newspaper?", "The news WHAT now?",
            "Mostly online"),
            Question("Have you ever had an overdue library book?", "Never!",
            "I owe a small fortune in late fees")
        ])

    ]



    names = ["Aiden", "Alex", "Sam", "Pat", "Kelly", "Kris"]

    hair_backs = ["back hair type 1", "back hair type 2"]
    hair_fronts = ["front hair type 1", "front hair type 2"]
    eye_types = ["eye type 1", "eye type 2"]
    bodies = ["body 1", "body 2"]
    faces = ["face 1", "face 2"]
