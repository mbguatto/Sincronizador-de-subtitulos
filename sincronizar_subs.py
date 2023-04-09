
# Dada una pista de subs sincronizada correctamente con el archivo de video,
# permite adaptar otra traducción según esta clave de tiempo. Ej:


""" PISTA BIEN SINCRONIZADA: (en neerlandés)  
    1
    00:00:26,404 --> 00:00:32,195
    Ik heb het gevoel dat ik op dat kind,
    dat jonge, argeloze meisje...

    2
    00:00:32,361 --> 00:00:36,902
    ...boos zou moeten zijn.
    Of dat ik haar niet mag vergeven...

    3
    00:00:37,069 --> 00:00:41,484
    ...dat ze de aard van dat monster
    niet heeft onderkend.

    -----------------------------------------------

    PISTA CON LA TRADUCCIÓN DESEADA: (en español)
    1
    00:00:25,314 --> 00:00:31,049
    Siento que debería estar
    furiosa con esa criatura, esa...

    2
    00:00:31,571 --> 00:00:35,742
    ...niña ingenua.
    O que no debo perdonarle...

    3
    00:00:36,264 --> 00:00:39,913
    ...por no reconocer la naturaleza
    de ese monstruo.

    -----------------------------------------------

    EL RESULTADO BUSCADO SERÍA:
    1
    00:00:26,404 --> 00:00:32,195
    Siento que debería estar
    furiosa con esa criatura, esa...

    2
    00:00:32,361 --> 00:00:36,902
    ...niña ingenua.
    O que no debo perdonarle...

    3
    00:00:37,069 --> 00:00:41,484
    ...por no reconocer la naturaleza
    de ese monstruo.

"""

# La pista de salida tendrá la clave de tiempo de los subtítulos en neerlandés,
# pero el texto en idioma español.
#
# PRECONDICIÓN: ambas pistas deben tener la misma cantidad de diálogos. Si la 
# pista a sincronizar es mayor a la de la clave de tiempo, quedarán subtítulos
# sin mostrar; si es menor, el programa se romperá.

def main() -> None:
    with open("src/pista-mal-sincronizada.srt","r", encoding="ISO 8859-1") as subs1:
        subs_idioma_correcto: list = subs1.readlines() 
    
    with open("src/pista-bien-sincronizada.srt","r", encoding="ISO 8859-1") as subs2:
        subs_clave_tiempo: list = subs2.readlines()

    i: int = 0
    j: int = 2
    while i<len(subs_clave_tiempo):
        leida: str = subs_clave_tiempo[i].rstrip('\n')
        if (leida.isnumeric()):
            escribir: str = leida +"\n" + subs_clave_tiempo[i+1]
            
            bloque_sub: list = []
            while (subs_idioma_correcto[j].rstrip('\n').isnumeric() == False and j<len(subs_clave_tiempo)):
                bloque_sub.append(subs_idioma_correcto[j])
                j+=1
            j+=2

            for k in range(len(bloque_sub)-1):
                escribir += bloque_sub[k]
            
            with open("output.srt", "a", encoding="ISO 8859-1") as escritura:
                escritura.write(str(escribir)+"\n")
        
        i+=1
    
main()