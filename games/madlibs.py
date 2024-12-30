import cuy

def start():
  while True:
    nama_teman = input("Nama teman : ")
    Alat_transportasi = input("Alat transportasi : ")
    jumlah_waktu = input("Jumlah waktu : ")
    alat_transportasi = input("Alat transportasi : ")
    jenis_tumbuhan = input(" Jenis tumbuhan : ")
    hewan_hewan = input("Hewan-hewan : ")
    Objek_objek = input("Objek-objek : ")
    Tempat = input("Tempat : ")
    Benda = input("Benda : ")
    Benda_lain = input("Benda lain : ")
    nama_hewan = input("Nama hewan : ")
    Nama_karakter = input("Nama karakter : ")
    Konsep_atau_nilai = input("konsep atau nilai : ")


    madlibs = f'''
    {nama_teman} dan aku memutuskan untuk mengunjungi pulau Ajaib. 
    Kami sangat antusias dan tidak sabar untuk melihat apa yang menanti kami di sana.
    Kami berangkat dengan {Alat_transportasi}, dan setelah {jumlah_waktu} perjalanan, akhirnya kami tiba di Pulau Ajaib. 
    Begitu kami turun dari {alat_transportasi}, kami langsung terpesona oleh keindahan pulau tersebut. Pulau ini dipenuhi dengan 
    {jenis_tumbuhan}, {hewan_hewan}, dan {Objek_objek} yang unik.
    
    Kami memutuskan untuk menjelajahi pulau dan menemukan sebuah {Tempat}. Di 
    dalamnya, kami menemukan {Benda} yang sangat berharga. Namun, {nama_teman}
    dengan cerobohnya menjatuhkan {Benda} tersebut dan membuatnya pecah. Kami 
    panik, tapi kemudian kami melihat ada {Benda_lain} yang bisa menggantikan {Benda} 
    yang pecah tadi.
    
    Selama petualangan kami di Pulau Ajaib, kami juga bertemu dengan {nama_hewan} 
    yang sangat lucu dan {Nama_karakter} yang mengajari kami tentang {Konsep_atau_nilai}. 
    Kami belajar banyak hal baru dan mengalami momen-momen tak terlupakan.
    
    Setelah beberapa hari di pulau, kami memutuskan untuk pulang dengan {alat_transportasi}. 
    Kami membawa pulang kenangan indah dan pengalaman yang tak 
    terlupakan dari petualangan kami di Pulau Ajaib.'''

    print(madlibs)

    ex = input('y or n : ')
    if ex == 'n':
       cuy.options()
       break
    elif ex == "y":
       start()
    

if __name__ == "__main__":
    start()