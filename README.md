# track_and_trace_project
link to github.com [github]
https://github.com/Fumitus/track_and_trace_project
## Kaunas Coding School project

- nuskaityti `kodus` iš failo
    - Įvesti `seriją`, `Pavadinimą` ir `galiojimo datą`
        - sujungti `kodą` + `serija` + `Pavadinimą` + `galiojimo datą` į vieną kodą


```
|kinta  |    pastovus duomenys serijai     |                      |             
|  code |Product name|Batch number|Exp date|    Pakuotės kodas    |
|-------|------------|------------|--------|----------------------|
|0000000|   content  |   content  |content |                      |
|-------|------------|------------|--------|----------------------|
|0000011|   content  |   content  |content |                      |
|-------|------------|------------|--------|----------------------|
```

## Kintamieji
- įvesti serijos duomenis: `serija`, `pavadinimas`, `galiojimo laikas`

```py
def batch_data('n'):
    input(`serija`)
    input(`pavadinimas`)
    input(`galiojimas laikas`)
```

## Registruoti gaunamus kodus
- sugeneruotus kodus išsaugoti
```py
def write_data(df):
    df.to.csv('Outpu_name.csv')
```

## Nuskaityti gaunamus kodus

- nuskaityti gaunamus duomenis
```py
def read_data():
    pd.read_csv('file.csv')
```

## Sukurti DatFrame iš turimų duomenų

```py
def table():
    pd.DataFrame()

## Code Agregation



sugrupuoti 2D kodus ir naujai grupei suteikti naują kodą
prieš suteikiant naują kodą patikrinti ar jis nėra panaudotas
suregistruoti panaudotus kodus
į failą sukelti kodus kurie liko nepanaudoti

sukurti saugius failus duomenų persiuntimui kartu su siunta

Nuskaityti gaunamo failo turinį
nuskaičius pakuotės kodą gauti info apie pakuotę iš duomenų failų

iš skirtingų siuntų gautus kodus (ant pakuočių) sugrupuoti į naują siuntą
naujais siuntai priskirti naują kodą
prieš suteikiant naują kodą patikrinti ar jis nėra panaudotas
suregistruoti panaudotus kodus
į failą sukelti kodus kurie liko nepanaudoti

nuskaityti kodą ir gauti info apie pakuotę, jos seriją, galiojimo datą, pavadinimą
duomenų bazėje surasti iš kur atkeliavo ši pakuotė
