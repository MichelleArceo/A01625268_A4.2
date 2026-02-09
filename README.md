# A01625268_A4.2

Entrega de la Actividad **A4.2** (TC4017.10) con 3 programas en Python, cumpliendo **PEP 8** y verificados con **PyLint**, usando los casos de prueba oficiales (TC1–TC7).

## Programas
- **P1:** `A4_2/P1/source/computeStatistics.py` → genera `StatisticsResults.txt`
- **P2:** `A4_2/P2/source/convertNumbers.py` → genera `ConvertionResults.txt`
- **P3:** `A4_2/P3/source/wordCount.py` → genera `WordCountResults.txt`

## Cómo ejecutar (ejemplo)
```bash
python A4_2/P1/source/computeStatistics.py A4_2/P1/tests/TC1.txt
python A4_2/P2/source/convertNumbers.py A4_2/P2/tests/TC1.txt
python A4_2/P3/source/wordCount.py A4_2/P3/tests/TC1.txt

## Evidencia (ejecución y resultados)

Para cada programa se ejecutaron los **7 casos oficiales (TC1–TC7)**.  
La evidencia generada se guarda en:

- Consola por caso: `A4_2/P*/results/console_TC#.txt`
- Archivo de resultados por caso: `A4_2/P*/results/*Results_TC#.txt`
- Reporte de PyLint: `A4_2/P*/results/pylint.txt`

# PyLint (reporte en results/)
pylint A4_2/P1/source/computeStatistics.py | tee A4_2/P1/results/pylint.txt
pylint A4_2/P2/source/convertNumbers.py | tee A4_2/P2/results/pylint.txt
pylint A4_2/P3/source/wordCount.py | tee A4_2/P3/results/pylint.txt
