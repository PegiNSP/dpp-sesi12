print("menghitung kemunculan huruf besar")
print("=================================")

def kalimat(kata):
    hurufBesar=0
    for kar in kata:
        if kar.isupper():
            hurufBesar = hurufBesar + 1
    print("banyaknya huruf besar adalah: ", hurufBesar)

