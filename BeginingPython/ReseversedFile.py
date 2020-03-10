with open("dataset_24465_4.txt") as fh, open("f2.txt", "w") as ans:
    lst = [line.rstrip() for line in fh]
    lst.reverse()
    ans.write("\n".join(lst))
