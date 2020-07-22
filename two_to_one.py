def longest(s1, s2):
    # your code
    s1list = []
    
    for i in range(len(s1)):
        if s1[i] not in s1list: 
            s1list.append(s1[i])
    
    for j in range(len(s2)):
        if s2[j] not in s1list: 
            s1list.append(s2[j])

    s1list.sort()
    
    return "".join(s1list)  


print(longest("aretheyhere", "yestheyarehere"))