def suma():
    while True:
        try:
            a = int(input("num1: "))
            b = int(input("num2: "))
            return a+b
        
        except Exception as e:
            print("no se puede pendejo")
            print(f"eror {e}")
            
suma()