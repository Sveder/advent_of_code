input = """Player 1:
24
22
26
6
14
19
27
17
39
34
40
41
23
30
36
11
28
3
10
21
9
50
32
25
8

Player 2:
48
49
47
15
42
44
5
4
13
7
20
43
12
37
29
18
45
16
1
46
38
35
2
33
31"""

# input = """Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10"""

p1, p2 = input.split("\n\n")

d1 = [int(i) for i in p1.split("\n")[1:]]
d2 = [int(i) for i in p2.split("\n")[1:]]

print(d1, d2)
import copy
import functools

@functools.lru_cache()
def play(d1, d2):
    previous_rounds = []
    d1, d2 = list(d1), list(d2)

    print("Game:", d1, d2)

    while d1 and d2:
        if (d1, d2) in previous_rounds:
            return 1, d1

        previous_rounds.append((list(d1), list(d2)))

        c1, d1 = d1[0], d1[1:]
        c2, d2 = d2[0], d2[1:]

        if len(d1) >= c1 and len(d2) >= c2:
            winner, _ = play(tuple(d1[:c1]), tuple(d2[:c2]))

            if winner == 1:
                d1.append(c1)
                d1.append(c2)

            else:
                d2.append(c2)
                d2.append(c1)

        elif c1 > c2:
            d1.append(c1)
            d1.append(c2)

        elif c1 < c2:
            d2.append(c2)
            d2.append(c1)

        if d1 and not d2:
            return 1, d1
        elif d2 and not d1:
            return 2, d2


winner, deck = play(tuple(d1), tuple(d2))
print("Winner:", winner, " deck:", deck)
print(sum([(i+1) * j for i, j in enumerate(deck[::-1])]))
