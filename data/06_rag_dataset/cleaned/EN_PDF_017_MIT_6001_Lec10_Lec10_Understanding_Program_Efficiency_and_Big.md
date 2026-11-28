## UNDERSTANDING PROGRAM EFFICIENCY: 1

(download slides and .py files and follow along!)

6.0001 LECTURE 10

## Today

§	Measuring	orders	of	growth	of	algorithms

§	Big	“Oh”	notaAon

§	Complexity	classes

## WANT TO UNDERSTAND EFFICIENCY OF PROGRAMS

§	computers	are	fast	and	geGng	faster	–	so	maybe	efficient programs	don’t	maLer?

◦ but	data	sets	can	be	very	large	(e.g.,	in	2014,	Google	served 30,000,000,000,000	pages,	covering	100,000,000	GB	–	how	long	to search	brute	force?)

◦ thus,	simple	soluAons	may	simply	not	scale	with	size	in	acceptable manner

§	how	can	we	decide	which	opAon	for	program	is	most	efficient?

## §	separate	!me	and	space	efficiency	of	a	program

§	tradeoff	between	them:

◦ can	someAmes	pre-compute	results	are	stored;	then	use	“lookup”	to retrieve	(e.g.,	memoizaAon	for	Fibonacci)

◦ will	focus	on	Ame	efficiency

## WANT TO UNDERSTAND EFFICIENCY OF PROGRAMS

Challenges	in	understanding	efficiency	of	soluAon	to	a computaAonal	problem:

§	a	program	can	be	**implemented	in	many	different ways**

§	you	can	solve	a	problem	using	only	a	handful	of different	**algorithms**

§ would	like	to	separate	choices	of	implementaAon from	choices	of	more	abstract	algorithm

## HOW TO EVALUATE EFFICIENCY OF PROGRAMS

§	measure	with	a	**!mer**

§ **count**	the	operaAons

§	abstract	noAon	of	**order	of	growth**

```python
import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.clock()
c_to_f(100000)
t1 = time.clock() - t0
Print("t =", t, ":", t1, "s,",")
python
■ recall that import time
importing means to def c_to_f(c):
bring in that class return c*9/5 + 32 into your own file
```

## TIMING A PROGRAM

§	use	Ame	module

§ **start** clock

§ **call** funcAon

§ **stop** clock

## TIMING PROGRAMS IS INCONSISTENT

§	GOAL:	to	evaluate	different	algorithms

§	running	Ame	**varies	between	algorithms**

§	running	Ame	**varies	between	implementa!ons**

§	running	Ame	**varies	between	computers**

§	running	Ame	is	**not	predictable**	based	on	small inputs

§	Ame	varies	for	different	inputs	but cannot	really	express	a	relaAonship between	inputs	and	Ame

```python
def c_to_f(c):
    return c*9.0/5 + 32
```

## COUNTING OPERATIONS

§	assume	these	steps	take **constant	!me**:

• 	mathemaAcal	operaAons

• 	comparisons

• 	assignments

• 	accessing	objects	in	memory

•	then	count	the	number	of operaAons	executed	as funcAon	of	size	of	input def <u>mysum(x):</u>

$$
\begin{array}{c} \text {loop x} \\ \text {times} \end{array}
$$

mysum à	1+3x	ops

## COUNTING OPERATIONS IS BETTER, BUT STILL…

§	GOAL:	to	evaluate	different	algorithms

§	count	**depends	on	algorithm**

§	count	**depends	on	implementa!ons**

§	count	**independent	of	computers**

§	no	clear	definiAon	of	**which	opera!ons**	to	count

§	count	varies	for	different	inputs	and can	come	up	with	a	relaAonship between	inputs	and	the	count

## STILL NEED A BETTER WAY

•	Aming	and	counAng	**evaluate	implementa!ons**

•	Aming	**evaluates	machines**

•	want	to	**evaluate	algorithm**

•	want	to	**evaluate	scalability**

•	want	to	**evaluate	in	terms	of	input	size**

## STILL NEED A BETTER WAY

§	Going	to	focus	on	idea	of	counAng	operaAons	in	an algorithm,	but	not	worry	about	small	variaAons	in implementaAon	(e.g.,	whether	we	take	3	or	4	primiAve operaAons	to	execute	the	steps	of	a	loop)

§	Going	to	focus	on	how	algorithm	performs	when	size of	problem	gets	arbitrarily	large

§	Want	to	relate	Ame	needed	to	complete	a computaAon,	measured	this	way,	against	the	size	of the	input	to	the	problem

§	Need	to	decide	what	to	measure,	given	that	actual number	of	steps	may	depend	on	specifics	of	trial

## NEED TO CHOOSE WHICH INPUT TO USE TO EVALUATE A FUNCTION

§	want	to	express	**efficiency	in	terms	of	size	of	input**,	so need	to	decide	what	your	input	is

§	could	be	an	**integer** --	mysum(x)

§	could	be	**length	of	list** --	list\_sum(L)

§ **you	decide**	when	mulAple	parameters	to	a	funcAon --	search\_for\_elmt(L, e)

## DIFFERENT INPUTS CHANGE HOW THE PROGRAM RUNS

```python
■ a function that searches for an element in a list
def search_for_elmt(L, e):
    for i in L:
        if i == e:
            return True
    return False
```

§	when	e	is	**first	element**	in	the	list	à	BEST	CASE

§	when	e	is	**not	in	list**	à	WORST	CASE

§	when	**look	through	about	half**	of	the	elements	in list	à	AVERAGE	CASE

§	want	to	measure	this	behavior	in	a	general	way

## BEST, AVERAGE, WORST CASES

§	suppose	you	are	given	a	list	L	of	some	length	len(L)

§ **best	case**:	minimum	running	Ame	over	all	possible	inputs of	a	given	size,	len(L)

• 	constant	for	search\_for\_elmt

• 	first	element	in	any	list

of	a	given	size,	len(L) perally this case

• 	pracAcal	measure

§ **worst	case**:	maximum	running	Ame	over	all	possible	inputs of	a	given	size,	len(L)

linear	in	length	of	list	for	search\_for\_elmt

• 	must	search	enAre	list	and	not	find	it

## ORDERS OF GROWTH

## Goals:

§	want	to	evaluate	program’s	efficiency	when	**input	is	very	big**

§	want	to	express	the	**growth	of	program’s	run	!me**	as	input size	grows

§	want	to	put	an	**upper	bound**	on	growth	–	as	Aght	as	possible

§	do	not	need	to	be	precise:	**“order	of”	not	“exact”**	growth

§	we	will	look	at	**largest	factors**	in	run	Ame	(which	secAon	of the	program	will	take	the	longest	to	run?)

§ **thus,	generally	we	want	!ght	upper	bound	on	growth,	as func!on	of	size	of	input,	in	worst	case**

## MEASURING ORDER OF GROWTH: BIG OH NOTATION

§	Big	Oh	notaAon	measures	an	**upper	bound	on	the asympto!c	growth**,	oien	called	order	of	growth

## § Big	Oh	or	O()	is	used	to	describe	worst	case

• 	worst	case	occurs	oien	and	is	the	boLleneck	when	a program	runs

• 	express	rate	of	growth	of	program	relaAve	to	the	input size

• 	evaluate	algorithm	**NOT**	machine	or	implementaAon

## EXACT STEPS vs O()

```python
def fact_iter(n):
    """assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
```

§	computes	factorial

§	number	of	steps:

§	worst	case	asymptoAc	complexity: O(n)

• 	ignore	addiAve	constants

• 	ignore	mulAplicaAve	constants

## WHAT DOES O(N) MEASURE?

§	Interested	in	describing	how	amount	of	Ame	needed grows	as	size	of	(input	to)	problem	grows

§	Thus,	given	an	expression	for	the	number	of operaAons	needed	to	compute	an	algorithm,	want	to know	asymptoAc	behavior	as	size	of	problem	gets	large

§	Hence,	will	focus	on	term	that	grows	most	rapidly	in	a sum	of	terms

§	And	will	ignore	mulAplicaAve	constants,	since	want	to know	how	rapidly	Ame	required	increases	as	increase size	of	input

## SIMPLIFICATION EXAMPLES

§	drop	constants	and	mulAplicaAve	factors

§	focus	on	**dominant	terms**

$o(n^{2}) : n^{2} + 2n + 2$
$o(n^{2}) : n^{2} + 100000n + 3^{1000}$
$o(n) : \log(n) + n + 4$
$o(n \log n) : 0.0001*n*\log(n) + 300n$
$o(3^{n}) : 2n^{30} + 3^{n}$

## TYPES OF ORDERS OF GROWTH

```python
for i in range(n):
    print('a')
for j in range(n*n):
    print('b')
is O(n) + O(n*n) = O(n+n^2) = O(n^2)
```

## ANALYZING PROGRAMS AND THEIR COMPLEXITY

§ **combine** complexity	classes

• 	analyze	statements	inside	funcAons

• 	apply	some	rules,	focus	on	dominant	term

**Law	of	Addi!on**	for	O():

• 	used	with	**sequen!al** statements

• $O(f(n)) + O(g(n))$is$O(f(n) + g(n))$

• 	for	example,

is $O(n) + O(n^{*}n) = O(n+n^{2}) = O(n^{2})$ because	of	dominant	term

## ANALYZING PROGRAMS AND THEIR COMPLEXITY

§ **combine** complexity	classes

• 	analyze	statements	inside	funcAons

• 	apply	some	rules,	focus	on	dominant	term

**Law	of	Mul!plica!on**	for	O():

• 	used	with	**nested** statements/loops

$O(f(n)) * O(g(n))$is$O(f(n) * g(n))$

• 	for	example,

```python
for i in range(n):
    for j in range(n):
        print('a')
} O(n) } n loops, each
O(n)*O(n)
```

is $O(n)^{*}O(n) = O(n^{*}n) = O(n^{2})$ because	the	outer	loop	goes	n Ames	and	the	inner	loop	goes	n	Ames	for	every	outer	loop	iter.

## COMPLEXITY CLASSES

§	O(1)	denotes	constant	running	Ame

§	O(log	n)	denotes	logarithmic	running	Ame

§	O(n)	denotes	linear	running	Ame

§	O(n	log	n)	denotes	log-linear	running	Ame

§	O(n<sup>c</sup>)		denotes	polynomial	running	Ame	(c	is	a constant)

§	O(c<sup>n</sup>)	denotes	exponenAal	running	Ame	(c	is	a constant	being	raised	to	a	power	based	on	size	of input)

## COMPLEXITY CLASSES ORDERED LOW TO HIGH

O(1)

O(log n)

O(n)

O(n log n):

cisa onstan

$O(n^{c})$

O(c<sup>n</sup>)

constant

logarithmic

linear

loglinear

polynomial

exponenAal

## COMPLEXITY GROWTH

| CLASS | n=10 | = 100 | = 1000 | = 1000000 |
| --- | --- | --- | --- | --- |
| O(1) | 1 | 1 | 1 | 1 |
| O(log n) | 1 | 2 | 3 | 6 |
| O(n) | 10 | 100 | 1000 | 1000000 |
| O(n log n) | 10 | 200 | 3000 | 6000000 |
| O(n^2) | 100 | 10000 | 1000000 | 1000000000000 |
| O(2^n) | 1024 | 1267650600228229401496703205376 | 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376 | Good luck!! |

## LINEAR COMPLEXITY

§	Simple	iteraAve	loop	algorithms	are	typically	linear	in complexity

## LINEAR SEARCH ON UNSORTED LIST

```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

§	must	look	through	all	e<u>lements	to	decide	it’s</u>	not	there

§	O(len(L))	for	the	loop	\*	<u>O(1)	to	test	if	e	==	L[i]</u> ◦ O(1	+	4n	+	1)	=	O(4n	+	2)	=	O(n)

§	overall	complexity	is	**O(n)	–	where	n	is	len(L)**

neswemen ssumue elerostan etrievin come time

## CONSTANT TIME LIST ACCESS

§	if	list	is	all	ints ◦ 	i<sup>th</sup>	element	at ◦ base + 4\*i

§if	list	is	heterogeneous ◦ 	indirecAon

◦ 	references	to	other	objects

## LINEAR SEARCH ON SORTED LIST

```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

§	<u>must	onl</u>y	look	unAl	reach	a	number	greater	than	e

§	O(len(L))	for	the	loop	\*	O(1)	to	test	if	e	==	L[i]

§	overall	complexity	is	**O(n)	–	where	n	is	len(L)**

§	**NOTE:**	order	of	growth	is	same,	though	run	Ame	may differ	for	two	search	methods

## LINEAR COMPLEXITY

§	searching	a	list	in	sequence	to	see	if	an	element	is	present

§	add	characters	of	a	string,	assumed	to	be	composed	of decimal	digits

```python
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
■ O(len(s))
```

## LINEAR COMPLEXITY

```python
- complexity often depends on number of iterations
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
- number of times around loop is n
- number of operations inside loop is a constant (in this case, 3 – set i, multiply, set prod)
    ° O(1 + 3n + 1) = O(3n + 2) = O(n)
```

§	overall	just	O(n)

## NESTED LOOPS

§	simple	loops	are	linear	in	complexity

§	what	about	loops	that	have	loops	within	them?

## QUADRATIC COMPLEXITY

determine	if	one	list	is	subset	of	second,	i.e.,	every	element of	first,	appears	in	second	(assume	no	duplicates)

```python
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

## QUADRATIC COMPLEXITY

```python
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

## QUADRATIC COMPLEXITY

```python
find intersection of two lists, return a list with each element
appearing only once
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
```

## QUADRATIC COMPLEXITY

```python
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
first nested loop takes len(L1)*len(L2) steps second loop takes at most len(L1) steps determining if element in list might take len(L1) steps if we assume lists are of roughly same length, then O(len(L1)^2)
```

## O() FOR NESTED LOOPS

```python
def g(n):
    """ assume n >= 0 """
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
```

§	computes	n<sup>2</sup>	very	inefficiently

§	when	dealing	with	nested	loops,	**look	at	the	ranges**

§	nested	loops,	**each	itera!ng	n	!mes**

- $O(n^{2})$

## THIS TIME AND NEXT TIME

§	have	seen	examples	of	loops,	and	nested	loops

§	give	rise	to	linear	and	quadraAc	complexity	algorithms

§	next	Ame,	will	more	carefully	examine	examples	from each	of	the	different	complexity	classes

6.0001 Introduction to Computer Science and Programming in Python Fall 2016

For information about citing these materials or our Terms of Use, visit: [https://ocw.mit.edu/terms](https://ocw.mit.edu/terms).