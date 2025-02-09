def multiply(a,b) :
    return a*b
def add(a,b) :
    return a+b
def subtract(a,b) :
    return a-b
def divide(a,b) :
    if b==0 :
        print("Error: division by zero is not allowed.")
        return None
    return a/b
if __name__ == "__main__":
    print("Simple Calculator")
    x=10
    y=5
    print("Add:", add(x,y) )
    print("Subtract:", subtract(x,y))
    print("Multiply:", multiply(x,y))
    print("Divide:", divide(x,y))

