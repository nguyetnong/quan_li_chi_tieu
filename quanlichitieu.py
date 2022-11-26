list_chitieu=[]
def themchitieu():
    tenthuchi=input("nhap ten thu chi:")
    sotien=float(input("nhap so tien:"))
    thoigian=input("nhap thoi gian thu chi:")
    khoanchi={"tenthuchi":tenthuchi,"sotien":sotien,"thoigian":thoigian}
    list_chitieu.append(khoanchi)
    

def xem_all():
    for khoanchi in list_chitieu:
        print(khoanchi)

def xem_theo_ten():
    item=input("nhap ten thu chi muon xem:")
    for khoanchi in list_chitieu:
        if item== khoanchi["tenthuchi"]:
            print(khoanchi)
sum=0
def xem_theo_ngay():
    ngay=input("nhap ngay can xem:")
    exist = False
    for khoanchi in list_chitieu:
        if ngay==khoanchi["thoigian"]:
            exist = True
            print(khoanchi)

    if exist == False:
        print("khong co ngay nao het")

array_ngay=[]
sum=0
def xem_ngay_den_ngay():
    array_ngay=input("nhap ngay bat dau_ngay ket thuc xem:")
    array_ngay_split=array_ngay.split()
    a=int(array_ngay_split[0])
    b=int(array_ngay_split[1])
    if a>b:
        print("ngay ket tthuc can lon hon ngay bat dau:a<b"  )
    else:
        for khoanchi in list_chitieu:   
            for i in range (a,b+1):               
                if i== int(khoanchi["thoigian"]):
                    print(khoanchi)

def xoa_all():
    list_chitieu.clear()

def xoa_theo_ten():
    item=input("nhap ten thu chi muon xoa:")
    for i in list_chitieu:
        if item==i["tenthuchi"]:
            list_chitieu.remove(i)  

def so_du(tongvon,tongchi):
    return tongvon-tongchi


while True:
    hanhdong = input("Nhap hanh dong cua ban : ")
    if hanhdong =='them':
        themchitieu()
    elif hanhdong =='xem_all':
        xem_all()
    elif hanhdong =='xem_theo_ngay':
        xem_theo_ngay()
    elif hanhdong == 'xem_tu_ngay_den_ngay':
        xem_ngay_den_ngay()
    elif hanhdong == 'xoa_all':
        xoa_all()
    elif hanhdong == 'xoa_theo_ten':
        xoa_theo_ten()
    else:
        print("khong co hanh dong nao phu hop")
            
               



    






        


