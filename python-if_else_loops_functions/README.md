# Python - if/else, loops, functions

### Files

`0-positive_or_negative.py` is a completion of this [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py). <br>
`1-last_digit.py` is a completion of this [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py).


Filename | Description
--- | ---
`0-positive_or_negative.py` | Prints is number is positive, negative or zero.
`1-last_digit.py` | Prints last digit of a number (e.g. `Last digit of 5169 is 9 and is greater than 5`).
`2-print_alphabet.py` | Prints ASCII alphabet in lowercase.
`3-print_alphabt.py` | Prints alphabet in lowercase, except letters `q` and `e`.
`4-print_hexa.py` | Prints numbers from 0 to 98 in decimal and hexadecimal.
`5-print_comb2.py` | Prints numbers from 00 to 99 separated by `, `.
`6-print_comb3.py` | Prints all possible different combinations of two digits.
`7-islower.py` | Checks for lowercase characters.
`8-uppercase.py` | Prints string in uppercase.
`9-print_last_digit.py` | Prints last digit of a number.
`10-add.py` | Adds two integers and returns the result.
`11-pow.py` | Computes `a` to the power of `b`.
`12-fizzbuzz.py` | Prints FizzBuzz pattern.
`100-print_tebahpla.py` | Prints alphabet in reverse, alternating lowercase and uppercase.
`101-remove_char_at.py` | Creates a copy of the string, removing the character at the position `n`.
`102-magic_calculation.py` | Function that does exactly the same as the following Python bytecode


Bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
