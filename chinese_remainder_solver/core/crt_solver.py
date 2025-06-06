from typing import List, Tuple, Dict
from .math_utils import gcd, extended_euclid, lcm, factorize

class CRTSolution:
    def __init__(self, congruences: List[Tuple[int, int]]):
        self.congruences = congruences
        self.gcd_value = None
        self.gcd_steps = []
        self.bezout_coeffs = None
        self.compatibility_check = None
        self.particular_solution = None
        self.period = None
        self.solution_set = None
        self.divisibility_checks = []
        self.m1_factorization = None
        self.m2_factorization = None
        self.diff = None
        self.compatible = None
        self.full_expansion = []
        self.expansion_steps = []


def solve_crt_system(congruences: List[Tuple[int, int]], options: Dict) -> CRTSolution:
    # Solo due congruenze per ora
    (a1, m1), (a2, m2) = congruences
    sol = CRTSolution(congruences)
    # Passo 1: Compatibilità
    d, steps = gcd(m1, m2, return_steps=True)
    sol.gcd_value = d
    sol.gcd_steps = steps
    sol.m1_factorization = factorize(m1)
    sol.m2_factorization = factorize(m2)
    diff = a2 - a1
    sol.diff = diff
    sol.compatible = (diff % d == 0)
    sol.compatibility_check = sol.compatible
    if not sol.compatible:
        return sol
    # Passo 2: Euclide esteso
    u, v, d2, euclid_steps, back_subs, expansion_steps = extended_euclid(m1, m2)
    sol.bezout_coeffs = (u, v)
    sol.gcd_steps = euclid_steps
    sol.back_subs = back_subs
    sol.expansion_steps = expansion_steps
    # Passo 3: Soluzione particolare
    k = diff // d
    x0 = a1 + k * u * m1
    sol.particular_solution = x0
    # Passo 4: Insieme soluzioni
    M = lcm(m1, m2)
    sol.period = M
    x0_norm = x0 % M
    sol.solution_set = f"{{{x0_norm} + {M}·k : k ∈ ℤ}}"
    return sol 