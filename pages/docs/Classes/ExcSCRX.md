# ExcSCRX

Simple excitation system with generic characteristics typical of many excitation systems; intended for use where negative field current could be a problem.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcSCRX
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcSCRX : +Boolean cswitch[1..1]
    ExcSCRX : +Float emax[1..1]
    ExcSCRX : +Float emin[1..1]
    ExcSCRX : +Float k[1..1]
    ExcSCRX : +Float rcrfd[1..1]
    ExcSCRX : +Float tatb[1..1]
    ExcSCRX : +Float tb[1..1]
    ExcSCRX : +Float te[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| cswitch | Boolean | 1..1 | Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage. |
| emax | Float | 1..1 | Maximum field voltage output (Emax) (> ExcSCRX.emin). Typical value = 5. |
| emin | Float | 1..1 | Minimum field voltage output (Emin) (< ExcSCRX.emax). Typical value = 0. |
| k | Float | 1..1 | Gain (K) (> 0). Typical value = 200. |
| rcrfd | Float | 1..1 | Ratio of field discharge resistance to field winding resistance ([rc / rfd]). Typical value = 0. |
| tatb | Float | 1..1 | Gain reduction ratio of lag-lead element ([Ta / Tb]). The parameter Ta is not defined explicitly. Typical value = 0.1. |
| tb | Float | 1..1 | Denominator time constant of lag-lead block (Tb) (>= 0). Typical value = 10. |
| te | Float | 1..1 | Time constant of gain block (Te) (> 0). Typical value = 0,02. |

