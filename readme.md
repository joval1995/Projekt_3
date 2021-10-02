# Projekt_3

Projekt_3 election-scraper.py slúži na extrahovanie výsledkov volieb z roku 2017 pre konkrétny okres podľa výberu
užívateľa. Príklad odkazu pre okres [Benešov](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101).

## Inštalácia knihovien

Knihovny použité v kóde sú uložene v súbore requirements.txt. Vytvoríme si nové virtuálne postredie a pomocou nainštalovaného manažera spustíme knihovny.


```python
pip3 --version                        # overenie verzie manažera
pip3 install -r requirements.txt       # inštalácia knihovien
```

## Spustenie projektu

Spustenie projektu _election-scraper.py_ vyžaduje dva argumenty:

```python
election-scraper.py <url_link_okresu> <výsledný_csv_súbor>
```

## Ukážka projektu
Výsledky hlasovania pre okres Benešov.
```python
1.argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2.argement: výsledky-Benešov.csv
```
Spustenie programu v cmd:
```python
python election-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "výsledky-Benešov.csv" 
```
Priebeh sťahovania:
```python
Downloading data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
Saving results to file: výsledky-Benešov.csv
Finishing election-scraper.py
```
Čiastočný výstup:
```python
Code,Location,Registred voters,Envelopes,Valid cotes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
```
