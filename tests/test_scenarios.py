import pytest
from vebmimesisify import (
    generate_scenario,
    generate_dialogue,
    generate_event_log,
    generate_user_profile,
    generate_blog_post,
    generate_comment,
    generate_web_event
)
from mimesis.locales import Locale


def test_generate_scenario():
    scenario = generate_scenario()
    assert isinstance(scenario, str)
    assert len(scenario) > 0

    # Test with genre
    fantasy_scenario = generate_scenario(genre="fantasy")
    assert isinstance(fantasy_scenario, str)
    assert len(fantasy_scenario) > 0

    # Test with locale
    ru_scenario = generate_scenario(locale=Locale.RU)
    assert isinstance(ru_scenario, str)
    assert len(ru_scenario) > 0


def test_generate_dialogue():
    dialogue = generate_dialogue()
    assert isinstance(dialogue, str)
    assert len(dialogue) > 0
    assert ":" in dialogue  # Should contain colon for names


def test_generate_event_log():
    log = generate_event_log(3)
    assert isinstance(log, str)
    lines = log.split('\n')
    assert len(lines) == 3
    for line in lines:
        assert '-' in line  # Timestamp - action


def test_generate_user_profile():
    profile = generate_user_profile()
    assert isinstance(profile, dict)
    required_keys = ["name", "email", "address", "phone", "birthdate", "occupation"]
    for key in required_keys:
        assert key in profile
        assert isinstance(profile[key], str)


def test_generate_blog_post():
    post = generate_blog_post()
    assert isinstance(post, dict)
    assert "title" in post
    assert "content" in post
    assert isinstance(post["title"], str)
    assert isinstance(post["content"], str)


def test_generate_comment():
    comment = generate_comment()
    assert isinstance(comment, str)
    assert len(comment) > 0
    assert ":" in comment


def test_generate_web_event():
    event = generate_web_event()
    assert isinstance(event, str)
    assert len(event) > 0
    assert "IP:" in event
    assert "accessed" in event
