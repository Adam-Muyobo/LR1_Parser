# LR(1) Parser

LR(1) parser for **CSI428 - Programming Language Translation** (Assignment 2). The project tokenizes a small Setswana sentence grammar, feeds the tokens into a hand-written LR(1) driver, and reports whether the sentence is accepted, rejected, or blocked by a grammar conflict in the supplied parsing table.

## What this project does
- Tokenizes assignment vocabulary into grammar terminals such as `x`, `n1`, `c1`, `c2`, `g`, `v`, `n`, `c3`, `c4`, and `l`
- Parses the resulting token stream using the provided LR(1) `ACTION` and `GOTO` tables
- Reports three failure categories clearly: lexical errors, syntax errors, and grammar conflicts
- Provides both an interactive parser shell and a file-driven test runner
- Includes extra code comments and a simplified `five.md` walkthrough

## Project Layout
- `main.py` - interactive parser CLI; keeps running until you type `Quit`
- `run_tests.py` - runs the parser on predefined statements loaded from `tests/sample_sentences.txt`
- `parser/grammar.py` - productions and terminal vocabularies
- `parser/lexer.py` - sentence-to-token conversion
- `parser/lr1_table.py` - LR(1) `ACTION` and `GOTO` tables
- `parser/parser_engine.py` - stack-based LR(1) parser driver
- `parser/exceptions.py` - parser-specific exception types
- `tests/sample_sentences.txt` - predefined input sentences for smoke testing
- `five.md` - simpler file-by-file explanation
- `LR(1) Transition Diagram.jpg` - reference diagram supplied for the assignment

## Usage

Start the live parser:
```bash
python main.py
```

Run the predefined parser checks:
```bash
python run_tests.py
```

## Input Notes
- The parser expects sentences built from the assignment vocabulary
- Tokenization is word-based and ignores common edge punctuation such as `. , ! ? ; :`
- The live parser accepts input repeatedly and only exits when you type `Quit`

## Error Types
- `Lexical Error` - a word is not in the parser vocabulary
- `Syntax Error` - the token stream does not fit the LR(1) table
- `Grammar Conflict` - the parsing table contains a conflict for the current state/lookahead

## Reuse Check Against Assignment 1
- The **Lexical Analyzer** from Assignment 1 is Python-specific, so it is not a good direct tokenizer for this Setswana grammar
- The **Leamanyi Analyzer** is regex-based and solves a different recognition problem, so it is also not a direct replacement for LR parsing
- The useful idea borrowed from Assignment 1 is documentation structure and clearer separation of responsibilities; if this parser grows later, the Leamanyi project's external word-list approach would be a reasonable next refactor

## Grammar Note
The supplied LR(1) table still contains a shift/reduce conflict in state `14` on lookahead `c3`. This project reports that conflict instead of silently choosing one action.

## Authors
- Adam Musakabantu Muyobo
- Zibisani Kgari Mholo
- Theo Kizito Tida
