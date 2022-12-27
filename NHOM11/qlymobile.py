#Quản lý hóa đơn
import os, csv
_path="files/ds_mobile.csv"
lstmobile=[]

def mo_file_hoa_don(_path,lstmobile):
    try:
        f=open(_path,'w', encoding ='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='ma_dt':
                continue
            lstmobile.append({'ma_dt':dong[0],'ten_dt':dong[1], 'don_gia':dong[2],'so_luong':dong[3],'chat_luong':dong[4],'thue_vat':dong[5],'tong_tien':dong[6]})
        f.close()
        return 1
    except Exception as ex1:
        print('Khong mở được file hop le ', ex1)
    return

def luu_ds_mobile(_path,lstHoaDon):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['ma_dt','ten_dt','don_gia','so_luong','Chat_luong','thue_vat','tong_tien'])
        for hd in lstmobile:
            csv.writer(f).writerow([hd['ma_dt'],hd['ten_dt'], hd['don_gia'],hd['so_luong'],hd['chat_luong'],hd['thue_vat'],hd['tong_tien']])
        f.close()
        return 1
    except Exception as ex1:
        return 0

def them_hoa_don(lstmobile):
    while True:
        ma_dt = input('Nhập số hóa đơn: ')
        ten_dt=input('Ngày hóa đơn: ')
        don_gia=input('Họ tên khách hàng: ')
        so_luong=input('Địa chỉ khách hàng: ')
        chat_luong=input('Quận : ')
        lstmobile.append({'ma_dt':ma_dt,'ten_dt':ten_dt,\
             'don_gia':don_gia,'so_luong':so_luong,'chat_luong':chat_luong}) 
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
    return

print("+--------------------------------------------------+")
print("|                    Menu chức năng                |")
print("|                 1: Mở file danh sách             |")
print("|                 2: Nhập dữ liệu cho file         |")
print("|                 3: Tính thuế VAt                 |")
print("|                 4: Lưu danh sách                 |")
print("|                 5: Sắp xếp cửa hàng              |")
print("+--------------------------------------------------+")

chucnang = int(input("Nhập chức năng bạn muốn chọn(1->5)"))

if chucnang==1:
    mo_file_hoa_don(_path,lstmobile)
elif chucnang==2:
    luu_ds_mobile(_path,lstmobile)
elif chucnang==3:
    them_hoa_don(lstmobile)