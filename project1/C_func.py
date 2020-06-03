# C_func.py

def case(a,b):
    if(a==1):  #상의가 녹색일때
        if((b==1)|(b==3)):
                result=80;
        elif(b==2):
                result=100;
        elif(b==4):
                result=0;
        elif(b==5):
                result=50;
    if (a == 2):  # 상의가 파란색일때
        if ((b == 3) | (b == 5)):
            result = 80;
        elif (b == 1):
            result = 100;
        elif (b == 4):
            result = 0;
        elif (b == 2):
            result = 50;
    if (a == 3):  # 상의가 노란색일때
        if ((b == 1) | (b == 5)):
            result = 100;
        elif (b == 4):
            result = 80;
        elif (b == 2):
            result = 0;
        elif (b == 3):
            result = 50;
    if (a == 4):  # 상의가 핑크색일때
        if ((b == 4) | (b == 3)):
            result = 50;
        elif (b == 2):
            result = 100;
        elif ((b == 5)|(b==1)):
            result = 80;
    if (a == 5):  # 상의가 네이비색일때
        if ((b == 3) | (b == 4)):
            result = 100;
        elif (b == 2):
            result = 80;
        elif (b == 1):
            result = 0;
        elif (b == 4):
            result = 50;
    if (a == 6):  # 상의가 흰색일때
        if (b ==4):
            result = 80;
        else:
            result =100;
    return result;
