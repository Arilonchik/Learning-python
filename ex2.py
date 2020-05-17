def check_pals_order(s):
    if len(s) == 0:
        return
    global palindroms_inorder
    for i in range(len(s)-1, 0, -1):
        a = s[0]
        b = s[i]
        if s[i] == s[0]:
            suspicion = s[0:i+1]
            if suspicion == suspicion[::-1]:
                palindroms_inorder.append(suspicion)
                c = s[i+1:]
                check_pals_order(s[i+1:])
                return len(suspicion)
    palindroms_inorder.append(s[0])
    check_pals_order(s[1:])
    return 0


def check_pals_out(s):
    if len(s) == 0:
        return
    global palindroms_outorder
    for i in range(0, len(s)-1):
        a = s[-1]
        b = s[i]
        if s[i] == s[-1]:
            suspicion = s[i:]
            if suspicion == suspicion[::-1]:
                palindroms_outorder.append(suspicion)
                c = s[:i]
                check_pals_out(s[:i])
                return len(suspicion)
    palindroms_outorder.append(s[-1])
    check_pals_out(s[:-1])
    return 0


string = input()
palindroms_inorder = []
palindroms_outorder = []
check_pals_order(string)
check_pals_out(string)

if len(palindroms_inorder) <= len(palindroms_outorder):
    print(len(palindroms_inorder))
    for p in palindroms_inorder:
        print(p, end=' ')
else:
    palindroms_outorder.reverse()
    print(len(palindroms_outorder))
    for p in palindroms_outorder:
        print(p, end=' ')
