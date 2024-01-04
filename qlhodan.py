print("")
print("Chức năng \n 1-Nhập thông tin hộ dân \n 2-Xem danh sách hộ dân \n 3-Tính trợ cấp \n 4-Sắp xếp các hộ dân theo thứ tự giảm dần của số thành viên")
print("_______________________________")

# Danh sách các hộ
households = []

while True:
    try:
        # Chọn chức năng để thực hiện
        control = int(input("Chọn chức năng: "))

        # Phím 1 thêm thông tin hộ dân
        if control == 1:
            print("__________________________")
            print("1-Nhập thông tin hộ dân")
            print("")

            # Nhập các thông tin của người dân
            id = int(input("Mã hộ: "))
            name = input("Tên chủ hộ: ")
            number = int(input("Số thành viên: "))
            income = int(input("Thu nhập: "))
            case = input("Hoàn cảnh(N là hộ nghèo/ M là những hộ còn lại ): ")

            # Thêm thông tin vào danh sách
            household = {"id": id, "name": name, "number": number, "income": income, "case": case}
            households.append(household)

        # Phím 2 show danh sách hộ dân
        elif control == 2:
            for household in households:
                print("__________________________")
                print("DANH SÁCH HỘ DÂN")
                print("Mã hộ: ", household["id"])
                print("Tên chủ hộ: ", household["name"])
                print("Số thành viên: ", household["number"])
                print("Thu nhập: ", household["income"], "/tháng")
                print("Hoàn cảnh: ", household["case"])
                print("__________________________")
            
        
        #Phím 3 tính trợ cấp cho từng hộ
        elif control == 3:
            subsidize = int(input("Nhập mã hộ để tính trợ cấp: "))
            print(" ")

            if subsidize == household["id"]:
                print("Mã hộ: ", household["id"])

                if household["case"] == "N" and household["number"] >=5 :
                    print("Trợ cấp: ",1000000*household["number"])
                    print(" ")

                elif household["case"] == "N" and 3<= household["number"] < 5:
                    print("Trợ cấp: ",800000*household["number"])
                    print(" ")

                elif household["case"] == "N" and 1<= household["number"] < 3:
                    print("Trợ cấp: ",500000*household["number"])
                    print(" ")
                
                else:
                    print("Không có trợ cấp")
                    print(" ")
            else:
                print("Không tìm thấy mã hộ")
                print(" ")
        
        elif control == 4:
            # Sắp xếp danh sách theo số thành viên giảm dần
            households_sorted = sorted(households, key=lambda x: x["number"], reverse=True)
            #key=lambda x: x["number"] được sử dụng để xác định phương thức sắp xếp theo số thành viên của mỗi hộ. 
            #Kiểu như là nó sẽ sắp xếp danh sách theo số thành viên giảm dần 

            print("__________________________")
            print("DANH SÁCH HỘ DÂN SAU KHI SẮP XẾP")
            for household in households_sorted:
                print("__________________________")
                print("Mã hộ: ", household["id"])
                print("Tên chủ hộ: ", household["name"])
                print("Số thành viên: ", household["number"])
                print("Thu nhập: ", household["income"], "/tháng")
                print("Hoàn cảnh: ", household["case"])
                print("__________________________")


    except ValueError:
        print("Đầu vào không hợp lệ")

    print(" ")
    control2 = input("Ấn Enter để dừng hoặc ấn phím bất kỳ để tiếp tục ")
    if control2 == "":
        break
    elif control2 != "":
        print(control)