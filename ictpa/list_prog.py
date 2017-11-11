"""list_prog.py

Do all the questions below. Simply replace 'pass' by your implementation of the
functions.

Try to do everything using only basic built-in operators/functions:
    - +-operator
    - list(..)
    - len(..)
    - x[i]
    - in
"""

def chooseInt(List):
    """Returns a list of elements in List that are integers. For example,
    - chooseInt(['gouda',3,10,'alibaba',2.34,0]) returns [3,10,0].
    
    You might find the function isinstance useful.
    """
    pass

def chooseEvenNumber(List):
    """Returns a list of elements in List that are even numbers. For example,
    - chooseEvenNumber(['gouda',3,10,'alibaba',2.34,0]) returns [10,0].

    You might find the function isinstance useful.
    """
    pass

def everyOtherItem(List):
    """Return every other item. For example, 
    (1) everyOtherItem([1,2,3,4,5]) returns [1,3,5].
    (2) everyOtherItem(['cheddar',4,'bob']) returns ['cheddar','bob']
    """
    pass

def middle(List):
    """Return the middle element of the list. If there is an even number of
    elements in the list, return the first one in the middle. For example:
    (1) middle([1,2,3]) returns 2
    (2) middle([1,3,2,1,7,'b']) returns 2
    """
    pass

def reverse(List):
    """Return a new copy of List in a reverse order (also, List should not
    be changed). For example, 

    - reverse([1,2,3,4,5]) returns [5,4,3,2,1]
    """
    pass

def palindrome(List):
    """Returns True if List is a ``palindrome'' (False otherwise). List is
    palindrome if it is the same as its reverse.
    """
    pass

def isSorted(List):
    """Returns True if List is a list of numbers that are sorted in an
    increasing order. For example:
    - isSorted([1,1,3,10]) returns True
    - isSorted([1,2,9,3]) returns False
    """
    pass

def count(el,List):
    """Return the number of occurrences of el in List. For example,
    - count(1,[1,1,3,10]) returns 2
    - count(2,[1,1,3,10]) returns 0
    - count('bob',[1,2,'bob,'guava',2.777]) returns 1
    """
    pass

def countSublist(List1,List2):
    """Return the number of occurrences of List1 in List2 as a sublist. For example,
    - count([1,3],[1,1,3,10]) returns 1
    - count([1,3],[1,1,3,1,3,10]) returns 2
    - count([1,1],[1,1,1,1,1,10]) returns 5
    """
    pass

def main():
    """Put whatever you want here."""
    pass

# DO NOT CHANGE THE LINES BELOW
if __name__ == '__main__':
    main()
