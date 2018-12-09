RESERVED_SUBSTITUTIONS = {
    0x1D455: 0x210E, 0x1D49D: 0x212C, 0x1D4A0: 0x2130, 0x1D4A1: 0x2131,
    0x1D4A3: 0x210B, 0x1D4A4: 0x2110, 0x1D4A7: 0x2112, 0x1D4A8: 0x2133,
    0x1D4AD: 0x211B, 0x1D4BA: 0x212F, 0x1D4BC: 0x210A, 0x1D4C4: 0x2134,
    0x1D506: 0x212D, 0x1D50B: 0x210C, 0x1D50C: 0x2111, 0x1D515: 0x211C,
    0x1D51D: 0x2128, 0x1D53A: 0x2102, 0x1D53F: 0x210D, 0x1D545: 0x2115,
    0x1D547: 0x2119, 0x1D548: 0x211A, 0x1D549: 0x211D, 0x1D551: 0x2124,
}

_chr = lambda n: chr(RESERVED_SUBSTITUTIONS.get(n, n))

MATHEMATICAL_BOLD_CAPITAL_LETTERS                   = tuple(map(_chr, range(0x1D400, 0x1D41A)))
MATHEMATICAL_BOLD_SMALL_LETTERS                     = tuple(map(_chr, range(0x1D41A, 0x1D434)))
MATHEMATICAL_ITALIC_CAPITAL_LETTERS                 = tuple(map(_chr, range(0x1D434, 0x1D44E)))
MATHEMATICAL_ITALIC_SMALL_LETTERS                   = tuple(map(_chr, range(0x1D44E, 0x1D468)))
MATHEMATICAL_BOLD_ITALIC_CAPITAL_LETTERS            = tuple(map(_chr, range(0x1D468, 0x1D482)))
MATHEMATICAL_BOLD_ITALIC_SMALL_LETTERS              = tuple(map(_chr, range(0x1D482, 0x1D49C)))
MATHEMATICAL_SCRIPT_CAPITAL_LETTERS                 = tuple(map(_chr, range(0x1D49C, 0x1D4B6)))
MATHEMATICAL_SCRIPT_SMALL_LETTERS                   = tuple(map(_chr, range(0x1D4B6, 0x1D4D0)))
MATHEMATICAL_BOLD_SCRIPT_CAPITAL_LETTERS            = tuple(map(_chr, range(0x1D4D0, 0x1D4EA)))
MATHEMATICAL_BOLD_SCRIPT_SMALL_LETTERS              = tuple(map(_chr, range(0x1D4EA, 0x1D504)))
MATHEMATICAL_FRAKTUR_CAPITAL_LETTERS                = tuple(map(_chr, range(0x1D504, 0x1D51E)))
MATHEMATICAL_FRAKTUR_SMALL_LETTERS                  = tuple(map(_chr, range(0x1D51E, 0x1D538)))
MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_LETTERS          = tuple(map(_chr, range(0x1D538, 0x1D552)))
MATHEMATICAL_DOUBLE_STRUCK_SMALL_LETTERS            = tuple(map(_chr, range(0x1D552, 0x1D56C)))
MATHEMATICAL_BOLD_FRAKTUR_CAPITAL_LETTERS           = tuple(map(_chr, range(0x1D56C, 0x1D586)))
MATHEMATICAL_BOLD_FRAKTUR_SMALL_LETTERS             = tuple(map(_chr, range(0x1D586, 0x1D5A0)))
MATHEMATICAL_SANS_SERIF_CAPITAL_LETTERS             = tuple(map(_chr, range(0x1D5A0, 0x1D5BA)))
MATHEMATICAL_SANS_SERIF_SMALL_LETTERS               = tuple(map(_chr, range(0x1D5BA, 0x1D5D4)))
MATHEMATICAL_SANS_SERIF_BOLD_CAPITAL_LETTERS        = tuple(map(_chr, range(0x1D5D4, 0x1D5EE)))
MATHEMATICAL_SANS_SERIF_BOLD_SMALL_LETTERS          = tuple(map(_chr, range(0x1D5EE, 0x1D608)))
MATHEMATICAL_SANS_SERIF_ITALIC_CAPITAL_LETTERS      = tuple(map(_chr, range(0x1D608, 0x1D622)))
MATHEMATICAL_SANS_SERIF_ITALIC_SMALL_LETTERS        = tuple(map(_chr, range(0x1D622, 0x1D63C)))
MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_CAPITAL_LETTERS = tuple(map(_chr, range(0x1D63C, 0x1D656)))
MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_SMALL_LETTERS   = tuple(map(_chr, range(0x1D656, 0x1D670)))
MATHEMATICAL_MONOSPACE_CAPITAL_LETTERS              = tuple(map(_chr, range(0x1D670, 0x1D68A)))
MATHEMATICAL_MONOSPACE_SMALL_LETTERS                = tuple(map(_chr, range(0x1D68A, 0x1D6A4)))

MATHEMATICAL_BOLD_GREEK_LETTERS                     = tuple(map(_chr, range(0x1D6A8, 0x1D6E2)))
MATHEMATICAL_ITALIC_GREEK_LETTERS                   = tuple(map(_chr, range(0x1D6E2, 0x1D71C)))
MATHEMATICAL_BOLD_ITALIC_GREEK_LETTERS              = tuple(map(_chr, range(0x1D71C, 0x1D756)))
MATHEMATICAL_SANS_SERIF_BOLD_GREEK_LETTERS          = tuple(map(_chr, range(0x1D756, 0x1D790)))
MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_GREEK_LETTERS   = tuple(map(_chr, range(0x1D790, 0x1D7CA)))

MATHEMATICAL_BOLD_DIGITS                            = tuple(map(_chr, range(0x1D7CE, 0x1D7D8)))
MATHEMATICAL_DOUBLE_STRUCK_DIGITS                   = tuple(map(_chr, range(0x1D7D8, 0x1D7E2)))
MATHEMATICAL_SANS_SERIF_DIGITS                      = tuple(map(_chr, range(0x1D7E2, 0x1D7EC)))
MATHEMATICAL_SANS_SERIF_BOLD_DIGITS                 = tuple(map(_chr, range(0x1D7EC, 0x1D7F6)))
MATHEMATICAL_MONOSPACE_DIGITS                       = tuple(map(_chr, range(0x1D7F6, 0x1D800)))

# TODO:
# 1D6A4 MATHEMATICAL ITALIC SMALL DOTLESS I (\imath)
# 1D6A5 MATHEMATICAL ITALIC SMALL DOTLESS J (\jmath)
# 1D7CA MATHEMATICAL BOLD CAPITAL DIGAMMA   (\Digamma)
# 1D7CB MATHEMATICAL BOLD SMALL DIGAMMA     (\digamma)

LATEX_GREEK_COMMANDS = (
    "\\\\Alpha", "\\\\Beta", "\\\\Gamma", "\\\\Delta", "\\\\Epsilon",
    "\\\\Zeta", "\\\\Eta", "\\\\Theta", "\\\\Iota", "\\\\Kappa", "\\\\Lambda",
    "\\\\Mu", "\\\\Nu", "\\\\Xi", "\\\\Omicron", "\\\\Pi", "\\\\Rho",
    "\\\\varTheta", "\\\\Sigma", "\\\\Tau", "\\\\Upsilon", "\\\\Phi",
    "\\\\Chi", "\\\\Psi", "\\\\Omega", "\\\\nabla", "\\\\alpha", "\\\\beta",
    "\\\\gamma", "\\\\delta", "\\\\varepsilon", "\\\\zeta", "\\\\eta",
    "\\\\theta", "\\\\iota", "\\\\kappa", "\\\\lambda", "\\\\mu", "\\\\nu",
    "\\\\xi", "\\\\omicron", "\\\\pi", "\\\\rho", "\\\\varsigma", "\\\\sigma",
    "\\\\tau", "\\\\upsilon", "\\\\varphi", "\\\\chi", "\\\\psi", "\\\\omega",
    "\\\\partial", "\\\\epsilon", "\\\\vartheta", "\\\\varkappa", "\\\\phi",
    "\\\\varrho", "\\\\varpi")

LATEX_STYLE_COMMANDS = {
    ("mathbf", "mathbfup", "symbf", "symbfup"):         (MATHEMATICAL_BOLD_CAPITAL_LETTERS,                   MATHEMATICAL_BOLD_SMALL_LETTERS,                   MATHEMATICAL_BOLD_GREEK_LETTERS,                   MATHEMATICAL_BOLD_DIGITS),
    ("mathit", "mathnormal", "symit", "symnormal"):     (MATHEMATICAL_ITALIC_CAPITAL_LETTERS,                 MATHEMATICAL_ITALIC_SMALL_LETTERS,                 MATHEMATICAL_ITALIC_GREEK_LETTERS,                 None),
    ("mathbfit", "symbfit", "boldsymbol", "bm"):        (MATHEMATICAL_BOLD_ITALIC_CAPITAL_LETTERS,            MATHEMATICAL_BOLD_ITALIC_SMALL_LETTERS,            MATHEMATICAL_BOLD_ITALIC_GREEK_LETTERS,            None),
    ("mathcal", "mathscr", "symcal", "symscr"):         (MATHEMATICAL_SCRIPT_CAPITAL_LETTERS,                 MATHEMATICAL_SCRIPT_SMALL_LETTERS,                 None,                                              None),
    ("mathbfcal", "mathbfscr", "symbfcal", "symbfscr"): (MATHEMATICAL_BOLD_SCRIPT_CAPITAL_LETTERS,            MATHEMATICAL_BOLD_SCRIPT_SMALL_LETTERS,            None,                                              None),
    ("mathfrak", "symfrak"):                            (MATHEMATICAL_FRAKTUR_CAPITAL_LETTERS,                MATHEMATICAL_FRAKTUR_SMALL_LETTERS,                None,                                              None),
    ("mathbb", "symbb", "Bbb"):                         (MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_LETTERS,          MATHEMATICAL_DOUBLE_STRUCK_SMALL_LETTERS,          None,                                              MATHEMATICAL_DOUBLE_STRUCK_DIGITS),
    ("mathbffrak", "symbffrak"):                        (MATHEMATICAL_BOLD_FRAKTUR_CAPITAL_LETTERS,           MATHEMATICAL_BOLD_FRAKTUR_SMALL_LETTERS,           None,                                              None),
    ("mathsf", "mathsfup", "symsf", "symsfup"):         (MATHEMATICAL_SANS_SERIF_CAPITAL_LETTERS,             MATHEMATICAL_SANS_SERIF_SMALL_LETTERS,             None,                                              MATHEMATICAL_SANS_SERIF_DIGITS),
    ("mathbfsf", "symbfsf"):                            (MATHEMATICAL_SANS_SERIF_BOLD_CAPITAL_LETTERS,        MATHEMATICAL_SANS_SERIF_BOLD_SMALL_LETTERS,        MATHEMATICAL_SANS_SERIF_BOLD_GREEK_LETTERS,        MATHEMATICAL_SANS_SERIF_BOLD_DIGITS),
    ("mathsfit", "symsfit"):                            (MATHEMATICAL_SANS_SERIF_ITALIC_CAPITAL_LETTERS,      MATHEMATICAL_SANS_SERIF_ITALIC_SMALL_LETTERS,      None,                                              None),
    ("mathbfsfit", "symbfsfit"):                        (MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_CAPITAL_LETTERS, MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_SMALL_LETTERS, MATHEMATICAL_SANS_SERIF_BOLD_ITALIC_GREEK_LETTERS, None),
    ("mathtt", "symtt"):                                (MATHEMATICAL_MONOSPACE_CAPITAL_LETTERS,              MATHEMATICAL_MONOSPACE_SMALL_LETTERS,              None,                                              MATHEMATICAL_MONOSPACE_DIGITS),
}
