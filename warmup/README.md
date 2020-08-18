
Overview
===========================

The goal of this homework is to make sure you're comfortable using
Python, checking out files, and interacting with data.

I've created the names of functions you'll need to implement.  Fill
them in and run the unit tests to see if they work.  When you've done
everything, the output should look like:
```
$ python test_word_count.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
(base) mac-mini:warmup jbg$ python test_matrix_multiply.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Matrix Math
===========================

There are many Python packages that do matrix multiplication for you,
but we won't be using any of them!  Instead, we'll implement matrix
multiplication ourselves to make sure you understand it weel enough to
implement it yourself.

Make sure that you check that matrices have the appropriate dimension
(raise an Exception if not).

Counting a Document's Words
===========================

Given the path of a document, count up the words in the document and
return a dictionary with the count of all of the words in the document.

Extra Credit
===========================

The count words function has several arguments.  Implement them so that:

 * Punctuation is removed from words

 * Words are lowercased before they are counted

(Half point available for each.)
