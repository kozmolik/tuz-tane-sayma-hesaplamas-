import time

# Veriler
top = 10**15  # Toplam atom sayısı (kum tanesindeki atom sayısı)
say = 10**9   # Saniyede sayılan atom sayısı
	
def kisayol():
	
	# Toplam süreyi saniye cinsinden hesapla
	total_seconds = top / say
	
	# Gün, ay, yıl hesaplamaları
	seconds_in_a_day = 86400
	seconds_in_a_month = 30.44 * seconds_in_a_day
	seconds_in_a_year = 365.25 * seconds_in_a_day
	
	# Gün cinsinden süre
	days = total_seconds / seconds_in_a_day
	
	# Ay cinsinden süre
	months = total_seconds / seconds_in_a_month
	
	# Yıl cinsinden süre
	years = total_seconds / seconds_in_a_year
	
	# Sonuçları yazdır
	print(f"Toplam süre: {int(days)} gün, {int(months)} ay, {int(years)} yıl")


def uzunhesap():
	yenisay = 0 # Sayma başlangıcı
	saniye = 0 # Saniye
	start_time = time.time() # Başlangıç zamanını al
	while True:
	    yenisay += say # Sayıya 1 milyar ekle
	    saniye += 1 # her saymada 1 saniye arttır
	    print(f"{saniye}. Saniye:", yenisay) # Durumu yazdır
	    
	    if yenisay >= top: # Eğer 10 katrilyonu geçersek
	        dakika = saniye / 60
	        saat = dakika / 60
	        gun = saat / 24
	        ay = gun / 365.25
	        yil = ay / 12
	        dakika = int(dakika)
	        saat = int(saat)
	        gun = int(gun)
	        ay  = int(ay)
	        yil = int(yil)
	        saat = int(saat)
	        print("*" * 20)
	        print(f"Bulundu")
	        print(f"Saniye : {saniye}")
	        print(f"Dakika : {dakika}")
	        print(f"Saat   : {saat}")
	        print(f"Gün    : {gun}")
	        print(f"Ay     : {ay}")
	        print(f"Yıl    : {yil}")
	        print("*" * 20)
	        break # Bulunursa işlemi sonlandır.
	    else:
	        pass
	
	# Bitiş zamanını al
	end_time = time.time()
	
	# Geçen süreyi hesapla
	elapsed_time = end_time - start_time
	print(f"İşlem süresi: {elapsed_time:.6f} saniye")
	print("*" * 20)
	
	
menu = """
  Bir tuzda toplam atom hesaplamak için daniyede 1 milyar atom sayan bir bilgisyar ortalama ne kadar sürede sayardı?
  [1] Kısa Hesap (Formülle)
  [2] Uzun Hesap (Manuel Sayımla)
"""
print(menu)
while True:
	try:
		secenek = input("Seçenek Giriniz: ")
		if secenek.strip() == "1":
			kisayol()
			break
		elif secenek.strip() == "2":
			uzunhesap()
			break
		else:
			print("Yanlış Değer")
	except:
		pass
