"""Interactive command-line entry point for the LR(1) parser."""

from __future__ import annotations

from parser.exceptions import GrammarConflictError, LexicalError, ParseSyntaxError
from parser.lexer import tokenize_sentence
from parser.parser_engine import LR1Parser


def parse_sentence(sentence: str, parser: LR1Parser | None = None) -> tuple[list[str], str]:
    """Tokenize and parse one sentence, returning the token stream and result."""

    active_parser = parser or LR1Parser()
    tokens = tokenize_sentence(sentence)
    result = active_parser.parse(tokens)
    return tokens, result


def print_sentence_result(sentence: str, parser: LR1Parser | None = None) -> None:
    """Run the parser for one sentence and print a readable report."""

    try:
        tokens, result = parse_sentence(sentence, parser)
        print(f"Tokens: {' '.join(tokens)}")
        print(f"Result: {result}")
    except LexicalError as error:
        print(f"Lexical Error: {error}")
    except GrammarConflictError as error:
        print(f"Grammar Conflict: {error}")
    except ParseSyntaxError as error:
        print(f"Syntax Error: {error}")


def main() -> None:
    """Start a live parser session that exits only when the user types Quit."""

    parser = LR1Parser()

    print("=" * 70)
    print("LR(1) PARSER")
    print("=" * 70)
    print('Type a Setswana sentence to parse, or type "Quit" to exit.')

    while True:
        sentence = input("parser> ").strip()

        if not sentence:
            print("Please enter a sentence or type Quit.")
            continue

        if sentence.lower() == "quit":
            print("Exiting LR(1) parser.")
            break

        print_sentence_result(sentence, parser)
        print("-" * 70)


if __name__ == "__main__":
    main()
