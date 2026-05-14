import random
from mimesis import Person, Text, Address, Datetime, Internet
from mimesis.locales import Locale

person = Person(Locale.EN)
text = Text(Locale.EN)
address = Address(Locale.EN)
dt = Datetime()
internet = Internet()


def generate_scenario():
    """
    Generate a random scenario story.

    Returns:
        str: A random scenario description.
    """
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
    """
    Generate a random dialogue between two people.

    Returns:
        str: A dialogue string.
    """
    name1 = person.first_name()
    name2 = person.first_name()
    return f"""{name1}: {text.quote()}
{name2}: {text.quote()}"""


def generate_event_log(n=5):
    """
    Generate a list of random event logs.

    Args:
        n (int): Number of log entries to generate. Default is 5.

    Returns:
        str: A string of log entries separated by newlines.
    """
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


def generate_user_profile():
    """
    Generate a random user profile.

    Returns:
        dict: A dictionary containing user profile information.
    """
    return {
        "name": person.full_name(),
        "email": person.email(),
        "address": address.address(),
        "phone": person.phone_number(),
        "birthdate": person.birthdate().strftime("%Y-%m-%d"),
        "occupation": person.occupation()
    }


def generate_blog_post():
    """
    Generate a random blog post.

    Returns:
        dict: A dictionary with title and content of the blog post.
    """
    title = text.title()
    content = text.text(quantity=3)  # Generate 3 paragraphs
    return {
        "title": title,
        "content": content
    }


def generate_comment():
    """
    Generate a random comment.

    Returns:
        str: A random comment text.
    """
    author = person.first_name()
    comment = text.sentence()
    return f"{author}: {comment}"


def generate_web_event():
    """
    Generate a random web event log.

    Returns:
        str: A web event description.
    """
    ip = internet.ip_v4()
    user_agent = internet.user_agent()
    page = random.choice(["/home", "/about", "/contact", "/blog"])
    timestamp = dt.datetime().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - IP: {ip} accessed {page} with User-Agent: {user_agent}"
