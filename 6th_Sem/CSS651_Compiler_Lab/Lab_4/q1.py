L = set(["a", "b", "c", "d", "e"])
D = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

def construct_language(lang):
    result = []
    for item in lang:
        result.append(item)
    return result

# L Union D
LD = L.union(D)
print("L Union D:", construct_language(LD))

# LD
LD_strings = []
for l in L:
    for d in D:
        LD_strings.append(l + d)
print("LD:", LD_strings)

# L(L U D)
LLD = []
for l in L:
    for item in LD:
        LLD.append(l + item)
print("L(L U D):", LLD)
