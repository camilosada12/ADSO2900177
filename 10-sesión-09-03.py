  primer ejercicio


      x = 0 
    
    try: 
        x = float(input("digite un numero"))
        
    
        if x % 2 == 0:
            print("el numero es par")
        else:
            print("el numero es impar")
    except:
            print ("debe ser valor numerico ")
    


 segundo ejercicio 
    

    x = 0 
    y = 0
    
    try: 
        x = float(input("digite un numero"))
        y = float(input("digite un segundo numero"))
    
        if x % 2 == 0:
            print("el numero es par")
            if x > 0:
                print("el numero es positivo ")
            else:
                print("el numero es negativo")
        else:
            print("el numero es impar")
    except:
            print ("debe ser valor numerico ")
    
 

tercer ejercicio

      
      try: 
          n1 = float(input("digite el primer número: "))
          n2 = float(input("digite el segundo número: "))
          
          if n2 <0 and n1 % 2 != 0: 
              if n1 > n2:
                  print(n1,"," ,n2)
              else:
                  print(n2,",",n1)
          else:
              if n2 > n1:
                  print(n2,",",n1)
              else:
                  print(n1,",",n2)
      except:
          print("Digito no valido, solo se aceptan números")  


cuarto ejercicio 


    try:
        n1 = float(input("digite el primer número: "))
        n2 = float(input("digite el segundo número: "))
        n3 = float(input("digite el tercer número: "))
    
        if n1 > n2 and n1 > n3:
            print ("el número ",n1," es mayor")
            if n2 > n3:
                print("el número ",n2," es el intermedio")
                if n2 < n3:
                     print("el numero ",n2," es el menor")   
                else:
                    print("el número ",n3," es menor")
            else:
                print("el número ",n3," es el intermedio")
        else:
            if n2 > n1 and n2 > n3:
                print ("el número ",n2," es mayor")
                if n1 > n3:
                    print("el número ",n1," es el intermedio")
                    if n1 < n3:
                        print("el número ",n1," es el menor")   
                    else:
                        print("el número ",n3," es menor")
                else:
                    print("el número ",n3," es el intermedio")
            else:
                if n3 > n1 and n3 > n2:
                    print ("el número ",n3," es mayor")
                    if n1 > n2:
                        print("el número ",n1," es el intermedio")
                        if n1 < n2:
                            print("el número ",n1," es el menor")   
                        else:
                            print("el número ",n2," es menor")
                    else:
                        print("el número ",n2," es el intermedio")
                else:
                    if (n1 == n2 == n3):
                        print("digitos no validos para hacer el proceso")
    except:
        print("Digito no valido, solo se aceptan números")    

