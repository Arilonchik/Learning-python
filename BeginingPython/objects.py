ans = 0
mn = []
for obj in objects: # доступная переменная objects
    if obj not in mn:
        mn.append(obj)
ans = len(mn)
print(ans)
#############
print(len(set(map(id, objects))))
