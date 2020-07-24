class Personel():

    def __init__(self , name , surname , age):
        # print("personel verileri", isim, soyisim, yas)

        self.name = name
        self.surname = surname
        self.age = age

    def set_name(self , name):
        self.name = name

    def set_surname(self , surname):
        self.surname = surname

    def set_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def bilgilergoster(self):
        print("*-" * 20)
        print("personelinismi:" , self.isim)
        print("personelinsoyismi:" , self.soyisim)
        print("personelinyasi:" , self.yas)
        print("*-" * 20)

    def printx(self):
        print("aractemizligi")


class Temizlikper(Personel):

    def __init__(self , meslek):
        self.meslek = meslek

    def set_meslek(self , meslek):
        self.meslek = meslek

    def get_meslek(self):
        return self.meslek


if __name__ == '__main__':
    person1 = Personel("Ahmet" , "kumas" , 25)
    print("personel 1 isim: {0} soy ismi : {1} yaşı: {2}".format(person1.get_name() , person1.get_surname() ,
                                                                 person1.get_age()))
    person1.set_name("ÇAĞRI")
    print("personel 1 isim: {0} soy ismi : {1} yaşı: {2}".format(person1.get_name() , person1.get_surname() ,
                                                                 person1.get_age()))
    temizlikci = Temizlikper("ev temizligi")
    print(temizlikci.meslek)
    print(temizlikci.get_meslek())
    print(temizlikci.printx())
