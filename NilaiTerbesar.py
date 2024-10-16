nilai1=input ("Masukan nilai pertama ")
nilai2=input ("Masukan nilai kedua ")
nilai3=input ("Masukan nilai ketiga ")

if int (nilai1) >= int (nilai2) and int (nilai1) >= int (nilai3):
    print("Nilai terbesar adalah", nilai1)
elif int (nilai2) >= int (nilai1) and int (nilai2) >= int (nilai3):
    print("Nilai terbesar adalah", nilai2)
elif int (nilai3) >= int (nilai1) and int (nilai3) >= int (nilai2):
    print("Nilai terbesar adalah", nilai3)