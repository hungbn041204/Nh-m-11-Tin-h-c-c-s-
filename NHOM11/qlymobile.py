print("Nhập số để chọn chức năng bạn muốn dùng \n Số 1: Mở file danh sách mobile \n Số 2: Nhập thông tin điện thoại từ bàn phím, không nhập tổng tiền và thuế VAT \n Số 3: Tính VAT của các mặt hàng \n Số 4: Lưu danh sách các điện thoại \n Số 5: Sắp xếp các của hàng và in ra danh sách trước và sau sắp xếp")
def chuc_nang_1():
    return "chuc nang 1"
def chuc_nang_2():
    return "Nhập thông tin"
def chuc_nang_3():
    return "Tính thuế VAT"
def chuc_nang_4():
    return "Lưu danh sách với đầy đủ thông tin"
def chuc_nang_5():
    return "Sắp xếp cửa hàng và in"

def menu(x):
    switcher = {
        1: chuc_nang_1(),
        2: chuc_nang_2(),
        3: chuc_nang_3(),
        4: chuc_nang_4(),
        5: chuc_nang_5(),
    }
    return switcher.get(x, "nothing")
print(menu(int(input("Nhập chức năng bạn cần chọn:"))))





