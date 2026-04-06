"""Core LR(1) parser implementation."""

from __future__ import annotations

from parser.exceptions import GrammarConflictError, ParseSyntaxError
from parser.grammar import PRODUCTIONS
from parser.lr1_table import ACTION, GOTO


class LR1Parser:
    """Table-driven LR(1) parser for the assignment grammar."""

    def parse(self, tokens: list[str]) -> str:
        # The stack alternates between grammar symbols and parser states.
        # It starts with only state 0, which is the LR automaton start state.
        stack: list[int | str] = [0]
        index = 0

        while True:
            state = stack[-1]
            if not isinstance(state, int):
                raise ParseSyntaxError("Parser stack is corrupted: expected a state.")

            if index >= len(tokens):
                raise ParseSyntaxError("Unexpected end of token stream.")

            lookahead = tokens[index]
            action = ACTION.get(state, {}).get(lookahead)

            if action is None:
                raise ParseSyntaxError(
                    f"Invalid syntax near token {lookahead!r} at position {index + 1}."
                )

            if isinstance(action, list):
                raise GrammarConflictError(
                    f"Grammar conflict at state {state} with lookahead {lookahead!r}."
                )

            action_type, value = action

            if action_type == "shift":
                stack.append(lookahead)
                stack.append(value)
                index += 1
                continue

            if action_type == "reduce":
                lhs, length, production = PRODUCTIONS[value]

                # Each grammar symbol on the stack is paired with a state.
                for _ in range(length * 2):
                    stack.pop()

                previous_state = stack[-1]
                if not isinstance(previous_state, int):
                    raise ParseSyntaxError(
                        "Parser stack is corrupted after reduction: expected a state."
                    )

                goto_state = GOTO.get(previous_state, {}).get(lhs)
                if goto_state is None:
                    raise ParseSyntaxError(
                        f"Missing goto after reducing {lhs} -> {production}."
                    )

                stack.append(lhs)
                stack.append(goto_state)
                continue

            if action_type == "accept":
                return "ACCEPTED"

            raise ParseSyntaxError(f"Unknown parser action: {action_type}")
