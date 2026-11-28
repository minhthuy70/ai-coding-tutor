## SEARCHING AND SORTING ALGORITHMS

(download slides and .py files and follow along!)

6.0001 LECTURE 12

## SEARCH ALGORITHMS

§	search	algorithm	–	method	for	finding	an	item	or group	of	items	with	specific	properAes	within	a collecAon	of	items

§	collecAon	could	be	implicit

◦ example	–	find	square	root	as	a	search	problem

◦ exhausAve	enumeraAon

◦ bisecAon	search

◦ Newton-Raphson

## §	collecAon	could	be	explicit

◦ example	–	is	a	student	record	in	a	stored	collecAon	of data?

## SEARCHING ALGORITHMS

§	linear	search

• **brute	force**	search	(aka	BriAsh	Museum	algorithm)

• 	list	does	not	have	to	be	sorted

§	bisecAon	search

• 	list	**MUST	be	sorted**	to	give	correct	answer

• 	saw	two	different	implementaAons	of	the	algorithm

## LINEAR SEARCH ON UNSORTED LIST: RECAP

```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

§	must	look	through	all	e<u>lements	to	decide	it’s</u>	not	there

§	O(len(L))	for	the	loop	\*	<u>O(1)	to	test	if	e	==	L[i]</u>

§	overall	complexity	is	**O(n)	–	where	n	is	len(L)**

mes wemen ssumue elerostan etriev in cone time

## LINEAR SEARCH ON SORTED LIST: RECAP

```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

§	must	only	look	unAl	reach	a	number	greater	than	e

§	O(len(L))	for	the	loop	\*	O(1)	to	test	if	e	==	L[i]

§	overall	complexity	is	**O(n)	–	where	n	is	len(L)**

## USE BISECTION SEARCH: RECAP

1. Pick	an	index,	i,	that	divides	list	in	half

2. Ask	if L[i] == e

3. If	not,	ask	if	L[i] is	larger	or	smaller	than	e

4. Depending	on	answer,	search	le\_	or	right	half	of L for e

A	new	version	of	a	divide-and-conquer	algorithm

Break	into	smaller	version	of	problem	(smaller	list),	plus some	simple	operaAons

Answer	to	smaller	version	is	answer	to	original	problem

## BISECTION SEARCH IMPLEMENTATION: RECAP

```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```

## COMPLEXITY OF BISECTION SEARCH: RECAP

§	**bisect\_search2**	and	its	helper

• 	O(log	n)	bisecAon	search	calls

• reduce	size	of	problem	by	factor	of	2	on	each	step

• 	pass	list	and	indices	as	parameters

• 	list	never	copied,	just	re-passed	as	pointer

• 	constant	work	inside	funcAon

• à **O(log	n)**

## SEARCHING A SORTED LIST -- n is len(L)

§	using	**linear	search**,	search	for	an	element	is	**O(n)**

§	using	**binary	search**,	can	search	for	an	element	in	**O(log	n)** • 	assumes	the	**list	is	sorted**!

§	when	does	it	make	sense	to	**sort	first	then	search**?

\- SORT + O(log n) < O(n) → SORT < O(n) - O(log n)

• 	when	sorAng	is	less	than	O(n)

## NEVER	TRUE!

• **to	sort	a	collecEon	of	n	elements	must	look	at	each	one	at least	once!**

## AMORTIZED COST -- n is len(L)

§	why	bother	sorAng	first?

§	in	some	cases,	may	**sort	a	list	once**	then	do	**many searches**

§ **AMORTIZE	cost**	of	the	sort	over	many	searches

§	SORT	+	K\*O(log n)	<	K\*O(n)

à	for	large	K,	**SORT	Eme	becomes	irrelevant,**	if cost	of	sorAng	is	small	enough

## SORT ALGORITHMS

§	Want	to	efficiently	sort	a	list	of	entries	(typically numbers)

§	Will	see	a	range	of	methods,	including	one	that	is quite	efficient

## MONKEY SORT

§	aka	bogosort,	stupid sort, slowsort, permutaAon	sort, shotgun	sort

§	to	sort	a	deck	of	cards

• 	throw	them	in	the	air

• 	pick	them	up

• 	are	they	sorted?

• 	repeat	if	not	sorted

## COMPLEXITY OF BOGO SORT

```python
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
```

§	best	case:	**O(n)	where	n	is	len(L)**	to	check	if	sorted

§	worst	case:	O(?)	it	is	**unbounded**	if	really	unlucky

## BUBBLE SORT

§ **compare	consecuEve	pairs** of	elements

§ **swap	elements**	in	pair	such that	smaller	is	first

§ when	reach	end	of	list, **start	over**	again

§ stop	when	**no	more	swaps** have	been	made

§ largest	unsorted	element always	at	end	a\_er	pass,	so at	most	n	passes CC-BY	Hydrargyrum ttps: commons.w me a.org w /File:Bubble\_sort\_animation.gif h // iki di / iki

## COMPLEXITY OF BUBBLE SORT

```python
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
```

§	inner	for	loop	is	for	doing	the	**comparisons**

§	outer	while	loop	is	for	doing	**mulEple	passes**	unAl	no	more swaps

- $O(n^{2})$ where n is len(L) to do len(L)-1 comparisons and len(L)-1 passes

## SELECTION SORT

§	first	step

• 	extract	**minimum	element**

• **swap	it**	with	element	at	**index	0**

§	subsequent	step

• 	in	remaining	sublist,	extract	**minimum	element**

• **swap	it**	with	the	element	at	**index	1**

§	keep	the	le\_	porAon	of	the	list	sorted

• 	at	i’th	step,	**first	i	elements	in	list	are	sorted**

• 	all	other	elements	are	bigger	than	first	i	elements

## ANALYZING SELECTION SORT

## §	loop	invariant

◦ given	prefix	of	list	L[0:i]	and	suffix	L[i+1:len(L)],	then prefix	is	sorted	and	no	element	in	prefix	is	larger	than smallest	element	in	suffix

1. base	case:	prefix	empty,	suffix	whole	list	–	invariant true

2. inducAon	step:	move	minimum	element	from	suffix to	end	of	prefix.		Since	invariant	true	before	move, prefix	sorted	a\_er	append

3. when	exit,	prefix	is	enAre	list,	suffix	empty,	so	sorted

```python
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
    suffixSt += 1

■ outer loop executes len(L) times
■ inner loop executes len(L) - i times
■ complexity of selection sort is O(n²) where n is len(L)
```

## COMPLEXITY OF SELECTION SORT

## MERGE SORT

§	use	a	divide-and-conquer	approach:

1. if	list	is	of	length	0	or	1,	already	sorted

2. if	list	has	more	than	one	element,	split	into	two	lists, and	sort	each

3. merge	sorted	sublists

1. look	at	first	element	of	each,	move	smaller	to	end	of	the result

2. when	one	list	empty,	just	copy	rest	of	other	list

## MERGE SORT

## §	divide	and	conquer

unsorted

unsorted

unsorted

unsorted

unsorted

unsorted

unsorted

unsor ted unsor 1 ted unsor ted unsor ted unsor ted unsor ted unsor ted unsor ted

merge

merge

merge

merge

merge

merge

merge

merge

§ **split	list	in	half**	unAl	have	sublists	of	only	1	element

## MERGE SORT

## §	divide	and	conquer

unsorted

unsorted

unsorted

unsorted

unsorted

unsorted

unsorted

sort

sort

sort

I sort sort

sort

sort

sort

merge

merge

merge

merge

§	merge	such	that	**sublists	will	be	sorted	aQer	merge**

## MERGE SORT

## §	divide	and	conquer

unsorted

unsorted

unsorted

sorted

sorted

sorted

sorted

merge

merge

§	merge	sorted	sublists

§	sublists	will	be	sorted	a\_er	merge

## MERGE SORT

## § divide	and	conquer

unsorted

sorted

sorted

merge

§ merge	sorted	sublists

§	sublists	will	be	sorted	a\_er	merge

## MERGE SORT

## §	divide	and	conquer	–	done!

sorted

## EXAMPLE OF MERGING

| Left in list 1 | Left in list 2 | Compare | Result |
| --- | --- | --- | --- |
| [1,5,12,18,19,20] | [2,3,4,17] | 1,2 | [] |
| [5,12,18,19,20] | [2,3,4,17] | 5,2 | [1] |
| [5,12,18,19,20] | [3,4,17] | 5,3 | [1,2] |
| [5,12,18,19,20] | [4,17] | 5,4 | [1,2,3] |
| [5,12,18,19,20] | [17] | 5,17 | [1,2,3,4] |
| [12,18,19,20] | [17] | 12,17 | [1,2,3,4,5] |
| [18,19,20] | [17] | 18,17 | [1,2,3,4,5,12] |
| [18,19,20] | [] | 18,-- | [1,2,3,4,5,12,17] |
| [] | [] |  | [1,2,3,4,5,12,17,18,19,20] |

## MERGING SUBLISTS STEP

```python
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right): - left and right sublists
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
```

## COMPLEXITY OF MERGING SUBLISTS STEP

§	go	through	two	lists,	only	one	pass

§	compare	only	**smallest	elements	in	each	sublist**

§	O(len(le\_)	+	len(right))	copied	elements

§	O(len(longer	list))	comparisons

§ **linear	in	length	of	the	lists**

## MERGE SORT ALGORITHM -- RECURSIVE

```python
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
```

§ **divide	list**	successively	into	halves

§	depth-first	such	that	**conquer	smallest	pieces	down one	branch**	first	before	moving	to	larger	pieces

## COMPLEXITY OF MERGE SORT

## §	at	first	recursion	level

n/2 elements	in	each	list

$O(n) + O(n) = O(n)$ where	n	is	len(L)

## §	at	second	recursion	level

• n/4 elements	in	each	list

• 	two	merges → O(n) where	n	is	len(L)

§	each	recursion	level	is	O(n)	where	n	is	len(L)

## § dividing	list	in	half	with	each	recursive	call

O(log(n)) where	n	is	len(L)

§	overall	complexity	is	**O(n	log(n))	where	n	is	len(L)**

## SORTING SUMMARY -- n is len(L)

§ bogo	sort

• 	randomness,	unbounded	O()

§	bubble	sort

$O(n^{2})$

§	selecAon	sort

• 	guaranteed	the	first	i	elements	were	sorted

§	merge	sort

§	O(n	log(n))	is	the	fastest	a	sort	can	be

## WHAT HAVE WE SEEN IN 6.0001?

## KEY TOPICS

§	represent	knowledge	with	**data structures**

§ **iteraEon	and	recursion** as	computaAonal	metaphors

§ **abstracEon**	of	procedures	and	data	types

§ **organize	and	modularize**	systems	using	object	classes and	methods

§	different	classes	of	**algorithms**,	searching	and	sorAng

§	**complexity** of	algorithms

## OVERVIEW OF COURSE

§	learn	computaAonal	modes	of thinking

§	begin	to	master	the	art	of computaAonal	problem	solving

§	make	computers	do	what	you	want them	to	do

Hope	we	have	started	you	down	the path	to	being	able	to	think	and	act like	a	computer	scienAst

## WHAT DO COMPUTER SCIENTISTS DO?

§	they	think	computaAonally ◦ 	abstracAons,	algorithms, automated	execuAon

§	just	like	the	three	r’s:		reading, ‘riting,	and	‘rithmeAc	– computaAonal	thinking	is becoming	a	fundamental	skill	that every	well-educated	person	will need

Alan	Turing

Image in the Public [Domain, courtesy of Wikipedia Commons](https://en.wikipedia.org/wiki/Alan_Turing#/media/File:Alan_Turing_Aged_16.jpg).

Ada	Lovelace

Image in the Public [Domain, courtesy of Wikipedia Commons](https://en.wikipedia.org/wiki/Ada_Lovelace#/media/File:Ada_Lovelace.jpg).

## THE THREE A’S OF COMPUTATIONAL THINKING

## §	abstracAon

◦ choosing	the	right	abstracAons

◦ operaAng	in	mulAple	layers	of	abstracAon simultaneously

◦ defining	the	relaAonships	between	the	abstracAon layers

## §	automaAon

◦ think	in	terms	of	mechanizing	our	abstracAons

◦ mechanizaAon	is	possible	–	because	we	have	precise and	exacAng	notaAons	and	models;	and	because	there	is some “machine”	that	can	interpret	our	notaAons

## §	algorithms

◦ language	for	describing	automated	processes

◦ also	allows	abstracAon	of	details

◦ language	for	communicaAng	ideas	&	processes

```python
def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
```

# ASPECTS OF COMPUTATIONAL THINKING

§	how	difficult	is	this	problem and	how	best	can	I	solve	it? ◦ theoreAcal	computer	science gives	precise	meaning	to	these and	related	quesAons	and	their answers

§	thinking	recursively reformulaAng	a	seemingly difficult	problem	into	one which	we	know	how	to	solve reduction,	embedding, transformation, 	simulaAon

O(log	n)	;	O(n)	; O(n	log	n)	; O(n<sup>2</sup>);	O(c<sup>n</sup>)

Image Licensed CC-BY, Courtesy of [Robson#](https://www.flickr.com/photos/_robson_/8952213840) on Flickr.

6.0001 Introduction to Computer Science and Programming in Python Fall 2016

For information about citing these materials or our Terms of Use, visit: [https://ocw.mit.edu/terms](https://ocw.mit.edu/terms).