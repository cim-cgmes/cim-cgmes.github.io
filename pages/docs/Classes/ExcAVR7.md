# ExcAVR7

IVO excitation system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcAVR7
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcAVR7 : +Float a1[1..1]
    ExcAVR7 : +Float a2[1..1]
    ExcAVR7 : +Float a3[1..1]
    ExcAVR7 : +Float a4[1..1]
    ExcAVR7 : +Float a5[1..1]
    ExcAVR7 : +Float a6[1..1]
    ExcAVR7 : +Float k1[1..1]
    ExcAVR7 : +Float k3[1..1]
    ExcAVR7 : +Float k5[1..1]
    ExcAVR7 : +Float t1[1..1]
    ExcAVR7 : +Float t2[1..1]
    ExcAVR7 : +Float t3[1..1]
    ExcAVR7 : +Float t4[1..1]
    ExcAVR7 : +Float t5[1..1]
    ExcAVR7 : +Float t6[1..1]
    ExcAVR7 : +Float vmax1[1..1]
    ExcAVR7 : +Float vmax3[1..1]
    ExcAVR7 : +Float vmax5[1..1]
    ExcAVR7 : +Float vmin1[1..1]
    ExcAVR7 : +Float vmin3[1..1]
    ExcAVR7 : +Float vmin5[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| a1 | Float | 1..1 | Lead coefficient (A1). Typical value = 0,5. |
| a2 | Float | 1..1 | Lag coefficient (A2). Typical value = 0,5. |
| a3 | Float | 1..1 | Lead coefficient (A3). Typical value = 0,5. |
| a4 | Float | 1..1 | Lag coefficient (A4). Typical value = 0,5. |
| a5 | Float | 1..1 | Lead coefficient (A5). Typical value = 0,5. |
| a6 | Float | 1..1 | Lag coefficient (A6). Typical value = 0,5. |
| k1 | Float | 1..1 | Gain (K1). Typical value = 1. |
| k3 | Float | 1..1 | Gain (K3). Typical value = 3. |
| k5 | Float | 1..1 | Gain (K5). Typical value = 1. |
| t1 | Float | 1..1 | Lead time constant (T1) (>= 0). Typical value = 0,05. |
| t2 | Float | 1..1 | Lag time constant (T2) (>= 0). Typical value = 0,1. |
| t3 | Float | 1..1 | Lead time constant (T3) (>= 0). Typical value = 0,1. |
| t4 | Float | 1..1 | Lag time constant (T4) (>= 0). Typical value = 0,1. |
| t5 | Float | 1..1 | Lead time constant (T5) (>= 0). Typical value = 0,1. |
| t6 | Float | 1..1 | Lag time constant (T6) (>= 0). Typical value = 0,1. |
| vmax1 | Float | 1..1 | Lead-lag maximum limit (Vmax1) (> ExcAVR7.vmin1). Typical value = 5. |
| vmax3 | Float | 1..1 | Lead-lag maximum limit (Vmax3) (> ExcAVR7.vmin3). Typical value = 5. |
| vmax5 | Float | 1..1 | Lead-lag maximum limit (Vmax5) (> ExcAVR7.vmin5). Typical value = 5. |
| vmin1 | Float | 1..1 | Lead-lag minimum limit (Vmin1) (< ExcAVR7.vmax1). Typical value = -5. |
| vmin3 | Float | 1..1 | Lead-lag minimum limit (Vmin3) (< ExcAVR7.vmax3). Typical value = -5. |
| vmin5 | Float | 1..1 | Lead-lag minimum limit (Vmin5) (< ExcAVR7.vmax5). Typical value = -2. |

