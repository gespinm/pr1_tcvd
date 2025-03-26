## Català

### Integrants del grup:
- Guillem Espín Martí
- Aleix Clavell Martínez

### Arxius que trobareu en aquest repositori:
- README.md: Instruccións i infomració bàsica i rellevant del projecte.
- requirements.txt: Fitxer on emmagatzemem el versionat dels paquets necessaris per fer funcionar el projecte.
- Carpeta /source: Carpeta principal d'emmagatzemament del codi en Python.
  - scrapper.py: Fitxer únic en Python el cual conté tot el codi.
- Carpeta /dataset: Dataset resultant en format CSV del script.
  - dataset.csv: Fitxer resultant en format csv.


### Instruccións d'ús:
#### Passos:
1- Executar el script fent ús de la següent comanda:
```
python .\source\scrapper.py --save-csv
```
2- Esperar a visualitzar el missatge final d'execució per CLI:
```
Scrapping was completed sucecssfully, results saved in csv /dataset/dataset.csv
```
#### Opcions:
--url: Permet afegir una url alternativa a la que fem servir per defecte.
--save-csv: Flag que ens permet emmagatzemar els resultats en csv localment, per defecte no s'emmagatzemen.

### DOI de Zenodo:
- BLABLABLA
