import os
import re

lst = []
for current_dir, dirs, files in os.walk("main"):
    for f in files:
        if re.search('.*.py', f):
            lst.append(current_dir)
            break
lst.sort()
with open("output.txt", "w") as out:
    out.write('\n'.join(lst))