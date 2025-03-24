# Metro_Simulation

Python ile yazılmış bu terminal tabanlı simülasyon, metro istasyonları arasındaki **en az aktarmalı** ve **en hızlı** rotayı hesaplar. Kullanıcıdan başlangıç ve hedef istasyon bilgileri alınarak, rotalar grafik yapısı üzerinde analiz edilir.

---

## Kullanılan Teknolojiler & Kütüphaneler

-  **Python 3**  
-  `collections`  
  - `deque`: BFS algoritması için kuyruk yapısı.  
  - `defaultdict`: Hat bazlı istasyonları gruplamak için.  
-  `heapq`: Dijkstra mantığında en kısa sürede varış için öncelik kuyruğu.  
-  `typing`: Tip güvenliği ve kod okunabilirliği için (`List`, `Dict`, `Optional`, `Tuple`).

---

## Algoritmaların Çalışma Mantığı

###  BFS – En Az Aktarma
- Kuyruk mantığıyla (FIFO) çalışır.
- Hedef istasyona en az aktarmayla varan ilk yol döndürülür.
- Her istasyon sadece bir kez ziyaret edilir.

###  Dijkstra (Heuristiksiz A*)
- Yolculuk süresi bazlı en kısa yolu bulur.
- `heapq` kullanılarak en kısa sürede ulaşan rota seçilir.
- Heuristik içermediği için klasik A* yerine Dijkstra mantığıyla çalışır.

###  Neden Bu Algoritmalar?
- **BFS**: Aktarma sayısını minimuma indirir.
- **Dijkstra**: Kullanıcıyı en kısa sürede hedefe ulaştırır.

---

##  Projeyi Başlat

```bash
python BuğraAnılYalçın_MetroSimulation.py
```

Konsolda bize sorulacak input'lar:
```
Başlangıç istasyon ID: 
Hedef istasyon ID:
```

Örnek input:
```
Başlangıç istasyon ID: M1
Hedef istasyon ID: K4
```

Çıktı:
```
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
```

---

##  Geliştirme Fikirleri

- Grafik Arayüz (Tkinter, PyQt5)
- Harita Görselleştirme (networkx + matplotlib)
- Gerçek A\* (heuristik mesafe tahmini ile)
- Veri Dosyasından Okuma (`.json`, `.csv`)
- Web Entegrasyonu (Flask/Django)

---

##  Dosyalar

| Dosya Adı | Açıklama |
|-----------|----------|
| `BuğraAnılYalçın_MetroSimulation.py` | Ana uygulama dosyası |
| `README.md` | Bu döküman |

---

Hazırlayan: **Buğra Anıl Yalçın**  
Proje: Global AI Hub x Akbank Python Bootcamp
