while True:
    print("\n-----<< CLOCK DURATION COUNTER >>-----\n")
    jam = int(input(">> Masukkan jam    : "))
    menit = int(input(">> Masukkan menit  : "))
    time = str(jam)+':'+str(menit)
    print('\n---<<',time,'>>---\n')

    durasi = int(input(">> Tambahan durasi [menit] : "))
    
    # Time Count
    tambahmenit = menit+durasi
    tambahjam = tambahmenit//60
    menit = tambahmenit%60
    jam = jam+tambahjam
    result = str(jam%24)+":"+str(menit)
    print('\n---<<',result,'>>---\n')

    print('>'+'-'*36+'<')
    end = input('\n>> Lanjut menghitung? [y/n]  : ')
    if end == 'n' or end == 'N': break