from datetime import *
import webbrowser
from textwrap import dedent

# Okay, so just as a note, don't think about this like a spreadsheet.
# Ultimately, this is a calculator which has some exceedingly fancy
# capabilities. Such as keeping a diary or some other such shit.

intProb = []

day26 = "easy", "medium", "medium", "easy"

remain = datetime(2019, 1, 1) - datetime(2018, 12, 5)
remaining = str(remain.days) + " days and " + str(remain.seconds//3600) + " hours to go."

bang = datetime(2019, 1, 1) - datetime.now()
bang = abs(bang)
banger = str(bang.days) + " days complete. Come get some."

# New journal start!!


print("\n"); print("-" * 20)
print("Day 26:" + "\n" + "-" * 20)
print(dedent("""
             So, today was a 0 day...relatively.
             Officially, it's time to switch gears to learning data structures
             and algorithms. Since apparently I know very little about them now.
             At least, it feels like I do.
             """))

print(f"That's {len(day26)} exercises done today.")

print(dedent(f"""
             Eh. Time to shift gears a bit since the rest of it can be
             gotten from online guides.
             """))

#Let's do it with a bang.
print(f"New journal started. {datetime(2019, 1, 1)}")

day26 = "easy", "medium", "medium", "easy"
intProb[:0] = day26

print("\n"); print("-" * 20)
print("Day 26:" + "\n" + "-" * 20)
print(dedent("""
             So, did some extra practice on the actual coding for live work practice.
             As well as doing some updated stuff with the budget.
             I suppose I should make a video since I have at least one person
             on my side.
             (u_u)

             END.
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

             On the other hand, got stuck today on the atoi question.
             Since I'm used to going
             input -> variable -> cast -> value
             And the function skips the "cast" part. Which is cool because it's
             then more universably applicable but also more difficult since I'm not
             casting.
             (@_@)

             END.
             """))

day28 = "easy", "medium", "medium", "medium"
intProb[:0] = day28
print("\n"); print("-" * 20)
print("Day 28:" + "\n" + "-" * 20)
print(dedent("""
             Finally quiet at work. Stupid garbage humans.
             HATEHATEHATEHATEHATEHATEHATEHATEHATEHATEHATETHEM
             Okay. That's out of my system. For now. At least until I go back to
             work tomorrow and see them again. Pieces of shit.
             (=n=) Fuck em.
             (*n*) FUCK EM HARD
             Figuratively of course.
             WE DESPISE THEM.
             """))

day29 = "medium", "medium",
intProb[:0] = day29
print("\n"); print("-" * 20)
print("Day 29:" + "\n" + "-" * 20)
print(dedent("""
            Okay. So today, this fucking fantastic human decided to have the
            balls to tell me AGAIN that he's going to help me. AGAIN. I mean,
            you had PLENTY of fucking chances to do so. YOU SAID THE SAME
            DAMN THING IN THE FIRST PLACE. What would make now any different?
            Why should I trust you any more now than any of the MILLION OF
            FUCKING TIMES you said the SAME DAMN LINE in the past?
            I mean, just like with my migraines. YOU GIVE THE SAME FUCKING
            BULLSHIT TIRES ASS LINE every time. EVERY FUCKING TIME.
            Fuck it. Stupid god damn cunt. Maybe if you didn't lie to me
            since we FIRST FUCKING MET then it'd be different.
            Fucking raging at that shit so hard right now.
            (*o*)
             """))

day30 = "medium","medium",
intProb[:0] = day30
print("\n"); print("-" * 20)
print("Day 30:" + "\n" + "-" * 20)
print(dedent("""
             So, officially hit the one month mark of practicing coding today.
             I still hate this place. Rather vehemently, might I add.
             I mean, there's no incentive for actual growth, just some weird
             new form of stagnation which I've never seen anywhere else before.
             But whatever. The agreement that I attempted to make what that
             if she became mine; that is my wife and the mother of my children;
             then I would stick around. But, however fortunate or unfortunate,
             we're dating at best (which is awesome in itself)
             and nothing is (probably) going to progress beyond that point
             until after she graduates her program (at least).
             Which means that, since the bargain has not in any way been struck.
             Which also means that I have 0 incentive to stick around and deal
             with their bullshit. 'Onward and upward' as they say. But clearly
             they like to preach a lot of bullshit and say things like,
             'we are committed to growth', career or otherwise, it's complete
             and utter bullshit. Oh well, not my problem. Not where there are
             more applicable positions offering at least double what I'm getting
             now. Loyalty doesn't mean shit these days. Especially when they only
             want you to be loyal so they can stab you in the back at the first
             opportunity.

             That is, since I'm still as alone as when this all began, then I have
             neither incentive nor reason. So, as they say colloquially, fuck you.

             I've already given you plenty of chances and you fucked them all.
             Threaten me all you like; it just gives me fuel. Best case scenario
             I'm out of this shit since yesterday. Worst case scenario, I'm out
             of this shit in 6 months. At least it feels that now they finally
             understand that I won't be taken in by their bullshit.
             (^n^)
             """))

day31 = "medium",
intProb[:0] = day31
print("\n"); print("-" * 20)
print("Day 31:" + "\n" + "-" * 20)
print(dedent("""
            So, today made me realize something.

            'They don't respect you at the bottom. They ignore you in the
            middle. They hate you at the top.' As the saying goes...

            I love her; I really do. But, at the same time, it feels like
            she only agreed to date me to be a leash. I mean, do I really know
            that she feels even remotely the same way about me? I would like
            to think that she does but... I do have my doubts.

            I'll continue as I have for the time being. When we next speak in
            person I won't be able to hide it though. Over the phone, I can
            always mask what I'm feeling; even easier to do via text.
            Because via text messages, I can just opt not to tell her and she
            would be, more or less, none the wiser for it. Though, I do honestly
            wonder how upset she'd be if I left.

            Would she wait for me? Would she come with me? Would she prefer that
            we separate entirely? These are all questions for which I have no
            answer. For that matter, she hasn't actually said explicitly how
            she feels either. So this, in the end, still feels a bit one way.
            Though she does seem to brighten when we speak. And she does seem
            to equivalently feel strongly about me. I just...I'd like to know
            for sure, you know?

            Maybe she's getting tired of being my leash and would actually be
            really happy to see me go? Maybe she's just being a really great
            friend who's worried about me. I don't know. I mean, I'm pretty sure
            she's also feeding them information rather directly. I mean, I know
            I'm being monitored and that she was probably contacted about it.
            Why else would our paths have crossed in the way that they did?
            And, of course, she would agree to date me to keep me safe; and to
            be my leash to make sure I don't leave? I mean, I know they've
            purchased my data and are watching me heavily. But how else would
            they know things that I didn't tell anyone but her even directly?
            I don't know. I still love her. I love her dearly. But, maybe it's
            time for me to kill my heart before I get hurt again. It always
            works out this way. It always does and I never seem to learn.

            (u_u)

            ...sigh. I guess, in the end, I'm as alone as when I began. Though,
            the one thing that's different this time is that we've kissed.
            Actually kissed I mean. Even had sex once.
            That makes me happy. But...did she only do so knowing that it would
            and that I'd just want to be tied to her even more closely?
            But...she does make me smile, and when she laughs (or smile in
            return) everything feels like it'll be okay.
            Meh.
            What do I know? Outside of math and how to be an unfeeling machine
            of a scientist? Not a god damn thing.

            At any rate, picked up JavaScript today. Pretty neat so far.
            Go me. Yay.

            d(-_-)b
            """))

print("\n"); print("-" * 20)
print("Day 32:" + "\n" + "-" * 20)
print(dedent("""
             She makes me very happy and I love her very much.
             But OH MY FUCKING DAYS stuffing this much info into my head in as
             short a time as I am now is REALLY strenuous. At least Python is
             providing a sufficient base so it's not unmanageable.

             Though I did find a  Java tutorial here:
             https://www.youtube.com/watch?reload=9&v=grEKMHGYyns

             Not gonna set an open webbrowser though; I'm going to do it in
             chrome.

             On a side note, I'll admit that the tags in JavaScript are weird.
             But they're not bad actually. Some of the attributes are kind of
             uncommon though since it seems to be primarily about drawing
             an image of some type (in general) on the screen; whether that is
             text, shapes, or an actual image. Though I do wonder if the same
             holds true for pictures or animated gifs; I'm sure it does but
             I'll test it later.

             (*u*)b
             """))

day33 = "medium", "medium",
intProb[:0] = day33
print("\n"); print("-" * 20)
print("Day 33:" + "\n" + "-" * 20)
print(dedent("""
            So, still stuck in this god damn place for now. But gave them a
            chance by pointing out that my interest in coding is second only
            to my formal training as a mathematician; yet another area they
            simply DO NOT HAVE. Also another area they seem unwilling to pay
            me for but want something for free. Except missing a rather crucial
            detail; I don't work for free.

            Which kind of says to me that they honestly don't review any of the
            documents which they request to be submitted. So, at this point,
            any dissent they experience is entirely self wrought.

            Humans.

            And somehow they feel that I'm compassionate enough such that if they
            threaten others then they will get to me. Except, my arms are
            literally only so long and I will always seek to completely erase
            my opposition.

            If you are not my ally, then you are very much my enemy; being my
            friend does not equal that you are my ally. At best, the inclusion
            goes only one way. At least, until proven otherwise; so far they
            are doing their absolute best to prove that they are nothing more
            than foes to be abandoned or vanquished.

            Let's not forget that I'm not heroic, not anymore; I'm just the hero.

            On the other hand, I still love her very much. Such that, I would
            want her to be my wife, my life, and the mother of my child(ren?).
            Though, I suppose the question really remains whether or not she
            wants it as well.

            (u_u)
             """))


print("\n"); print("-" * 20)
print("Day 34:" + "\n" + "-" * 20)
print(dedent("""
             So, finally started scanning and uploading my notes like I've been
             meaning to do. ADVANCED CALC WAS SO FUCKING AWESOME.
             I just wish so much shit didn't happen during these two semesters.
             Apartment burnt. Became homeless. Moved into (what at first seemed
             like) a "okay" community. Wouldn't find out that they're complete
             and utter shit bags until later. And by "later", I mean "within the
             past few months". I swear, fucking Merrill Lynch is the worst place
             to ever work if you don't feel like sucking dicks for a living.

             Why? They fucking lie to you, want to pay you in dirt, and then
             expect you to trust them openly. NOPE. They had their chances.
             Nine of them so far, actually. Well, everyone who knows cyclic
             groups know that the number after nine is 0. So to speak freely,
             first chance I get, I'M OUT OF THIS BITCH. And ideally, that
             chance may arrive much sooner than expected. SO STOKED.

             (^u^)

             """))

print("\n"); print("-" * 20)
print("Day 35:" + "\n" + "-" * 20)
print(dedent("""
             So, the bullying more or less reached a peak today. Such that my
             direct managed tried to pretend that he wasn't at fault by
             suddenly pretending to take an interest in differential convex
             sets. In particular, suddenly take an interest in my notes.
             Thankfully, I got a call and I didn't have to deal with his
             bullshit. Though they seem to think that they can appease me with
             anything less than the offer made by the other company. No. I
             vehemently refuse.

             I'm done hiding. I'm done holding back. I'm done pretending.
             They wanted to get to know me and then cried wolf when they
             realized that I'm of a much higher intelligence. Now they threaten
             and think that I'm just going to cower and hide from their shit.
             No. Fuck that. Come at me directly and receive a direct response.

             And don't suddenly attempt to use vocabulary words and think that
             it's going to change my mind. One thing that mathematicians can do
             is deliver an unbiased evaluation. Unfortunately for them, my
             evaluations have always been unbiased.

             As I mentioned before, they had their chance; nine of them to be
             exact. I've been sufficiently lenient. Now that I seem to have
             found a path and otherwise means of exit, then I am done.

             (-n-)
             """))

print("\n"); print("-" * 20)
print("Day 36:" + "\n" + "-" * 20)
print(dedent("""
             No code done today. Spent the day being harassed again at work and
             thus spent the night writing a paper on software development
             techniques. Wasn't a bad paper, we feel, although we did have some
             trouble writing about some of the more niche topics.

             Oh well.

             (u_u)
             """))

day37 = "medium",
intProb[:0] = day37
print("\n"); print("-" * 20)
print("Day 37:" + "\n" + "-" * 20)
print(dedent("""
             Still haven't written anything today either. Considering playing
             around with some of the ideas in our head but also don't really have
             any ideas of where to start. I mean, a complex valued vector?
             That shit is higly bonkers. But at the same time it's also not
             something we've ever really messed with before.

             Meh. For now we'll just focus on m-dimensional differentiability
             and integrability. Seems like that'll be more useful for developing
             that thing.

             In either case, we still have 0 interest in remaining with this
             bullshit. Although they seem to keep hinting that there's something
             super ultra shady going on and that that program is highly
             suspicious, if not the center of the maelstrom.

             (>_>)

             Though it's really not my problem. We're really just better off
             making something that would be leased.

             Lol, although the notes make it seem like we missed 3 days isntead.

             (*u*)
             """))

print("\n"); print("-" * 20)
print("Day 37:" + "\n" + "-" * 20)
print(dedent("""
             So, uploaded more of my science-based videos online. Also shared
             my notes online to various places. As well as updated certain
             automated messages. The ones who pay for it are the ones who will
             get it, we feel. It's kind of amusing that we don't feel comfortable
             using 'I' in a sentence sometimes but always comfortable using 'we'.
             Like, the difference between 'boku' and 'ware'. Kind of amusing
             that as someone who studied Mandarin formally ended up learning
             Taiwanese idioms but ends up using random Japanese phrases in my
             head. And no, we don't have a problem using 'my'.

             Anyway, we also found a machine learning tutorial online. Kind
             of curious to see how the new material will work with my existing
             ideas.

             On a side note, we still love her very much. Very very much. She...
             it's difficult to explain. We are hers as much as she is mine.
             Kind of interesting that we're also a bit different with respect
             to emotions. Although she understands that we are simply actively
             interpreting internal bodily signals and applying a definition to
             them rather than passively, even innately, understanding what they
             should mean.

             But, back to topic, something that will be leased. If they are
             okay with the lease, then they can use it. If they are not okay
             with the lease then they won't use it. The primary theorems will be
             open and if they are clever enough then they can use it as a base
             for their own purposes. Much like Steve Wozniak did with Linux.
             Conversely, if they are not sufficiently clever, then that's a
             whole lot of not my problem. Yes.

             We are a mathematician, first and foremost.

             (vnv)

             On second thought, that fat fuck has pretty much ensured that
             they're on their own. If they want to play in the new age,
             then they'll have to do so on their own as well.

             (*n*)
             """))

print("\n"); print("-" * 20)
print("Day 37:" + "\n" + "-" * 20)
print(dedent("""
             So, finished up some shopping today (more or less) and did a test
             run of concealment MK I. It worked out really well, we feel.
             However, these bitches seem to think that I'm going to back down.
             They got Scurti and somehow painted it like a suicide. Unfortunately
             for them, if my account isn't active, then their names and everything
             else becomes publicly known. Well, even more public than now.

             At any rate, started writing the curve to be used. I suppose,
             once the largest sections covered have been established,
             then we can establish the greatest common value (GCV) on fixed
             intervals. On the other hand, still have to determine the intervals.
             Though that should honestly be the easiest part; we're assuming that
             we can just start between 0 and 1.

             We will take her with us if she will go.

             (-3-)

             Anyway, wrote the first algorithmic hilbert curve. But at the same
             time, we encounter the same problem here that we did with Tensor;
             the newer versions of Python are unsupported. Which means we
             probably have to either depend on a ComplexSpace(n), L2(Interval(0, n)),
             or otherwise HilbertSpace() to generate the actual curve.

             We'll test it later. But it's actually pretty convenient since it's
             already done, so no worries.

             We probably don't understand enough about them yet to fully grasp
             how to use them for the GCV though. We'll do a bit more reading
             first and see.

             (n3n)

             """))

print("\n"); print("-" * 20)
print("Day 37:" + "\n" + "-" * 20)
print(dedent("""
             Eh. Wish I had some good news to offer this thing once in a while.
             Other than finishing my book with several an hour to go, I ended
             up working overtime tonight. Threw off my eating schedule a bit.
             Oh well. Honestly tired of this shit. Every day seems to be a new
             and creative Sisyphean task.

             At any rate, although we love her and would love to spend the night
             in fantasy, we have work to do.

             On the other hand, we did start configuring SciKit today. So that's
             a plus.

             (-u-)
             """))

print("\n"); print("-" * 20)
print("Day 38:" + "\n" + "-" * 20)
print(dedent("""
             So, nothing but garbage. Utter garbage today.

             MY NOTES ARE MY FUCKING NOTES. They have NOTHING to do with ANYONE
             unless we're doing a god damn research project ABOUT the entity
             specifically. Since we are not, then THE NOTES ARE MINE AND WE WILL
             DO AS WE PLEASE.

             Also learned something new just now, "with" in all caps means
             something in Python.

             Oh well. It'll be over
             soon enough.  On the upside, we did a mass upload of all my python
             projects. Next we need to do a database, we think. Java can go
             suck a dick. I'ma do SAS.

             (-_-)

             It can't be over soon enough. we need to hustle. Also started an
             actual ML course today. Omg it's a real class. We actually have to
             take notes on this shit or else we'll lose super hard.

             BUT IT'S SO DELICIOUS

             (*_*)
             """))

print("\n"); print("-" * 20)
print("Day 39:" + "\n" + "-" * 20)
print(dedent("""
             Also, "with" in Python seems to be used when working with unmanaged
             resources like file steams. It allows you to ensure that a resource
             is cleaned when the code that uses it finishes running; even if
             exceptions are thrown.

             Anyway.

             Let's get to it. I had a chance to let myself recover today so my
             mind is relatively fresh at this point. Though I think they noticed
             at the last minute that I was using it as recovery time. Heh. A
             little late to try and recover though.

             We have already given our word. We gave them borders and they chose
             to not respect them. Not our problem by any stretch of the word; we
             are done. Entirely done with their shit.

             (ono)

             On the upside, we're almost done with the first week and it's only
             been two days! Rather exciting. It's like I'm gorging myself on a
             veritable feast. Just gotta make sure not to puke this time. But
             I know she's cheering for me too so I can go rather far.

             'Come get some.'

             10 points if you know where that's from.

             (>*n*)> =3

             """))

print("\n"); print("-" * 20)
print("Day 40:" + "\n" + "-" * 20)
print(dedent("""
             'There are two types of people who will tell you that you cannot
             make a difference in this world: those who are afraid to try and
             those who are afraid you will succeed.' - Ray Goforth

             Continuing with that machine learning course. More or less put the
             programming interview questions on hold. Since, it's much more
             sensible for us to focus on being the mathematician than we are,
             and honing that to the highest capability. we'll do SAS over the
             weekend or on Monday or something like that.

             On the other hand, she did mention that she'd be going to part time
             in about a month. we're not certain that has anything to do with us
             but we're also not certain that it doesn't. Although, we do wonder
             if she's getting tired of being our leash and is simply waiting on
             me to do something amazing instead. Shit, we're waiting on us to do
             something amazing too, haha.

             Although, we gotta say, gradient descent's level of cool is highly
             unexpected and polynomial regression seems to have much more grave
             consequences, if used incorrectly, than we first assumed that it
             would.

             BIOBOOST!!

             (>*n*)> c~=D
             """))

print("\n"); print("-" * 20)
print("Day 41:" + "\n" + "-" * 20)
print(dedent("""
             So, today perhaps they finally realized that we no longer give a
             shit about them and their...what did he call it? Politics? We act
             for our own purposes and our own benefit. Since we cannot yet be 100%
             certain about her and we have little to no allies, then we will
             continue to operate in solitude. If we must go alone, then that will
             be no different that it's always been.

             We love her. Yes, we do. But we cannot burden her. We will make it
             so that she may join us with free will and be our leash no more.
             After all, she must be tired and we have much ground to cover.

             Fuck. Fell asleep while studying and now we have ink in strange
             places.

             (>*n*)> c~==D
             """))

print("\n"); print("-" * 20)
print("Day 42:" + "\n" + "-" * 20)
print(dedent("""
             Today is a special day.

             Read/watch Hitchhiker's Guide to the Galaxy.
             Definitely movie night.

             ...wow that was terrible. Well, at least now I know where I stand.
             And now I know what to improve. And now I have a method to improve.

             So, finishing up the second week. Two weeks of work done in five
             days. I think I'm beating my own record here.

             (>*n*)> c~===D
             """))

print("\n"); print("-" * 20)
print("Day 44:" + "\n" + "-" * 20)
print(dedent("""
             So, today, started doing the stuff on gradient descent, aka, linear
             regression. Pretty cool except the stupid thing doesn't work for
             a portion of the results. Like, expected_theta0 < theta0 and
             expected_theta1 > theta1. Not even sure what to make of that.
             I skipped day 43 since it was a lunar eclpise.

             Plus, I'm not sure if she's trying to discourage me or encourage
             me. Either way, for my own sake, I have to keep going. Why for my
             own sake? I've more or less accepted that I'm currently living in
             a world of empty promises and the only one who can give me what
             I want is myself. So if I don't do it for me then it's probably not
             going to get done.

             But, I'm sure she cherishes me at the very least. Even if 'love' is
             not the word to be used to describe it. I feel the same way,
             however, since I seem to interpret these things (emotions) with
             much less attachment, and more of an understanding of 'that is
             simply how I feel', maybe that makes me either a cold person or
             emphasizes my broken-ness. But I'm fine with it since science, math
             and logic are not things which will give way easily for rose
             coloured things.

             (>*n*)> c~====D
             """))

print("\n"); print("-" * 20)
print("Day 46:" + "\n" + "-" * 20)
print(dedent("""
             Yesterday and today. Stuck on the same problem. BUT we think we may
             have found something that works. In either case, these bitches are
             now growing even more greedy and think that we really give a shit.
             Like we said, they had their chances and they fucked them all up.
             we gave warnings that none of them listened to. So anything else is
             really not my problem.

             We did not lie to them at any point and all they could respond with
             was lies and threats. We did mention that we did not respond well
             to lies and threats. Still they continued. We've lost interest in
             their game. We've lost interest in the empty promises they have
             to offer. We've lost interest in them. Much like a losing interest
             in a diseased relationship. Pity, it could have been fun.

             Not like they aren't a walking mass of problems to which there are
             probably simple solutions. Yes, we remember that simple and easy
             are not synonymous.

             Either way, upward and onward. She will come if she wants to.
             We still love her but we will free her from being our leash.

             (>*n*)> c~=====D
             """))

print("\n"); print("-" * 20)
print("Day 47:" + "\n" + "-" * 20)
print(dedent("""
             Maybe now they'll finally leave me alone. Maybe now the truth is
             finally out in the open; stupid fucker like to push people. Push me
             one more mother fucking time.

             I may very well end up alone at this rate. But that's okay; nothing
             new in that regard since I'm used to have few to no allies.

             However, if we are her beast and she our tamer then we will fly
             higher than even Icarus could imagine.

             Well, time to get some food and make some progress.
             UPWARD AND ONWARD!!

             On a high note, WEEK 2 FINALLY FINISHED. Omg. That was AWESOME.
             And I know she's encouraging me, even silently. We will soar.

             Upward and mother fucking onward.

             (>*n*)> c~======D
             """))

print("\n"); print("-" * 20)
print("Day 48:" + "\n" + "-" * 20)
print(dedent("""
             Yeah. Three legged dogs. Three legged dogs. Three legged dogs.
             Three legged dogs. Three legged dogs. Three legged dogs. FUCKING
             THREE LEGGED DOGS.

             Still haven’t gotten the original gradient descent to work properly
             yet. Kind of feel like my values for theta are being updated much
             too soon; normalization did squat.

             Oh well, got a quiz done so at least it wasn't a complete loss.

             (>*n*)> c~=======D
             """))

print("\n"); print("-" * 20)
print("Day 49:" + "\n" + "-" * 20)
print(dedent("""
             So, today shit basically reached a head. But that's fine. I no
             don't particularly care; I decided to make a running log of events.

             Aside from that, the connection has particularly suspicious
             behaviour given a certain condition. I am interested in this since
             it seems as though it means I shouldn't trust her either. Which is
             highly ironic considering I was considering her to be the only
             person I could trust. Sad, really. Oh well, at least now I know what
             that phrase meant.

             On the other hand, I won't turn on her or anything like that. It's
             just highly strange that that's a condition. Oh well, whatever.
             Nothing has changed and it's unlikely that anything will change.

             Reworked my first assignment today. Still no progress since I don't
             know where the error lies and don't have anyone to bounce the idea
             off of. Though I suppose this is good practice for graduate programs
             since I'd only have minor assistance at best there.

             (>*n*)> c~========D
             """))

print("\n"); print("-" * 20)
print("Day 50:" + "\n" + "-" * 20)
print(dedent("""
             If all goes according to plan, then this should be over soon enough.
             I'm probably going to be alone at the end of everything but... we
             really don't see how that's any different than now. But whatever.
             Still sounds like a whole lot of not our problem.

             Observably, there are at least a few names of people who are
             suspects and are explicitly not being mentioned for personal
             reasons.

             That being said, we do not believe that she is someone to be
             trusted. Not with any of our actual secrets anyway. Our fears, our
             doubts; she has all but explicitly said that she will tell
             everyone. The only one we can trust is us. Yes.

             (>*n*)> c~=========D
             """))

print("\n"); print("-" * 20)
print("Day 50:" + "\n" + "-" * 20)
print(dedent("""
             Somehow, we do not think she is our ally.

             (>*n*)> c~=========D
             """))




print(dedent(f"""
              Easy: {intProb.count("easy")}
              Medium: {intProb.count("medium")}
              Hard: {intProb.count("hard")}

              That's {len(intProb)} exercises completed so far.
              Given an increasing number of days, {round(len(intProb)/float(bang.days), 2)} per day?
              """))
print(f"\n \t {banger} ")
print("END.")

print("Become a 1337 C0|)3R \n \n \n")
# webbrowser.open("https://leetcode.com/")
