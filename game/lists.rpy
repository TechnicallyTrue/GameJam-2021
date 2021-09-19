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
            Question("Do you believe the flu exists?", "Yes", "No"),
            Question("Should I have washed my hands?",
            "Disgusting! Get away with your uncleanliness",
            "Never. Your beautiful hands could never be washed"),
            Question("Does it gross you out that I'm coughing into your open mouth?", "D:",
            "Definitely not. That's how I roll")
        ]),
        Fact("Likes reading", [
            Question("Do you have any favourite books?", "So many!", "No"),
            Question("Do you read the newspaper?",
            "Yeah! Mostly online", "The news WHAT now?"),
            Question("Have you ever had an overdue library book?", "Never!",
            "I owe a small fortune in late fees")
        ]),
        Fact("Enjoys screaming into the void", [
            Question("What is your favourite song?", "Screaming", "Nothing"),
            Question("Do you enjoy screamo?", "AHHHHHHHHHH!!!", "No"),
            Question("Do you have any other hobbies?", "Too busy screaming",
            "YeaAAAAHHHHHHHhhhHHH!!")
        ]),
        Fact("Odd tastes in the bedroom", [
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
            Question("Do you like any animals?", "Yes, but not all of them", "I love cats!"),
            Question("Do you prefer dogs over cats?", "Yap!", "Nope!"),
            Question("Who hurt you", "A cat.", "Yes")
        ]),
        Fact("Hates chess", [
            Question("Do you like chess?", "I love it!", "Chess is for nerds."),
            Question("What are your favourite board games?", "Settlers of Katan",
            "Chess"),
            Question("Would you prefer to CHECK me out?", "Please get away from me.", "Haha ha. Ha.")
        ]),
        Fact("Has gorgeous, sparkling lungs", [
            Question("What do you treat your lungs with?",
            "Just fresh air and exercise", "Asbestos"),
            Question("May I please have one of your lungs when you die?",
            "*blushes* Why YES.",
            "You are a psychopath, aren't you?"),
            Question("Would you be okay if I smoked in here?",
            "My lungs are steel. Smoke away!",
            "What a filthy habit...")
        ]),
        Fact("Does not eat snails", [
            Question("Do you enjoy consuming molluscs?", "No", "Yes"),
            Question("Whats wet, rubbery and full of slime?", "Snails, ew.", "..."),
            Question("Is my fancy French meal just a joke to you?",
            "Snails are a gross thing to eat", "YOU are a gross thing to eat")
        ]),
        Fact("Denies COVID exists", [
            Question("What's your favourite food?", "Horse dewormer",
            "Eggs 'n bacon!'"),
            Question("What do you do in your free time?", "Block off hospitals with my protests",
            "Screaming"),
            Question("Can I take my mask off?", "Yes", "No")
        ]),
        Fact("Dislikes reading", [
            Question("What was your favourite subject in school?", "English", "PE"),
            Question("Do you like watching TV?", "Yes", "No"),
            Question("Do you read tweets?", "tl;dr", "Occasionally")
        ]),
        Fact("Prefers the cold silence of eternity", [
            Question("What is your favourite song?",
            "Music is just a futile attempt to delay entropy?",
            "I am particular to Despacito"),
            Question("Do the stars call to you?", "I refuse to answer. Text instead",
            "I cannot say"),
            Question("Where were you when I was new?",
            "IT LIVES", "Probably preschool")
        ]),
        Fact("Vanilla in the bedroom", [
            Question("Do you like chocolate?", "No. Only vanilla",
            "Yes"),
            Question("What is your favourite pillow vendor?",
            "I sleep on alcohol tinctures of an orchid's seedpods", "Endy"),
            Question("How kinky are you in bed?",
            "I don't have a bed. I just sleep on bottles of vanilla.",
            "My back is just a minefield of knots. I need to see a chiro")
        ])
    ]
    names = ["Aiden", "Alex", "Sam", "Pat", "Kelly", "Kris", "Lee", "Shaun",
             "Steph", "Jasper", "Sky", "River", "Charlie", "Khaleesi", "Max",
             "Tony", "Avery", "Emrey", "Ari", "Cameron", "Sam", "Tatum",
             "Corey", "Blake", "Casey", "Dylan", "Marion", "Parker", "Spencer",
             "Hayden", "Rowan", "Phoenix", "Jessie", "Jackie", "Ollie", "Jodie",
             "Kerry", "Tracy", "Noel", "Rene", "Jan", "Robbie", "Remy", "Milan",
             "Gerry", "Santana", "Hunter", "Elliot", "Jude", "Aubrey", "Gray",
             "Jordan", "Morgan", "Reese", "Riley", "Robin", "Sawyer", "Shae",
             "Shiloh"]
    hair_backs = ["back hair type 1", "back hair type 2", "back hair type 3", "back hair type 4", "back hair type 5"]
    hair_fronts = ["front hair type 1", "front hair type 2", "front hair type 3", "front hair type 4", "front hair type 5"]
    eye_types = ["eye type 1", "eye type 2"]
    skin_colours = ["#dab9ab", "#ffe9e3", "#e3b69a", "#b0714f", "#8f6751", "#c9997f", "#855840"]
    bodies = ["body 1", "body 2", "body 3"]
    faces = ["face 1", "face 2"]

    chars = ["NULL"]
