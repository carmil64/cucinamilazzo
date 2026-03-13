from recipe_scrapers import scrape_me
import sqlite3
import requests
from bs4 import BeautifulSoup

def analizza_e_salva(url):
    try:
        scraper = scrape_me(url)
        tempo = scraper.total_time()
        if tempo > 30 or tempo == 0: return
        
        titolo = scraper.title()
        ingredients = ", ".join(scraper.ingredients()).lower()
        
        score = 0
        if "patate" in ingredients: score += 10
        if "zucchine" in ingredients: score -= 8
        if any(x in ingredients for x in ["parmigiano", "pecorino", "grana"]): score -= 8
        
        # Salviamo come "pasta" se è nella categoria corretta, altrimenti generico
        categoria = "pasta" if "pasta" in titolo.lower() or "pasta" in url else "secondo"

        if score >= -5:
            conn = sqlite3.connect('cucinamilazzo.db')
            cursor = conn.cursor()
            cursor.execute('''INSERT OR IGNORE INTO ricette 
                (titolo, tempo, ingredienti, url, categoria, punteggio) 
                VALUES (?, ?, ?, ?, ?, ?)''', 
                (titolo, tempo, ingredients, url, categoria, score))
            conn.commit()
            conn.close()
            print(f"✔️ {titolo} aggiunta al database.")
    except Exception as e:
        pass

def avvia(url_cat):
    print(f"🕵️ Esploro: {url_cat}")
    res = requests.get(url_cat, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.select('a'):
        href = link.get('href', '')
        if '/ricette/' in href and href.endswith('.html'):
            full_url = "https://www.cucchiaio.it" + href if href.startswith('/') else href
            analizza_e_salva(full_url)

if __name__ == "__main__":
    # Partiamo dai primi di pasta
    avvia("https://www.cucchiaio.it/ricette/primi_pasta~1/")