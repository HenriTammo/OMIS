import arvutus
soov = input("romb või ruut")
if soov == "ruut":
    print(arvutus.ruut())
else:
    print(arvutus.romb())