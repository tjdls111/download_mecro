import pyautogui as pag
import keyboard
from time import sleep
from PIL import ImageGrab

def fast_download():
    # 이미지 다운로드를 찾아서 클릭
    y_start = 500  # 체크 시작 위치(y좌표)
    y_end = 921  # 얼만큼 체크할지

    red, green, blue = 62, 64, 74  # '이미지 다운로드'버튼의 색깔
    red1, green1, blue1 = 0, 128, 128

    screen = ImageGrab.grab()

    for y in range(y_end, y_start, -1):
        a, b, c = screen.getpixel((910, y))
        if keyboard.is_pressed('F2') == True:
            break
        if (a, b, c) == (red1, green1, blue1):  # 전체 다운로드가 있는 경우(이미지 복수일 때)
            pag.click(910, y-1)
            if keyboard.is_pressed('F2')==True:
                break
            sleep(1)
            if keyboard.is_pressed('F2')==True:
                break
            # 이미지 다운로드 팝업창에서 클릭하는 과정
            screen2 = ImageGrab.grab()
            if keyboard.is_pressed('F2')==True:
                break
            for m in range(713, 980):
                a1, b1, c1 = screen2.getpixel((536, m))
                if keyboard.is_pressed('F2') == True:
                    break
                if (a1, b1, c1) == (0, 128, 128):
                    pag.click(536, m - 580)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(0.3)
                    pag.click(536, m - 343)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(0.3)
                    pag.click(536, m + 7)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(1)
                    pag.click(862, m + 7)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(1)
                    if keyboard.is_pressed('F2') == True:
                        break
                    return 0
        elif (a, b, c) == (red, green, blue):  # 전체 이미지가 단수일 때
            pag.click(910, y-1)
            if keyboard.is_pressed('F2')==True:
                break
            sleep(1)
            if keyboard.is_pressed('F2')==True:
                break
            # 이미지 다운로드 팝업창에서 클릭하는 과정
            screen2 = ImageGrab.grab()
            if keyboard.is_pressed('F2')==True:
                break
            for m in range(704, 950):
                a1, b1, c1 = screen2.getpixel((536, m))
                if keyboard.is_pressed('F2') == True:
                    break
                if (a1, b1, c1) == (0, 128, 128):
                    if keyboard.is_pressed('F2') == True:
                        break
                    pag.click(536, m - 578)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(0.3)
                    if keyboard.is_pressed('F2') == True:
                        break
                    pag.click(536, m - 343)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(0.3)
                    pag.click(536, m + 13)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(1)
                    pag.click(862, m + 13)
                    if keyboard.is_pressed('F2') == True:
                        break
                    sleep(1)
                    return 0
    #만약에 다운로드 버튼이 없으면
    f = open('memo0417_1211.txt', 'a')
    f.write("{}페이지의 {}번째 줄의 {}번째 유물은 다운로드 불가능입니다.".format(num1+1,num2+1,num3+1))
    f.write('\n')
    f.close()

def download(pagenum):
    for page in range(pagenum):
        for i in range(12):  # 세로-12줄(13줄이 있긴 한데 거기는 들쭉날쭉이라서 일단 뺌)
            for j in range(4):  # 가로 4개씩 있음
                global num1
                num1=page
                if keyboard.is_pressed('F2')==True:
                    break
                global num2
                num2=i
                if keyboard.is_pressed('F2')==True:
                    break
                global num3
                num3=j
                if keyboard.is_pressed('F2')==True:
                    break
                print("{}번째 유물 이미지를 다운로드 받는 중입니다.".format(page * 50 + i * 4 + j + 1))
                if keyboard.is_pressed('F2')==True:
                    break

                #print("{}페이지-{}번째 줄-{}번째 유물".format(page,i,j))
                #print("멈추려면 0.5초 안에 F4를 누르세요!")D
                #sleep(0.5)
                #if keyboard.is_pressed('f4'): break  # 반복 종료

                pag.click(476 + (285 * j), 834)
                if keyboard.is_pressed('F2')==True:
                    break
                sleep(2)  # 로딩될 동안 1초 기다리기
                if keyboard.is_pressed('F2')==True:
                    break
                fast_download()
                if keyboard.is_pressed('F2')==True:
                    break
                pag.click(28, 56)  # 뒤로 가기
                if keyboard.is_pressed('F2')==True:
                    break
                sleep(1)  # 로딩될 동안 1초 기다리기
                if keyboard.is_pressed('F2')==True:
                    break

                # 마우스를 적절한 위치에 가져다두기(뒤로 가기 해서 이상한 위치로 갈 경우를 대비)
                if 1 < i:
                    pag.click(1514, 137)
                    if keyboard.is_pressed('F2') == True:
                        break
                    pag.click(clicks=5)
                    if keyboard.is_pressed('F2') == True:
                        break
                    pag.moveTo(1514, 191)
                    if keyboard.is_pressed('F2') == True:
                        break
                    pag.dragTo(1514, 191 + 53 * i, 2, button='left')
                    if keyboard.is_pressed('F2') == True:
                        break

            pag.click(1514, 191 + 53 * i)
            if keyboard.is_pressed('F2') == True:
                break
            pag.dragRel(0, 53, 2, button='left')  # 스크롤 내리기
            if keyboard.is_pressed('F2') == True:
                break

        #마지막 줄
        pag.moveTo(1514, 961)  # 맨 아래로 가게 함
        if keyboard.is_pressed('F2') == True:
            break
        pag.click(clicks=6)
        if keyboard.is_pressed('F2') == True:
            break
        screen3 = ImageGrab.grab()
        if keyboard.is_pressed('F2') == True:
            break
        k_cnt = 0
        for k in range(4):
            if keyboard.is_pressed('F2') == True:
                break
            if screen3.getpixel((364 + 282 * k, 419)) == (220, 219, 219):
                k_cnt = k_cnt + 1
                if keyboard.is_pressed('F2')==True:
                    break
                print("{}번째 유물 이미지를 다운로드 받는 중입니다.".format(page * 50 + 48+k_cnt))
                if keyboard.is_pressed('F2')==True:
                    break
                pag.click(475+(282 * k), 477)
                if keyboard.is_pressed('F2')==True:
                    break
                sleep(2)  # 로딩될 동안 1초 기다리기
                if keyboard.is_pressed('F2')==True:
                    break
                fast_download()
                if keyboard.is_pressed('F2')==True:
                    break
                pag.click(20, 50)  # 뒤로 가기
                if keyboard.is_pressed('F2')==True:
                    break
                sleep(3)  # 로딩될 동안 3초 기다리기
                if keyboard.is_pressed('F2')==True:
                    break
                pag.moveTo(1514, 961)  # 맨 아래로 가게 함
                if keyboard.is_pressed('F2')==True:
                    break
                pag.click(clicks=6)
                if keyboard.is_pressed('F2')==True:
                    break

        # 페이지 넘기기
        pag.moveTo(1514, 953)  # 맨 아래로 가게 함
        if keyboard.is_pressed('F2') == True:
            break
        pag.click(clicks=2)
        if keyboard.is_pressed('F2') == True:
            break
        sleep(1)
        if keyboard.is_pressed('F2') == True:
            break
        if pagenum==10: #10페이지가 꽉 차 있으면
            if page==0: pag.click(767, 721)
            elif page==1: pag.click(809,718)
            elif page==2: pag.click(843,719)
            elif page==3: pag.click(886,720)
            elif page==4:pag.click(922,722)
            elif page==5:pag.click(959,722)
            elif page==6:pag.click(997,722)
            elif page==7:pag.click(1034,722)
            elif page==8:pag.click(1073,722)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break
        elif pagenum==9: #9페이지가 꽉 차 있으면
            if page == 0:
                pag.click(795, 721)
            elif page == 1:
                pag.click(829, 718)
            elif page == 2:
                pag.click(868, 719)
            elif page == 3:
                pag.click(905, 720)
            elif page == 4:
                pag.click(943, 722)
            elif page == 5:
                pag.click(981, 722)
            elif page == 6:
                pag.click(1021, 722)
            elif page == 7:
                pag.click(1057, 722)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break
        elif pagenum==8: #8페이지가 꽉 차 있으면
            if page == 0:
                pag.click(810, 721)
            elif page == 1:
                pag.click(847, 718)
            elif page == 2:
                pag.click(888, 719)
            elif page == 3:
                pag.click(923, 720)
            elif page == 4:
                pag.click(964, 722)
            elif page == 5:
                pag.click(999, 722)
            elif page == 6:
                pag.click(1039, 722)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==7: #7페이지가 꽉 차 있으면
            if page == 0:
                pag.click(830, 721)
            elif page == 1:
                pag.click(867, 718)
            elif page == 2:
                pag.click(903, 719)
            elif page == 3:
                pag.click(942, 720)
            elif page == 4:
                pag.click(984, 722)
            elif page == 5:
                pag.click(1019, 722)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==6: #6페이지가 꽉 차 있으면
            if page == 0:
                pag.click(849, 721)
            elif page == 1:
                pag.click(887, 718)
            elif page == 2:
                pag.click(926, 719)
            elif page == 3:
                pag.click(963, 720)
            elif page == 4:
                pag.click(1002, 722)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==5: #5페이지가 꽉 차 있으면
            if page == 0:
                pag.click(868, 721)
            elif page == 1:
                pag.click(906, 718)
            elif page == 2:
                pag.click(946, 719)
            elif page == 3:
                pag.click(981, 720)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==4: #4페이지가 꽉 차 있으면
            if page == 0:
                pag.click(885, 721)
            elif page == 1:
                pag.click(925, 718)
            elif page == 2:
                pag.click(962, 719)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==3: #3페이지가 꽉 차 있으면
            if page == 0:
                pag.click(905, 721)
            elif page == 1:
                pag.click(943, 718)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==3: #3페이지가 꽉 차 있으면
            if page == 0:
                pag.click(905, 721)
            elif page == 1:
                pag.click(943, 718)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

        elif pagenum==2: #2페이지가 꽉 차 있으면
            if page == 0:
                pag.click(924, 721)
            if keyboard.is_pressed('F2') == True:
                break
            sleep(5)
            if keyboard.is_pressed('F2') == True:
                break

    print("다운로드가 끝났습니다. 감사합니다.")

how_much_page=int(input('50개 가득 찬 페이지가 몇 개인가요? (1-10)'))
download(how_much_page)