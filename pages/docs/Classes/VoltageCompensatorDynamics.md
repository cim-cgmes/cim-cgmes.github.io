# VoltageCompensatorDynamics

Voltage compensator function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- VoltageCompensatorDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    VoltageCompensatorDynamics <|-- VCompIEEEType1
    VCompIEEEType1 : +Float rc[1..1]
    VCompIEEEType1 : +Float tr[1..1]
    VCompIEEEType1 : +Float xc[1..1]
    click VCompIEEEType1 href "VCompIEEEType1"
    VoltageCompensatorDynamics <|-- VCompIEEEType2
    VCompIEEEType2 : +GenICompensationForGenJ GenICompensationForGenJ[2..n]
    VCompIEEEType2 : +Float tr[1..1]
    click VCompIEEEType2 href "VCompIEEEType2"
    VoltageCompensatorDynamics <|-- VoltageCompensatorUserDefined
    VoltageCompensatorUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    VoltageCompensatorUserDefined : +Boolean proprietary[1..1]
    click VoltageCompensatorUserDefined href "VoltageCompensatorUserDefined"
    VoltageCompensatorDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    VoltageCompensatorDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this voltage compensator is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this voltage compensator model. |

