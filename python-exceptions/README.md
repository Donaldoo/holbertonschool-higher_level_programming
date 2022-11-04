# Python - Exceptions

`try` - tests a block of code for errors.
`except` - handles errors.
`else` - executes code when there's no errors.
`finally` - executes code, regardless of the resuslt of the `try` and `except` blocks.

### Exception handling
When an error occurs, Python will stop and generate an error message. These exceptions can be handled using the `try` statement. If the try block raises an error, the except block will be executed. Without the try block the program will crash.
```
try:
  print(x)
except:
  print("An exception occured")
```

## Files

All functions are written using `try:/except:`.

Filename | Description
-------- | -----------
`0-safe_print_list.py` | Prints `x` elements of a list.
`1-safe_print_integer.py` | Prints an integer with `"{:d}".format()`.
`2-safe_print_list_integers.py` | Prints the first `x` elements of a list and only integers.
`3-safe_print_division.py` | Divides 2 integers and prints the result.
`4-list_division.py` | Divides element by element 2 lists.
`5-raise_exception.py` | Function that raises a type exception.
`6-raise_exception_msg.py` | Function that raises a name exception with a message.
`100-safe_print_integer_err.py` | Function that prints an integer.
`101-safe_function.py` | Function that executes a function safely.
