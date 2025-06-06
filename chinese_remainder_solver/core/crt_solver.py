from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
from .math_utils import gcd, extended_euclid, lcm, factorize, EuclidResult

@dataclass
class Congruence:
    """Rappresenta una congruenza lineare x ≡ a (mod m)."""
    a: int  # resto
    m: int  # modulo

@dataclass
class CRTSolution:
    """Rappresenta la soluzione di un sistema di congruenze."""
    congruences: List[Tuple[int, int]]
    compatible: bool = False
    gcd_value: Optional[int] = None
    gcd_steps: List[str] = None
    bezout_coeffs: Optional[Tuple[int, int]] = None
    particular_solution: Optional[int] = None
    period: Optional[int] = None
    solution_set: Optional[str] = None
    m1_factorization: Optional[str] = None
    m2_factorization: Optional[str] = None
    diff: Optional[int] = None
    back_subs: List[str] = None
    expansion_steps: List[str] = None

    def __post_init__(self):
        """Inizializza le liste vuote."""
        if self.gcd_steps is None:
            self.gcd_steps = []
        if self.back_subs is None:
            self.back_subs = []
        if self.expansion_steps is None:
            self.expansion_steps = []

def solve_crt_system(congruences: List[Tuple[int, int]], options: Dict) -> CRTSolution:
    """Risolve un sistema di due congruenze lineari usando il Teorema Cinese del Resto.
    
    Args:
        congruences: lista di coppie (a, m) rappresentanti le congruenze
        options: opzioni per la soluzione
        
    Returns:
        CRTSolution contenente tutti i dettagli della soluzione
    """
    # Estrai le due congruenze
    (a1, m1), (a2, m2) = congruences
    sol = CRTSolution(congruences)
    
    # Passo 1: Verifica compatibilità
    d, steps = gcd(m1, m2, return_steps=True)
    sol.gcd_value = d
    sol.gcd_steps = steps
    sol.m1_factorization = factorize(m1)
    sol.m2_factorization = factorize(m2)
    sol.diff = a2 - a1
    sol.compatible = (sol.diff % d == 0)
    
    if not sol.compatible:
        return sol
        
    # Passo 2: Calcolo coefficienti di Bézout
    euclid_result = extended_euclid(m1, m2)
    sol.bezout_coeffs = (euclid_result.u, euclid_result.v)
    sol.gcd_steps = euclid_result.steps
    sol.back_subs = euclid_result.back_subs
    sol.expansion_steps = euclid_result.expansion
    
    # Passo 3: Calcolo soluzione particolare
    k = sol.diff // d
    x0 = a1 + k * euclid_result.u * m1
    sol.particular_solution = x0 % lcm(m1, m2)
    
    # Passo 4: Calcolo insieme soluzioni
    M = lcm(m1, m2)
    sol.period = M
    sol.solution_set = f"{{{sol.particular_solution} + {M}·k : k ∈ ℤ}}"
    
    return sol 