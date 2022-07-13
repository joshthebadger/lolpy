import unittest

from lolpy import parsers

INVALID_STRINGS = (None, '', ' ', '\t\n')


class TestParsers(unittest.TestCase):

    def test_parse_str(self):
        # invalid strings
        for s in INVALID_STRINGS:
            self.assertIsNone(parsers.parse_str(s))
        default = 'default'
        for s in INVALID_STRINGS:
            self.assertEquals(parsers.parse_str(s, default=default), default)
        value = 'value'
        for s in ('\tvalue', ' value', value):
            self.assertEquals(parsers.parse_str(s), value)


if __name__ == '__main__':
    unittest.main()
