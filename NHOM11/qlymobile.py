#mở và tạo file
import csv
_path="D:/NHOM11/files/ds_mobile.csv"
with open(_path,'w',encoding = 'utf-8') as f:
        f.write('Mã điện thoại','Tên điện thoại','đơn giá','Số Lượng','Chất lượng','Thuế VAT','Tổng tiền')
        f.close()

