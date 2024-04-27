import csv
from pathlib import Path

read_dataset= Path ('./datasets/ar-airports.csv')
write_dataset= Path ('./datasets_custom/ar-airports-custom.csv')


with( read_dataset.open (mode='r',encoding= 'UTF-8') as lectura, 
     write_dataset.open(mode='w',encoding= 'UTF-8' ,newline= '')  as escritura
     ):
    
    lectorcsv= csv.reader(lectura)
    escritorcsv= csv.writer (escritura)

    encabezado = next(lectorcsv)
    encabezado.append ('elevation_name')
    escritorcsv.writerow (encabezado)

    for fila in lectorcsv:
        try: 
            elevacion = float(fila[6])
            if elevacion <= 131:
                elevation_name= 'bajo'
            elif elevacion <=903:
                elevation_name= 'medio'
            else:   
                elevation_name='alto'

            fila.append(elevation_name)
            escritorcsv.writerow(fila)

        except ValueError: 
            fila.append ('Sin altura')
            escritorcsv.writerow(fila)

