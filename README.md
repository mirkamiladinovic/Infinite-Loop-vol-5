# Struktura

cli.py – glavni fajl koji se pokrece
log_utils.py - sve funkcije za obradu logova  
errors_logs.txt - pravi se automatski 
gui.py- jednostavan graficki prikaz sa funckionalnlostima

# Pokretanje

python cli.py --file nazivFajla.txt [opcije]

python gui.py 
(prije pokretanja u fajlu gui.py vrijednost self.file_path treba postaviti na ime zeljenog fajla )

# Funkcionalnosti

# 1. Brojanje tipova logova (DEBUG, INFO, WARNING, ERROR)


python cli.py --file vegini_logovi.txt --count

# 2. Top 5 servisa sa najviše ERROR logova


python cli.py --file vegini_logovi.txt --top


# 3. Ekstrakcija ERROR logova u fajl error_logs.txt

python cli.py --file vegini_logovi.txt --errors

# 4. Filter i pretraga logova

# Filtriranje po tipu loga

python cli.py --file vegini_logovi.txt --filter --level ERROR


# Filtriranje po tekstu
python cli.py --file vegini_logovi.txt --filter --search "text"

# Filtriranje po datumu

python cli.py --file vegini_logovi.txt --filter --from_date 2025-03-10 --to_date 2025-03-13


# Kombinacija + sortiranje

python cli.py --file vegini_logovi.txt --filter --level ERROR --search "memory" --from_date 2025-03-08 --to_date 2025-03-12 --sort

