import csv
_path="D:/NHOM11/files/ds_mobile.csv"
listmobile = []


print("+--------------------------------------------------+")
print("|                    Menu chức năng                |")
print("|                 1: Mở file danh sách             |")
print("|                 2: Nhập dữ liệu cho file         |")
print("|                 3: Tính thuế VAt                 |")
print("|                 4: Lưu danh sách                 |")
print("|                 5: Sắp xếp cửa hàng              |")
print("+--------------------------------------------------+")

chuc_nang = int(input("Nhập chức năng bạn muốn chọn(1->5)"))


#mở file
with open(_path,'w',encoding = 'utf-8') as f:
        f.write('Mã điện thoại, Tên điện thoại, đơn giá, số Lượng, Chất lượng, Thuế VAT, Tổng tiền')
        f.close()

#nhập thông tin
tt_dien_thoai = []
while True:
        ma_dt = input('Nhập mã điện thoại:')
        ten_dt = input('Nhập tên điện thoại:')
        don_gia = input('Nhập đơn giá:')
        so_luong = input('Nhập số lượng:')
        chat_luong = input('Chất lượng:')
        tt_dien_thoai.append({'Mã điện thoại':ma_dt,'Tên điện thoại':ten_dt,\
             'Đơn giá':don_gia,'Số lượng':so_luong,'Chất lượng':chat_luong})
        print(tt_dien_thoai)
        break

def tinh_vat(x):
        if chat_luong==1:
                x = (don_gia*so_luong/100*30)
        elif chat_luong==2:
                x = (don_gia*so_luong/100*10)
                
def tong_tien(tong):
        tong = don_gia*so_luong             
