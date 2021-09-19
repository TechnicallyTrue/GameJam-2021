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
        ]),
        Fact("Enjoys screaming into the void", [
            Question("What is your favourite song?", "Nothing", "Screaming"),
            Question("Do you enjoy screamo?", "No", "AHHHHHHHHHH!!!"),
            Question("Do you have any other hobbies?", "Too busy screaming",
            "YeaAAAAHHHHHHHhhhHHH!!")
        ]),
        Fact("Has some odd tastes in the bedroom", [
            Question("Do you like duvets?", "I prefer lying on bare mattress",
            "They make my bed feel cozy"),
            Question("How many stuffies do you have?",
            "I do not have stuffies. The stuffies have ME",
            "Too many to count!"),
            Question("What is your opinion on memory foam?",
            "It's quite delicious", "I sleep on it sometimes")
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
            "Sports 'n stuff"),
            Question("Would you prefer to CHECK me out?", "Please get away from me.", "Haha ha. Ha.")
        ]),
        Fact("Has gorgeous, sparkling lungs", [
            Question("What do you treat your lungs with?",
            "Just fresh air and exercise", "Asbestos"),
            Question("May I please have one of your lungs when you die?",
            "You are a psychopath, aren't you?",
            "*blushes* Why YES."),
            Question("Would you be okay if I smoked in here?",
            "What a filthy habit...", "My lungs are steel. Smoke away!")
        ]),
        Fact("Does not eat snails", [
            Question("Do you enjoy consuming molluscs?", "No", "Yes"),
            Question("Whats wet, rubbery and full of slime?", "Snails, ew.", "..."),
            Question("Is my fancy French meal just a joke to you?",
            "Snails are a gross thing to eat", "YOU are a gross thing to eat")
        ]),
        Fact("Denies COVID exists", [
            Question("What's your favourite food?", "Horse dewormer",
            "Pool cleaner"),
            Question("What do you do in your free time?", "Block off hospitals",
            "Save small businesses by wasting tons of their food and time"),
            Question("Can I take my mask off?", "Yes", "Yes")
        ]),
        Fact("Dislikes reading", [
            Question("What was your favourite subject in school?", "Math", "PE"),
            Question("Do you like watching TV?", "No", "Yes"),
            Question("Do you read tweets?", "tl;dr", "Occasionally")
        ]),
        Fact("Prefers the cold silence of eternity", [
            Question("What is your favourite song?", "...",
            "Music is just a futile attempt to delay entropy?"),
            Question("Do the stars call to you?", "I refuse to answer. Text instead",
            "I cannot say"),
            Question("Where were you when I was new?",
            "I have been here always been here for always", "We are all new")
        ]),
        Fact("Vanilla in the bedroom", [
            Question("Do you like chocolate?", "No. Only vanilla",
            "Yes, but only if it also contains vanilla"),
            Question("What is your favourite pillow vendor?",
            "I sleep on alcohol tinctures of an orchid's seedpods", "Endy"),
            Question("How kinky are you in bed?",
            "My back is just a minefield of knots. I need to see a chiro.",
            "I find that sleeping on hard surfaces really works out all the kinks")
        ])
    ]

    names = ["Aiden", "Alex", "Sam", "Pat", "Kelly", "Kris"]

    hair_backs = ["back hair type 1", "back hair type 2", "back hair type 3", "back hair type 4", "back hair type 5"]
    hair_fronts = ["front hair type 1", "front hair type 2", "front hair type 3", "front hair type 4", "front hair type 5"]
    eye_types = ["eye type 1", "eye type 2"]
    bodies = ["body 1", "body 2"]
    faces = ["face 1", "face 2"]
