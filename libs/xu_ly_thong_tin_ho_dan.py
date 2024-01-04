#File này để lưu thông tin

import pandas as pd

def mo_file():
    try:
        return pd.read_excel("ds_ho_dan.xlsx").to_dict('records')
    except FileNotFoundError:
        return []
    
def them_thong_tin_ho_dan(ma_ho, chu_ho, so_tv, muc_tn, ho_ngheo):
    return {"ma_ho": ma_ho, "chu_ho": chu_ho, "so_tv": so_tv, "muc_tn": muc_tn, "ho_ngheo": ho_ngheo, "tro_cap": 0}

def in_danh_sach_ho_dan(danh_sach):
    print("__________________________")
    for ho_dan in danh_sach:
        print("Mã hộ: ", ho_dan["ma_ho"])
        print("Tên chủ hộ: ", ho_dan["chu_ho"])
        print("Số thành viên: ", ho_dan["so_tv"])
        print("Thu nhập: ", ho_dan["muc_tn"], "/tháng")
        print("Hoàn cảnh: ", ho_dan["ho_ngheo"] if ho_dan["ho_ngheo"] else "Không nghèo")
        print("__________________________")

def luu_file(danh_sach):
    df = pd.DataFrame(danh_sach)
    df.to_excel("ds_ho_dan.xlsx", index=False)
    
def tinh_tro_cap_theo_ma_ho(ds_ho_dan, ma_ho):
    for ho_dan in ds_ho_dan:
        if ho_dan["ma_ho"] == ma_ho:
            print("Mã hộ: ", ho_dan["ma_ho"])

            if ho_dan["ho_ngheo"] == "N" and ho_dan["so_tv"] >= 5:
                tro_cap = 1000000 * ho_dan["so_tv"]
                print(f"Trợ cấp: {tro_cap}")
                ho_dan["tro_cap"] = tro_cap
                print(" ")

            elif ho_dan["ho_ngheo"] == "N" and 3 <= ho_dan["so_tv"] < 5:
                tro_cap = 800000 * ho_dan["so_tv"]
                print(f"Trợ cấp: {tro_cap}")
                ho_dan["tro_cap"] = tro_cap
                print(" ")

            elif ho_dan["ho_ngheo"] == "N" and 1 <= ho_dan["so_tv"] < 3:
                tro_cap = 500000 * ho_dan["so_tv"]
                print(f"Trợ cấp: {tro_cap}")
                ho_dan["tro_cap"] = tro_cap
                print(" ")

            else:
                print("Không có trợ cấp")
                print(" ")
            return

    print("Không tìm thấy mã hộ")
    print(" ")

#In thông tin các hộ dân thu nhập nhỏ nhất
def thu_nhap_thap_nhat(danh_sach):
    if not danh_sach:
        return None
    return min(danh_sach, key=lambda x: x["muc_tn"])

#Xóa khỏi danh sách hộ dân
def xoa_ho_dan(danh_sach, ten_chu_ho):
    return [ho_dan for ho_dan in danh_sach if ho_dan["chu_ho"] != ten_chu_ho]

#Thống kê mức thu nhập
def thong_ke_muc_thu_nhap(danh_sach):
    return sum(ho_dan["muc_tn"] for ho_dan in danh_sach)

#Lọc hộ dân theo mức thu nhập
def loc_theo_muc_thu_nhap(danh_sach, muc_tn):
    return [ho_dan for ho_dan in danh_sach if ho_dan["muc_tn"] == muc_tn]

#Hộ dân có trợ cấp cao nhất
def tro_cap_cao_nhat(danh_sach):
    if not danh_sach:
        return None
    return max(danh_sach, key=lambda x: x["tro_cap"])
