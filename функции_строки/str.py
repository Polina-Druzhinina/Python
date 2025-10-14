def summ(a,b):
    """Документация работы функции""" #документация функции(summ.__doc__)
    if isinstance(a,(int, float)) and isinstance(b,(int, float)):
        return a+b
    if isinstance(a,str) and isinstance(b,(int, float)):
        return a + str(b)

k = ["gfddf","efsa","bfgd","vaw","vfdg"]
print("--".join(k))
