
words = input().split()
s_end = []
for i, _ in enumerate(words):
    if words[i].endswith('s'):
        s_end.append(words[i])
        
print('_'.join(s_end))
