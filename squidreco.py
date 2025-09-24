

import os
import time
import webbrowser

print("Bilgisayarın öldü... 😵")
time.sleep(2)
print("Hayatta kalmak için tek şansın Squid Game'e katılmak.")
time.sleep(2)

choice = input("Katılmak için 'evet' yaz ve Enter'a bas: ")

if choice.lower() == "evet":
    print("Katılım onaylandı. Recep İvedik seni almaya geliyor... 😱")
    time.sleep(2)

    # Jumpscare görseli açılıyor (düzeltilmiş link)
    webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbzQN4ZnAT1XBz2q7HHnT2MJAUCkz1AkkNsA&s")

    time.sleep(10)  # Görsel açıldıktan sonra biraz bekle

    # CMD pencereleri açılmaya başlıyor
    for i in range(1000098000000000000000000000000000000000000):  # Sayıyı artırırsan daha çok pencere açılır
        os.system('start cmd /k echo Squid Game\'e hoş geldin!')
        time.sleep(0.1)
else:
    print("Katılmadın. Bilgisayar sonsuza dek karanlıkta kalacak... 💀")

