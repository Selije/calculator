# calculator
Calculator in Python 3

A simple calculator program using recursive descent parser which computes arithmetic expressions consisting four basic arithmetic operations.
Correctly handles operator precendnce and grouping with parantheses. 

Currently supports **only integer** number literals (but results are floating point numbers). 

## Usage

One can provide an expression as a command line argument:

```
$ python3 calculator.py "(3 + 2*5) - 8"
5.0
$ python3 calculator.py -12 + 7 *3
9.0
```

or invoke it without arguments to start read-eval-print loop:
```
$ python3 calculator.py
> 3
3.0
> 2*8
16.0
> 12 * (135- 8/2) + 9 + 53
1634.0
> -82 /4 - 17
-37.5
> 15 /(5-5)
Must not divide by 0!
```

## Tests

[Parser](parser.py#L80-L136), [evaluator](evaluator.py#L44-L61) and [tokenizer](tokenizer.py#L84-L106) have unit tests written using python `unittest` module.
