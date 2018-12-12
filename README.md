# track_and_trace_project

<<<<<<< HEAD
```
|-----------------------------------------------------------------|               |                |
|  code |Product name|    Batch   |Exp date|    Product Code      |   Box_code    |   Pallet_code  |
|-------|------------|------------|--------|----------------------|---------------|----------------|
|0000000|       c1   |     c2     |   c3   |   code+c1+c2+c3      | code+c1+c2+c3 | code+c1+c2+c3  |
|-------|------------|------------|--------|----------------------|
|0000011|   content1 |   content2 |content3|   code+c1+c2+c3      |
|-------|------------|------------|--------|----------------------|
```
=======
Šis projektas yra Kaunas Coding School Python kursų dalis
>>>>>>> e39831236be4690a079b73d15c907469a5b4529d

Kodų panaudojimo sekimo programa. Gaunas riboto naudojimo kodų kiekis. Kodus reikia naudoti įvedant produktą(seriją, pavadinimą ir galiojimo datą). Apjungiant produkto pavadinimo ir galiojimo datos turi būtu sukuriamas produkto kodas (`code` + `product_name` + `galiojimo datą` į vieną `Product_code`

## Diegimas
    
`pip install requirements.py`

## Naudojimas

`python track_and_track.py serija pavadinimas galiojimo_laikas --nepanaudoti=nepanaudoti.csv --output=panaudoti.csv`
`python track_and_track.py AAAAA SARIDON 2020-20-20 --nepanaudoti=nepanaudoti.csv --output=panaudoti.csv`
Ši komanda turėtų iš `nepanaudoti.csv` failo nuskaityti vieną nepanaudotą kodą ir sukurti naują eilutę faile `panaudoti.csv`

Tarkime, jog turėjome du nepanaudotus kodus. 000000 ir 000001.
Paleidus aukščiau parašytą komandą `nepanaudoti.csv` turinys turėtų pasikeisti į:
```csv
code
0000001
```
kitaip tariant, iš jo turėtų būti ištrinta  000000 eilutė.

Tuo tarpu `panaudoti.csv` turinys turėjo tapti:

```AAAAA SARIDON 2020-20-20
code   ,Product name,Batch,Exp date  ,Product Code
0000000,SARIDON     ,AAAAA,2020-20-20,0000000SARIDONAAAAA20202020
...
```


## Įrankiai

CSV failai skaitomi naudojant `csv` biblioteką https://docs.python.org/3.5/library/csv.html


## Product Code Agregation

- sukurti funkciją kuri paklausia po kiek `Product Code` bus grupuojamą vienoje `Box` grupėje ir kiek `Box` bus `Pallet` grupėje.
- sukurti funkciją kuri grupuoja `Prduct Code` į numatyto dydžio `Box` grupę.
- sukurti funkciją kuri grupuoja `Box` į numatyto dydžio `Pallet` grupę.

- Išsaugoti failą su `Product Code` ir `Box` bei `Pallet` konfigūracijomis/kiekiais.

## Product Code reading

- Nuskaityti gaunamo failo turinį
- nuskaičius pakuotės kodą gauti info apie pakuotę iš duomenų failų: koks Product, Batch, expire date

- iš skirtingų siuntų gautus kodus (ant pakuočių) sugrupuoti į naują siuntą
- naujais siuntai priskirti naują kodą
- prieš suteikiant naują kodą patikrinti ar jis nėra panaudotas
- suregistruoti panaudotus kodus
- į failą sukelti kodus kurie liko nepanaudoti


## duomenų bazėje surasti iš kur atkeliavo ši pakuotė
