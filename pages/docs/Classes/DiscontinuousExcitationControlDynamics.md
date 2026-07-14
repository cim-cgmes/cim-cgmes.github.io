# DiscontinuousExcitationControlDynamics

Discontinuous excitation control function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- DiscontinuousExcitationControlDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC1A
    DiscExcContIEEEDEC1A : +Float esc[1..1]
    DiscExcContIEEEDEC1A : +Float kan[1..1]
    DiscExcContIEEEDEC1A : +Float ketl[1..1]
    DiscExcContIEEEDEC1A : +Float tan[1..1]
    DiscExcContIEEEDEC1A : +Float td[1..1]
    DiscExcContIEEEDEC1A : +Float tl1[1..1]
    DiscExcContIEEEDEC1A : +Float tl2[1..1]
    DiscExcContIEEEDEC1A : +Float tw5[1..1]
    DiscExcContIEEEDEC1A : +Float val[1..1]
    DiscExcContIEEEDEC1A : +Float vanmax[1..1]
    DiscExcContIEEEDEC1A : +Float vomax[1..1]
    DiscExcContIEEEDEC1A : +Float vomin[1..1]
    DiscExcContIEEEDEC1A : +Float vsmax[1..1]
    DiscExcContIEEEDEC1A : +Float vsmin[1..1]
    DiscExcContIEEEDEC1A : +Float vtc[1..1]
    DiscExcContIEEEDEC1A : +Float vtlmt[1..1]
    DiscExcContIEEEDEC1A : +Float vtm[1..1]
    DiscExcContIEEEDEC1A : +Float vtn[1..1]
    click DiscExcContIEEEDEC1A href "DiscExcContIEEEDEC1A"
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC2A
    DiscExcContIEEEDEC2A : +Float td1[1..1]
    DiscExcContIEEEDEC2A : +Float td2[1..1]
    DiscExcContIEEEDEC2A : +Float vdmax[1..1]
    DiscExcContIEEEDEC2A : +Float vdmin[1..1]
    DiscExcContIEEEDEC2A : +Float vk[1..1]
    click DiscExcContIEEEDEC2A href "DiscExcContIEEEDEC2A"
    DiscontinuousExcitationControlDynamics <|-- DiscontinuousExcitationControlUserDefined
    DiscontinuousExcitationControlUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    DiscontinuousExcitationControlUserDefined : +Boolean proprietary[1..1]
    click DiscontinuousExcitationControlUserDefined href "DiscontinuousExcitationControlUserDefined"
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC3A
    DiscExcContIEEEDEC3A : +Float tdr[1..1]
    DiscExcContIEEEDEC3A : +Float vtmin[1..1]
    click DiscExcContIEEEDEC3A href "DiscExcContIEEEDEC3A"
    DiscontinuousExcitationControlDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    DiscontinuousExcitationControlDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this discontinuous excitation control model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this discontinuous excitation control system model. |

