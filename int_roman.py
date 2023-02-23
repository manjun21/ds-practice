
def intToRoman(num: int) -> str:
        table = [(1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")]
        res = ""
        for cap,roman in table:
            #d,m = divmod(num,cap)
            d = num // cap
            m = num % cap
            res = res + roman * d
            num = m
        
        return res

num = 1520
print(intToRoman(num))

num = 1994
print(intToRoman(num))

    

