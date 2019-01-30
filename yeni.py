ad=input("Adınız: ")
sirket=input("Şirketiniz: ")
ofis=input("Ofis: ")

def input():
  c=(ad+ " " +sirket+ " " +ofis)
print(c)

# tersten alma fonksiyonu

def reverse_input():
    b=(c[::-1])
print(b)

#aynı olanların elenmesi fonksiyonu
def remove_duplicates(b):
    yeni = list()
    seen = list()
    for value in b:

        if value not in seen:
            yeni.append(value)
            seen.append(value)
    return yeni

result = remove_duplicates(b)
print(result)






