# Kit sequence 2933048 "Welcome: Sports Academi new member", in the same 480px card as the webinar confirmation.
# Five emails across five days: 0, 1, 2, 3, 5 (Kit delays are days after the previous email).
# Writes welcome-<n>.html (one Kit HTML block each, Liquid for names and gap-analysis fields).
import os
from build_cards import (HERE, BLUE, INK, WA, F, kicker, h1, h2, para, quote, label, button, section, checklist, card)

FIRST = '{{ subscriber.first_name | default: "there" }}'
SIGN = f'Conor<br><span style="color:#8C867C;font-size:13px;">Founder, Sports Academi</span>'
WAITLIST = 'https://tally.so/r/2jEkpg?source=welcome-sequence'
# Same advice the gap analysis shows on its results page (src/lib/quiz.ts in the Lovable app).
ADVICE = {
    'Offer': 'Package what you do into a named programme with a fixed price. This week: write your offer in one sentence and price it.',
    'Audience': 'Your expertise needs to be seen. This week: post 3 times showing how you coach.',
    'Clients': 'Word of mouth caps your growth. This week: start an email list or community you can reach directly.',
    'Systems': 'Scattered tools eat your coaching time. This week: list every manual task and pick one to automate.',
    'Income': 'Chasing payments costs you money. This week: move one client onto a recurring payment.',
}

EMAILS = []

# 1. Day 0: the invite
EMAILS.append(dict(
    subject="You're in: your Sports Academi invite",
    preview="Your WhatsApp link is inside, plus how the group works.",
    delay=0,
    html=card([
        section(kicker('WELCOME') + h1('welcome to sports academi.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para('Thanks for joining. Sports Academi is a free community for athletes, coaches and practitioners: people talking sport, careers and what it takes to go independent.', 16)
                + button('Join the WhatsApp community &rarr;', WA, top=18), first=True),
        section(kicker('HOW THE GROUP WORKS') + checklist([
            '<strong>Announcements:</strong> new episodes, webinars and anything important. Only we post here.',
            '<strong>General chat:</strong> questions, wins, hot takes. Be useful, be kind.',
            '<strong>Webinars:</strong> links and replays for our free sessions every other Thursday.'])
                + para("No selling or spam in the group, please. If you want to share something you've made, ask first.", 14)),
        section(kicker('ONE QUICK FAVOUR') + h2("reply and tell me what you're working on")
                + para("Your sport, and the one thing you're working on right now. I read every reply.")),
    ], '', SIGN)))

# 2. Day 1: gap analysis follow-up (personalised if they took it, a short primer if not)
gap_rows = ''.join(
    f'{{% {"if" if i == 0 else "elsif"} subscriber.biggest_gap == "{area}" %}}{quote(text, 10)}'
    for i, (area, text) in enumerate(ADVICE.items())) + '{% endif %}'
EMAILS.append(dict(
    subject='Your biggest gap, and one thing to do this week',
    preview='The one change that moves your coaching business forward fastest.',
    delay=1,
    html=card([
        section('{% if subscriber.gap_tier != blank %}'
                + kicker('YOUR GAP ANALYSIS') + h1('{{ subscriber.gap_tier | downcase }}.')
                + para(f'Hey {FIRST}, you scored <strong style="color:{INK};">{{{{ subscriber.gap_score }}}}%</strong>. Your biggest gap right now is <strong style="color:{INK};">{{{{ subscriber.biggest_gap }}}}</strong>.', 16, top=14)
                + label('YOUR NEXT STEP', 18) + gap_rows
                + para("Pick that one thing and do it this week. Small and done beats big and planned.")
                + '{% else %}'
                + kicker('FIVE AREAS') + h1('where coaching businesses get stuck.')
                + para(f'Hey {FIRST}, when athletes and coaches go independent, the same five gaps come up again and again:', 16, top=14)
                + checklist([f'<strong>{a}.</strong> {t.split(" This week")[0]}' for a, t in ADVICE.items()])
                + para('Which one is yours? Hit reply and tell me. I read every reply.')
                + '{% endif %}', first=True),
        section(kicker('TALK IT THROUGH') + h2('bring it to the group')
                + para("Post your biggest gap in the WhatsApp community. Someone in there has already solved it.")
                + button('Open the WhatsApp community &rarr;', WA)),
    ], '', SIGN)))

# 3. Day 2: Academi Podcast question
EMAILS.append(dict(
    subject='What would you ask a pro who went independent?',
    preview="We're building The Academi Podcast around your questions.",
    delay=1,
    html=card([
        section(kicker('THE ACADEMI PODCAST') + h1('the academi podcast is coming.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("We're launching The Academi Podcast, a show about the move from athlete to coach. Every episode is a conversation with someone who has made that jump, or who helps athletes make it: players turned coaches, physios, S&amp;C coaches, sports psychologists.", 16)
                + para("We talk about the stuff nobody tells you: landing your first clients, what to charge, building a name while you're still playing, and the admin that eats your week.", 16), first=True),
        section(kicker('HELP US SHAPE IT') + h2('send us one question')
                + para('If you could sit down with a pro who went independent, what would you ask them? Hit reply with one question. The best ones go straight to our guests, and we credit you on the episode.')
                + para('Members of the WhatsApp community hear about each episode first, the night before it goes public.', 14)),
    ], '', SIGN)))

# 4. Day 3: say hello
EMAILS.append(dict(
    subject='Say hello in the group (copy and paste this)',
    preview='A 30-second intro that gets you talking to the right people.',
    delay=1,
    html=card([
        section(kicker('SAY HELLO') + h1('say hello.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para('The people who get the most out of Sports Academi are the ones who introduce themselves early. It takes 30 seconds. Copy this into the general chat and fill in the gaps:', 16)
                + quote("Hi all, I'm [name]. I [play / coach / work in] [sport]. Right now I'm working on [one thing]. I'd love to hear from anyone who has [one thing you want help with].", 14)
                + button('Open the WhatsApp community &rarr;', WA), first=True),
        section(kicker('FREE WEBINARS') + h2('every other thursday, 7pm')
                + para('Every other Thursday at 7pm UK/Irish time, someone who has done it shares what they learned, live on Google Meet with Q&amp;A. They are free, and each one is announced in the Webinars group first.')),
    ], '', f'See you in there,<br>{SIGN}')))

# 5. Day 5: host your own Academi
EMAILS.append(dict(
    subject='Want to host your own Academi?',
    preview="We're building the place to run your coaching business. Early access is open.",
    delay=2,
    html=card([
        section(kicker('COMING SOON') + h1('host your own academi.')
                + para(f'Hey {FIRST},', 16, top=14)
                + para("We're building an app where you can host your own Academi, earn from what you know, and run your coaching, mentoring or consulting business in one place.", 16)
                + para('Your programmes, your clients, your check-ins and your payments, together instead of spread across messages, PDFs and spreadsheets.', 16)
                + button('Join the early waitlist &rarr;', WAITLIST, top=18)
                + para('Early waitlist members get first access, and help shape what we build.', 14, top=12), first=True),
    ], '', SIGN)))

for n, e in enumerate(EMAILS, 1):
    with open(os.path.join(HERE, f'welcome-{n}.html'), 'w') as f:
        f.write(e['html'] + '\n')
import json
json.dump([{k: v for k, v in e.items()} for e in EMAILS], open(os.path.join(HERE, 'welcome-sequence.json'), 'w'), indent=1)
print(len(EMAILS), 'emails')
