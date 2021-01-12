s = set()
s.add(20)
s.add(20.0) ##  in python it takes only one times as it shares same value in integer and float
s.add("20")
print(s)
print(len(s))
