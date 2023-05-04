print("-----Exercise_8 โปรแกรมสั่งซื้อของ-----")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Wolfkung" and passwordInput == "9876":
    print("----------Welcome----------")
    print("----------- To ------------")
    print("--------Ipeemy Shop--------")
    print("---------รายการสิ้นค้า---------")
    print("1. Wolf Doll (Big size)    : 250 THB")
    print("2. Wolf Doll (Small size)  : 150 THB")
    print("3. Fox Doll  (Big size)    : 250 THB")
    print("4. Fox Doll  (Small size)  : 150 THB")
    print("โปรดเลือกหมายเลขของสิ้นค้าที่ต้องการจะซื้อ")
    userSelected = int(input(">>"))
    if userSelected == 1 or 3:
        amount = int(input("จำนวนสิ้้นค้าที่ต้องการ : "))
        price = 250
        result = price * amount
        print("ราคารวมสิ้นค้าทั้งหมด : ",result,"THB")
        print("ขอบคุณที่มาซื้อสินค้ากับเรา")
        print("-- Ipeemy Shop :) --")
    elif userSelected == 2 or 4:
        amount = int(input("จำนวนสิ้้นค้าที่ต้องการ : "))
        price = 150
        result = price * amount
        print("ราคารวมสิ้นค้าทั้งหมด :",result,"THB")
        print("ขอบคุณที่มาซื้อสินค้ากับเรา")
        print("-- Ipeemy Shop :) --")
else :
    print("----------ขออภัย----------")
    print("--Username หรือ Password--")
    print("-------ของท่านผิดพลาด------")



