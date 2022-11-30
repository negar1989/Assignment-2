number=int(input("number in second:"))
hour=number//3600
r=number-(3600*hour)
minute=r//60
second=r-(minute*60)


print(f"{hour}:{minute}:{second}")