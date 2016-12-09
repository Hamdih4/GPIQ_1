# Library System #

The library system is a mini program for a digital library to help people search, borrow and return books. The book table will be saved in a separate data file (could be .json), so at the end, the books table might look something like this:

```
 ---------------------
 | # | Title | State |
 ---------------------
 | 1 |   1   |   B   |   
 | 2 |   2   |   A   |   
 | 3 |   3   |   R   |   
 | 4 |   4   |   A   |   
 ---------------------

 (B) Borrowed
 (A) Available
 (R) Returned
```

## Running the program ##
 * The program does not have any UI, it can be run from the command line.
 * When running the program, the user will be prompted to select one of the options to execute a feature.

 ```
 What do you want to do today? (S)earch for a book? (B)orrow a book? (R)eturn a book?
 ```

## Features ##

* List of program features:

#### Feature 1: Searching for a book ####
 * When `search for a book` is selected, the user will be prompted again to enter the book id number.

 ```
 Enter the book id to search for: __
 ```
  * If user entered (1), the result will be something like this:

  ```
  1 Borrowed
  ```

  * If user entered (2), the result will be something like this:

  ```
  2 Available
  ```

#### Feature 2: Borrowing a book ####
 * When `borrow a book` is selected, the user will be prompted again to enter the book id number.

 ```
 Enter the book id to search for: __
 ```

  * If user entered (1), the result will be something like this:

 ```
 Sorry, you cannot borrow this time, the books is not available.
 ```

  * If user entered (2), the result will be something like this:

 ```
 2 Available, successfully borrowed by you.
 ```

#### Feature 3: Returning a book ####
 * When `return a book` is selected, the user will be prompted again to enter the book id number.

 ```
 Enter the book id to search for: __
 ```

  * If user entered (1), the result will be something like this:

 ```
 1 Borrowed, successfully returned by you.
 ```

  * If user entered (2), the result will be something like this:

 ```
 2 Available, you cannot return a book that is already available.
 ```

  * If user entered (3), the result will be something like this:

 ```
 3 Returned, you cannot return a book that was already returned.
 ```
