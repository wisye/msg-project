# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character('MC', color="#ffffff")
image mc normal = "default mc 1.png"
image mc panic = "panic mc 1.png"
image mc amazed = "amazed mc 1.png"
transform pos:
    xalign 0.5
    zoom 0.8

define n = Character('') # This is a placeholder for the narrator.
define prof = Character('Professor', color="#999999")
define ga = Character('Guardian A', color="#fc0000")
define gb = Character('Guardian B', color="#fcf800")
define gc = Character('Guardian C', color="#00fcff")
define gd = Character('Guardian D', color="#00ff00")
define ge = Character('Guardian E', color="#e9dfd3")
define gf = Character('Guardian F', color="#f286d7")
define gg = Character('Guardian G', color="#8900c9")
define ov = Character('Overseer', color="#ff00b3")

define gef = Character('Guardian E & Guardian F', color="#eeb2d5")
define gefg = Character('Trio Guardian', color="#bc59cf")

image guardian_a = "ga.png"
image guardian_b = "gb.png"
image guardian_c = "gc.png"
image guardian_d = "gd.png"
image guardian_e = "ge.png"
image guardian_f = "gf.png"
image guardian_g = "gg.png"
transform jumpscare_transform:
    xalign 0.5
    yalign 0.3
    zoom 7

transform jumpscare_transform_left:
    xalign 0.01
    yalign 0.5
    zoom 5

transform jumpscare_transform_center:
    xalign 0.5
    yalign 0.5
    zoom 5

transform jumpscare_transform_right:
    xalign 0.99
    yalign 0.5
    zoom 5


default choice = None
default choice2 = None
default choice3 = None
default jump = None

init python:
    import random

    def play_jump():
        sound = random.choice(["jump1.ogg", "jump2.ogg", "jump3.ogg"])
        renpy.sound.play(sound)

    def random_jumpscare():
        jumpscare = random.choice(["guardian_a", "guardian_b", "guardian_c", "guardian_d", "guardian_e", "guardian_f", "guardian_g"])
        return jumpscare

label start:

    scene bg room

    show mc normal at pos

    n "A gust of fresh wind flew by as birds started to chirp."
    n "It was the beginning of a new semester."
    n "Everyone was getting ready to start the day."
    n "But that was not the case for MC."

    mc "(snoring loudly)"

    n "It was 8 o'clock and MC's alarm had already blared for the past 10 minutes."

    n "Alarm : (ring ring)"

    mc "(continues to snore)"

    n "The alarm continues to ring."

    n "Eventually, the alarm's effort is awarded as MC starts to wake up."

    mc "(slowly opens his eyes)"
    mc "(yawns while reaching for his phone)"
    mc "What time is it? Why is it so noisy?"
    mc "(checks his phone)"
    mc "Oh, it's only 8 o'clock..."
    mc "(realizes)"

    show mc panic at pos

    mc "Eh?"
    mc "HUH??"
    mc "IT'S 8 O'CLOCK??"

    n "MC gets out of his bed and frantically searches for his belongings."

    mc "I need this.. and this…"

    n "That was the fastest preparation that MC has ever done in his life"

    mc "And don't forget this"
    mc "(grabs his camera and dashes out of his one-room apartment)"
    mc "I'm definitely dying today"

    mc "(runs as fast as he can to his university)"

    jump scene_2

label scene_2:

    n "The hurried MC makes it just in time for his first class of the year."

    mc "*pants pants*"
    mc "I.. made… it…"

    n "MC takes a seat and gets through the class while being sleepy."

    prof "And that concludes today's class, see you next week for the quiz"

    mc "First class done..."
    mc "*yawns*"
    mc "I'm going to need some coffee"

    jump scene_3

label scene_3:

    n "MC goes to the canteen to buy some coffee from the vending machine"
    n "As MC arrived at the vending machine, MC saw a poster for a photography contest"

    mc "Hmm, a photography contest huh?.."
    mc "Let's see, what are the requirements.."

    n "MC looks over the requirements for the contest"

    mc "Okay, this should be doable, and what's the theme?.."
    mc "The theme is…"
    mc "Paranormal Activity??!!"
    mc "And the deadline is.. next week??!!"
    mc "I'll have to start taking pictures today then.."
    n "MC touches his camera and suddenly is filled with energy"

    mc "Alright, I'll take it on!"

    n "As the MC is full of energy, he contemplates as whether he should buy coffee or not"

    mc "Should I buy the coffee?"
    mc "I'm not as sleepy since I saw the contest"

    menu:
        "Buy the coffee":
            $ choice = "buy"

            mc "I suppose I still should get one!"
            
            n "MC bought the coffee from the vending machine, and drank it while going back to his class"
            n "MC finished his class as usual and made his way back to his home safely"
        
        "Don't buy the coffee":
            $ choice = "dont buy"

            mc "I suppose I don't need to!"

            n "The energized MC left the vending machine without buying coffee, completely smitten by the photography contest"

    if choice == "buy":
        return
    elif choice == "dont buy":
        jump scene_4

label scene_4:

    n "MC goes back to his class and went through the rest of his class for the day"
    n "As MC didn't buy the coffee, MC became very sleepy"

    mc "Damn, I should've bought that coffee,"
    mc "Now I'm very sleepy.."
    mc "*checks for time on his phone*"

    n "MC's clock shows 16:00"

    mc "I still have some time left.."
    mc "I guess I'm taking a nap first"

    jump scene_5

label scene_5:

    n "A considerable amount of time has passed."

    mc "*drools*"
    mc "*wakes up*"
    mc "Hmm... where am I?"
    mc "*looks around*"
    mc "Oh yeah, I slept in the class."
    mc "But why does the class look a bit different?"
    mc "*rubs his eyes*"
    mc "Why the hell is the class in a mess?"

    n "MC looks around his ruined class."

    mc "Are we having Halloween or something?"
    mc "But it's only January..."
    mc "Whatever... I'm going home."
    mc "takes his bag and goes out of his class"

    n "Before he left, he saw that the hallway that he usually goes through to get to his class is also ruined."

    mc "What the hell?"

    n "Puzzled, MC hastily makes his way through the hallway and out towards the middle of his campus."

    jump scene_6

label scene_6:

    n "As MC got out of his building, MC saw that the sky was dark red just like blood."

    mc "I seriously got to go back home fast!"

    n "MC ran as fast as he could to the gate."
    n "Unfortunately, the gate was covered in an invisible barrier, so MC was held by the gate."

    mc "What is this?"
    mc "Why can't I go out?"

    n "MC could not exit the gate, so MC decided to go back inside the campus."
    n "MC arrived back at the middle of the campus."

    mc "What has this place become?"

    n "MC becomes very confused and looks around the place."
    n "MC saw that there was a stone tablet near what seems to be an altar."
    n "MC approached the stone tablet and noticed some strange words engraved in it."
    n "Thus was written in the stone tablet:"
    n "\"Once lived a Grand Overseer who rules above all.\""
    n "\"It was a peaceful time until the Overseer fell into madness.\""
    n "\"Fortunately, ten brave people banded together to make a deal with the Overseer.\""
    n "\"The deal was that those ten people were to be sacrificed into offerings,\""
    n "\"which in turn would ease the Overseer's madness.\""
    n "\"The Overseer would then leave, but those offerings would remain here.\""
    n "\"Those ten offerings are spread across this domain and should be presented to ease"
    n "the Overseer's anger if The Overseer was ever to come back.\""
    n "\"Among those offerings, a strong bond exists between some of them.\""
    n "\"Those offerings have long since lost much of their power; hence, it is needed to make"
    n "a set out of them.\""
    n "\"Only offerings with a strong bond can calm the Overseer, and only then might you be"
    n "spared.\""
    n "\"Beware that only thrice are you given the chance to present your offerings.\""
    n "The writing ends there."

    mc "What does this mean?"
    mc "Does this mean that the Overseer is back?"
    mc "Does this also mean that I need to go and gather those offerings?"
    mc "How do I even find these things? It's not like I know how they look like."

    n "There was a small piece of paper with words written in blood on it."
    n "MC took the paper and decides to take a look."
    n "\"Use the light, and darkness will be imprisoned.\""

    mc "Light? Why would I need light? Where would I even get light from?"
    mc "*suddenly realizes*"
    mc "OH RIGHT! I have my phone!"
    mc "*reaches out for his phone*"
    mc "I should try and call my friend-"

    n "MC's phone screen shows a dead battery icon."

    mc "ARE YOU KIDDING ME?"
    mc "What can I do…."
    mc "*looks down and saw that he brought his camera with him*"
    mc "THIS IS IT! I can use my flash for the light, although I don't know when it will be used."
    mc "Alright then… time to get those offerings ASAP. I don't want to be here for much longer."

    jump scene_7

label scene_7:
    
    n "To gather the offerings, MC decided to wander through the altered university and arrived at the parking lot."

    mc "Where can I find one of these offerings?"
    mc "*looks around*"

    n "Suddenly, a loud noise can be heard."
    n "*screeches*"

    n "(insert jumpscare 1: Guardian A)"
    $ play_jump()
    show guardian_a at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_a with Dissolve(0.2)

    mc "WOAHHH"

    n "A guardian of the offering shows itself to MC."

    ga "FOR WHAT REASON HAVE YOU COME HERE?"

    mc "(Oh.. damn..)"
    mc "(What the hell is that thing??)"
    mc "(Is that the Overseer?)"
    mc "(I should try to ask it first.)"
    mc "Are you the Overseer?"

    ga "I am not the Overseer."
    ga "I will ask again, WHY HAVE YOU COME HERE?"

    mc "Okay, okay.. chill out.."
    mc "I'm here to gather offerings for the Overseer."
    mc "Do you know of any such things around here?"

    ga "I happen to know some of it."

    mc "Oh yea?? Tell me about it!"

    ga "I don't think I will."

    mc "Why???"

    ga "Because I AM the guardian for the offerings here."

    mc "WHAT??"
    mc "(I'LL BE DAMNED.)"

    ga "Although…"
    ga "I will hand over the offering and some information if you pass my trial."

    mc "A trial…?"
    mc "You're not going to ask me to die, won't you?"

    ga "No, but if you fail…"
    ga "I WILL EAT YOU!"

    mc "THAT'S NOT FAIR!"
    mc "Fine! If I win, I'll also get the opportunity to take a photo of you!"

    ga "Do as you wish."
    ga "You won't pass this trial anyway!"

    mc "I'll take you ON!"

    jump choice_2

label choice_2:

    ga "Your trial is to answer my questions."
    ga "I weave unity in diversity and a sweet embrace which silences discord."
    ga "I exist internally."
    ga "What am I?"

    $ choice = None
    menu:
        "Harmony":
            $ choice = "harmony"
        "Humanity":
            $ choice = "humanity"
    
    ga "I am the invisible thread that ties the human spirit in the past, present, and future."
    ga "I exist within people."
    ga "What am I?"

    menu:
        "Harmony":
            $ choice2 = "harmony"
        "Humanity":
            $ choice2 = "humanity"
    
    if choice == "harmony" and choice2 == "humanity":

        ga "Huh?"
        ga "You got both answers right?"
        ga "NO WAY"

        mc "YOU'RE MINE NOW!"

        n "(insert camera flash)"

        ga "NOOOO!"

        n "Guardian A vanished and dropped two orbs and a scroll."

        mc "So.. this is the offering? And this scroll…. let's see…"

        n "MC reads the scroll."
        n "This is Harmony and Humanity."
        n "Harmony connects and humanity exchanges."
        n "Without information, humanity collapses."
        n "To have harmony, a thorough evaluation is needed."
        n "The scroll ends there."

        mc "So.. this is harmony and humanity."
        mc "We got two, so eight more to go."
        mc "I can do this!"

        n "MC proceeds to wander the altered university."

        jump scene_8

    elif (choice == choice2):
        
        ga "HAHAHAHA"
        ga "TOO BAD"
        ga "YOU'RE MINE!"

        $ play_jump()
        show guardian_a at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_a with Dissolve(0.2)

        jump game_over_c2

    else:
        
        ga "HAHAHAHA"
        ga "You are DEAD wrong!"

        $ play_jump()
        show guardian_a at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_a with Dissolve(0.2)

        jump game_over_c2

label game_over_c2:
    "Game Over. Would you like to try again?"

    menu:
        "Yes":
            "Let's try again..."
            jump choice_2
        "No":
            "Game ended."
            return

label scene_8:
    n "After wandering around for a bit, MC found a library."

    mc "A library huh..."
    mc "There should be something here."

    n "MC enters the library."

    mc "*looks around*"

    n "MC saw a guardian sleeping right at the center of the library."

    mc "Erm, excuse me!"

    n "The sleeping guardian doesn't budge."
    
    mc "This should be the next guardian, right?? I should wake it up."
    mc "HEY! WAKE UP!"

    n "(insert jumpscare 2: Guardian B)"
    $ play_jump()
    show guardian_b at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_b with Dissolve(0.2)

    gb "WHAT DO YOU WANT?"

    mc "*shocked*"
    mc "I- I.. want to take your offerings!"

    gb "You think a puny human like you who disturbs one's rest is worthy of getting my offerings?"
    gb "Try again, fool!"

    n "Guardian B goes back to sleep."

    mc "Damn it!"
    mc "(Quick! I need to think how to persuade this thing.)"
    mc "Hey!"
    mc "You don't seem to be having a good rest."
    mc "What about a bet?"
    mc "A bet where you challenge me to your trial!"

    n "Guardian B is listening carefully."

    mc "If I lose, I will offer you my body to be your personal pillow."
    mc "However, if I win, you will give me your offerings, and I get to take a photo of you."
    mc "How about that?"

    n "Guardian B wakes up."

    gb "*looks at MC*"
    gb "Your body is too scrawny!"

    mc "You can stuff me with anything!"
    mc "I might die, but at least you will have something to sleep on!"

    gb "FINE!"
    gb "I accept your bet!"

    jump choice_3

label choice_3:

    gb "Here's my trial!"
    gb "I am the endless realm of a fanciful dream."
    gb "Without me, innovation wouldn't exist."
    gb "What am I?"

    $ choice = None
    $ choice2 = None

    menu: 
        "Imagination":
            $ choice = "imagination"
        "Evaluation":
            $ choice = "Evaluation"

    gb "I am the root of judgment."
    gb "Without me, an order will fall, and a scribe would fail."
    gb "What am I?"

    menu:
        "Imagination":
            $ choice2 = "imagination"
        "Evaluation":
            $ choice2 = "Evaluation"

    if choice == "imagination" and choice2 == "Evaluation":

        gb "Hmm.."
        gb "You got both answers right..."
        gb "You are worthy of my offering."

        mc "Neat!"
        mc "Hey! Check this out!"

        n "(insert camera flash)"
        n "Guardian B vanished, and just like Guardian A, dropped two orbs and a scroll."

        mc "Let's see what this scroll says."

        n "MC reads the scroll."
        n "This is Imagination and Evaluation."
        n "Through imagination, growth prevails, and through evaluation, a connection is achieved."
        n "Without evaluation, harmony won't exist."
        n "But depictions stem from imaginations."
        n "The scroll ends there."

        mc "Hmm.. okay.."
        mc "I don't really understand but okay."
        mc "Time to get to the next ones!"

        n "MC exits the library and continues the journey."

        jump scene_9
    
    elif (choice == choice2):

        gb "You got one wrong."
        gb "That's what you get for being a smartass."
        gb "But, A BET'S A BET!"

        $ play_jump()
        show guardian_b at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_b with Dissolve(0.2)

        jump game_over_c3

    else:

        gb "You didn't even get anything right."
        gb "Why did you even try?"
        gb "You are not even worthy to be a pillow."
        gb "BEGONE, FOOL!"

        $ play_jump()
        show guardian_b at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_b with Dissolve(0.2)

        jump game_over_c3

label game_over_c3:
    "Game Over. Would you like to try again?"

    menu:
        "Yes":
            "Let's try again..."
            jump choice_3
        "No":
            "Game ended."
            return

label scene_9:

    n "MC decides to head to the laboratory to see if there is anything there."

    mc "This place might be different, but it's fundamentally the same."
    mc "The lab might have something inside."
    mc "*heads inside the lab*"
    mc "*looks around*"
    mc "Not much has changed hu-HH???"

    n "(insert jumpscare 3: Guardian C)"
    $ play_jump()
    show guardian_c at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_c with Dissolve(0.2)

    n "MC sees a guardian mixing chemicals in the lab."
    n "The guardian, realizing someone went in, went up to MC's face."

    gc "WHY DID YOU DISTURB ME?"

    mc "Oh, sorry."
    mc "I didn't know that someone was here."

    gc "LEAVE!"

    mc "What is your problem, man?"
    mc "I bet you're not even smart enough to mix those chemicals properly."

    gc "WHAT DID YOU SAY?!"

    mc "I said that you're dumb."

    gc "YOU DARE TO SAY THAT TO MY FACE?!"
    gc "FINE! IF YOU CAN'T ANSWER MY QUESTION, YOU WILL BE MY TEST SUBJECT."

    mc "Sure, you professor wannabe. I'll even take a photo of you as a commemoration for the dumbest scientist ever!"

    jump choice_4

label choice_4:

    gc "ANSWER THESE QUESTIONS."
    gc "I AM OF GIVE AND TAKE."
    gc "TO TRADERS, I AM LIFE ITSELF."

    $ choice = None
    $ choice2 = None

    menu:
        "growth":
            $ choice = "growth"
        "exchange":
            $ choice = "exchange"

    gc "I AM OF ADVANCEMENT."
    gc "I AM A MUST FOR DEVELOPMENT WITH OTHERS."

    menu:
        "growth":
            $ choice2 = "growth"
        "exchange":
            $ choice2 = "exchange"

    if choice == "exchange" and choice2 == "growth":

        gc "HUH?"
        gc "YOU ANSWERED CORRECTLY?"
        gc "YOU MUST BE CHEATING."
        gc "THERE IS NO OTHER EXPLANATION."

        mc "It's just that your question is too easy."
        mc "Truly a dumb wannabe."

        gc "*ROARS*"

        mc "So loud… Bye Bye."

        n "(insert camera flash)"
        n "Guardian C vanished and dropped two orbs and a scroll, just like its predecessors."

        mc "Phew… that was quick and fearsome."
        mc "Thank goodness, I didn't stutter back then."
        mc "Now let's see what this wannabe has to offer."

        n "MC reads the scroll."
        n "This is the Growth and Exchange."
        n "To have growth, you need to have imagination, and to exchange something, you need to have information."
        n "Growth affects depiction."
        n "While exchange is a part of humanity."
        n "The scroll ends here."

        mc "More weird stuff.."
        mc "I'll keep it in mind, though."
        mc "Let's keep going!"

        jump scene_10

    else:

        gc "HAHAHAH"
        gc "A RUNT LIKE YOU TRIES TO DEFY ME BUT YOU COULD NOT EVEN ANSWER CORRECTLY"
        gc "COME HERE!"

        $ play_jump()
        show guardian_c at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_c with Dissolve(0.2)

        jump game_over_c4

label game_over_c4:
    "Game Over. Would you like to try again?"

    menu:
        "Yes":
            "Let's try again..."
            jump choice_4
        "No":
            "Game ended."
            return 

label scene_10:

    n "The search for the offerings continues for MC."

    mc "Damn, where are the rest of these offerings."
    mc "I've been looking everywhere, man."

    n "As MC walks on, MC passed through a basketball court."

    mc "A basketball court, huh?"

    n "MC saw a basketball right at the center of the court."

    mc "It's fine to let off some steam, right?"
    mc "*walks over to grab the ball*"
    mc "Why does this ball seem a bit weird?"
    mc "*reaches out for the ball*"

    n "(insert jumpscare 4: Guardian D)"
    $ play_jump()
    show guardian_d at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_d with Dissolve(0.2)

    mc "UWAHHHHH"

    n "Guardian D manifested from the basketball."

    mc "THE BALL WAS A GUARDIAN?!"

    gd "AHAHAHAHAHAH"
    gd "How do you like that?"
    gd "Your reactions are excellent!"
    gd "Little pranks like this always work."

    mc "You got me good there."

    gd "Now let's get to the serious part."
    gd "You are here to get my offerings, aren't you?"

    mc "How do you kno-"

    gd "OF COURSEEE, I would knoww."
    gd "For I am the most enchanting and elegant guardian of all."

    mc "(What the hell..)"
    mc "Yeah, I'm here to take your orbs or whatever."
    mc "Hand 'em over!"

    gd "Now, now, don't be too hasty."
    gd "You wouldn't want the fun to be over so soon, right?"

    mc "Hell no!"
    mc "I wanna get home as quickly as possible!"

    gd "C'mon! Let's play a game!"

    mc "No! I don't wanna play!"

    gd "*sighs*"
    gd "Fine, just answer my question correctly, and you'll get what you want."
    gd "However, if you get even one wrong, I'll just make you my plaything then."

    mc "Deal!"

    jump choice_5

label choice_5:

    gd "Listen carefully."
    gd "I am the key to the truth."
    gd "Knowledge without me is nothing."
    gd "What am I?"

    $ choice = None
    $ choice2 = None
    menu:
        "Connection":
            $ choice = "connection"
        "Information":
            $ choice = "information"
        "Depiction":
            $ choice = "depiction"
    
    gd "I am the intertwiner of fate."
    gd "A nexus is created through me."
    gd "What am I?"

    menu:
        "Connection":
            $ choice2 = "connection"
        "Information":
            $ choice2 = "information"
        "Depiction":
            $ choice2 = "depiction"
    
    gd "I am the representation."
    gd "An expression of concept is my expertise."
    gd "What am I?"

    menu:
        "Connection":
            $ choice3 = "connection"
        "Information":
            $ choice3 = "information"
        "Depiction":
            $ choice3 = "depiction"

    if choice == "information" and choice2 == "connection" and choice3 == "depiction":

        gd "Everything.. is correct.."

        mc "Serves you right, now hand'em over!"

        gd "Nuh uh!"

        mc "You jerk!"

        gd "I'm just kidding, here's my gift for you before I go."
        gd "Head towards your past, it will lead you towards the future."

        mc "Huh?"

        gd "Good luck! Now finish me!"

        mc "No… not before you explain yourself."

        gd "FINE! Then I'll do it myself."

        n "Guardian D took MC's camera and flashed itself."
        n "(insert camera flash)"
        n "Guardian D vanished and dropped not two, but three orbs and a scroll."
        n "The scroll reads:"
        n "This is Information, Connection, and Depiction."
        n "Depicting an imagination would amplify growth."
        n "But an exchange of information would form humanity."
        n "And through connection and evaluation, harmony is achieved."
        n "The scroll ends here."

        mc "What the hell was that!"
        mc "Damn, head towards my past?"
        mc "Could it be hinting me to go back to where I woke up?"
        mc "I should check it out."

        n "Heeding Guardian D's advice, MC went back to where he woke up, his classroom."

        jump scene_11
    
    elif(choice == "information" and choice2 == "connection") or (choice == "information" and choice3 == "depiction") or (choice2 == "connection" and choice3 == "depiction"):

        gd "OH NO!"

        mc "What? Did I get everything right?"

        gd "You… you did…"
        gd "NOT!"
        gd "AHHAHAHAHAH"

        $ play_jump()
        show guardian_d at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_d with Dissolve(0.2)

        jump game_over_c5
    
    elif choice == "information" or choice2 == "connection" or choice3 == "depiction":

        gd "Ooh, nice try, but you only got one right."
        gd "Tough luck, Big Boy!"

        $ play_jump()
        show guardian_d at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_d with Dissolve(0.2)

        jump game_over_c5
    
    else:

        gd "I see that you got everything wrong."
        gd "BE MY SLAVE FOR ETERNITY!"

        $ play_jump()
        show guardian_d at jumpscare_transform onlayer master with Dissolve(0.2)
        pause 0.5
        hide guardian_d with Dissolve(0.2)

        jump game_over_c5

label game_over_c5:
    "Game Over. Would you like to try again?"

    menu:
        "Yes":
            "Let's try again..."
            jump choice_5
        "No":
            "Game ended."
            return

label scene_11:

    n "Upon arriving at his classroom, MC realized something strange."

    mc "Why did that guardian lead me here?"
    mc "There must be something important that I missed."

    n "As MC investigated more of the classroom, the more he became sure."

    mc "There must be something here, I'm sure of it!"

    n "MC looks towards the whiteboard."
    n "MC realized it wasn't just some random scribbles."
    n "The whiteboard says:"
    n "Behind you!"

    $ play_jump()
    show guardian_e at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_e with Dissolve(0.2)

    mc "WOAHHH"
    n "Guardian E appears from the walls and it calls for its friend."
    ge "Come, my friends."

    $ play_jump()
    show guardian_f at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_f with Dissolve(0.2)

    n "Guardian F came down from the ceiling."
    mc "WAHHHHH"
    mc "Why do you guys keep appearing one by one?!"
    gef "It's not over."

    $ play_jump()
    show guardian_g at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide guardian_g with Dissolve(0.2)

    n "Guardian G was formed from the words written on the whiteboard."

    mc "Wh- what do you want??"
    mc "Why are there so many of you??"

    ge "This is where the Orb of Sovereignty is held."
    gf "We are the guardians of this place."
    gg "No one shall take the Orb of Sovereignty from us."

    mc "So, this is the final place."
    mc "Give me your orb!"

    gefg "NO!"

    mc "But, that's the only way I can go home."

    gefg "That's true, so if you want this, you have to get through us."

    mc "Heh, I got this camera, why should I be afraid of you."

    n "MC looks at his camera and realizes that his camera battery is dead."
    n "For the first time in his life, MC felt most horrified."
    
    mc "(What should I do????)"

    jump choice_6

label choice_6:

    gefg "You may choose, to remain here for eternity or to face us and get away"

    $ choice = None

    menu:
        "Remain":
            $ choice = "remain"
        "Fight":
            $ choice = "fight"

    if choice == "remain":

        mc "I choose to remain here."
        mc "*fearful*"
        gefg "Then you will be one of us."
        n "The Trio Guardian raises the Orb of Sovereignty and casts its power upon MC."
        n "MC was then turned into one of the guardians, waiting for the next generation to come."

        $ play_jump()
        show mc amazed at pos

        n ""

        return

    else:

        mc "I'll fight for my survival!"
        mc "I will conquer you and be free!"
        gefg "Very well, then face us!"

        jump choice_7

label choice_7:

    ge "I am the one true king."
    gf "Everything is under my rule."
    gg "Conquering is what I do best."
    gefg "What am I?"

    $ choice = None
    menu:
        "Sovereignty":
            $ choice = "sovereignty"
        "Overseer":
            $ choice = "overseer"
        "God":
            $ choice = "god"
    
    if choice == "overseer":

        gefg "You have answered correctly."
        gefg "However, you won't be able to defeat us."
        gefg "Your light is no more."

        mc "My light might be gone, but I can always get more light!"

        n "MC rushes through the three guardians and took the Orb of Sovereignty."

        mc "SHINE BRIGHTLY!"

        n "The light from the Orb of Sovereignty clashes with the guardians, which made them vanish and revert back into writings on the wall."
        n "The writing says:"
        n "A sovereign needs to be able to evaluate themselves through their imagination."
        n "But for a sovereign to grow, they will need to depict themselves through their connections."
        n "A sovereign's humanity allows them to exchange information with harmony."
        n "Among these gardens of words, a secret is told."
        n "The writing ends there."

        mc "I finally have all of them!"
        mc "Now, to the altar!"

        jump scene_12

    else:

        gefg "Your chance ends here."
        gefg "Goodbye"

        $ play_jump()
        show guardian_e at jumpscare_transform_left
        show guardian_f at jumpscare_transform_center
        show guardian_g at jumpscare_transform_right

        n ""
        return

label scene_12:

    n "After obtaining all 10 offerings, MC heads over to the altar to present the offerings he got."

    mc "This is it, the moment of truth."

    n "MC walks up to the altar and contemplates the offerings he has obtained."

    mc "Which one should I offer up?"

    n "MC recalls the scrolls and writings he acquired."

    jump choice_8

label choice_8:
    
    $ choice = None
    menu:
        "Scroll 1":
            $ choice = "scroll1"
        "Scroll 2":
            $ choice = "scroll2"
        "Scroll 3":
            $ choice = "scroll3"
        "Scroll 4":
            $ choice = "scroll4"
        "Whiteboard Writing":
            $ choice = "whiteboard"
        "I got it":
            mc "I got it!"
            jump choice_9

    if choice == "scroll1":
        n "This is Harmony and Humanity."
        n "Harmony connects and humanity exchanges."
        n "Without information, humanity collapses."
        n "To have harmony, a thorough evaluation is needed."
    elif choice == "scroll2":
        n "This is Imagination and Evaluation."
        n "Through imagination, growth prevails, and through evaluation, a connection is achieved."
        n "Without evaluation, harmony won't exist."
        n "But depictions stem from imaginations."
    elif choice == "scroll3":
        n "This is Growth and Exchange."
        n "To have growth, you need to have imagination, and to exchange something, you need to have information."
        n "Growth affects depiction."
        n "While exchange is a part of humanity."
    elif choice == "scroll4":
        n "This is Information, Connection, and Depiction."
        n "Depicting an imagination would amplify growth."
        n "But an exchange of information would form humanity."
        n "And through connection and evaluation, harmony is achieved."
    else:
        n "A sovereign needs to be able to evaluate themselves through their imagination."
        n "But for a sovereign to grow, they will need to depict themselves through their connections."
        n "A sovereign's humanity allows them to exchange information with harmony."
        n "Among these gardens of words, a secret is told."
    
    jump choice_8

label choice_9:

    n "Select which offering to give on the left side"

    $ choice = None
    $ choice2 = None
    $ choice3 = None
    menu:
        "Connection":
            $ choice = "connection"
        "Information":
            $ choice = "information"
        "Imagination":
            $ choice = "imagination"
    
    n "Select which offering to give on the middle"

    menu:
        "Sovereignty":
            $ choice2 = "sovereignty"
        "Harmony":
            $ choice2 = "harmony"
        "Exchange":
            $ choice2 = "exchange"
        "Depiction":
            $ choice2 = "depiction"

    n "Select which offering to give on the right side"

    menu:
        "Evaluation":
            $ choice3 = "evaluation"
        "Humanity":
            $ choice3 = "humanity"
        "Growth":
            $ choice3 = "growth"

    if (choice == "connection" and choice2 == "harmony" and choice3 == "evaluation") or (choice == "information" and choice2 == "exchange" and choice3 == "humanity") or (choice == "imagination" and choice2 == "depiction" and choice3 == "growth"):

        n "A ring of a bell can be heard from the altar."
        n "A portal opens, and from it emerges all the previous guardians along with the Overseer."
        ov "YOU HAVE PLEASED ME."
        mc "What?!"
        ov "Head into the portal."
        n "The Overseer, along with the guardians, heads inside the portal."
        n "MC also decides to come along."

        jump scene_13

    elif (choice == "imagination" and choice2 == "sovereignty" and choice3 == "evaluation") or (choice == "information" and choice2 == "harmony" and choice3 == "humanity") or (choice == "connection" and choice2 == "exchange" and choice3 == "depiction"):

        n "No sound came from the altar."
        n "A portal opened, and from it emerged all the previous guardians, standing guard beside the portal."

        guardians "PLEASE HEAD INSIDE!"

        mc "Huh?"

        n "MC looks confused and heads inside."

        jump scene_15

    else:

        n "An ominous sound came from the altar."
        n "A portal opened, and from it emerged all the previous guardians along with the Overseer."

        ov "YOU HAVE DISAPPOINTED ME."

        mc "What?!"

        ov "Head into the portal."

        n "The Overseer, along with the guardians, heads inside the portal."
        n "MC also decides to come along."

        jump scene_14


    return

label scene_13:

    mc "Huh? Where am I?"
    mc "*looks around*"
    mc "I'm back! Or was it just a dream?"
    mc "*looks at his camera*"
    mc "*checks his photos*"

    n "Pictures of the previous guardians can be seen inside of MC's photo roll."

    mc "Oh my god, IT WAS REAL?!!!"

    n "The freaked out MC leaves the classroom hurriedly and goes straight home."

    mc "I AM NEVER GOING TO SLEEP IN CLASS AGAIN!!!"

    n "From a far distance, the Overseer watches MC."

    ov "Now, who's next?"

    n "THE END"

    return

label scene_14:

    mc "*wakes up*"
    mc "Huh? Where am I?"
    mc "*looks around*"

    n "MC is surrounded by the Overseer's guardians."

    ov "You are to be sacrificed."
    ov "PREPARE YOURSELF."

    mc "WHAT? NO!"

    n "MC's soul was sacrificed to the Overseer by one of the guardians."
    n "(insert one of the previous jumpscares except jumpscare 9)"

    $ play_jump()
    $ jump = random_jumpscare()
    show expression ("{}".format(jump)) at jumpscare_transform onlayer master with Dissolve(0.2)
    pause 0.5
    hide expression ("{}".format(jump)) with Dissolve(0.2)
    
    ov "Now, who's next?"

    n "THE END"

    return

label scene_15:

    n "Inside the clubroom was the Overseer."

    ov "Welcome, MC."

    mc "Who are you? Are you the Overseer?"

    ov "Yes, I am."
    ov "You were brought here, either to be a sacrifice or to be an entertainer for me."

    mc "Why me?"

    ov "Because you were sleeping."

    mc "THAT'S ALL?"

    ov "Yes, however, you have exceeded my expectations, and so I will change your fate."
    ov "You will be the next Overseer."

    mc "WHAT?!"

    ov "NO OBJECTIONS!"

    n "THE END"
    
    return
