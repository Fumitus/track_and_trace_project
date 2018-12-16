# track_and_trace_project

Šis projektas yra Kaunas Coding School Python kursų dalis

Kodų panaudojimo sekimo programa. Gaunas riboto naudojimo kodų kiekis. Kodus reikia naudoti įvedant produktą(seriją, pavadinimą ir galiojimo datą). Apjungiant produkto pavadinimo ir galiojimo datos turi būtu sukuriamas produkto kodas (`code` + `pavadinimas` + `serija` + `galiojimo data` į vieną `product_code`

## Diegimas
    
`pip install requirements.py`

## Naudojimas

`python track_and_track.py  pavadinimas serija galiojimo_laikas --nepanaudoti=nepanaudoti.csv --output=panaudoti.csv`
`python track_and_track.py AAAAA SARIDON 2020-20-20 --nepanaudoti=nepanaudoti.csv --output=panaudoti.csv`
Ši komanda turėtų iš `codes.txt` failo nuskaityti vieną nepanaudotą kodą ir sukurti naują eilutę faile `used_codes.txt`. Taip pat sukuria naują `product_code` eilutę `product_codes.txt` faile. Papildomai sukuriamas `Tat_data.csv` kuriame kaskart sugeneravus kodą yra įrašoma papildoma eilutė (append) iš `codes`, `product_codes`, `box_codes`, `pallet_codes`.

Tarkime, jog turėjome du nepanaudotus kodus. 000000 ir 000001.
Paleidus aukščiau parašytą komandą `codes.txt` turinys turėtų pasikeisti į:
```txt
code
0000001
```
kitaip tariant, iš jo turėtų būti ištrinta  000000 eilutė.

Tuo tarpu `used_codes.txt` turinys turėjo tapti:
```txt
000000
```
`Tat_data.csv` turinys pasipildo eilute

```csv
  code|        product_codes       |         box_codes              |            pallet_codes           |
000000|SARIDON20181212202012/000000|SARIDON20181212202012/000001/box|SARIDON20181212202012/000002/pallet|
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
