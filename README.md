# track_and_trace_project

Šis projektas yra Kaunas Coding School Python kursų dalis

Kodų panaudojimo sekimo programa. Gaunas riboto naudojimo kodų kiekis. Kodus reikia naudoti įvedant produktą(seriją, pavadinimą, galiojimo datą, dėžės dydį kuris parodo kiek kodų vienu kartu bus sunaudota). Apjungiant produkto pavadinimo ir galiojimo datos turi būtu sukuriamas produkto kodas (`code` + `pavadinimas` + `serija` + `galiojimo data` į vieną `product_code`

## Diegimas
    
`pip install requirements.py`

## Naudojimas

`python track_and_track.py  pavadinimas serija galiojimo_laikas dėžės_dydis (dėžė apibrėžta nuo 2 iki 10 kodų taupant codes.txt faile esančius kodus)
pvz.:

> python track_and_track.py Pavadinimas 2020-20-20 202012 6 

Ši komanda turėtų iš `codes.txt` failo nuskaityti vieną nepanaudotą kodą ir sukurti naują eilutę faile `used_codes.txt`. Taip pat sukuria naują `product_code_group` eilutę `product_codes.txt` faile. Ši eilutė turi duomenis kokioje dėžutėje su unikaliu kodu yra užregistruoti unikalūs `product_code`.

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
Taip pat `product_codes.txt` pasipildo nauja eilute pvz. :
`{'Morfin2018-12-212020-12/`000000`/box': ['Morfin2018-12-212020-12/`000001`']}`

## Product Code grupavimas

- funkcija kuri pagal apibrėžtą dėžės dydį pirmą `Product Code` sunaudos `box_code` sukūrimui, o likusius kodus `product_code` sukūrimui.
- bus sukuriamas kodų rinkinys kuris parodo kiek product_code yra sutalpinta viename `box_code` `{'Box_code': ['Product_code1','Product_code2']}`

pvz.:

`{'Morfin2018-12-212020-12/100171/box': ['Morfin2018-12-212020-12/100172']}`

- Gautos eilutės išsaugomos `product_codes.txt`, `box_result.json`.



