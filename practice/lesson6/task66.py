def check(func):
    print(" before deviding")
    func()
    print(" after dividing")
    
@check
def function():
        while True:
            number = int(input("Write your number: "))    
            if number == 0:
                break
            try:
                denominator = int(input(" write denominator: ")) 
                result = number / denominator
                if number % denominator == 0:
                    print(result) 
                #else:
                   #print(" your denominator can't divide number")
            except :
                print("your denominator can't divide number")   
                continue     
