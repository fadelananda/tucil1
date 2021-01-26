# Nama    : Fadel Ananda Dotty
# NIM     : 13519146

import time

name = input("Masukkan nama file: ")

tesCount = 0
f = open("test/" + name, "r")

text=f.readlines()

stripIndex = 0 #mencari index untuk memisahkan operand

for i in range(len(text)): #mencari index berisi strip
    text[i]=text[i].strip()
    if (text[i][0]=="-"):
        stripIndex = i

a = []
for i in range(len(text)): #memasukkan semua operand ke dalam array
    if i<stripIndex:
        a.append(text[i])

a.append(text[stripIndex+1]) #memasukkan result ke dalam array

uniqueCharSet = set("".join(a)) #mengambil karakter unik di dalam array dan merubahnya ke bentuk set, waktu eksekusi program bergantung urutan set yang dibuat

uniqueChar = []
for letter in uniqueCharSet:
    uniqueChar.append(letter) #membuat array karakter unik

keyValue = []
for i in range(len(uniqueChar)):
    keyValue.append(0) #membuat array value yang berkorespondensi dengan array karakter unik dan menginisialisasi dengan 0

result = text[stripIndex+1] #memasukkan result ke dalam variabel
intResult = []
intOperand = []

print("Counting...")
if (len(uniqueChar) > 10): #apabila jumlah karakter unik lebih dari 10, ditampilkan pesan error
    print("Jumlah karakter unik tidak boleh melebihi 10")
else:
    isNotFound = True
    start = time.time() #start timer
    while isNotFound: #looping selama solusi belum ketemu
        sumOperand = 0
        sumRes = 0
        for i in range(len(text)):  #proses untuk mengevaluasi jumlah nilai operand
            if i<stripIndex:
                for k in range(len(text[i])):
                    for j in range(len(uniqueChar)):
                        if(text[i][k] == uniqueChar[j]):
                            intOperand.append(keyValue[j])
                strOperand = [str(integer) for integer in intOperand]
                str1 = "".join(strOperand)
                sumO = int(str1)
                sumOperand = sumOperand + sumO                       
                intOperand = []     
    
        for i in range(len(result)): #proses untuk mengevaluasi jumlah nilai result
            for j in range(len(uniqueChar)):
                if(result[i] == uniqueChar[j]):
                    intResult.append(keyValue[j])

        strRes = [str(integer) for integer in intResult]
        str2 = "".join(strRes)
        sumRes = int(str2)  
        intResult = []

        isUnique = True
        isNotZero = True
        if (sumOperand == sumRes): #apabila jumlah operand sama dengan jumlah hasil
            for i in range(len(text)): #mengevaluasi apakah awalan huruf berupa 0
                for j in range(len(uniqueChar)):
                    if (text[i][0] == uniqueChar[j] and keyValue[j]==0):
                        isNotZero = False

            for i in range(len(keyValue)): #mengevaluasi apakah key value semuanya unik
                for j in range(i+1, len(keyValue)):
                    if (keyValue[i] == keyValue[j]):
                        isUnique = False
            
            if (isUnique and isNotZero): #keluar dari loop apabila solusi ketemu, unik, dan awalan tidak 0
                isNotFound = False
            else:
                for i in range(len(keyValue)): #proses mengubah key value satu persatu
                    if (9 > keyValue[i] and keyValue[i] >= 0):
                        keyValue[i] += 1
                        break
                    elif (keyValue[i] == 9):
                        keyValue[i] = 0
        else:
            for i in range(len(keyValue)): #proses mengubah key value satu persatu
                if (9 > keyValue[i] and keyValue[i] >= 0):
                    keyValue[i] += 1
                    break
                elif (keyValue[i] == 9):
                    keyValue[i] = 0
        tesCount += 1 #menambah tes count
        

end = time.time() #end time

#prosedur print hasil output
print("---SOAL---")
for i in range(len(text)):
    print(text[i].strip())
print("*******************")
print("Karakter unik dalam soal \t: ")
print(uniqueChar)
print("*******************")
print("Tes Count \t= ", end="")
print(tesCount)
print("*******************")
print("Execution Time \t= ", end="")
print(end - start, end="")
print(" Detik")
print("*******************")
print("Solusi \t:")
for i in range(len(keyValue)):
    print(uniqueChar[i], end=" ")
    print("=", end=" ")
    print(keyValue[i], end="")
    if (i != len(keyValue) - 1):
        print(",", end=" ")

print(".")
print("*******************")
print("SOLUSI NUMERIK")
for i in range(len(text)):
    if i<stripIndex:
        for k in range(len(text[i])):
            for j in range(len(uniqueChar)):
                if(text[i][k] == uniqueChar[j]):
                    intOperand.append(keyValue[j])
        strOperand = [str(integer) for integer in intOperand]
        str1 = "".join(strOperand)
        sumO = int(str1)
        print(sumO)               
        intOperand = []

print("----------------------- +")
print(sumRes)
f.close()