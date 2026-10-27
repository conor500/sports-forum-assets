# The three opt-in funnels, each with its own Kit sequence, in the same 480px card as the welcome sequence.
#   A2  academi waitlist   (Tally 2jEkpg)          -> funnel-a-<n>.html
#   B2  gap analysis audit (Lovable app)           -> funnel-b-<n>.html
#   C2  The Arc podcast    (Tally podcast form)    -> funnel-c-<n>.html
# Kit delays are days after the previous email. funnels.json holds subject, preview, delay and html for each.
import json
import os
from build_cards import (HERE, BLUE, INK, WA, F, kicker, h1, h2, para, quote, label, button, section, checklist, card)
from build_welcome import FIRST, ADVICE

SIGN = 'Conor<br><span style="color:#8C867C;font-size:13px;">Founder, Academi</span>'
CALL = 'https://calendly.com/conor-academi/30min'
AUDIT = 'AUDIT_URL'  # live gap analysis URL, still to come from Conor
WAITLIST = 'https://tally.so/r/2jEkpg?source='
A_SHELL = dict(logo=('logo-academi-v1.png', 'Academi', 130), tagline='Academi &middot; host your own academi', powered_by=False)
SA_SHELL = dict(powered_by=True)


def cape_town(src):
    """The Cape Town trip, worded only from Conor's own facts (27 Oct 2026)."""
    return [
        section(kicker('CAPE TOWN &middot; 1 TO 5 MARCH') + h1('come to south africa with us.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("If you're an ex-athlete who wants to go independent as a coach, mentor or consultant, and you need help working out how, you should consider joining our <strong style=\"color:%s;\">free South Africa trip</strong>." % INK, 16)
                + para("It's also a chance to get the training partner community back. We'll train together, run workshops, do activities during the day, and have a class holiday while we're out there.", 16), first=True),
        section(kicker('THE DETAILS')
                + checklist(['<strong>When:</strong> 1st to 5th March',
                             '<strong>Where:</strong> 39 Libert&eacute;, Stellenbosch, Western Cape 7600, South Africa',
                             '<strong>Who:</strong> ex-athletes who want to go independent',
                             '<strong>What:</strong> training, workshops, daytime activities and a class holiday'])
                + para('Register your interest by booking a call in with me. We\'ll talk about where you are and whether the trip is right for you.', top=14)
                + button('Book a call with Conor &rarr;', f'{CALL}?utm_source={src}', top=16)),
    ]


A, B, C = [], [], []

# ---------------- A2: academi waitlist ----------------
A.append(dict(
    subject="You're on the Academi waitlist",
    preview="You'll be first in when we open. Here's what we're building.",
    delay=0,
    html=card([
        section(kicker("YOU'RE ON THE LIST") + h1("you're on the waitlist.")
                + para(f'Hey {FIRST},', 16, top=14)
                + para("Thanks for joining the Academi waitlist. We're building an app where you can host your own Academi, earn from what you know, and run your coaching, mentoring or consulting business in one place.", 16)
                + para('Your programmes, your clients, your check-ins and your payments, together instead of spread across messages, PDFs and spreadsheets. Waitlist members get first access, and help shape what we build.', 16), first=True),
        section(kicker('ONE QUICK QUESTION') + h2('what would your academi teach?')
                + para("Hit reply and tell me in a line or two: your sport, and what you'd want to teach or coach. I read every reply, and it shapes what we build first.")),
        section(kicker('IN THE MEANTIME') + h2('join the free community')
                + para("Sports Academi is our free WhatsApp community for athletes, coaches and practitioners, talking sport, careers and going independent.")
                + button('Join the WhatsApp community &rarr;', WA)),
    ], '', SIGN, **A_SHELL)))

A.append(dict(
    subject='A free trip to South Africa for athletes going independent',
    preview='1 to 5 March in Stellenbosch: train, workshops, activities and a class holiday.',
    delay=2,
    html=card(cape_town('funnel-a'), '', SIGN, **A_SHELL)))

A.append(dict(
    subject='Where is your coaching business right now?',
    preview='9 quick questions, under 2 minutes, and a free score.',
    delay=2,
    html=card([
        section(kicker('FREE GAP ANALYSIS') + h1('find the gaps in your coaching business.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para('Before you host your own Academi, it helps to know where you stand. Our free gap analysis is 9 quick questions, takes under 2 minutes, and gives you a score plus the one gap to fix first.', 16)
                + checklist([f'<strong>{a}</strong>' for a in ADVICE])
                + button('Start my free analysis &rarr;', f'{AUDIT}?utm_source=funnel-a', top=18), first=True),
    ], '', SIGN, **A_SHELL)))

A.append(dict(
    subject='Learn from people who made the jump',
    preview='The Arc: conversations with athletes who went independent.',
    delay=3,
    html=card([
        section(kicker('THE ARC') + h1('learn from people who made the jump.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("The Arc is our podcast about the move from athlete to coach. Every episode is a conversation with someone who made that jump, or who helps athletes make it.", 16)
                + para("We talk about the stuff nobody tells you: landing your first clients, what to charge, building a name while you're still playing, and the admin that eats your week.", 16), first=True),
        section(kicker('STILL THINKING ABOUT CAPE TOWN?') + h2('book a call')
                + para('Spaces on the South Africa trip (1 to 5 March, Stellenbosch) start with a call. Book one and we\'ll talk it through.')
                + button('Book a call with Conor &rarr;', f'{CALL}?utm_source=funnel-a')),
    ], '', SIGN, **A_SHELL)))

# ---------------- B2: gap analysis audit ----------------
gap_rows = ''.join(
    f'{{% {"if" if i == 0 else "elsif"} subscriber.biggest_gap == "{area}" %}}{quote(text, 10)}'
    for i, (area, text) in enumerate(ADVICE.items())) + '{% endif %}'
B.append(dict(
    subject='Your gap analysis results',
    preview='Your score, your biggest gap, and one thing to do this week.',
    delay=0,
    html=card([
        section('{% if subscriber.gap_tier != blank %}'
                + kicker('YOUR GAP ANALYSIS') + h1('{{ subscriber.gap_tier | downcase }}.')
                + para(f'Hey {FIRST}, thanks for taking the gap analysis. You scored <strong style="color:{INK};">{{{{ subscriber.gap_score }}}}%</strong>, and your biggest gap right now is <strong style="color:{INK};">{{{{ subscriber.biggest_gap }}}}</strong>.', 16, top=14)
                + label('YOUR NEXT STEP', 18) + gap_rows
                + para("Pick that one thing and do it this week. Small and done beats big and planned.")
                + '{% else %}'
                + kicker('YOUR GAP ANALYSIS') + h1('thanks for taking it.')
                + para(f'Hey {FIRST}, thanks for taking the gap analysis. Your results are on the page you finished on.', 16, top=14)
                + '{% endif %}', first=True),
        section(kicker('TALK IT THROUGH') + h2('join the free community')
                + para("Sports Academi is a free WhatsApp community for athletes, coaches and practitioners. Post your biggest gap in there. Someone has already solved it.")
                + button('Join the WhatsApp community &rarr;', WA)),
    ], '', SIGN, **SA_SHELL)))

B.append(dict(
    subject='The five gaps, and the order to fix them',
    preview='Offer, audience, clients, systems, income.',
    delay=2,
    html=card([
        section(kicker('FIVE AREAS') + h1('where coaching businesses get stuck.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para('The gap analysis looks at five areas. Once your biggest gap is moving, here is what to do this week in each of the others:', 16)
                + ''.join(label(a.upper(), 14) + para(t, 15, top=4) for a, t in ADVICE.items()), first=True),
        section(kicker('ONE QUICK FAVOUR') + h2("reply and tell me which one you're fixing")
                + para('One line is plenty. I read every reply.')),
    ], '', SIGN, **SA_SHELL)))

B.append(dict(
    subject='A free trip to South Africa for athletes going independent',
    preview='1 to 5 March in Stellenbosch: train, workshops, activities and a class holiday.',
    delay=2,
    html=card(cape_town('funnel-b'), '', SIGN, **SA_SHELL)))

B.append(dict(
    subject='Want to host your own Academi?',
    preview="We're building the place to run your coaching business. Early access is open.",
    delay=3,
    html=card([
        section(kicker('COMING SOON') + h1('host your own academi.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("Most of the gaps in the analysis come down to the same thing: your coaching business is spread across messages, PDFs and spreadsheets.", 16)
                + para("We're building an app where you can host your own Academi, earn from what you know, and run your coaching, mentoring or consulting business in one place.", 16)
                + button('Join the early waitlist &rarr;', WAITLIST + 'funnel-b', top=18)
                + para('Early waitlist members get first access, and help shape what we build.', 14, top=12), first=True),
        section(kicker('THE ARC') + h2('hear from people who made the jump')
                + para("The Arc is our podcast about the move from athlete to coach. Hit reply with one question you'd ask a guest who went independent.")),
    ], '', SIGN, **SA_SHELL)))

# ---------------- C2: The Arc podcast ----------------
C.append(dict(
    subject="You're in: welcome to The Arc",
    preview='Conversations about the move from athlete to coach.',
    delay=0,
    html=card([
        section(kicker('THE ARC') + h1('welcome to the arc.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("Thanks for signing up. The Arc is our podcast about the move from athlete to coach. Every episode is a conversation with someone who made that jump, or who helps athletes make it: players turned coaches, physios, S&amp;C coaches, sports psychologists.", 16)
                + para("We talk about the stuff nobody tells you: landing your first clients, what to charge, building a name while you're still playing, and the admin that eats your week.", 16), first=True),
        section(kicker('YOUR QUESTION') + h2('ask our guests anything')
                + '{% if subscriber.podcast_question != blank %}'
                + para('You sent us this one:') + quote('{{ subscriber.podcast_question }}', 10)
                + para("It's on the list. The best questions go straight to our guests, and we credit you on the episode.")
                + '{% else %}'
                + para("If you could sit down with a pro who went independent, what would you ask? Hit reply with one question. The best ones go straight to our guests, and we credit you on the episode.")
                + '{% endif %}'),
    ], '', SIGN, **SA_SHELL)))

C.append(dict(
    subject='Hear about every episode first',
    preview='Join the free community: athletes, coaches and practitioners.',
    delay=2,
    html=card([
        section(kicker('THE COMMUNITY') + h1('hear about every episode first.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("Sports Academi is our free WhatsApp community for athletes, coaches and practitioners, talking sport, careers and going independent. Members hear about each episode of The Arc first, the night before it goes public.", 16)
                + button('Join the WhatsApp community &rarr;', WA, top=18), first=True),
        section(kicker('FREE WEBINARS') + h2('every other thursday, 7pm')
                + para('Every other Thursday at 7pm UK/Irish time, someone who has done it shares what they learned, live on Google Meet with Q&amp;A. They are free, and announced in the community first.')),
    ], '', SIGN, **SA_SHELL)))

C.append(dict(
    subject='Where is your coaching business right now?',
    preview='9 quick questions, under 2 minutes, and a free score.',
    delay=2,
    html=card([
        section(kicker('FREE GAP ANALYSIS') + h1('find the gaps in your coaching business.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para('The guests on The Arc all hit the same five gaps when they went independent. Our free gap analysis is 9 quick questions, takes under 2 minutes, and shows you which one is yours.', 16)
                + checklist([f'<strong>{a}</strong>' for a in ADVICE])
                + button('Start my free analysis &rarr;', f'{AUDIT}?utm_source=funnel-c', top=18), first=True),
    ], '', SIGN, **SA_SHELL)))

C.append(dict(
    subject='Want to host your own Academi?',
    preview="We're building the place to run your coaching business. Early access is open.",
    delay=3,
    html=card([
        section(kicker('COMING SOON') + h1('host your own academi.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("We're building an app where you can host your own Academi, earn from what you know, and run your coaching, mentoring or consulting business in one place.", 16)
                + button('Join the early waitlist &rarr;', WAITLIST + 'funnel-c', top=18)
                + para('Early waitlist members get first access, and help shape what we build.', 14, top=12), first=True),
    ], '', SIGN, **SA_SHELL)))

out = {}
for key, emails in (('a', A), ('b', B), ('c', C)):
    for n, e in enumerate(emails, 1):
        with open(os.path.join(HERE, f'funnel-{key}-{n}.html'), 'w') as f:
            f.write(e['html'] + '\n')
    out[key] = emails
json.dump(out, open(os.path.join(HERE, 'funnels.json'), 'w'), indent=1)
print({k: len(v) for k, v in out.items()})
