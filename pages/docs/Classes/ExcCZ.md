# ExcCZ

Czech proportion/integral exciter.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcCZ
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcCZ : +Float efdmax[1..1]
    ExcCZ : +Float efdmin[1..1]
    ExcCZ : +Float ka[1..1]
    ExcCZ : +Float ke[1..1]
    ExcCZ : +Float kp[1..1]
    ExcCZ : +Float ta[1..1]
    ExcCZ : +Float tc[1..1]
    ExcCZ : +Float te[1..1]
    ExcCZ : +Float vrmax[1..1]
    ExcCZ : +Float vrmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| efdmax | Float | 1..1 | Exciter output maximum limit (Efdmax) (> ExcCZ.efdmin). |
| efdmin | Float | 1..1 | Exciter output minimum limit (Efdmin) (< ExcCZ.efdmax). |
| ka | Float | 1..1 | Regulator gain (Ka). |
| ke | Float | 1..1 | Exciter constant related to self-excited field (Ke). |
| kp | Float | 1..1 | Regulator proportional gain (Kp). |
| ta | Float | 1..1 | Regulator time constant (Ta) (>= 0). |
| tc | Float | 1..1 | Regulator integral time constant (Tc) (>= 0). |
| te | Float | 1..1 | Exciter time constant, integration rate associated with exciter control (Te) (>= 0). |
| vrmax | Float | 1..1 | Voltage regulator maximum limit (Vrmax) (> ExcCZ.vrmin). |
| vrmin | Float | 1..1 | Voltage regulator minimum limit (Vrmin) (< ExcCZ.vrmax). |

