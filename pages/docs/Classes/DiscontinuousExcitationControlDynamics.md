# DiscontinuousExcitationControlDynamics

Discontinuous excitation control function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- DiscontinuousExcitationControlDynamics
    DiscontinuousExcitationControlDynamics <|-- DiscontinuousExcitationControlUserDefined
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC1A
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC3A
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC2A
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this discontinuous excitation control model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this discontinuous excitation control system model. |

