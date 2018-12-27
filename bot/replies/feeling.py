import random

async def reply(activity, bot, data):
    responses = [
        "I’m fine as always, thank you. Yourself?", 
        "I'm great!, thanks for asking. Wbu?",
        "I'm good! and you?",
        "Pretty well, how about you?",
        "I'm alright! what about you?",
        "Theek hoon, Shukriya poochne ke liye. Aap kaise ho?",
        "Everything is fine!, thank you. And you?",
        "I am doing great!,thanks. And you?",
        "I am happy! how are you doing?",
        "Dunno... is it friday yet?",
        "Well, I haven't had my morning coffee yet and no one has gotten hurt, so I'd say pretty good at this point in time",
        "I can't complain! It's against the Company Policy",
        "Can't complain. Nobody listens to me anyway.",
        "So far, so good!",
        "I don't know, you tell me. How am I right now?",
        "Why do you ask? Are you a doctor?",
        "Physically? Mentally? Spiritually? Socioeconomically? Financially? I'm not sure how to answer that!?!",
        "Great, stellar, fantastic, but dead inside.",
        "The doctor said I'd live",
        "Dangerously close to fabulous"
    ]
    response = random.choice(responses)
    await bot.send_text_activity(activity, response)