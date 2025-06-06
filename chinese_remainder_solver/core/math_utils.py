from typing import Tuple, List, Optional
import math

def gcd(a: int, b: int, return_steps: bool = False) -> Tuple[int, Optional[List[str]]]:
    """Calcola il MCD tra due numeri usando l'algoritmo di Euclide.
    
    Args:
        a: primo numero
        b: secondo numero
        return_steps: se True, restituisce anche i passaggi dell'algoritmo
        
    Returns:
        Tuple contenente il MCD e opzionalmente i passaggi
    """
    steps = []
    while b:
        step = f"{a} = {a // b} · {b} + {a % b}"
        if return_steps:
            steps.append(step)
        a, b = b, a % b
    return (a, steps) if return_steps else (a, None)

def lcm(a: int, b: int) -> int:
    """Calcola il MCM tra due numeri usando il MCD."""
    return abs(a * b) // gcd(a, b)[0]

class EuclidResult:
    """Classe per contenere i risultati dell'algoritmo di Euclide esteso."""
    def __init__(self, u: int, v: int, d: int, steps: List[Tuple[str, bool]], 
                 back_subs: List[str], expansion: List[str]):
        self.u = u  # coefficiente di Bézout per a
        self.v = v  # coefficiente di Bézout per b
        self.d = d  # MCD
        self.steps = steps  # passaggi dell'algoritmo
        self.back_subs = back_subs  # sostituzioni a ritroso
        self.expansion = expansion  # espansione completa

def extended_euclid(a: int, b: int) -> EuclidResult:
    """Calcola l'algoritmo di Euclide esteso tra due numeri.
    
    Args:
        a: primo numero
        b: secondo numero
        
    Returns:
        EuclidResult contenente tutti i risultati dell'algoritmo
    """
    # Inizializzazione variabili
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    euclid_steps = []
    equations = []

    # Algoritmo di Euclide
    while r != 0:
        q = old_r // r
        remainder = old_r - q * r
        equations.append((old_r, r, q, remainder))
        euclid_steps.append((f"{old_r} = {q} · {r} + {remainder}", False))
        old_r, r = r, remainder
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    # Marca ultimo passo
    if euclid_steps:
        last_step, _ = euclid_steps[-1]
        euclid_steps[-1] = (last_step, True)

    # Generazione sostituzioni a ritroso
    back_subs = [f"{R} = {A} - {q} · {B}" for A, B, q, R in reversed(equations)]

    # Espansione completa
    expansion_steps = []
    if len(equations) < 2:
        expansion_steps.append(f"{old_r} &= {old_s}\cdot{a} + {old_t}\cdot{b}")
    else:
        gcd_eq = equations[-2]
        current_expr = f"{gcd_eq[3]} &= {gcd_eq[0]} - {gcd_eq[2]}\cdot{gcd_eq[1]}"
        expansion_steps.append(current_expr)

        for i in range(len(equations)-3, -1, -1):
            A, B, q, R = equations[i]
            current_expr = current_expr.replace(str(R), f"({A} - {q}\cdot{B})")
            expansion_steps.append(current_expr)

        expansion_steps.append(f"{old_r} &= {old_s}\cdot{a} + {old_t}\cdot{b}")

    return EuclidResult(old_s, old_t, old_r, euclid_steps, back_subs, expansion_steps)

def factorize(n: int) -> str:
    """Fattorizza un numero in primi e restituisce la rappresentazione LaTeX.
    
    Args:
        n: numero da fattorizzare
        
    Returns:
        Stringa LaTeX con la fattorizzazione
    """
    if n == 1:
        return "1"
        
    i = 2
    factors = []
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count:
            factors.append(f"{i}^{{{count}}}" if count > 1 else f"{i}")
        i += 1
    if n > 1:
        factors.append(f"{n}")
    return r' \cdot '.join(factors)     