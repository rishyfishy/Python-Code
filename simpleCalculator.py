def isNumber(this):
    if (type(this)==float or type(this)== int):
        return True
    return False
    
def evaluate(expression:str):
    ans = eval(expression)
    if isNumber(ans):
        return ans
    return 1

def main():

    print ("Welcome to the Calculator")
    while True:
        question = input("What would you like to calculate?")
        if (question=="exit" or question=="Exit"):
            break
        print (evaluate(question))

main()