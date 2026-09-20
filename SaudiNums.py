import random

nums=[]

print("\n Script create saudi phone numbers without duplucated\n")
print("          L  A  Y  A  N\n\n")
print("            &&&   &&& ")
print("           &&&&& &&&&&")
print("            &&&&&&&&&")
print("             &&&&&&&")
print("               &&&")
print("                &\n\n\n\n")
while True:
    x = int(input("how many saudi numbers you want?: "))
    for i in range(x):
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        num = ''.join([random.choice(numbers) for i in range(8)])
        if num not in nums:
            nums.append("05"+str(num))
            print("05"+ str(num))
        else:
            continue

