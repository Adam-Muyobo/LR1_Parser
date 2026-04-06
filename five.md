# LR(1) Parser (Explain Like I'm 5)

This project is a small sentence checker.

It takes a Setswana sentence, changes each word into a grammar token, and then asks:

"Does this sentence fit the grammar table exactly?"

If yes, the parser says `ACCEPTED`.
If not, it tells you whether the problem is:
- an unknown word,
- a bad sentence structure, or
- a conflict already present in the grammar table.

## File Tour

## `main.py`
This is the live parser mode.

- You run it in the terminal.
- It keeps asking for a sentence.
- It only stops when you type `Quit`.

## `run_tests.py`
This is the batch runner.

- It reads sample sentences from `tests/sample_sentences.txt`.
- It runs the parser on each one.
- It prints a small report and a summary.

## `parser/lexer.py`
This is the word-to-token converter.

- It reads the sentence word by word.
- It turns words like `ya`, `bana`, and `gatang` into grammar symbols.
- It treats the first `ba` as `c1` and the second `ba` as `c2` because the grammar needs that distinction.

## `parser/grammar.py`
This is the grammar data.

- `PRODUCTIONS` says what grammar rules exist.
- `TERMINALS` lists which surface words belong to each terminal symbol.

## `parser/lr1_table.py`
This is the parser's decision table.

- `ACTION` says whether to shift, reduce, accept, or hit a conflict.
- `GOTO` says where to move after a reduction.

## `parser/parser_engine.py`
This is the parser engine.

- It uses a stack.
- It follows the LR(1) table step by step.
- It returns `ACCEPTED` if the sentence fits the grammar.

## `parser/exceptions.py`
This file stores the custom error names used by the parser.

## `tests/sample_sentences.txt`
This is the sample input file for the batch runner.

- Blank lines are ignored.
- Lines starting with `#` are treated as comments.

## How to run

Live mode:

```bash
python main.py
```

Batch mode:

```bash
python run_tests.py
```

## Authors
- Adam Musakabantu Muyobo
- Zibisani Kgari Mholo
- Theo Kizito Tida
