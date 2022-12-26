#Quản lý hóa đơn
import csv
#from csv import reader
_path="files/ds_mobile.csv"
List_mobile=[]

#lưu và tạo
def luu_ds_hoa_don(_path,List_mobile):
    try:
        f=open(_path,'w+',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['Mã điện thoại','Tên điện thoại','đơn giá','Số Lượng','Chất lượng','Thuế VAT','Tổng tiền','tam_ung','con_lai'])
        for hd in List_mobile:
            csv.writer(f).writerow([hd['Mã điện thoại'],hd['Tên điện thoại'], hd['đơn giá'],hd['Số lượng'],hd['Chất lượng'],hd['Thuế VAT'],hd['Tổng tiền']])
        f.close()
        return 1
    except Exception as ex1:
        return 0


