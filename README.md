# Sincronizador de subtítulos en Python

## Prerrequisitos:

- Para compilar y correr:

```bash
pip install python3
```

## Precondiciones:

- Ambas pistas deben tener la misma cantidad de diálogos.
- Deben encontrarse en la carpeta `\src` con los nombres `pista-mal-sincronizada` y `pista-bien-sincronizada`

## Post-condición:

- La pista correctamente sincronizada `output.srt` se exporta en el directorio raíz.


---

##  Funcionamiento

Dada una pista de subs sincronizada correctamente con el archivo de video, permite adaptar otra traducción según esta clave de tiempo. Ej:

```c
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
````

Como se puede apreciar, la pista de salida tendrá la clave de tiempo de los subtítulos en neerlandés, pero el texto en idioma español.
