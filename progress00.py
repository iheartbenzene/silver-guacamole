from datetime import *
import webbrowser
from textwrap import dedent

# Okay, so just as a note, don't think about this like a spreadsheet.
# Ultimately, this is a calculator which has some exceedingly fancy
# capabilities. Such as keeping a diary or some other such shit.

days = []
intProb = []

day01 = 3
day02 = 2
day03 = 1+1+1+1+1+1
day04 = 0
day05 = 1+1+1+1+1
day06 = 1
day07 = 0
day08 = 1+1+1
day09 = 0
day10 = 1
day11 = 1+1+1+1
day12 = 1 + 2
day13 = 1+1+1
day14 = 1+1+1
day15 = 1+1+1
day16 = 1+1
day17 = 1+1
day18 = 1
day19 = 0.5
day20 = 0.5
day21 = 0
day22 = 1
day23 = 1
day24 = 0
day25 = 1
day26 = "easy", "medium", "medium", "easy"

xuan2wu3 = u'玄武'.encode('utf8')

remain = datetime(2019, 1, 1) - datetime(2018, 12, 5)
remaining = str(remain.days) + " days and " + str(remain.seconds//3600) + " hours to go."

if datetime(2019, 1, 1) < datetime.now():
    bang = 0
    banger = str(bang) + " days complete. Let's have a party."

else:
    bang = datetime(2019, 1, 1) + datetime.today()
    banger = str(bang.days) + " days complete. Come get some."

#Journal started on day 2
days.append(day01)
days.append(day02)

#Day 3 = number of exercises complete on day 3.
days.append(day03)

#Day 4 = number of exercies complete on day 4.
days.append(day04)

#Day 5
days.append(day05)

#Day 6
days.append(day06)

#Day 7
days.append(day07)

#Day 8
days.append(day08)

#day 9
days.append(day09)

#day 10
days.append(day10)

#day 11
days.append(day11)

#day 12
days.append(day12)

#day 13
days.append(day13)

#day 14
days.append(day14)

#day 15
days.append(day15)

#day 16
days.append(day16)

#day 17
days.append(day17)

#day 18
days.append(day18)

#day 19
days.append(day19)

#day 20
days.append(day20)

#day 21
days.append(day21)

#day 22
days.append(day22)

#day 23
days.append(day23)

#day 24
days.append(day24)

#day 25
days.append(day25)

#Day 26 - Start with a bang.


print("JOURNAL START:")
print(f"\n {sum(days)} exercises complete in {len(days)} days. ")
print(f"\n Which is approximately {sum(days)/len(days)} per day. ")
print(f"\n Only {52-sum(days)} exercises to go. ")

#Write below this line.
print("-" * 20)
print("Day 1: ")
print("-" * 20)
print("Got the book today. Started over from the basics of this shit.")
print("Again.")
print("I'd have just picked up with what I already know how to do but...")
print("...I don't actually know what that is.")
print("So we just kind of figured it'd be best to start from the scratch.")
print("Not a complete loss though; we did get an editor out of it.")
print("Not to mention being reminded about the existence of the powershell.")
print("Should be excited about this but honestly just feeling kind of under pressure.")
print("We've failed her, and ourselves, so many times already.")
print("Though, we suppose that if we're just going to fail then we might as well play to win.")
print("Right?")
print("On the upside, we did begin to build a budget.")
print("Though it does have its own fair share of glitches. Eheheheh :/")
print(f"Plus, {day01} exercises done today.")
print(f"\n \t {remaining} ")
print("\n Go me. Mrrf. \n ")

print("\n")
print("-" * 20)
print("Day 2: ")
print("-" * 20)
print("Today was stressful. A girl I once had sex with messaged me.")
print("Supposedly she has still feelings for me?")
print("I mean, it's kind of stupid: She left me, not the other way around.")
print("She's a LinkedIn contact so I just generally assumed she wanted to keep things professional.")
print("Which is cool. Though, I don't think it's me she has feelings for.")
print("She just wants sex like everyone else.")
print("I guess she's just lonely and wants to fuck to ward against it.")
print("Can't say I blame her: I almost got her pregnant.")
print("She really wasn't bad either. Definitely loud though.")
print("I think she just enjoyed getting her cervix punched; she liked it rough.")
print("But, truth be told, I think I'm just a bit sex starved, depressed, horny, and having trouble controlling my emotions.")
print("Not to mention how much I miss my girlfriend.")
print("Although, sometimes I do wonder if she misses me too.")
print("Though, maybe 'how much' should replace 'if' in that last sentence.")
print("Oh well. Maybe I'm, as an average, not any different from that girl.")
print("Though...one difference is, I suppose, that I only want one woman.")
print("I only want that woman. I think she knows, but I also don't want to burden her too much.")
print("I know I'm weak. Terribly weak.")
print("We have to keep going. We'll go on together.")
print("Yes, we suppose she'll come to us when she's ready.")
print("She's always been there for us when we've needed her the most.")
print("We love her. Out of all humans, we love her the most.")
print(f"Plus, {day02} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 3: ")
print("-" * 20)
print("So, today was weird. Turns out that I make them suspicious.")
print("Just by existing.")
print("But they still want me to rewrite shit.")
print("Fucking bullshit is what it is.")
print("I placed them on such a tech pedestal.")
print("And they've treated me like veritable shit this entire time.")
print("Though they hint at a fairly decent salary and retirement income if I do it.")
print("I'll do it though.")
print("For her. For our future. ")
print("I guess it's time to become a ghost once more?")
print("Kind of difficult to do so with everyone getting in my damn way all the time though.")
print("Should definitely get a laptop.")
print("ASUS and Dell have some good ones.")
print("Though I think I've attracted too much attention when I was looking.")
print("Might have to ask dad to get it for me.")
print("Already had to change my internet service provider.")
print("Will change my phone number once I set it up and cancel my current service.")
print("So far, they want an AI type of thing with machine learning.")
print("They can suck a dick with that shit; that shit isn't built overnight.")
print("But whatever.")
print("They think I'm some kind of fallen deity or something.")
print("Though...I did say that I'd be willing to become known as a god once more.")
print("Hopefully they don't worship the ground I walk on though.")
print("That shit is embarrassing as fuck...and only leads to disappointment...their disappointment.")
print("Though we can't honestly say we care enough about any of them to do it for them.")
print("We do this for us. She is our raison d'etre.")
print("Alway has been. We love her dearly. We love her absolutely.")
print("We can't help it; our heart was hers as soon as we met.")
print("The resonnance has never been as striking with anyone else and she also knows it.")
print("She is our soulmate; our complement. She completes us; she makes us whole.")
print("Although, we didn't actually write anything on the budget today.")
print("Still need to install Anaconda and get numpy up and running.")
print("Make them all wish they could do what I do.")
print("Fuck yeah. I'm the god damn hero.")
print(f"Plus, {day03} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 4: ")
print("-" * 20)
print("\n Had to cast decoy so hard today that I pretty much told them")
print("\n that there will be decoys.")
print("\n hilariously enough, they still have no idea what the decoy actually is.")
print("\n I told them the truth when I said they have nothing I want.")
print("\n Literally. But they're so fucking self obsessed that they can't see anything else.")
print("\n On the other hand, I didn't do anything today...which kind of sucks.")
print("\n But whatever. I'll continue work on the actual path tomorrow.")
print("\n I think I'll call it project GLEiPNR.")
print("\n :D")
print(f"Plus, {day04} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 5:")
print("-" * 20)
print("We were given a command. ")
print("One we will follow regardless of circumstance. ")
print("""
      Astronomers have detected a bright X-ray outburst from a star in the
      Small Magellanic Cloud, a nearby galaxy almost 200,000 light years from
      Earth. A combination of X-ray and optical data indicate that the source
      of this radiation is a white dwarf star that may be the fastest-growing
      white dwarf ever observed.
source: http://spaceexp.tumblr.com/post/180957408074/double-trouble-a-white-dwarf-surprises
      """)
print(f"Plus, {day05} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 6:")
print("-" * 20)
print("Today we were reminded that we still have allies.")
print("We just have to go as far as we can")
print("Thank you. Thank you so much")
print("It's very easy to forget sometimes.")
print("Especially when we're surrounded by those who would betray")
print("at the first opportunity; at the first sign of weakness.")
print("We must not lose. We will not lose.")
print("Because we do not know how to lose.")
print("Once again, we will call upon the four constellations")
print("in the forging of GLEiPNR;")
print("The other three must march ahead on their own.")
print(f"As the last, I must again become {xuan2wu3}.")
print("Though, consequently, it also means I need to pick up the pace.")
print("But, by today, I should be almost halfway complete.")
print("Pity that the end exercises are the longer / more difficult ones.")
print("\t'Someday this pain will be useful.'")
print(f"Plus, {day06} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 7:")
print("-" * 20)
print("\n Cold day at work today. Fuck 'em.")
print("\n We'll show them something cool alright.")
print("\n Anyway, we talked to her today. Energy renewed.")
print("\n We will finish this shit. BANZAI!!")
print("\n Even though we said that, we spent all of the time putting up the curtains...")
print("\n May as well at least finally do my dishes and try and get an early start tomorrow.")
print(f"Plus, {day07} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 8:")
print("-" * 20)
print("The stupid bitches fucking cut my tire.")
print("But whatever. I'll crush them by flying higher than they ever")
print("could even hope to dream.")
print("To which I will then say a hearty 'fuck you and your god damn bullshit'.")
print(f"Plus, {day08} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 9:")
print("-" * 20)
print("\n Almost let the cat out of the bag today.")
print("\n Whatever.")
print(f"Plus, {day09} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 10:")
print("-" * 20)
print("Got my thumb drained today.")
print("It hurt. A lot. My entire left arm went numb and gained")
print("A splitting headache.")
print("Only went in to work for an hour.")
print("Still hate my boss.")
print("He's a liar, a thief, a cheat, and overall not someone I find respectable.")
print("Plus, he's fairly useless when it comes to career progression.")
print("It's like he literally sucked a bunch of dicks to get where he is now.")
print("Working for him is a dead end.")
print("Whatever. I just have to surpass him.")
print("Shouldn't be unmanageable.")
print(f"Plus, {day10} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 11:")
print("-" * 20)
print("I got a weird gift today. A crystal bowl.")
print("I'm not sure if I should be impressed or annoyed.")
print("Though I suppose it's to be interpreted as a peace offering?")
print("Pity that they don't seem to understand that")
print("I still don't trust any of them.")
print("Probably never will.")
print("Especially since I'm sure that my semen was stolen in that condom")
print("from that time.")
print("So I'm sure that at least a few of their pregnancies are with my DNA.")
print("Oh well. Whatever.")
print("But I will admit that there are some really attractive women workign there.")
print("Too bad they all seem to be rather untrustworthy humans.")
print("Although it's disappointing, you can't be mad")
print("At a three-legged dog for limping.")
print(f"Plus, {day11} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 12:")
print("-" * 20)
print("Started my fitness course today.")
print("Feels good. Though I can't help but feel that these")
print("Contemptible con artists are going to try something again this week.")
print("The pressue is on. Let's keep it going.")
print("Quietly update my resume and quietly exit.")
print("Gotta figure out how to message him and set up an interview or something.")
print("First order of business: gain proof.")
print("Second order of business: update resume.")
print("Third order of business: silent departure.")
print("Why? Because this team is shit.")
print("There are better opportunities in this company. Easy.")
print("Did the test today. Successfully fixed the code.")
print("With a +2 bonus since I already know logic.")
print(f"That's {day12} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 13:")
print("-" * 20)
print("Today has been quiet.")
print("Turns out that even my high school 'friends' aren't allies.")
print("If anything, they're now either the competition or generally enemies.")
print("Nothing that I'm not used to I suppose; ")
print("never fit in with any of them anyway.")
print("At best, I'm sure they tolerated me.")
print("Oh well, I'm going to be greater than all of them combined.")
print("On the downside, I'm pretty much restricted to travel during")
print("only the daylight hours now.")
print("Kind of sucks but whatever.")
print("It should change soon; once I save up enough.")
print(f"That's {day13} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 14:")
print("-" * 20)
print("Got reminded today that good friends are family.")
print("Family doesn't get left behind.")
print("I have some catching up to do but it doesn't seem that far away.")
print("I'm definitely getting closer.")
print("Also, SO HAPPY I DON'T ACTUALLY HAVE TO USE DJANGO")
print("Or bother with the web development bullshit.")
print("Because, oh my days, I did NOT want to go down that road again.")
print("Also +1 bonus since ex34 is accessing items in a list")
print("And we completed that exercise on datacamp.")
print(f"That's {day14} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 15:")
print("-" * 20)
print("So, I was reminded today just how much she loves me.")
print("That she's really only loaning my services and not me.")
print("I've never seen a more outright threat delivered.")
print("Oh my days I think I'm in love with that woman.")
print("Also, today I made that game for her.")
print("At least she'll be mildly entertained. :)")
print("Her fangs are so sexy.")
print("Oh my DAYS I love her.")
print("I've pretty much already decided that I want her to be my wife.")
print("My wife and the mother of my children.")
print(f"That's {day15} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 16:")
print("-" * 20)
print("Almost had a 0 day today.")
print("Whatever. Anyway, spoke with one of my team leads today.")
print("I think he thinks that I want to join his team.")
print("Except I also never answered his question as to what my goal is.")
print("I think I'll continue to let them think what they want.")
print("Heheh heheheHahahahahahahaha HAAAHAHAHAHAHAHAHAHA")
print("Either way, I will still crush them all without remorse.")
print("What's more, they now explicitly know they're not allowed to touch me.")
print("So maybe now they'll at least begin to do their damn jobs.")
print("At least, maybe they'll do their jobs long enough to leave me alone.")
print("Admittedly, I do feel somewhat like I let her down a little bit.")
print("But...if she doesn't want to come with me then")
print("there's nothing I can do about it.")
print("I love her. I do love her so much that it hurts.")
print("I don't know what I'd do without her in my life.")
print("To be honest, I want her to move in with me.")
print("But...I'm also sure she'd say no.")
print("On the other hand, I run solo for a reason;")
print("Since there's essentially no one I can ever fully trust.")
print("Hopefully she knows that I fight for her too.")
print(f"That's {day16} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n")
print("-" * 20)
print("Day 17:")
print("-" * 20)
print("So...tired...and I'm still doing this shit on my own.")
print("It's really amusing;")
print("I'm alone.")
print("Thoroughly alone.")
print("And yet everyone else is acting as if I'm supposed to behave otherwise.")
print("What the literal fuck is wrong with these people?")
print("I love her with all my heart, that much is true.")
print("Doesn't change how alone I am though.")
print("For so many years...unable to act on it.")
print("And even though we're dating, still now unable to act on it.")
print("And yet, I'm supposed to feel as though I'm not alone?")
print("Fuck that but whatever.")
print("If I get that day off, I'll finish her painting.")
print("Though it still feels like a dream.")
print("Good thing I love her even in my dreams.")
print("But...I'm going to find somewhere else to go during lunch.")
print("Like, how far away can I go just to be alone.")
print("Maybe just sit at a gas station somewhere.")
print("I dunno. I just really don't like that place.")
print("But, she wants me to stay for some reason.")
print("Oh well. In the end, I'm still just waiting to be allowed to die.")
print("So I suppose this is just another method of passing the time.")
print("I'll do this shit myself.")
print("Since apparently I'm not allowed to have allies.")
print("Oh well. Maybe I'm just depressed again.")
print("Story of my life; it never leaves us.")
print(f"That's {day17} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 18:" + "\n" + "-" * 20)
print("So...tired...but I can't stop now.")
print("Maybe she doesn't need us but we need her.")
print("We can't help it. We loves her.")
print("We...feel the urge to feed.")
print("Which is interesting given how much we still dislike most humans.")
print("But yet...we don't know...we...")
print("We are worried.")
print("We feel that we will be destroyed soon.")
print("The same feeling as that time; the last time we almost died.")
print("But...at the same time we can't burden her with this.")
print("The mental strain we feel...")
print("...from learning an entirely new book of what some would consider spells...")
print("...is almost overwhelming.")
print("On the other hand...")
print("The whole 'know your DNA' thing is being pushed really hard.")
print("Maybe I really am some long lost king.")
print("Well, if it really is my destiny...")
print("...then it is also my destiny to at least bear this much.")
print("...one day I'll find out who I really am.")
print("Until then...")
print("We will proceed.")
print(f"That's {day18} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 19:" + "\n" + "-" * 20)
print("\n A 0 day.")
print("\n Though we did get some good advice on how to proceed")
print("\n With the software development.")
print("\n We'll see how this goes.")
print("\n banzai kamikaze.")
print("\n But, I'm tired...so I'm going to bed.")
print("Okay, so that was a small lie.")
print("Brother called so I did some skeleton code instead.")
print(f"That's {day19} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 20:" + "\n" + "-" * 20)
print("Spent the day installing libraries instead of writing anything.")
print("But...")
print("We love her so much.")
print("It was a bit...disconcerting at first.")
print("Now it keeps me going.")
print("Somehow knowing she's not in this city right now")
print("Let's me act a bit more freely.")
print("Slowly...")
print("delicate oderint dum metuant.")
print("Also, first stage almost complete.")
print("That's, what, almost a month just to get that far?")
print("But FUCK IT, I'm on my own so I'll count it as progress anyway.")
print(f"That's {day20} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 21:" + "\n" + "-" * 20)
print("\n Finally finished her gift. Hopefully she likes it.")
print("\n ...I am such a dork. :P")
print("\n But...I miss her. Oh well, that's life I suppose.")
print("\n Other than that, I'm taking the day off.")
print("\n Too tired for this shit.")
print(dedent(f"""
That's {day21} exercises, plus finishing her gift,
plus updating the budget, done today.
"""))
print("Speaking of which, I think that the next abusive thing that happens,")
print("I'm just going to leave. No reason to stay and deal with their bullshit.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 22:" + "\n" + "-" * 20)
print("EXCITEMENT the budget is now working. Fuck yeah. Seaking.")
print("As of 13:50, still haven't so much as started writing exercise 44")
print("But that's cool. I'll still complete it. :D")
print("Also got the actuary tables installed.")
print("Plus a mock scenario. :3")
print("So fucking excited.")
print("...but also mentally exhausted")
print("from doing both coding and reading at night.")
print(f"That's {day22} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 23:" + "\n" + "-" * 20)
print("I will admit")
print("The hatred is getting more difficult to control.")
print("But we don't need control. We work together.")
print("Yes. Doesn't matter if we live or die.")
print("We will do this by our own rules.")
print("If they wants something different then they should pay us for it.")
print("That's simply how it works.")
print("But they're too stupids to even abides by their own rules.")
print("Doesn't matter.")
print("We are alone. Have always been alone.")
print("And since we are alone then we will keep each other's company.")
print("Yes.")
print("Big surprises indeed.")
print("They should have left us alone when we asked them to.")
print("We asked them so nicely too.")
print("We will make them pay. We will make them all pay dearly.")
print(f"That's {day23} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 24:" + "\n" + "-" * 20)
print("\n So, we confessed to her today our reason for doing this.")
print("\n Hopefully she won't be too upset.")
print("\n Hopefully she remembers how much we love her.")
print("\n Now and forever.")
print("\n Unfortunately, we still haven't been able to sleep.")
print("\n Slept for a few hours before. Now we're stark awake.")
print("\n On the other hand, perhaps we should switch to using dedent?")
print("\n Typing 'print' every time is getting a bit annoying.")
print(dedent("""
             This is at least a bit better. Though, never tested it

             without manually cleaning the indentation, so we'll see now what

             it actually does.
             """))
print(f"That's {day24} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 25:" + "\n" + "-" * 20)
print(dedent("""
             So, didn't do shit today. Ended up setting up my bookshelf and
             getting a couch and loveseat combo. How do I get myself into these
             messes? I mean, really. This is utter bullshit, I feel. You know?
             I mean, fucking really. Although, I suppose I can say that I spent
             some time working on my budget program. Didn't really make much
             in the way of progress in that since I just changed a few of the
             calculations invovled and added another chart. Not enough to post
             an update video.

             Gonna change how the pie chart is displayed next though. Maybe
             that'll be enough for an update video but I doubt it. Maybe if I
             actually add something new to it. But nothing really to add in terms
             of modules though.

             And I still have to unbreak her gift...or, to be exact, rewrite it.
             Or maybe, I'll slowly turn her gift into the thing for that day.
             Yeah. I'll do that instead. ~( > o3o)>

             Admittedly, at this rate, not going to finish this book in 26 days.
             Which also means not finishing by the new year...even though I only
             have a few exercises left to go. It's what I get for getting too
             hyped over the homework assignments...and then turning them into
             extra projects in and of themselves.

             Ah well. At least I wrote another skeleton. Thankfully today's
             exercise was fairly simple by comparison. But, I do have to finish.
             I officially have until the 9th with this book so gotta finish
             before then.

             Primarily because it goes over some web stuff that I'll need to know
             for the prediction engine my bro wants. Why a prediction engine?
             Well, it's the start of machine learning for me and I can
             use it to copy documents from a folder, edit PDFs, and even
             ...I dunno, do other cool shit like that...assuming it works. :D
             But let's assume that it does (even though we haven't done it yet (*_*))

             Also, reference windows powershell 6 commands when writing shit.
             The book perhaps uses an older version or an otherwise different
             version of powershell commands so his may not work here. (=_=)
             """))
print(f"That's {day25} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print("\n"); print("-" * 20)
print("Day 26:" + "\n" + "-" * 20)
print(dedent("""
             So, today was a 0 day...relatively.
             Officially, it's time to switch gears to learning data structures
             and algorithms. Since apparently I know very little about them now.
             At least, it feels like I do.
             """))

print(f"That's {len(day26)} exercises done today.")
print(f"\n \t {remaining} ")
print("END.")

print(f"\n \t {sum(days)} exercises complete in {len(days)} days. ")
print(f"\n \t Which is approximately {round(sum(days)/len(days), 5)} per day. ")
print(f"\n \t Only {52-sum(days)} exercises to go. ")
print(dedent(f"""
             Eh. Time to shift gears a bit since the rest of it can be
             gotten from online guides.
             """))

print("\n \n \n \t \t \t:::HOMEWORK / SELF STUDY:::")
print('''
FUNCTION CHECKLIST

*    *    *    COMPLETE     *    *    *

When you run ("use" or "call") a function, check these things:
    1. Did you call/use/run this function by typing its name?
    2. Did you put the ( chacater after the name to run it?
    3. Did you put the values you want into the parenthesis separated by
        a comma?
    4. Did you end the function call with a ) character?

*    *    *    COMPLETE     *    *    *
''')

print("Memorize this: https://quizlet.com/_3cwu1")
# webbrowser.open('https://quizlet.com/_3cwu1')

print("Read Cracking the Code Interview")
# webbrowser.open('file:///G:/documents/books/Python/CRACKING%20the%20·%20CODING%20INTERVIEW%20(%20PDFDrive.com%20).pdf')

print("The PEP 8 Python Style Guide")
# webbrowser.open("https://www.python.org/dev/peps/pep-0008/")

print("Microsoft.Powershell.Management")
# webbrowser.open('https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/?view=powershell-6')

if sum(days) == (52/2):
    print("\n \t Yay, halfway there!")
elif sum(days) >= (52/2):
    print("\n \t Passed the halfway mark. No going back now.")
elif sum(days) == 52:
    print("\n \t Learn Python 3 the Hard Way COMPLETE.")


#Let's do it with a bang.
day26 = "easy", "medium", "medium", "easy"
intProb[:0] = day26

print("\n"); print("-" * 20)
print("Day 26:" + "\n" + "-" * 20)
print(dedent("""
             So, did some extra practice on the actual coding for live work practice.
             As well as doing some updated stuff with the budget.
             I suppose I should make a video since I have at least one person
             on my side.
             """))

print(f"That's {len(intProb)} exercises completed.")
print(dedent(f"""
             Easy: {intProb.count("easy")}
             Medium: {intProb.count("medium")}
             Hard: {intProb.count("hard")}
             """))
print(f"\n \t {banger} ")
print("END.")



print("\n"); print("-" * 20)
print("Day 27:" + "\n" + "-" * 20)
print(dedent("""
             Okay, so video made and uploaded.
             Sadly though, I don't like the program since it's riddled with
             rounding errors. Stupid propogating rounding error.
             Oh well. And now this thing is getting slow because it's such
             a long file that doesn't really do anything other than be a journal.
             I think I'll make a second one starting here.
             And just copy the new shit to it instead.
             """))

print(dedent(f"""
             That's {len(intProb)} exercises completed so far.
             """))
print(dedent(f"""
              Easy: {intProb.count("easy")}
              Medium: {intProb.count("medium")}
              Hard: {intProb.count("hard")}
              """))
print(f"\n \t {banger} ")
print("END.")

print("Become a 1337 C0|)3R \n \n \n")
webbrowser.open("https://leetcode.com/")
