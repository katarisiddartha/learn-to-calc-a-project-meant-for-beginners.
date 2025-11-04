def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Error (divide by zero)"

def main():
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Exit")
        ch = int(input("Enter choice: "))
        if ch == 5: break
        a,b = map(float, input("Enter two numbers: ").split())
        if ch==1: print("Result:", add(a,b))
        elif ch==2: print("Result:", sub(a,b))
        elif ch==3: print("Result:", mul(a,b))
        elif ch==4: print("Result:", div(a,b))
        else: print("Invalid choice!")
main()
