def validar_hora(hora: int) -> bool:
    """Valida que la hora esté entre 0 y 23."""
    return 0 <= hora <= 23

def validar_minuto(minuto: int) -> bool:
    """Valida que el minuto esté entre 0 y 59."""
    return 0 <= minuto <= 59

def validar_segundo(segundo: int) -> bool:
    """Valida que el segundo esté entre 0 y 59."""
    return 0 <= segundo <= 59

def validar_tiempo(h: int, m: int, s: int) -> bool:
    """Valida si el conjunto de hora, minuto y segundo es correcto."""
    return validar_hora(h) and validar_minuto(m) and validar_segundo(s)

def formatear_tiempo(h: int, m: int, s: int) -> str:
    """Devuelve el tiempo en formato 'HH:MM:SS'."""
    return f"{h:02d}:{m:02d}:{s:02d}"
