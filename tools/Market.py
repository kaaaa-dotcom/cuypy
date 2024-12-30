import cuy
from services import DB

def add():
    KODE_BARANG=input('Kode Barang : ')
    NAMA_BARANG=input('Nama Barang : ')
    HARGA_BARANG=int(input('Harga Barang : '))
    STOK_BARANG=int(input('Stok Barang : '))

    DB.insert_items(KODE_BARANG, NAMA_BARANG, HARGA_BARANG, STOK_BARANG)

def cek():
    items = DB.fecth_item()
    for item in items:
        id=item[0]
        kode_barang=item[1]
        nama_barang=item[2]
        harga_barang=item[3]
        stok_barang=item[4]
        print(f'''
ID : {id}
KODE : {kode_barang}
{nama_barang} | Rp{harga_barang}
Stock = {stok_barang}
''')
        
def delete():
    ID = int(input("Masukan id yang akan dihapus = "))

    DB.Delete(ID)

def start():
    while True:
        menu = int(input('menu:\n1.Tambah Barang\n2.Cek Barang\n3.Kembali\n4.(Delete)\n\nPilih : '))

        if menu == 1:
            add()
        elif menu == 2:
            cek()
        elif menu == 3:
            cuy.options()
        elif menu == 4:
            delete()
        else:
            break

if __name__ == '__main__':
    start()

