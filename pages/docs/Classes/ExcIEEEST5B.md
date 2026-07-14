# ExcIEEEST5B

IEEE 421.5-2005 type ST5B model. The type ST5B excitation system is a variation of the type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider summation point with Vref. Reference: IEEE 421.5-2005, 7.5.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcIEEEST5B
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcIEEEST5B : +Float kc[1..1]
    ExcIEEEST5B : +Float kr[1..1]
    ExcIEEEST5B : +Float t1[1..1]
    ExcIEEEST5B : +Float tb1[1..1]
    ExcIEEEST5B : +Float tb2[1..1]
    ExcIEEEST5B : +Float tc1[1..1]
    ExcIEEEST5B : +Float tc2[1..1]
    ExcIEEEST5B : +Float tob1[1..1]
    ExcIEEEST5B : +Float tob2[1..1]
    ExcIEEEST5B : +Float toc1[1..1]
    ExcIEEEST5B : +Float toc2[1..1]
    ExcIEEEST5B : +Float tub1[1..1]
    ExcIEEEST5B : +Float tub2[1..1]
    ExcIEEEST5B : +Float tuc1[1..1]
    ExcIEEEST5B : +Float tuc2[1..1]
    ExcIEEEST5B : +Float vrmax[1..1]
    ExcIEEEST5B : +Float vrmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| kc | Float | 1..1 | Rectifier regulation factor (KC) (>= 0). Typical value = 0,004. |
| kr | Float | 1..1 | Regulator gain (KR) (> 0). Typical value = 200. |
| t1 | Float | 1..1 | Firing circuit time constant (T1) (>= 0). Typical value = 0,004. |
| tb1 | Float | 1..1 | Regulator lag time constant (TB1) (>= 0). Typical value = 6. |
| tb2 | Float | 1..1 | Regulator lag time constant (TB2) (>= 0). Typical value = 0,01. |
| tc1 | Float | 1..1 | Regulator lead time constant (TC1) (>= 0). Typical value = 0,8. |
| tc2 | Float | 1..1 | Regulator lead time constant (TC2) (>= 0). Typical value = 0,08. |
| tob1 | Float | 1..1 | OEL lag time constant (TOB1) (>= 0). Typical value = 2. |
| tob2 | Float | 1..1 | OEL lag time constant (TOB2) (>= 0). Typical value = 0,08. |
| toc1 | Float | 1..1 | OEL lead time constant (TOC1) (>= 0). Typical value = 0,1. |
| toc2 | Float | 1..1 | OEL lead time constant (TOC2) (>= 0). Typical value = 0,08. |
| tub1 | Float | 1..1 | UEL lag time constant (TUB1) (>= 0). Typical value = 10. |
| tub2 | Float | 1..1 | UEL lag time constant (TUB2) (>= 0). Typical value = 0,05. |
| tuc1 | Float | 1..1 | UEL lead time constant (TUC1) (>= 0). Typical value = 2. |
| tuc2 | Float | 1..1 | UEL lead time constant (TUC2) (>= 0). Typical value = 0,1. |
| vrmax | Float | 1..1 | Maximum voltage regulator output (VRMAX) (> 0). Typical value = 5. |
| vrmin | Float | 1..1 | Minimum voltage regulator output (VRMIN) (< 0). Typical value = -4. |

