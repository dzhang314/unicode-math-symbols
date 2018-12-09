import itertools as it
import string
import unicodedata
from unicode_math_symbols import *

JSON_SNIPPET_TEMPLATE = """\
    "{0}": {{
        "prefix": "{0}",
        "body": ["{1}"],
        "description": "{2}"
    }},
"""

def json_escape(char):
    codepoint = ord(char)
    if codepoint <= 0xFFFF:
        return "\\u{0:X}".format(codepoint)
    else:
        high = (codepoint - 0x10000) // 0x400 + 0xD800
        low = (codepoint - 0x10000) % 0x400 + 0xDC00
        return "\\u{0:X}\\u{1:X}".format(high, low)

def snippet_generator(command, symbols, args):
    assert len(symbols) == len(args)
    for symbol, arg in zip(symbols, args):
        yield JSON_SNIPPET_TEMPLATE.format(
            "\\\\{0}{{{1}}}".format(command, arg),
            json_escape(symbol),
            unicodedata.name(symbol))

def naked_greek_snippet_generator():
    MATHEMATICAL_NAKED_GREEK_LETTERS = (
        MATHEMATICAL_ITALIC_GREEK_LETTERS[:25] +
        (chr(0x2207),) +
        MATHEMATICAL_ITALIC_GREEK_LETTERS[26:51] +
        (chr(0x2202),) +
        MATHEMATICAL_ITALIC_GREEK_LETTERS[52:58])
    for letter, command in zip(MATHEMATICAL_NAKED_GREEK_LETTERS,
                               LATEX_GREEK_COMMANDS):
        yield JSON_SNIPPET_TEMPLATE.format(
            command,
            json_escape(letter),
            unicodedata.name(letter))

def full_snippet_generator(command, capitals, smalls, greeks, digits):
    if capitals is not None:
        yield from snippet_generator(command, capitals, string.ascii_uppercase)
    if smalls is not None:
        yield from snippet_generator(command, smalls, string.ascii_lowercase)
    if greeks is not None:
        yield from snippet_generator(command, greeks, LATEX_GREEK_COMMANDS)
    if digits is not None:
        yield from snippet_generator(command, digits, string.digits)

if __name__ == "__main__":
    with open("snippets.json", "w+") as f:
        for commands, (capitals, smalls,
                       greeks, digits) in LATEX_STYLE_COMMANDS.items():
            for command in commands:
                for snippet in full_snippet_generator(command, capitals, smalls,
                                                      greeks, digits):
                    f.write(snippet)
        for snippet in naked_greek_snippet_generator():
            f.write(snippet)
