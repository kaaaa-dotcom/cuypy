import mysql.connector
# import module mysql jika belum memiliki <pip install mysql-python>

# Hubungkan python dengan mysql server
DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='the market'
)

 # <----bertugas untuk memberitahu apakah sudah connect atau belum

# buat Table pada mysql lalu jalankan dengan python
def insert_items(KODE_BARANG,NAMA_BARANG,HARGA_BARANG,STOK_BARANG):
    cursor = DB.cursor()
    cursor.execute('INSERT INTO tabel_barang (KODE_BARANG,NAMA_BARANG,HARGA_BARANG,STOK_BARANG) VALUES (%s,%s,%s,%s)',
                   (KODE_BARANG,NAMA_BARANG,HARGA_BARANG,STOK_BARANG))
    DB.commit()

    if cursor.rowcount > 0:
        print('\nData berhasil diubah....!\n')
    else:
        print('\nData tidak dapat diubah....!\n')

def fecth_item():
    cursor = DB.cursor()
    cursor.execute('SELECT * FROM tabel_barang')
    return cursor.fetchall()

def Delete(ID):
    cursor = DB.cursor()
    cursor.execute(f"DELETE FROM tabel_barang WHERE `tabel_barang`.`ID` = {ID}")

    DB.commit()

    print(cursor.rowcount,'Data Berhasil dihapus...!')