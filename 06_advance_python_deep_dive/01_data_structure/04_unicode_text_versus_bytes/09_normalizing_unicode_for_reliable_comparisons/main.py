s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1, s2)  # Output: ('café', 'café')
print(len(s1), len(s2))  # Output: (4, 5)
print(s1 == s2)  # Output: False
