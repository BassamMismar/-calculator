def atm(monye , request):
    if monye < request:
        print ('00')
    if monye > request:
        while monye >=-1:
            if request >=500:
                print ('500')
                monye -= 500
                request -=500

            elif request >=100:
                print ('100'   )
                monye -= 100
                request -=100

            elif request >= 50:
                monye -= 50
                print ('50')
                request -=50

            elif  request >= 10:
                monye -= 10
                print ('10')
                request -=10

            elif  request >= 1:
                print ('1')
                monye -= 1
                request -=1  
            else :
                print('finesh')
                break;

atm(1000 , 1100)