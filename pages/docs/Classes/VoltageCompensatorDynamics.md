# VoltageCompensatorDynamics

Voltage compensator function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- VoltageCompensatorDynamics
    VoltageCompensatorDynamics <|-- VCompIEEEType1
    VoltageCompensatorDynamics <|-- VCompIEEEType2
    VoltageCompensatorDynamics <|-- VoltageCompensatorUserDefined
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this voltage compensator is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this voltage compensator model. |

