import requests
import time
import os
import sys

def Txtkirici():
        os.system("clear")
        yazar = """
            # # # # # # # # # # # # # # #
            #   TXT KIRICI VERSİYON 1   #
            #                           #
            #  Instagram: @hz.fatal1ty  #
            #                           #
            #   Kodlayıcı: HzFatal1ty   #
            #                           #
            #         çıkış = q         #
            # # # # # # # # # # # # # # #
        """
        print(yazar)

        url = input("Site url girin (örn: https://lsntagramcopyright.cf/): ")
        if url == "q" or url == "Q":
            sys.exit()
        liste = [
            "index.txt",
            "kurbanlar.txt",
            "kurban.txt",
            "siktik.txt",
            "bensikerim.txt",
            "mallar.txt",
            "inekler.txt",
            "cerezler.txt",
            "telefon.txt",
            "dusenler.txt",
            "dustu.txt",
            "bakalim.txt",
            "baktik.txt",
            "vayamk.txt",
            "bebeler.txt",
            "bebe.txt",
            "users.txt",
            "kullanicilar.txt",
            "user.txt",
            "kullanici.txt",
            "indexler.txt",
            "indexs.txt",
            "musteriler.txt",
            "musteri.txt",
            "kurbagalar.txt",
            "kurbaga.txt",
            "hacker.txt",
            "hacklendin.txt",
            "enayiler.txt",
            "enayi.txt",
            "siktikseni.txt",
            "sikildin.txt",
            "agla.txt",
            "insanlar.txt",
            "admin.txt",
            "adminler.txt",
            "yonetici.txt",
            "yoneticiler.txt",
            "robot.txt",
            "robotlar.txt",
            "robots.txt",
            "adam.txt",
            "adamlar.txt",
            "kadin.txt",
            "kadinlar.txt",
            "mrrobot.txt",
            "kimlik.txt",
            "kimlikler.txt",
            "txt.txt",
            "dosya.txt",
            "mr.txt",
            "kopek.txt",
            "kopekler.txt",
            "kedi.txt",
            "team.txt",
            "takim.txt",
            "gg.txt",
            "ezik.txt",
            "ezikler.txt",
            "babus.txt",
            "babuslar.txt",
            "kurbanlistesi.txt",
            "liste.txt",
            "listeler.txt",
            "kullanicilistesi.txt",
            "MrRobot.txt",
            "para.txt",
            "cerez.txt",
            "cerezler.txt",
            "çerezler.txt",
            "çerez.txt",
            "düşenler.txt",
            "düşen.txt",
            "düştü.txt",
        ]
        for i in liste:
            try:
                page = requests.get(url + i, allow_redirects=False)
                if page.status_code == 200:
                    res = url + i
                    print("*********************************")
                    print("\n")
                    print("[+] Bulundu: " + res)
                    print("\n")
                    print("*********************************")
                    break
                else:
                    print("[-] Bulunamadı")
            except:
                print("Url'yi Kontrol ediniz.")
                break

Txtkirici()
