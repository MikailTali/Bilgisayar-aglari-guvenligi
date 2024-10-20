# Başlangıç Değeri (İlk Kullanılabilir IP Adresi):
#           Başlangıç değeri, ağ adresinin bir fazlasıdır. Yani, ağ adresine 1 eklenir:
#           Başlangıç Değeri = Ağ Adresi +1
# Bitiş Değeri (Son Kullanılabilir IP Adresi):
#           Bitiş değeri, ağ adresi ve toplam IP adresi sayısının toplamından bir eksiktir:
#           


import ipaddress

def Mikail_Tali(ağ_adresi, subnet_maskesi):
    network = ipaddress.ip_network(f"{ağ_adresi}/{subnet_maskesi}", strict=False) # strict=False bu parametre, IP adresinin ağ adresi olmasını zorunlu kılmaz.
    
    print(f"Ağ Adresi: {network.network_address}")
    print(f"Kullanılabilir IP Sayısı: {network.num_addresses - 2}")  # ağ adresi ve yayın adresi kullanmadığından -2 yapıyoruz

    print("Kullanılabilir IP Adresleri:")
    başlangıç = int(network.network_address) + 1  # Ağ adresi + 1
    bitiş = int(network.network_address) + network.num_addresses - 1  # Ağ adresi + toplam IP adres sayısı - 1

    for ip in range(başlangıç, bitiş):
        print(ipaddress.ip_address(ip)) # tam sayı formatındaki IP adresini tekrar IP adresi formatına çevirir.

# Kullanıcıdan IP adresi ve subnet maskesi al
ağ_adresi = input("Ağ Adresini girin (örn. 192.168.1.0): ")
subnet_maskesi = input("Subnet Maskesini girin (örn. 24): ")

# Fonksiyonu çağır
Mikail_Tali(ağ_adresi, subnet_maskesi)

