print("""
  _ __  _   _ _ __   ___  _ __   
 | '_ \| | | | '_ \ / _ \| '_ \  
 | |_) | |_| | | | | (_) | | | | 
 | .__/ \__, |_| |_|\___/|_| |_| 
 | |     __/ |                   
 |_|    |___/                    
""")
print("[+] Welcome to the pynon! Your ultimate bioinformatics pipeline to evaluate your work.")
print("[Uses:] Just simply input your sequence and see the magic!")

seq = input("[+] Enter your sequence:\n")
count_g = 0
count_c = 0

for digit in seq:
    if digit == "G":
        count_g += 1
    elif digit == "C":
        count_c += 1

print("\n[+] Your sequence has " + str(count_g) + " G's")
print("\n[+] Your sequence has " + str(count_c) + " C's")
