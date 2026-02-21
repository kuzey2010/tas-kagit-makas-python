"""
Rock Paper Scissors - Taş Kağıt Makas Oyunu
Kullanıcı ile bilgisayar arasında oynanan klasik oyun.
"""

import random

print("--- Rock Paper Scissors ---")
choice = input("rock / paper / scissors (r / p / s): ").strip().lower()

if choice == "r":
    print("Rock seçtin")
elif choice == "s":
    print("Scissors seçtin")
elif choice == "p":
    print("Paper seçtin")
else:
    print("Geçersiz seçim. r, p veya s girin.")
    exit()

randomchoice = random.choice(["r", "p", "s"])
print("Bilgisayar seçti:", randomchoice)

if choice == randomchoice:
    print("Sonuç: Berabere")
elif randomchoice == "r":
    if choice == "s":
        print("Sonuç: Kaybettin")
    else:
        print("Sonuç: Kazandın")
elif randomchoice == "s":
    if choice == "p":
        print("Sonuç: Kaybettin")
    else:
        print("Sonuç: Kazandın")
elif randomchoice == "p":
    if choice == "r":
        print("Sonuç: Kaybettin")
    else:
        print("Sonuç: Kazandın")
