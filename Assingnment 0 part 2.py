num = []
c = 0
while c<5:
  a = int(input(f"Enter a number {c+1}: "))
  num.append(a)
  c += 1
for a in num:
  if a % 2 == 0:
    print(f"{a} is Even")
  else:
    print(f"{a} is Odd")