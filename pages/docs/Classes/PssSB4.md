# PssSB4

Power sensitive stabilizer model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemStabilizerDynamics <|-- PssSB4
    PowerSystemStabilizerDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PowerSystemStabilizerDynamics : +RemoteInputSignal RemoteInputSignal[0..n]
    click PowerSystemStabilizerDynamics href "PowerSystemStabilizerDynamics"
    PssSB4 : +Float kx[1..1]
    PssSB4 : +Float ta[1..1]
    PssSB4 : +Float tb[1..1]
    PssSB4 : +Float tc[1..1]
    PssSB4 : +Float td[1..1]
    PssSB4 : +Float te[1..1]
    PssSB4 : +Float tt[1..1]
    PssSB4 : +Float tx1[1..1]
    PssSB4 : +Float tx2[1..1]
    PssSB4 : +Float vsmax[1..1]
    PssSB4 : +Float vsmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| kx | Float | 1..1 | Gain (Kx). Typical value = 2,7. |
| ta | Float | 1..1 | Time constant (Ta) (>= 0). Typical value = 0,37. |
| tb | Float | 1..1 | Time constant (Tb) (>= 0). Typical value = 0,37. |
| tc | Float | 1..1 | Time constant (Tc) (>= 0). Typical value = 0,035. |
| td | Float | 1..1 | Time constant (Td) (>= 0). Typical value = 0,0. |
| te | Float | 1..1 | Time constant (Te) (>= 0). Typical value = 0,0169. |
| tt | Float | 1..1 | Time constant (Tt) (>= 0). Typical value = 0,18. |
| tx1 | Float | 1..1 | Reset time constant (Tx1) (>= 0). Typical value = 0,035. |
| tx2 | Float | 1..1 | Time constant (Tx2) (>= 0). Typical value = 5,0. |
| vsmax | Float | 1..1 | Limiter (Vsmax) (> PssSB4.vsmin). Typical value = 0,062. |
| vsmin | Float | 1..1 | Limiter (Vsmin) (< PssSB4.vsmax). Typical value = -0,062. |

