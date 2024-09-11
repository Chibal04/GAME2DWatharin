import random

def guess_number():
    # สุ่มเลขระหว่าง 1 ถึง 10
    number_to_guess = random.randint(1, 10)
    
    print("ทายเลขระหว่าง 1 ถึง 10")
    
    # ให้ผู้ใช้ทายเลข
    while True:
        try:
            user_guess = int(input("ป้อนเลขที่ทาย: "))
            if 1 <= user_guess <= 10:
                break
            else:
                print("โปรดป้อนเลขระหว่าง 1 ถึง 10")
        except ValueError:
            print("โปรดป้อนเลขจำนวนเต็ม")

    # ตรวจสอบผล
