init python:
    likes_cats = -1
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

    neg_facts = [
        Fact("Hates cats", [
            Question("Do you like any animals?", "No", "Yes"),
            Question("Do you prefer dogs?", "Nope!", "Yap!"),
            Question("Who hurt you", "A cat.", "Yes")
        ]),
        Fact("Hates chess", [
            Question("Are you a computer?", "No", "Beep beep boop"),
            Question("What are your preferred games?", "I play no games",
            "Sports 'n stuff")
            Question("Would you prefer to CHECK me out?", "Please get away from me.", "Haha ha. Ha.")
        ]),
        Fact("Has gorgeous, sparkling lungs" [
            Question("What do you treat your lungs with?",
            "Just fresh air and exercise", "Asbestos"),
            Question("May I please have one of your lungs when you die?",
            "You are a psychopath, aren't you?",
            "*blushes* Why YES."),
            Question("Would you be okay if I smoked in here?",
            "What a filthy habit...", "My lungs are steel. Smoke away!")
        ]),
        Fact("Does not eat snails" [
            Question("Do you enjoy consuming molluscs?", "No", "Yes"),
            Question("Whats wet, rubbery and full of slime?", "Snails, ew.", "..."),
            Question("Is my fancy French meal just a joke to you?",
            "Snails are a gross thing to eat", "YOU are a gross thing to eat")
        ]),
        Fact("Denies COVID exists", [
            Question("What's your favourite food?", "Horse dewormer",
            "Pool cleaner"),
            Question("What do you do in your free time?", "Block off hospitals",
            "Save small businesses by wasting tons of their food and time")
            Question("Can I take my mask off?", "Yes", "Yes")
        ]),
        Fact("Dislikes reading", [
            Question("What was your favourite subject in school?", "Math", "PE"),
            Question("Do you like watching TV?", "No", "Yes"),
            Question("Do you read tweets?", "tl;dr", "Occasionally")
        ])
    ]

    names = ["Aiden", "Alex", "Sam", "Pat", "Kelly", "Kris"]
