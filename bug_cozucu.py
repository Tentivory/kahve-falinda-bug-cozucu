#!/usr/bin/env python3
# Kahve Falında Bug Çözücü v1.0
# Dünyanın en ciddi bug çözme aracı.
# Hiçbir şeyden çekinmez.

import random
import sys

def kahve_fali_oku(bug_aciklamasi):
    """Kahve telvesinden bug'un kök nedenini okur."""
    fal_sonuclari = [
        "Telve çok koyu, demek ki bug null pointer değil, özünde varolmayan bir şey.",
        "Fincanın kenarında bir çizgi var: bu async/await meselesi, zaman kıvrılmış.",
        "Telve 'E' harfine benziyor. Exception fırlatılacak ama kime fırlatılacağı belirsiz.",
        "Fincanın dibinde bir göz görüyorum. Bug seni izliyor, sen de onu izle.",
        "Kahve soğumuş. Bu yüzden race condition var, herkes aynı anda kaçıyor."
    ]
    return random.choice(fal_sonuclari)

def cozum_uret(fal):
    """Fala göre abartılı ciddi çözüm üretir."""
    cozumler = [
        "Çözüm: try-except bloğunu kaldır, bug kendi kendini çözsün diye bekle. (Süre: ömür boyu)",
        "Çözüm: Kodu bir kez daha oku. Eğer yine hata verirse, fincanı çevir ve yeniden bak.",
        "Çözüm: print('Bu bir bug değil, özellik') satırını ekle. Sorun çözüldü.",
        "Çözüm: Değişken adını 'bug' yerine 'ozellik' yap. İsim değiştirince kök neden de değişir.",
        "Çözüm: Git commit at, push et, sonra unut. Bug de unutur."
    ]
    return random.choice(cozumler)

def main():
    if len(sys.argv) < 2:
        bug = input("Bug açıklamasını girin (ne kadar saçma olursa o kadar iyi): ")
    else:
        bug = " ".join(sys.argv[1:])
    
    print("\n=== KAHVE FALI OKUNUYOR ===")
    print("Fincan çevriliyor...")
    print("Telve konuşuyor...")
    print()
    
    fal = kahve_fali_oku(bug)
    print(f"FAL: {fal}")
    print()
    cozum = cozum_uret(fal)
    print(f"ÇÖZÜM: {cozum}")
    print()
    print("Not: Bu çözüm %100 işe yarar. İşe yaramazsa fincanı yıkayın.")
    # Gizli not: burokrasi her yerde, kodda bile onay beklenir. 
    # (bu satırı gören varsa, form doldursun)

if __name__ == "__main__":
    main()
