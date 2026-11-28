## Key-Value Pairs

• The last built-in type: dictionary (or dict)

§ One of the most important in all of Python

§ Like a list, but built of key-value pairs

• **Keys:** Unique identifiers

§ Think social security number

§ At Cornell we have netids: jrs1

• **Values:** Non-unique Python values

§ John Smith (class ’13) is jrs1

§ John Smith (class ’16) is jrs2

**Idea:** Lookup

values by keys

## Using Dictionaries (Type dict)

• Access elts. like a list

§ d['jrs1'] evals to 'John’

§ d['jrs2'] does too d = {'js1':'John','js2':'John', 'wmw2':'Walker'}

§ d['wmw2'] evals to 'Walker'

**id8**

§ d['abc1'] is an **error**

**dict**

• Can test if a key exists

§ 'jrs1’ in d evals to True

§ 'abc1' in d evals to False

'jrs2'

• But cannot slice ranges!

'wmw2' 'Walker'

Key-Value order in

folder is not important

## Dictionaries: Iterable, but not Sliceable

• Can loop over a dict

## for k in d:

§ Only gives you the keys

\# Loops over **keys**

§ Use key to access value

print(k) # key

print(d[k]) # value

• Can iterate over values

§ **Method:** d.values()

\# To loop over values only

for v in d.values():

§ But no way to get key

print(v) # value

§ Values are not unique

## Basic Syntax

• Create with format: {k1:v1, k2:v2, …}

§ Both keys and values must exist

§ **Ex:** d={‘jrs1':'John',’jrs2':'John','wmw2':'Walker'}

• **Keys** must be **non-mutable**

§ ints, floats, bools, strings, tuples

§ **Not** lists or custom objects

§ Changing a key’s contents hurts lookup

• **Values** can be **anything**

## Dictionaries Can be Modified

• Can reassign values

§ d['jrs1'] = 'Jane’

§ Very similar to lists d = {'jrs1':'John','jrs2':'John', 'wmw2':'Walker'}

• Can add new keys

**id8**

§ d[‘aaa1'] = 'Allen’

§ Do not think of order

• Can delete keys

§ del d['wmw2’]

§ Deletes both key, value

## Dictionary Loop with Accumulator

## def max\_grade(grades):

"""Returns max grade in the grade dictionary

Precondition: grades has netids as keys, ints as values"""

maximum = 0

\# Accumulator

\# Loop over keys

for k in grades:

if grades[k] > maximum:

maximum = grades[k]

return maximum

## Dictionaries and Mutable Functions

• Restrictions are different than list

§ Okay to loop over dictionary to change

§ You are looping over keys, not values

§ Like looping over positions

• But you **may not add or remove** keys!

§ Any attempt to do this will fail

§ Have to create a key list if you want this

## Nesting Dictionaries

• Remember, values can be anything § Only restrictions are on the keys

• Values can be lists (**Visualizer**) § d = {'a':[1,2], 'b':[3,4]}

• Values can be other dicts (**Visualizer**) § d = {'a':{'c':1,'d':2}, 'b':{'e':3,'f':4}}

• Access rules similar to nested lists

§ **Example:** d['a']['d'] = 10

§ Often the answer to a recursion, not the input

• However, the **key list** is sliceable

§ Helper is recursive, not the main function

§ This requires a helper function

§ Can recurse on key list, not the dict

## But This is Okay

def add\_bonus(grades,bonus):

§ So rare to be used in recursion by itself

"""Gives bonus points to everyone in grades

Precondition: grades has netids as keys, ints as values.

bonus is an int."""

\# No accumulator. This is a procedure

## for student in grades:

## Dictionaries and Recursion

\# Modifies the dictionary, but does not change keys

§ Makes it difficult to do divide and conquer

## Example: JSON File

Nested Dictionary

grades[student] = grades[student]+bonus

"wind" : {"speed" : 13.0, "crosswind" : 5.0 • **JSON:** File w/ Python dict

§ Actually, minor differences

• Dictionaries are **not sliceable**

• weather.json:

}, Nested "sky" : List § Weather measurements at Ithaca Airport (2017)

"cover" : "clouds", "type" : "broken", "height" : 1200.0 § **Keys**: Times (Each hour)

§ **Values**: Weather readings

• This is a nested JSON "type" : "overcast", "height" : 1800.0

Nested Dictionary

§ Values are also dictionaries

§ Containing more dictionaries

§ And also containing lists

## The Recursive Version

def max\_grade\_helper(netids,grades):

"""Returns max grade among given netids

Precond: netids a list of keys in grades, grades a dict w/ int values"""

\# Process small data

if len(netids) <= 1:

return grades[netids[0]] if len(netids) == 1 else 0

\# Break it up into left and right

left = grades[netids[0]]

right = max\_grade\_helper(netids[1:],grades)

\# Combine the answers

return max(left,right)