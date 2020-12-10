input = """48
171
156
51
26
6
80
62
65
82
130
97
49
31
142
83
75
20
154
119
56
114
92
33
140
74
118
1
96
44
128
134
121
64
158
27
17
101
59
12
89
88
145
167
11
3
39
43
105
16
170
63
111
2
108
21
146
77
45
52
32
127
147
76
58
37
86
129
57
133
120
163
138
161
139
71
9
141
168
164
124
157
95
25
38
69
87
155
135
15
102
70
34
42
24
50
68
169
10
55
117
30
81
151
100
162
148"""

# input = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
#
# input = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

input = [int(i) for i in input.split("\n")]

cur_jol = 0
jump_list = []

while True:
    if cur_jol + 1 in input:
        jump_list.append(1)
        cur_jol += 1

    elif cur_jol + 2 in input:
        jump_list.append(2)
        cur_jol += 2

    elif cur_jol + 3 in input:
        jump_list.append(3)
        cur_jol += 3
    else:
        break

print("Vals:", jump_list.count(1), jump_list.count(3) + 1)
print("Diffs:", jump_list.count(1) * (jump_list.count(3) + 1))

max = max(input)

import functools

@functools.lru_cache(100000)
def f(cur_jol, input):
    count = 0
    global max

    print("f(", cur_jol, ")")


    if cur_jol == max:
        return 1

    if cur_jol != 0 and cur_jol not in input:
        return 0

    count += f(cur_jol + 1, input)
    count += f(cur_jol + 2, input)
    count += f(cur_jol + 3, input)
    return count

print(f(0, tuple(input)))