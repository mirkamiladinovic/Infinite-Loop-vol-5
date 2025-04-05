
# Log Viewer GUI — INFLOOP

## Opis

Ova aplikacija omogućava pregledavanje i filtriranje velikih `.txt` log fajlova preko jednostavnog i funkcionalnog grafičkog interfejsa.

Takođe podržava izvršavanje nezavisnih zadataka (`vz1.py`, `vz2.py`, `vz3.py`) direktno iz GUI-ja — bez dodatnog ručnog pokretanja.

---

## Funkcionalnosti

-  Otvaranje `.txt` log fajlova
-  Filtriranje po:
  - log nivou (`DEBUG`, `INFO`, `WARNING`, `ERROR`)
  - tekstualnom sadržaju
  - datumu (`From` i `To`)
  - `Limit` i `Offset` za brži prikaz
-  Sortiranje po datumu (`asc` i `desc`)
-  Pokretanje dodatnih zadataka:
  - `vz1.py` — prikaz top 3 najčešće greške
  - `vz2.py` — prikaz top 5 fajlova koji generišu greške
  - `vz3.py` — kreiranje posebnog fajla sa samo `ERROR` logovima

---

##  Pokretanje aplikacije

- Pokreni fajl interface.exe iz VEGINDIO/dist/

##  Korišćenje

1. Klikni na **"Open Log File"** i izaberi `.txt` fajl sa logovima.
2. Postavi filtere (log nivo, datum, tekst, limit...).
3. Klikni **"Apply Filters"** da vidiš rezultate.
4. Klikni na jedno od sledećih dugmića:
   - `Pokreni zadatak 1` – prikazuje najčešće greške
   - `Pokreni zadatak 2` – prikazuje fajlove koji najčešće prave greške
   - `Napravi error file` – pravi novi fajl `error_logs.txt` sa samo `ERROR` logovima

---

##  Output fajlovi

- `error_logs.txt` — automatski kreira se u istom folderu kao originalni log fajl kada se pokrene `vz3.py`.

---

##  Zahtevi

- Python 3.7+
- Tkinter
- tkcalendar

---

