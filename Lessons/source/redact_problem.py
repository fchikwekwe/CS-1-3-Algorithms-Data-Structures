from redact import redact_words
import unittest


class RedactTest(unittest.TestCase):

    def test_redact(self):
        list_with_banned = ["the", "poopy", "house"]
        banned = ["droopy", "random", "poopy"]
        assert redact_words(list_with_banned, banned) == ["the", "house"]

        list_without_banned = ["the", "big", "house"]
        banned = ["droopy", "random", "poopy"]
        assert redact_words(list_without_banned, banned) == ["the", "big", "house"]

        list_with_banned = ["the", "poopy", "house"]
        more_banned = ["big", "comfy", "couch"]
        assert redact_words(list_with_banned, more_banned) == ["the", "poopy", "house"]

        list_without_banned = ["the", "big", "house"]
        more_banned = ["big", "comfy", "couch"]
        assert redact_words(list_without_banned, more_banned) == ["the", "house"]