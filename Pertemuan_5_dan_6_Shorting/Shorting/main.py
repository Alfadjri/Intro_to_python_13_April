import random

def random_number_generate(nilai):
    list_data = []
    for i in range(nilai):
        list_data.append(random.randrange(1,100))  
    return list_data



# pengurutan nilai dari yang kecil ke besar (ASCENDING)
# pengurutan nilai def yang besar ke kecil (descending)
def short_bubble(data):
    panjang_data = len(data)
    
    # logic 
    for i in range(panjang_data):
        for j in range(0,panjang_data-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j],data[j+1] = data[j+1],data[j]
                
def selection_short(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        min_index = i 
        for j in range(i+1, panjang_data):
            if data[j] < data[min_index]:
                data[j],data[min_index] = data[min_index],data[j]
        

def main():
    banyak_data = int(input("banyak data yang akan di buat : "))
    list_data = random_number_generate(banyak_data)
    print("List data sebelum di urutkan")
    print(list_data)
    while True:
        selection = input("Tekan y untuk melanjutkan tahap ......")
        match selection:
            case "y":
                break
            case _:
                print("input yang anda masukan Salah tolong tekan Y")
                
    # short_bubble(list_data)
    selection_short(list_data)
    print("List data yang sudah di urutkan")
    print(list_data)


if __name__ == "__main__":
    main()