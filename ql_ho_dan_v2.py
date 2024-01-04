#File này để nhập thông tin để lưu vào bên module xu_ly_thong_tin_ho_dan.py

from libs.xu_ly_thong_tin_ho_dan import *

print("")
print("Chức năng \n 1-Nhập thông tin hộ dân \n 2-Xem danh sách hộ dân \n 3-Tính trợ cấp \n 4-Sắp xếp các hộ dân theo thứ tự giảm dần của số thành viên\n 5-Các hộ dân có thu nhập nhỏ nhất\n 6-Xóa thông tin hộ dân\n 7-Thống kê mức thu nhập\n 8-Lọc hộ dân theo mức thu nhập\n 9-Hộ dân có trợ cấp cao nhất")
print("_______________________________")


# Danh sách các hộ
ds_ho_dan = []
ds_ho_dan = mo_file()

def mo_file_excel():
    try:
        return pd.read_excel("ds_ho_dan.xlsx").to_dict('records')
    except FileNotFoundError:
        return []

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
            ma_ho = input("Mã hộ: ")
            chu_ho = input("Tên chủ hộ: ")
            so_tv = int(input("Số thành viên: "))
            muc_tn = int(input("Thu nhập: "))
            ho_ngheo = input("Hoàn cảnh(N là hộ nghèo/ M là những hộ còn lại ): ")

            # Thêm thông tin vào danh sách
            ho_dan = them_thong_tin_ho_dan(ma_ho, chu_ho, so_tv, muc_tn, ho_ngheo)
            ds_ho_dan.append(ho_dan)
            luu_file(ds_ho_dan)

        # Phím 2 show danh sách hộ dân
        elif control == 2:
            in_danh_sach_ho_dan(ds_ho_dan)
            luu_file(ds_ho_dan)
        # Phím 3 tính trợ cấp cho từng hộ
        elif control == 3:
            subsidize = input("Nhập mã hộ để tính trợ cấp: ")
            print(" ")
            tinh_tro_cap_theo_ma_ho(ds_ho_dan, subsidize)
            luu_file(ds_ho_dan)
            

        # Phím 4 sắp xếp các hộ dân theo thứ tự giảm dần của số thành viên
        elif control == 4:
            # Sắp xếp danh sách theo số thành viên giảm dần
            ds_ho_dan = sorted(ds_ho_dan, key=lambda x: x["so_tv"], reverse=True)

            print("__________________________")
            print("DANH SÁCH HỘ DÂN SAU KHI SẮP XẾP")
            in_danh_sach_ho_dan(ds_ho_dan)
            luu_file(ds_ho_dan)

        elif control == 5:
            thu_nhap_thap_nhat(ds_ho_dan)
            luu_file(ds_ho_dan)

        elif control == 6:
            ten_chu_ho = input("Nhập tên chủ hộ để xóa: ")
            ds_ho_dan = xoa_ho_dan(ds_ho_dan, ten_chu_ho)
            luu_file(ds_ho_dan)

        elif control == 7:
            thong_ke_muc_thu_nhap(ds_ho_dan)
            luu_file(ds_ho_dan)

        elif control == 8:
            muc_tn = int(input("Nhập mức thu nhập để lọc: "))
            ket_qua_loc = loc_theo_muc_thu_nhap(ds_ho_dan, muc_tn)
            in_danh_sach_ho_dan(ket_qua_loc)
            luu_file(ds_ho_dan)
            
        elif control == 9:
            tro_cap_cao_nhat(ds_ho_dan)
            luu_file(ds_ho_dan)

    except ValueError:
        print("Đầu vào không hợp lệ")

    print(" ")
    control2 = input("Ấn Enter để dừng hoặc ấn phím bất kỳ để tiếp tục ")
    if control2 == "":
        break
    elif control2 != "":
        print(control)

# Lưu lại danh sách sau khi thoát chương trình
def luu_file(danh_sach):
    danh_sach_df = pd.DataFrame(danh_sach)
    danh_sach_df.to_excel("ds_ho_dan.xlsx", index=False, engine='openpyxl')

ds_ho_dan = mo_file_excel()
luu_file(ds_ho_dan)
