n = int(input("Enter a positive number: ").strip())
if n % 2 == 1:
    print("Weird")
elif n in range(2,6):
    print("Not weird")
elif n in range(6,21):
    print("Weird")
elif n > 20:
    print("Not weird")
