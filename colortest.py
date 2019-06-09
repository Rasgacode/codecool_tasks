lista = [2, 4, 8, 16, 1024, 32, 64, 128, 256, 512]
colors = {
    4: "\033[91m   4\033[00m",
    8: "\033[92m   8\033[00m", 
    16: "\033[93m  16\033[00m", 
    32: "\033[94m  32\033[00m", 
    64: "\033[96m  64\033[00m", 
    128: "\033[97m 128\033[00m", 
    256: "\033[33m 256\033[00m", 
    512: "\033[34m 512\033[00m", 
    1024: "\033[95m1024\033[00m"
}
for x in range(10):
    for key, value in colors.items():
        if lista[x] == key:
            print("|"+value, end="")
    if x == 2 or x == 4 or x == 6 or x == 8:
        print("|")