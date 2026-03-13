# Cucinamilazzo 🍝

Sistema di Meal Prep automatizzato per 1 persona.

## Installazione sulla VPS
1. `git clone <tuo-repo>`
2. `pip install recipe-scrapers beautifulsoup4 requests`
3. `python3 init_db.py`

## Flusso di lavoro
1. **Importa:** `python3 siphon.py` (scarica ricette dal web)
2. **Pianifica:** `python3 settimana.py` (genera il menu settimanale)
3. **Gestisci:** Vai su `http://tua-vps/cucinamilazzo` per vedere il menu e generare la spesa.
