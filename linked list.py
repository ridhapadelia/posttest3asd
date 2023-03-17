
class Webtoon:
    def __init__(self, title):
        self.title = title
        self.next = None

class WebtoonList:
    def __init__(self):
        self.head = None
    
    def add_webtoon(self, title):
        new_webtoon = Webtoon(title)
        if self.head is None:
            self.head = new_webtoon
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next 
            current_node.next = new_webtoon

    def remove_webtoon(self, key):
        temp = self.head
        if (temp is not None and temp.title == key):
            self.head = temp.next 
            temp = None 
            return
        while(temp is not None):
            if temp.title == key:
                break 
            prev = temptemp = temp.next 
            if(temp==None):
                print("tidak ada")
                return
            prev.next = temp.next
            temp = None


    def favorit_webtoon(self):
        print("======================================================")
        print("================== WEBTOON FAVORIT ===================")
        print("======================================================")
        if self.head is None:
            print("Tidak Ada Favorit")
        else:
            current_node = self.head 
            while current_node is not None:
                print(current_node.title)
                current_node = current_node.next
     
webtoon_list = WebtoonList()

# User menu
def menu():
    while True:
        print("\n======================================================")
        print("                        USER                 ")
        print("======================================================")
        print("1. Tambahkan ke favorit")
        print("2. Hapus Webtoon Favorit")
        print("3. Webtoon Favorit")
        print("4. Keluar")
        choice = input("Masukkan Pilihan : ")
        if choice == '1':
            title = input("Masukkan Judul Webtoon Yang Ingin Ditambahkan : ")
            webtoon_list.add_webtoon(title)
            masukkan = input("tambah webtoon favorit lagi?(y/t): ")
            print("======================================================")
            if masukkan == 'y':
                title = input("Masukkan Judul Webtoon Yang Ingin Ditambahkan : ")
                webtoon_list.add_webtoon(title)
            elif masukkan =='t':
                menu()
            else:
                ("input invalid")

        elif choice == '2':
            title = input("Masukkan Judul Webtoon Yang Ingin Di Hapus : ")
            webtoon_list.remove_webtoon(title)
        elif choice == '3':
            webtoon_list.favorit_webtoon()
        elif choice =='4':
            break
        else:
            print("Pilihan Tidak Ada")


print("\nFOR YOU")
print("BINGUNG MAU BACA APA?\n")
print("*Top*\n""1. Marry My Husband\n""2. WEE!!!\n""3. The Secret Of Angle\n""4. Must Be a Happy Ending\n""5. I'm The Queen in This Life\n")
print("*Top Drama*\n""1. Mistake\n""2. Girl's World\n""3. GOOD/BAD FORTUNE\n""4. QUESTISM\n""5. Reborn Rich\n")
print("*Top Fantasi*\n""1. Troll Trap\n""2. 7 Wonders\n""3. I'm Not That Kind of Talent\n""4. DARK MOON: THE BLOOD ALTAR""5. Eleeced\n")
print("*Top Komedi*\n""1. OTENBA\n""2. Eh, Sorry Kesantet!\n""3. BAD GUY\n""4. My Three Annoying Brothers\n""5. Si Ocong\n")
print("*Top Horor\n""1. The Girl's Trial\n""2. Sinister Stories\n""3. Diary Mystery\n""4. Survived Romance\n""5. Vending Machine Of Death\n")
print("*Top Slice of Life*\n""1. WEE!!!\n""2. Pupus Putus Sekolah\n""3. Bima, Temanku Yang Imut\n""4. Ngopi, yuk!\n""5. Pak Guru Inyong:Pendidikan Khusus")
menu()
