# track_and_trace_project

Šis projektas yra Kaunas Coding School Python kursų dalis

Kodų panaudojimo sekimo programa. Gaunas riboto naudojimo kodų kiekis. Kodus reikia naudoti įvedant produktą(seriją, pavadinimą, galiojimo datą, dėžės dydį kuris parodo kiek kodų vienu kartu bus sunaudota). Apjungiant produkto pavadinimo ir galiojimo datos turi būtu sukuriamas produkto kodas (`code` + `pavadinimas` + `serija` + `galiojimo data` į vieną `product_code`

## Diegimas
    
`pip install requirements.py`

## Naudojimas

`python track_and_track.py  pavadinimas serija galiojimo_laikas --nepanaudoti=nepanaudoti.txt --output=panaudoti.txt`
`python track_and_track.py Pavadinimas 2020-20-20 202012 6 --nepanaudoti=nepanaudoti.txt --output=panaudoti.txt`
Ši komanda turėtų iš `codes.txt` failo nuskaityti vieną nepanaudotą kodą ir sukurti naują eilutę faile `used_codes.txt`. Taip pat sukuria naują `product_code` eilutę `product_codes.txt` faile. Papildomai sukuriamas `Tat_data.csv` kuriame kaskart sugeneravus kodą yra įrašoma papildoma eilutė (append) iš `codes`, `product_codes`, `box_codes`.

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

## Product Code grupavimas

- sukurti funkciją kuri pagal apibrėžtą dėžės dydį pirmą `Product Code` sunaudos `Box_code` sukūrimui, o likusius kodus `Product_code` sukūrimui.
- bus sukuriamas kodų rinkinys kuris parodo kiek product_code yra sutalpinta viename `Box_code` {'Box_code': ['Product_code1','Product_code2']}

- Išsaugoti `product_codes.txt` failą su `Box_Code` ir `product_code`.



