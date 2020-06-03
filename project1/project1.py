#project1.py
from C_func import case

while(1):
    print("시작하려면 1번을 누르시오")
    num = int(input())
    if num==1:
        break
    else:
        continue

print("'내가 골라주마'에 오신 것을 환영합니다")

class Clo:
    def setdata(self, spe, color):
        self.spe = spe
        self.color = color

def Pyo():
    print("상의: 녹색-1 파란색-2 노란색-3 \n 핑크-4 네이비-5 흰색-6\n")
    print("하의: 진청-1 연청-2 베이지-3 \n 카키/차콜-4 검정-5\n ")

def trans_c(a,b):
    if(a==1):
        if(b==1):
            print("녹색")
        elif (b == 2):
            print("파란색")
        elif(b == 3):
            print("노란색")
        elif(b == 4):
            print("핑크색")
        elif (b == 5):
            print("네이비색")
        elif (b == 6):
            print("흰색")
    elif (a == 2):
        if (b == 1):
            print("진청")
        elif (b == 2):
            print("연청")
        elif (b == 3):
            print("베이지")
        elif (b == 4):
            print("카키/차콜")
        elif (b == 5):
            print("검정")



matrix = [[0 for col in range(2)] for row in range(50)]

while(1):
    standNum=int(input("옷장기능 사용은 1번, 빠른기능 사용은 2번 나가기는 3번을 눌러주세요"))
    if standNum==1:
        for i in range(0, 51, 1):
            print("옷장의 옷을 넣으려면 1번을 누르시오(2-출력, 3-나가기)")
            num = int(input())
            if num == 1:
                a = Clo()
                a.spe = int(input("옷의 종류는 무엇입니까?(상의-1),(하의-2)"))
                Pyo()
                a.color = int(input("옷의 색깔은 무엇입니까?"))

                matrix[i][0] = a.spe
                matrix[i][1] = a.color

            elif num == 2:
                print("옷장의 옷들을 출력합니다")
                for x in range(50):
                    for y in range(2):
                        if (matrix[x][y] != 0):
                            if (y == 0):
                                print("Case %d의 옷 종류:" % (x + 1))
                                if (matrix[x][0] == 1):
                                    trans_c(matrix[x][0], matrix[x][1])
                                    print("윗옷")
                                elif (matrix[x][0] == 2):
                                    trans_c(matrix[x][0], matrix[x][1])
                                    print("바지")
            else:
                break

    elif standNum==2:
        while(1):
            array=[0,0]
            Pyo()
            index1=int(input("상의 색깔을 입력하세요"))
            index2=int(input("하의 색깔을 입력하세요\n"))
            array[0]=index1
            array[1]=index2
            result=case(index1,index2)
            if result == 100:
                print("좋은 조합!\n")
            elif result == 80:
                print("나쁘지 않군\n")
            elif result == 50:
                print("별로 추천하지않아\n")
            else:
                print("입지마\n")











