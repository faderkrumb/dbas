# $~~~~~~~~~~~~~~~~~$Beviskontroll med Prolog

![alt](~/misc/lumon/lumon.png);

# $~~~~~~~~~~~~~~~~~~~~~~~$Grupp Lumon 
$~~~~~~~~~~~~~~~~~~~~~~~~~~~$Ludwig Berglind, Simon Severinsson

\pagebreak

## Functional Dependencies
An FD on a relation R is defined by: \
    If  two tuples of R agree on all attributes A<sub>1</sub>,...,An then they must
    also agree on all attributes B1,...,Bm.
    We say that A1,...,An determines B1,...,Bm, denoted as A -> B.

A set K = {A1,...,An} of attributes is key for reltion R if:
    - K functionally determine all other attr. of R.
    - No proper subset of K functionally determines all other attr. of R
      ,that is, all keys are minimal.

A set of attr. that contains a key is called a superkey.

### FD Reasoning
FD's can be inferred from other FD's.
    - If R(A,B,C) satisfies A -> B and B -> C then A -> C and A -> B, C can be
      inferred.
    - If A1,...,Am -> B1,...,Bm then A1,...,An -> B1,..., A1,...,An -> Bm.

Trivial FD's.
A constraint on a relation R is trivial if holds for every instance of R,
regardless of other constraints.
    - An FD A -> B is trivial if B is a subset of A.
      Ex: A1, A2 -> A2 always holds and thusly is trivial.

Attribute Closures
If A is a set of attr {A1,...,An} and S is a set of FD's then the closure of
A under the FD's in S is the set of attributes B such that every relation
that satisfies all of S als satisfies A -> B, that is, A -> B follows from
the FD's of S. The closure of a A is denoted as A<sup>+</sup>
