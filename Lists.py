def twolists(list1, list2):
    newlist = []
    a1 = len(list1)
    a2 = len(list2)
    for i in range(max(a1,a2)):
        if i <a1:
            newlist.append(list1[i])
        if i <a2:
            newlist.append(list2[i])
    return newlist

def main():
    print (twolists([1,2,3], ['a','b','c','d']))
main()

# Corrected caption: New file not addition of authorship