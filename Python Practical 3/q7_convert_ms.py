n = int(input("Enter time in milliseconds: "))
def convert_ms(n):
    sec = n // 1000
    minu = sec // 60
    hr = minu // 60
    while sec >= 60:
        sec = sec % 60
    while minu >= 60:
        minu = minu % 60
    print("{0}:{1}:{2}".format(hr,minu,sec))
    

convert_ms(n)

