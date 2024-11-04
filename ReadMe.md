markdown
Copy code
# Kép Rendező Script

Ez a Python szkript segít rendszerezni a képeket a készítés dátuma alapján egy megadott mappában. A program a képek EXIF metaadatainak segítségével rendezi a képeket évek és hónapok szerint mappákba.

## Követelmények

- **Python 3.x**
- **Pillow könyvtár**: telepíthető a következő paranccsal:
  ```bash
  pip install pillow

## Használat

A script futtatása a következő módon történik:

```bash
python imageOrganizer.py <elérési út a képekkel>
```
#### Példa
```bash
python imageOrganizer.py C:/felhasználó/képek
```
A script végigmegy a megadott mappában található összes képen, és rendszerezi azokat az EXIF adatok alapján a megfelelő év és hónap mappákba. Ha egy képnél nincs elérhető EXIF dátum, a program kihagyja azt a fájlt.

### Működés

A script megnyitja a képet, és próbálja megkeresni a készítés dátumát az EXIF metaadatokban.
Ha a dátum megtalálható, a képet egy olyan mappába helyezi át, amely a készítés éve és hónapja szerint van elnevezve.
Év mappa: Az év, pl. 2024
Hónap mappa: Az adott hónap, pl. 2024/03
Ha a képen nincs érvényes dátum információ, a program figyelmeztetést ad a konzolon.
Fájltípusok

### A program az alábbi fájltípusokkal működik:

- .jpg
- .jpeg
- .png
- .heif 

### Hibakezelés

Ha egy képről nem olvasható ki a dátum, a program figyelmeztetést jelenít meg.
Ha a megadott mappa nem létezik, vagy nem elérhető, a program egy hibaüzenettel kilép.

### Példa Kimenet

2023_foto.jpg átmozgatva ide: C:/felhasználó/képek/2023/05/2023_foto.jpg
2022_nyar.jpg átmozgatva ide: C:/felhasználó/képek/2022/07/2022_nyar.jpg
Nincs infó a dátumról ebben a fájlban: 2021_random.png.

### Megjegyzések

A script a képeket az aktuális mappaszerkezet alapján áthelyezi, így győződjön meg arról, hogy van elegendő hely és jogosultság a művelethez.
Windows és Linux rendszeren is működik.