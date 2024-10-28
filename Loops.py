# Loops
def main():
    number = get_number()
    meow(number)

def get_number():
    n = int(input("Enter the no of echo: "))
    if n > 0:
        return n
    
def meow(num):
    for _ in range(num):
        print("meow")

if __name__=="__main__":
    main()

