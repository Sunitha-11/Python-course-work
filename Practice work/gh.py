def check_annagram(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
print(check_annagram("listen", "silent"))  #True