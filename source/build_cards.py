# Builds the two Academi emails as a narrow centred card (phone-width, like Kit's own system emails).
# All text is dark on light so nothing disappears in mail apps that drop background colours.
#   speaker-confirmation-template.html  -> Gmail, sent by the speaker pipeline ({{tokens}} filled per speaker)
#   webinar-confirmation-card.html      -> Kit sequence 2933081 email, as one HTML block (Liquid for first name)
import os
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = 'https://raw.githubusercontent.com/conor500/sports-forum-assets/main/email/academi/'
BLUE, INK, BODY, MUTED, LINE, OUTER = '#2B4BD8', '#141414', '#3A3732', '#8C867C', '#E4DFD6', '#F0EEE9'
WA = 'https://chat.whatsapp.com/BKzWZgolWF00YniMUyg0I1'
F = 'font-family:Helvetica,Arial,sans-serif;'


def kicker(s):
    return f'<div style="{F}font-size:11px;font-weight:bold;letter-spacing:2px;color:{BLUE};">{s}</div>'


def h1(s):
    return f'<div style="{F}font-size:30px;line-height:1.08;font-weight:900;color:{INK};letter-spacing:-0.5px;padding-top:8px;">{s}</div>'


def h2(s):
    return f'<div style="{F}font-size:22px;line-height:1.15;font-weight:900;color:{INK};padding-top:6px;">{s}</div>'


def para(s, size=15, color=BODY, top=10):
    return f'<div style="{F}font-size:{size}px;line-height:1.55;color:{color};padding-top:{top}px;">{s}</div>'


def quote(s, top=8):
    return f'<div style="{F}font-size:15px;line-height:1.55;color:{INK};border-left:3px solid {BLUE};padding:2px 0 2px 12px;margin-top:{top}px;">{s}</div>'


def label(s, top=14):
    return f'<div style="{F}font-size:10px;font-weight:bold;letter-spacing:1.5px;color:{MUTED};padding-top:{top}px;">{s}</div>'


def button(text, href, color=BLUE, top=16):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:{top}px;"><tr>'
            f'<td align="center" style="border:2px solid {color};border-radius:6px;"><a href="{href}" style="{F}display:block;padding:13px 10px;font-size:15px;font-weight:bold;color:{color};text-decoration:none;">{text}</a></td>'
            '</tr></table>')


def button_grid(items):
    cells = [f'<td width="50%" style="padding:{p}"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px solid {INK};border-radius:6px;"><a href="{h}" style="{F}display:block;padding:11px 6px;font-size:14px;font-weight:bold;color:{INK};text-decoration:none;">{t}</a></td></tr></table></td>'
             for (t, h), p in zip(items, ['0 4px 8px 0;', '0 0 8px 4px;', '0 4px 0 0;', '0 0 0 4px;'])]
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:14px;"><tr>{cells[0]}{cells[1]}</tr><tr>{cells[2]}{cells[3]}</tr></table>'


def when_where(when):
    cell = lambda k, v, pad: f'<td width="50%" valign="top" style="padding:{pad}">{label(k, 0)}<div style="{F}font-size:15px;font-weight:bold;color:{INK};padding-top:3px;">{v}</div></td>'
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:14px;"><tr>'
            f'{cell("WHEN", when, "0 6px 0 0;")}{cell("WHERE", "Google Meet, 45 min + Q&amp;A", "0 0 0 6px;")}</tr></table>')


def img(src, alt, href=None, top=14):
    i = f'<img src="{src}" width="424" alt="{alt}" style="display:block;width:100%;max-width:424px;height:auto;border:0;border-radius:6px;">'
    if href:
        i = f'<a href="{href}">{i}</a>'
    return f'<div style="padding-top:{top}px;">{i}</div>'


def section(inner, first=False):
    border = '' if first else f'border-top:1px solid {LINE};'
    return f'<tr><td style="{border}padding:24px 28px;">{inner}</td></tr>'


def checklist(items):
    rows = ''.join(f'<tr><td width="28" valign="top" style="{F}font-size:14px;font-weight:900;color:{BLUE};padding:5px 0;">{n:02d}</td><td style="{F}font-size:15px;line-height:1.45;color:{INK};padding:5px 0;">{t}</td></tr>' for n, t in enumerate(items, 1))
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;">{rows}</table>'


def card(sections, preheader, footer, logo=('logo-academi-sports-v1.png', 'Sports Academi', 150),
         tagline='Sports Academi &middot; a free community for athletes, coaches and practitioners', powered_by=False):
    """The shared shell: light outer background, white 480px card, logo on top, sign-off under the card."""
    pre = f'<div style="display:none;max-height:0;overflow:hidden;">{preheader}</div>' if preheader else ''
    return (pre +
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{OUTER}" style="background-color:{OUTER};"><tr><td align="center" style="padding:28px 12px;">'
            f'<table role="presentation" width="480" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="width:100%;max-width:480px;background-color:#FFFFFF;border:1px solid {LINE};border-radius:8px;">'
            f'<tr><td align="center" style="padding:28px 28px 4px;"><img src="{RAW}{logo[0]}" width="{logo[2]}" alt="{logo[1]}" style="display:block;width:{logo[2]}px;height:auto;border:0;"></td></tr>'
            + ''.join(sections) +
            f'<tr><td style="border-top:1px solid {LINE};padding:22px 28px 26px;{F}font-size:15px;line-height:1.55;color:{BODY};">{footer}</td></tr>'
            '</table>'
            + (f'<img src="{RAW}powered-by-academi-v1.png" width="90" alt="Powered by Academi" style="display:block;width:90px;height:auto;border:0;margin:18px auto 0;">' if powered_by else '') +
            f'<div style="{F}font-size:11px;color:{MUTED};padding-top:14px;">{tagline}</div>'
            '</td></tr></table>')


def coming_soon(src):
    return section(kicker('COMING SOON') + h2('host your own academi')
                   + para("We're building an app where you can host your own Academi, earn from what you know, and run your coaching, mentoring or consulting business in one place. Early waitlist members get first access.")
                   + f'<div style="padding-top:12px;"><a href="https://tally.so/r/2jEkpg?source={src}" style="{F}font-size:16px;font-weight:bold;color:{BLUE};">Join the early waitlist &rarr;</a></div>')


# ---------- speaker confirmation (Gmail) ----------
speaker = card([
    section(kicker("YOU'RE ON") + h1("you're speaking at sports academi!")
            + para('Thanks for jumping onboard, {{speaker_first}}. Everything you need is below, including a promo pack you can post in one tap.', 16), first=True),
    section(kicker('YOUR SESSION') + h2('{{talk_title}}') + when_where('{{date_long}}, 7pm UK/Irish')
            + button('Open your Google Meet link &rarr;', '{{meet_link}}')
            + para('It\'s in your calendar invite too. Your personal registration link, for anyone you want in the room:<br>'
                   f'<a href="{{{{register_link}}}}" style="color:{BLUE};font-weight:bold;word-break:break-all;">{{{{register_link_display}}}}</a>', 14, top=12)),
    section(kicker('YOUR PROMO PACK') + h2('ready to post. one tap each.')
            + para('Tap a button and the file downloads straight to your phone or laptop.')
            + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:14px;"><tr>'
              f'<td width="58%" valign="top" style="padding-right:6px;"><a href="{{{{poster_png}}}}"><img src="{{{{poster_thumb}}}}" width="240" alt="Your 4:5 poster" style="display:block;width:100%;height:auto;border:1px solid {LINE};border-radius:4px;"></a></td>'
              f'<td width="42%" valign="top" style="padding-left:6px;"><a href="{{{{story_png}}}}"><img src="{{{{story_thumb}}}}" width="170" alt="Your 9:16 story" style="display:block;width:100%;height:auto;border:1px solid {LINE};border-radius:4px;"></a></td>'
              '</tr></table>'
            + button_grid([('Poster &middot; PNG', '{{poster_png}}'), ('Carousel &middot; PDF', '{{carousel_pdf}}'),
                           ('Story &middot; PNG', '{{story_png}}'), ('QR code &middot; PNG', '{{qr_png}}')])
            + para('Post the carousel as a LinkedIn document, the poster on your feed, and the story on Instagram with your link sticker.', 13, MUTED, 12)),
    section(kicker('CAPTIONS TO COPY') + label('LINKEDIN') + quote('{{caption_linkedin}}')
            + label('INSTAGRAM') + quote('{{caption_instagram}}') + label('X') + quote('{{caption_x}}')),
    section(kicker('BEFORE THE NIGHT') + h2('make sure you join the community')
            + para("It's free, it's on WhatsApp, and it's where athletes, coaches and practitioners will hear about your session first. Say hello and drop this in the group:")
            + quote('{{whatsapp_message}}', 12) + button('Join the free community &rarr;', WA)),
    section(kicker('ON THE DAY') + checklist(['Test your Meet link a day or two before.', 'Keep it to 15 to 20 slides.',
                                              'Leave 10 minutes for Q&amp;A.', 'Join 10 minutes early so we can say hello.'])),
    coming_soon('speaker-confirmation'),
], "You're on for {{date_long}}. Your Meet link, your registration link and your promo pack, ready to post.",
    f"Any questions, just reply to this email.<br><br>Can't wait to hear you on the {{{{date_ordinal}}}},<br><strong style=\"color:{INK};\">Conor</strong>")

with open(os.path.join(HERE, 'speaker-confirmation-template.html'), 'w') as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="color-scheme" content="light only">\n<meta name="supported-color-schemes" content="light only">\n'
            "<title>You're speaking at Sports Academi</title>\n</head>\n"
            f'<body style="margin:0;padding:0;background-color:{OUTER};" bgcolor="{OUTER}">\n' + speaker + '\n</body>\n</html>\n')

# ---------- webinar registrant confirmation (Kit) ----------
kit = card([
    section(img(RAW + 'welcome-hero-v1.png', 'Sports Academi free webinar. Thanks for jumping onboard! Your seat is saved.', top=0)
            + para('Hey {{ subscriber.first_name | default: "there" }},', 16, top=18)
            + para("<strong style=\"color:%s;\">Thanks for jumping onboard!</strong> Your seat is saved, and I'm buzzing to have you in the room. Here's everything you need for the night." % INK, 16), first=True),
    section(kicker('YOUR SESSION')
            + img(RAW + 'ticket-generic-v1.png', 'Your seat: Sports Academi free live webinar. Thursday, 7pm UK and Irish time, on Google Meet. 45 minute talk plus live Q&amp;A.', top=10)
            + when_where('Thursday, 7pm UK/Irish')
            + para(f'<strong style="color:{INK};">Your Google Meet link is coming in a calendar invite.</strong> Accept it and it sits in your calendar with a reminder. If it\'s not in your inbox, check junk and mark it as not junk.', top=14)
            + para("Can't make it live? Stay registered. Everyone who signs up gets the replay.")
            + para(f'<strong style="color:{INK};">Save your ticket:</strong> <a href="{RAW}ticket-generic-v1.pdf" style="color:{BLUE};font-weight:bold;">PDF</a> &middot; <a href="{RAW}ticket-generic-v1.png" style="color:{BLUE};font-weight:bold;">PNG</a>')),
    section(kicker('BEFORE THE NIGHT') + h2('make sure you join the community')
            + para("It's free, it's on WhatsApp, and it's where athletes, coaches and practitioners talk sport, careers and going independent. Drop your questions for the session in there before the night, and you'll hear about every future webinar first.")
            + button('Join the free community &rarr;', WA)),
    coming_soon('webinar-confirmation'),
], '',  # Kit sets its own preview text
    f'See you on the night,<br><strong style="color:{INK};">Conor</strong>')

with open(os.path.join(HERE, 'webinar-confirmation-card.html'), 'w') as f:
    f.write(kit + '\n')
print('ok')
