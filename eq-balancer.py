# Requirements: sympy
from sympy import *
import re                   # Clashes with Re(z) from sympy, so must be imported after
import itertools as it
import math

def split_list(l, x):
    i = l.index(x)
    return l[:i], l[i+1:]

def parse_compound(comp):
    if comp == '->': return {}
    tl = re.findall(r'([A-Z][a-z]*)(\d*)', comp)
    k, v = zip(*tl)
    return dict(zip(k, (int(n) if n else 1 for n in v)))

unbalanced     = input('Enter an unbalanced equation: ')
compounds      = re.findall(r'((?:(?:[A-Z][a-z]*)(?:\d*))+|\->)', unbalanced)
reacts, prods  = split_list(compounds, '->')
element_set    = set(it.chain.from_iterable(parse_compound(x).keys() for x in compounds))
syms           = dict(zip(compounds, symbols(list(map('coeff<{}>'.format, compounds)))))
system         = [ sum(parse_compound(compound).get(elem, 0) * syms[compound] for compound in reacts)
                 - sum(parse_compound(compound).get(elem, 0) * syms[compound] for compound in  prods) for elem in element_set]
solution       = list(linsolve(system, [v for k, v in syms.items() if k != '->']))[0]
denom_lcm      = math.lcm(*(x.as_numer_denom()[1] for x in solution))
free_var       = list(solution[0].free_symbols)[0]
simplest_sol   = [x.subs(free_var, denom_lcm) for x in solution]
reacts_str     = ' + '.join(map('{{}} {}'.format, reacts))
prods_str      = ' + '.join(map('{{}} {}'.format, prods))
print((reacts_str + ' -> ' + prods_str).format(*simplest_sol))
