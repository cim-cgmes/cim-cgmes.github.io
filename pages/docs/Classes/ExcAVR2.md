# ExcAVR2

Italian excitation system corresponding to IEEE (1968) type 2 model. It represents an alternator and rotating diodes and electromechanic voltage regulators.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcAVR2
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcAVR2 : +Float e1[1..1]
    ExcAVR2 : +Float e2[1..1]
    ExcAVR2 : +Float ka[1..1]
    ExcAVR2 : +Float kf[1..1]
    ExcAVR2 : +Float se1[1..1]
    ExcAVR2 : +Float se2[1..1]
    ExcAVR2 : +Float ta[1..1]
    ExcAVR2 : +Float tb[1..1]
    ExcAVR2 : +Float te[1..1]
    ExcAVR2 : +Float tf1[1..1]
    ExcAVR2 : +Float tf2[1..1]
    ExcAVR2 : +Float vrmn[1..1]
    ExcAVR2 : +Float vrmx[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| e1 | Float | 1..1 | Field voltage value 1 (E1). Typical value = 4,18. |
| e2 | Float | 1..1 | Field voltage value 2 (E2). Typical value = 3,14. |
| ka | Float | 1..1 | AVR gain (KA). Typical value = 500. |
| kf | Float | 1..1 | Rate feedback gain (KF). Typical value = 0,12. |
| se1 | Float | 1..1 | Saturation factor at E1 (S[E1]). Typical value = 0.1. |
| se2 | Float | 1..1 | Saturation factor at E2 (S[E2]). Typical value = 0,03. |
| ta | Float | 1..1 | AVR time constant (TA) (>= 0). Typical value = 0,02. |
| tb | Float | 1..1 | AVR time constant (TB) (>= 0). Typical value = 0. |
| te | Float | 1..1 | Exciter time constant (TE) (>= 0). Typical value = 1. |
| tf1 | Float | 1..1 | Rate feedback time constant (TF1) (>= 0). Typical value = 1. |
| tf2 | Float | 1..1 | Rate feedback time constant (TF2) (>= 0). Typical value = 1. |
| vrmn | Float | 1..1 | Minimum AVR output (VRMN). Typical value = -6. |
| vrmx | Float | 1..1 | Maximum AVR output (VRMX). Typical value = 7. |

