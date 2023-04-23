# chem-equation-solver

Well, it solves chemical equations. It balances them. That's what it does.

The only dependency is sympy, which is pretty lightweight.

## Usage

You run the program, then give it an unbalanced chemical equation, like so

```
λ python3 eq-balancer.py
Enter an unbalanced equation: ZnCl2 + Al2O3 -> AlCl3 + ZnO
3 ZnCl2 + 1 Al2O3 -> 2 AlCl3 + 3 ZnO
```

Don't hold back! It can do combustion as well! (I'm a high school student, so
this is the most advanced chemical reaction I know as of now):

```
λ python3 eq-balancer.py
Enter an unbalanced equation: CH3CH2CH2CH3 + O2 -> CO2 + H2O
4 CH3CH2CH2CH3 + 7 O2 -> 4 CO2 + 6 H2O
```
