from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

# Istasyon sınıfı, her metro istasyonunu temsil eder
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyon ID'si
        self.ad = ad    # İstasyon adı
        self.hat = hat  # Hangi hatta ait olduğu
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşu istasyonlar ve aradaki süre

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

# Metro ağı sınıfı, tüm istasyonları ve bağlantıları yönetir
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        # Yeni istasyon ID daha önce eklenmemişse istasyon listesine eklenir
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        # İki istasyon arası çift yönlü bağlantı (komşuluk) kurar
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # En az aktarma yapan rotayı BFS algoritması ile bulur
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        queue = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()

        while queue:
            mevcut, yol = queue.popleft()
            if mevcut.idx == hedef.idx:
                return yol

            ziyaret_edildi.add(mevcut.idx)

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edildi:
                    queue.append((komsu, yol + [komsu]))
                    ziyaret_edildi.add(komsu.idx)
        return None

    # En kısa sürede ulaşan rotayı Dijkstra mantığıyla bulur (heuristik yok)
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = {}

        while pq:
            toplam_sure, _, mevcut, yol = heapq.heappop(pq)

            if mevcut.idx in ziyaret_edildi and ziyaret_edildi[mevcut.idx] <= toplam_sure:
                continue

            ziyaret_edildi[mevcut.idx] = toplam_sure

            if mevcut.idx == hedef.idx:
                return yol, toplam_sure

            for komsu, sure in mevcut.komsular:
                yeni_sure = toplam_sure + sure
                heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yol + [komsu]))

        return None


if __name__ == "__main__":
    metro = MetroAgi()

    # Metro istasyonları tanımlanıyor
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Metro hatları arası bağlantılar tanımlanıyor
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)

    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)

    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)

    # Hatlar arası aktarmalar (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)

    # Kullanıcıdan giriş alma kısmı
    print("\n=== Dinamik Rota Bulucu ===")
    baslangic = input("Başlangıç istasyon ID: ").strip()
    hedef = input("Hedef istasyon ID: ").strip()

    # En az aktarmalı rota hesaplanıyor
    rota = metro.en_az_aktarma_bul(baslangic, hedef)
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    else:
        print("Geçerli rota bulunamadı (en az aktarma).")

    # En hızlı rota hesaplanıyor
    sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    else:
        print("Geçerli rota bulunamadı (en hızlı).")
