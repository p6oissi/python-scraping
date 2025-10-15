# Proovitöö Variant B – Veebipoodide hinnapäringu programm

## Ülevaade
- Programmi eesmärgiks on **esitada** veebipoodidele lihtne andmepäring, mis
põhineb kasutaja märksõnal, ning kuvada tulemused struktureeritul kujul (terminalis).

- Programmi kaudu saab jälgida toodete hindu ja leida automaatselt uusi 
kuulutusi, kindla ajavahemiku järel

## Funktsionaalsus

### Veebipoed kuhu päringuid esitatakse
- **www.yaga.ee**
- **www.arvutitark.ee**

### Automaatsed korduspäringud
- Programm sooritab otsinguid määratud ajaintervalliga.

### Uute toodete tuvastamine 
- Jälgib, millised tooted on juba nähtud, ning kuvab ainult uued tulemused.

### Andmete salvestamine
- Iga päringu tulemused salvestatakse eraldi `.json` faili koos ajatempliga.

## Kasutamine
0. Seadista kui tihti sa soovid päringuid esitada.
Vaikimisi on see 300 sekundit (5 minutit)
```
   main.py
   if __name__ == '__main__':
    keyword = input("Enter the keyword: ")
    run_periodically(keyword, interval=SIIN)
```
1. Käivita programm
```bash
   python -m src.main
```
2. Sisesta märksõna
```yaml
Enter the keyword: AMD
```
3. Tulemused
- Programm kogub andmed erinevatest allikatest ja kuvab need konsoolis tabelina.
```
============================================================
Results for 'AMD' (40 items found)

Search run at 18:02:12
============================================================

Product #1
Name: Uus amd protsessori jahutus 
Ühendus and am4 ja am5
Toote kood 712-000055
Toide 4 kontakt
Maksimaalne tdp 95w
Kiiruse regulaator automaatne
Price: 15 €
Link: https://www.yaga.ee/roosid/toode/8u7bfd451h
Source: yaga.ee
------------------------------------------------------------

Product #2
Name: Onexplayer X1 Pro AMD AI370 64GB RAM 2TB kaasaskantav konsool
Price: 1941.3 €
Link: https://arvutitark.ee/est/tooted/onexplayer-x1-pro-amd-ai370-64gb-ram-2tb-kaasaskantav-konsoo-1490565
Source: arvutitark.ee
------------------------------------------------------------
```
4. Salvestamine
- Iga otsing salvestatakse kausta `results/`
```
results-amd_20251015_18-02-12.json
```

## Struktuur
```
Proovitöö_VariantB/src/
│
├── main.py                     # Põhiprogramm
├── results/                    # JSON-failid otsingutulemustega
├── utils.py                    # Ühised abifunktsioonid
├── README.md
└── scrapers/
    ├── yaga_scraper.py         # Yaga API päring
    └── arvutitark_scraper.py   # Arvutitark API päring
```

Autor: **Markus Tiedemann**

Valmimisaeg: Oktoober 2025