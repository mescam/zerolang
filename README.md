zerolang
========

Zero Language - just simple esoteric programming language highly inspired by brainfuck and Zeroists, for fun only ;)

###examples
````bash
mescam@armisael ~/P/ZeroLang:master> ./zero.py hello.zero 
zero world!
````
````bash
mescam@armisael ~/P/ZeroLang:master> ./zero.py fib.zero 
15
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
````

###instructions
instruction | descrption
--- | ---
0+ | increment pointer (```ptr++```)
0- | decrement pointer (```ptr--```)
0++ | increment value (```(*ptr)++```)
0-- | decrement value (```(*ptr)--```)
0/ | loop (sth like ```while(*ptr) {```)
/0 | end loop (ends 0/)
0. | print as ascii
0, | print as integer
0? | read as ascii
0; | read as integer

###todo
nothing ;)

###author
Jakub Woźniak
