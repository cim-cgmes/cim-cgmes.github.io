# OverexcitationLimiterDynamics

Overexcitation limiter function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- OverexcitationLimiterDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    OverexcitationLimiterDynamics <|-- OverexcLimX1
    OverexcLimX1 : +Float efd1[1..1]
    OverexcLimX1 : +Float efd2[1..1]
    OverexcLimX1 : +Float efd3[1..1]
    OverexcLimX1 : +Float efddes[1..1]
    OverexcLimX1 : +Float efdrated[1..1]
    OverexcLimX1 : +Float kmx[1..1]
    OverexcLimX1 : +Float t1[1..1]
    OverexcLimX1 : +Float t2[1..1]
    OverexcLimX1 : +Float t3[1..1]
    OverexcLimX1 : +Float vlow[1..1]
    click OverexcLimX1 href "OverexcLimX1"
    OverexcitationLimiterDynamics <|-- OverexcLimIEEE
    OverexcLimIEEE : +Float hyst[1..1]
    OverexcLimIEEE : +Float ifdlim[1..1]
    OverexcLimIEEE : +Float ifdmax[1..1]
    OverexcLimIEEE : +Float itfpu[1..1]
    OverexcLimIEEE : +Float kcd[1..1]
    OverexcLimIEEE : +Float kramp[1..1]
    click OverexcLimIEEE href "OverexcLimIEEE"
    OverexcitationLimiterDynamics <|-- OverexcLim2
    OverexcLim2 : +Float ifdlim[1..1]
    OverexcLim2 : +Float koi[1..1]
    OverexcLim2 : +Float voimax[1..1]
    OverexcLim2 : +Float voimin[1..1]
    click OverexcLim2 href "OverexcLim2"
    OverexcitationLimiterDynamics <|-- OverexcitationLimiterUserDefined
    OverexcitationLimiterUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    OverexcitationLimiterUserDefined : +Boolean proprietary[1..1]
    click OverexcitationLimiterUserDefined href "OverexcitationLimiterUserDefined"
    OverexcitationLimiterDynamics <|-- OverexcLimX2
    OverexcLimX2 : +Float efd1[1..1]
    OverexcLimX2 : +Float efd2[1..1]
    OverexcLimX2 : +Float efd3[1..1]
    OverexcLimX2 : +Float efddes[1..1]
    OverexcLimX2 : +Float efdrated[1..1]
    OverexcLimX2 : +Float kmx[1..1]
    OverexcLimX2 : +Boolean m[1..1]
    OverexcLimX2 : +Float t1[1..1]
    OverexcLimX2 : +Float t2[1..1]
    OverexcLimX2 : +Float t3[1..1]
    OverexcLimX2 : +Float vlow[1..1]
    click OverexcLimX2 href "OverexcLimX2"
    OverexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this overexcitation limiter model is associated. |

