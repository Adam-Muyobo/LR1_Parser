"""Run the LR(1) parser against predefined statements from a file."""

from __future__ import annotations

from pathlib import Path

from main import parse_sentence
from parser.exceptions import GrammarConflictError, LexicalError, ParseSyntaxError
from parser.parser_engine import LR1Parser

TEST_INPUT_FILE = Path(__file__).parent / "tests" / "sample_sentences.txt"


def iter_test_sentences(path: Path) -> list[str]:
    """Load non-empty, non-comment test sentences from `path`."""

    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def main() -> None:
    parser = LR1Parser()
    sentences = iter_test_sentences(TEST_INPUT_FILE)

    accepted = 0
    rejected = 0

    print("=" * 70)
    print("LR(1) PARSER TEST RUNNER")
    print("=" * 70)
    print(f"Input file: {TEST_INPUT_FILE}")
    print(f"Loaded {len(sentences)} test sentence(s).")
    print("=" * 70)

    for index, sentence in enumerate(sentences, start=1):
        print(f"[{index}] Sentence: {sentence}")
        try:
            tokens, result = parse_sentence(sentence, parser)
            print(f"    Tokens: {' '.join(tokens)}")
            print(f"    Result: {result}")
            accepted += 1
        except LexicalError as error:
            print(f"    Lexical Error: {error}")
            rejected += 1
        except GrammarConflictError as error:
            print(f"    Grammar Conflict: {error}")
            rejected += 1
        except ParseSyntaxError as error:
            print(f"    Syntax Error: {error}")
            rejected += 1
        print("-" * 70)

    print("Summary")
    print(f"Accepted: {accepted}")
    print(f"Not accepted: {rejected}")


if __name__ == "__main__":
    main()
