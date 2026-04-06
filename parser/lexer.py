"""Tokenization helpers for the LR(1) parser.

The parser grammar works on terminal symbols such as `x`, `n1`, `v`, and `l`.
This module maps surface words from the assignment vocabulary onto those grammar
terminals before the LR(1) machine runs.
"""

from __future__ import annotations

from parser.exceptions import LexicalError
from parser.grammar import TERMINALS

IGNORED_EDGE_PUNCTUATION = ".,!?;:"

# `ba` is context-sensitive in this grammar: the first occurrence becomes `c1`
# and the second becomes `c2`. The rest of the vocabulary is a direct lookup.
WORD_TO_TOKEN = {
    word: token
    for token, vocabulary in TERMINALS.items()
    if token not in {"c1", "c2"}
    for word in vocabulary
}


def tokenize_sentence(sentence: str) -> list[str]:
    """Convert a surface sentence into grammar terminals.

    A small amount of normalization is applied so that common trailing
    punctuation in interactive input does not break otherwise valid examples.
    """

    words = [
        word.strip(IGNORED_EDGE_PUNCTUATION)
        for word in sentence.lower().split()
        if word.strip(IGNORED_EDGE_PUNCTUATION)
    ]

    tokens: list[str] = []
    ba_count = 0

    for position, word in enumerate(words, start=1):
        if word == "ba":
            ba_count += 1
            tokens.append("c1" if ba_count == 1 else "c2")
            continue

        token = WORD_TO_TOKEN.get(word)
        if token is None:
            raise LexicalError(f"Unknown word at position {position}: {word}")
        tokens.append(token)

    tokens.append("$")
    return tokens
