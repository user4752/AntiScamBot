# AntiScamBot
A discord bot that shares commission scammer ban lists. These things are currently a scourge on our Discord communities. Unfortunately, unless they are banned in all relative servers, they'll hop onto the next
server and then attempt to scam people from there next.

To stop this from happening, we share bans, so that the scammers are unable to contact anyone.

## What is this?
Think of this as a glorified shared ban list with auditing and public logging. This is the source code of said project. It requires a discord server to run. Socks currently hosts an instance
for free that you can use.

## FAQ:
---

### How do I enable it in my server?

Ask Socks for an invite to the control server. You'll then be given the option to add the bot to your server, and then activate it.

### What is a commission scammer?

A commission scammer is someone who plays a confidence game in order to sell you on either AI art, traced/stolen artwork or just takes your money and runs.
They will always solicit you first. Do not give them money.

### Why is the icon of the bot "hey^^"

When these scammers first ran rampant, they would always open their dms with the message "hey^^". It was really easy to tell if someone was fake because of it.

### How does it know who is a commission scammer?

User reports. Vetters go through the user report and then trigger a ban on the user in question if they are a scammer.

### What about abuse?

So currently, this bot requires that someone with a "Trusted" role approves the scammers proposed. If they are approved, the ban will be blasted to all servers that subscribe
to the bot. The name of the person that initiated this action as well as the user that it happened to will be blasted to a subscribable Discord feed, of which you can get
updates as to the going ons.

All bans will be logged into your server's audit log. You can revert any ban if you wish and the bot will not attempt to readd it.

### What about mistakes?

The bot can revert any mistakes and unban someone if this needs to happen. You can also just simply unban the user if you feel like it.