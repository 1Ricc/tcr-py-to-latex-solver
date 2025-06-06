from typing import Tuple, List
import math

def gcd(a: int, b: int, return_steps=False) -> Tuple[int, List[str]]:
    steps = []
    while b:
        steps.append(f"{a} = {a // b} · {b} + {a % b}")
        a, b = b, a % b
    if return_steps:
        return a, steps
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)

import re
from typing import Tuple, List

def extended_euclid(a: int, b: int) -> Tuple[int, int, int, List[Tuple[str, bool]], List[str], List[str]]:
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

    # Generazione sostituzioni a ritroso (per tabella)
    back_subs = []
    for A, B, q, R in reversed(equations):
        back_subs.append(f"{R} = {A} - {q} · {B}")

    # Espansione completa con sostituzioni progressive
    expansion_steps = []
    
    # Se non ci sono abbastanza equazioni, usa direttamente i coefficienti di Bézout
    if len(equations) < 2:
        expansion_steps.append(f"{old_r} &= {old_s}\cdot{a} + {old_t}\cdot{b}")
    else:
        # Inizia dal gcd (penultima equazione)
        gcd_eq = equations[-2]  # Prendi la penultima equazione che contiene il gcd
        current_expr = f"{gcd_eq[3]} &= {gcd_eq[0]} - {gcd_eq[2]}\cdot{gcd_eq[1]}"
        expansion_steps.append(current_expr)

        # Sostituisci progressivamente ogni resto con la sua espressione
        for i in range(len(equations)-3, -1, -1):
            A, B, q, R = equations[i]
            # Sostituisci il resto corrente nella sua espressione
            current_expr = current_expr.replace(str(R), f"({A} - {q}\cdot{B})")
            expansion_steps.append(current_expr)

        # Aggiungi l'equazione finale con i coefficienti di Bézout
        expansion_steps.append(f"{old_r} &= {old_s}\cdot{a} + {old_t}\cdot{b}")

    return old_s, old_t, old_r, euclid_steps, list(reversed(back_subs)), expansion_steps


def factorize(n: int) -> str:
    # Fattorizzazione in stringa LaTeX
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
            if count == 1:
                factors.append(f"{i}")
            else:
                factors.append(f"{i}^{{{count}}}")
        i += 1
    if n > 1:
        factors.append(f"{n}")
    return r' \cdot '.join(factors)     