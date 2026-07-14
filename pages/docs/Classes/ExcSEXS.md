# ExcSEXS

Simplified excitation system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcSEXS
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcSEXS : +Float efdmax[1..1]
    ExcSEXS : +Float efdmin[1..1]
    ExcSEXS : +Float emax[1..1]
    ExcSEXS : +Float emin[1..1]
    ExcSEXS : +Float k[1..1]
    ExcSEXS : +Float kc[1..1]
    ExcSEXS : +Float tatb[1..1]
    ExcSEXS : +Float tb[1..1]
    ExcSEXS : +Float tc[1..1]
    ExcSEXS : +Float te[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| efdmax | Float | 1..1 | Field voltage clipping maximum limit (Efdmax) (> ExcSEXS.efdmin). Typical value = 5. |
| efdmin | Float | 1..1 | Field voltage clipping minimum limit (Efdmin) (< ExcSEXS.efdmax). Typical value = -5. |
| emax | Float | 1..1 | Maximum field voltage output (Emax) (> ExcSEXS.emin). Typical value = 5. |
| emin | Float | 1..1 | Minimum field voltage output (Emin) (< ExcSEXS.emax). Typical value = -5. |
| k | Float | 1..1 | Gain (K) (> 0). Typical value = 100. |
| kc | Float | 1..1 | PI controller gain (Kc) (> 0 if ExcSEXS.tc > 0). Typical value = 0,08. |
| tatb | Float | 1..1 | Gain reduction ratio of lag-lead element ([Ta / Tb]). Typical value = 0,1. |
| tb | Float | 1..1 | Denominator time constant of lag-lead block (Tb) (>= 0). Typical value = 10. |
| tc | Float | 1..1 | PI controller phase lead time constant (Tc) (>= 0). Typical value = 0. |
| te | Float | 1..1 | Time constant of gain block (Te) (> 0). Typical value = 0,05. |

