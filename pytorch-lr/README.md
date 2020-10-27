
Logistic Regression
=

Overview
--------

In this homework you'll implement a stochastic gradient ascent for
logistic regression and you'll apply it to the task of determining
whether documents are talking about hockey or baseball.  Sound familiar?  It should be!

This should be very easy: unlike before, you weren't allowed to use many utilities.  This time, you can and should use all of the capabilities that PyTorch offers.


What you have to do
----

Coding (15 points):

1. Load in the data and create a data iterator.  This will be the most difficult bit.  Use the sklearn feature creation function.
2. Create a logistic regression model with a softmax activation function and 
3. Create a stochastic gradient optimizer.
4. Optimize the function (remember to zero out gradients) and analyze the output.
5. Save the model.

Analysis (10 points):

1. How does the model differ from the model you learned "by hand"
2. How is the objective function different from what you used in the last homework?

Extra credit:

1. Compare different optimizers
2.  Use [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

What to turn in
-

1. Submit your _pytorch-lr.py_ file (include your name at the top of the source)
1. Submit your _analysis.pdf_ file
    - no more than one page
    - pictures are better than text
    - include your name at the top of the PDF

