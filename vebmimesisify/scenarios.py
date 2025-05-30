import random
from mimesis import Person, Text, Address, Datetime
from mimesis.locales import Locale

person = Person(Locale.EN)
text = Text(Locale.EN)
address = Address(Locale.EN)
dt = Datetime()

def generate_scenario():
    name = person.full_name()
    location = address.city()
    time = dt.datetime().strftime("%Y-%m-%d %H:%M")
    story = random.choice([
        f"At {time}, {name} found themselves in {location} with no memory of how they arrived.",
        f"On a rainy evening in {location}, {name} uncovered a hidden room behind a bookcase.",
        f"{name} received an encrypted letter pointing to a meeting in {location} at {time}.",
        f"Strange events began to unfold when {name} stepped into {location} on {time}."
    ])
    return story

def generate_dialogue():
    name1 = person.first_name()
    name2 = person.first_name()
    return f"""{name1}: {text.quote()}
{name2}: {text.quote()}"""

def generate_event_log(n=5):
    log = []
    for _ in range(n):
        timestamp = dt.datetime().strftime("%Y-%m-%d %H:%M:%S")
        action = random.choice([
            "Accessed secure terminal.",
            "Bypassed security door.",
            "Transmitted encrypted signal.",
            "Detected unknown presence.",
            "Activated emergency protocol."
        ])
        log.append(f"{timestamp} - {action}")
    return "\n".join(log)
