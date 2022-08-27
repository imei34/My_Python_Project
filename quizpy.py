import time
import mysql.connector
from datetime import datetime

class Quiziz:
    #class variable
    score = 0
    date_quiz = datetime.now()
    #inisialisasi
    def __init__(self):
        self.__soal = 'df'
        self.__a = 'a'
        self.__b = 'b'
        self.__c = 'c'
        self.__d = 'd'
        self.__benar = ''
        
        
        
    ##setter untuk soal dan jawaban
    def set_soal(self,soal):
        self.__soal = soal
    def set_a(self,a):
        self.__a = a
    def set_b(self,b):
        self.__b = b
    def set_c(self,c):
        self.__c = c
    def set_d(self,d):
        self.__d = d
    def set_benar(self,benar):
        self.__benar = int(benar)

    # getter untuk soal dan jawban
    def getSoal(self):
        return self.__soal
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getBenar(self):
        return self.__benar


#buat list menampung data csv

list_quiz = []
#buka file
with open('soal.csv','r') as input_file:
    for line in input_file:
        kolom = line.split(",")
        # buat object instance yang menampung input file
        quiz = Quiziz()
        quiz.set_soal(kolom[0])
        quiz.set_a(kolom[1])
        quiz.set_b(kolom[2])
        quiz.set_c(kolom[3])
        quiz.set_d(kolom[4])
        quiz.set_benar(kolom[5])
        #tambahkan object instance kedalam list
        list_quiz.append(quiz)

## List Functions
#connect python with mysql
def host_user(user):
    db = mysql.connector.connect(
        host = '<YOUR HOST>',
        user = '<YOUR USER>',
        passwd = '<YOUR PASSWORD>',
        database = user
    )
    return db

#messege welcome
def welcome():
    print("""
    ==============================================
    =     SELAMAT DATANG DI APLIKASI QUIZ PY     =
    =             created by marccel             =
    =                                            =
    =                                            =
    =  1. Daftar quiz                            =
    =  2. Kerjakan quiz                          =
    =  3. Keluar                                 =                                          
    =                                            =
    ==============================================
    """)


welcome()

#function for insert data to databases
def insert_data():
    print("Silahkan masukan identitas anda")
    db = host_user('quizpy')
    npm = input("NPM : ")
    nama = input("Nama mahasiswa: ")
    jurusan = input("Jurusan : ")
    email = input("Email : ")
    passwd = input("Password : ")
    gender = input('Gender (L/P) : '.upper())
    values = (npm,nama,jurusan,email,passwd,gender)
    cursor = db.cursor()
    sql = "INSERT INTO user(npm,nama,jurusan,email,password,gender) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,values)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

def keluar():
    print("Sampai berjumpa lagi :)")

def title():
    print("""
    ---SELAMAT DATANG DIAPLIKASI QUIZ PYTHON---
    """)

def quizku():
    print("Halo kakak yang ganteng/cantik, silahkan masukan identitas anda")
    email = input("Masukan email anda : ")
    password = input("Masukan password anda : ")
    db = host_user('quizpy')
    cursor = db.cursor()
    
    nama_sql = 'SELECT * FROM user WHERE email = "{}" AND password = "{}"'.format(email,password)
    
    cursor.execute(nama_sql)

    result = cursor.fetchall()

    list_user = []
    for i in result:
        for j in i:
            list_user.append(j)
    try:
        if email == list_user[4] and password == list_user[5]:
            print("Login berhasil")
            print(f"Selamat datang {list_user[2]}")
            print(f'login pada {Quiziz.date_quiz}')
            for kuis in list_quiz:
                f = open('data_nilai.csv','a')
                print(f"Jawablah pertanyaan {kuis.getSoal()}")
                print("{}  {}  {}  {}".format(kuis.getA(),kuis.getB(),kuis.getC(),kuis.getD()))
                inputan = input("Pilih jawaban yang benar : ")
                if inputan.lower() == 'a':
                    if kuis.getBenar() == 1: 
                        print("Jawaban anda benar")
                        Quiziz.score+= 10 
                    else:
                        print("Jawaban anda salah")
                elif inputan.lower() == 'b':
                    if kuis.getBenar() == 2: 
                        print("Jawaban anda benar")
                        Quiziz.score+= 10
                    else:
                        print("Jawaban anda salah")
                elif inputan.lower() == 'c':
                    if kuis.getBenar() == 3: 
                        print("Jawaban anda benar")
                        Quiziz.score+= 10
                    else:
                        print("Jawaban anda salah")
                elif inputan.lower() == 'd':
                    if kuis.getBenar() == 4: 
                        print("Jawaban anda benar")
                        Quiziz.score+= 10
                    else:
                        print("Jawaban anda salah")

            print(f""" 
            ===============================
            =    NIM    : {list_user[1]}
            =    Nama   : {list_user[2]}
            =    Prodi  : {list_user[3]}
            =    Gender : {list_user[6]}                
            =    Skor   : {Quiziz.score}
            =    Waktu  : {Quiziz.date_quiz}  
            ===============================
            """)
            f.writelines(str(Quiziz.date_quiz)+","+list_user[1]+','+list_user[2]+','+str(Quiziz.score)+','+list_user[3]+','+list_user[6]+"\n")
            f.close()
    except IndexError:
        print("Nama atau password yang anda masukan salah")

pilih = int(input("Pilih menu : "))
if pilih == 1:
    insert_data()
    print("Silahkan lakukan pengerjaan quiz :)")

elif pilih == 2:
    title()
    quizku()
    keluar()

elif pilih == 3:
    keluar()
    exit()

