# ExcAVR4

Italian excitation system. It represents a static exciter and electric voltage regulator.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcAVR4
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcAVR4 : +Boolean imul[1..1]
    ExcAVR4 : +Float ka[1..1]
    ExcAVR4 : +Float ke[1..1]
    ExcAVR4 : +Float kif[1..1]
    ExcAVR4 : +Float t1[1..1]
    ExcAVR4 : +Float t1if[1..1]
    ExcAVR4 : +Float t2[1..1]
    ExcAVR4 : +Float t3[1..1]
    ExcAVR4 : +Float t4[1..1]
    ExcAVR4 : +Float tif[1..1]
    ExcAVR4 : +Float vfmn[1..1]
    ExcAVR4 : +Float vfmx[1..1]
    ExcAVR4 : +Float vrmn[1..1]
    ExcAVR4 : +Float vrmx[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| imul | Boolean | 1..1 | AVR output voltage dependency selector (IMUL). true = selector is connected false = selector is not connected. Typical value = true. |
| ka | Float | 1..1 | AVR gain (KA). Typical value = 300. |
| ke | Float | 1..1 | Exciter gain (KE). Typical value = 1. |
| kif | Float | 1..1 | Exciter internal reactance (KIF). Typical value = 0. |
| t1 | Float | 1..1 | AVR time constant (T1) (>= 0). Typical value = 4,8. |
| t1if | Float | 1..1 | Exciter current feedback time constant (T1IF) (>= 0). Typical value = 60. |
| t2 | Float | 1..1 | AVR time constant (T2) (>= 0). Typical value = 1,5. |
| t3 | Float | 1..1 | AVR time constant (T3) (>= 0). Typical value = 0. |
| t4 | Float | 1..1 | AVR time constant (T4) (>= 0). Typical value = 0. |
| tif | Float | 1..1 | Exciter current feedback time constant (TIF) (>= 0). Typical value = 0. |
| vfmn | Float | 1..1 | Minimum exciter output (VFMN). Typical value = 0. |
| vfmx | Float | 1..1 | Maximum exciter output (VFMX). Typical value = 5. |
| vrmn | Float | 1..1 | Minimum AVR output (VRMN). Typical value = 0. |
| vrmx | Float | 1..1 | Maximum AVR output (VRMX). Typical value = 5. |

