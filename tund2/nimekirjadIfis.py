nimekiri = ["õun", "banaan", "pirn", "aprikoos", "apelsin"]

if len(nimekiri) >= 5:
    print("Suur valik sööki")
elif nimekiri[0] == "õun":
    nimekiri.remove("õun")
    print (nimekiri)
    