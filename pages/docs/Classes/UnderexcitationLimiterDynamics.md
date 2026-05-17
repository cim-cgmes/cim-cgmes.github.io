# UnderexcitationLimiterDynamics

Underexcitation limiter function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- UnderexcitationLimiterDynamics
    UnderexcitationLimiterDynamics <|-- UnderexcLimX1
    UnderexcitationLimiterDynamics <|-- UnderexcLimIEEE2
    UnderexcitationLimiterDynamics <|-- UnderexcitationLimiterUserDefined
    UnderexcitationLimiterDynamics <|-- UnderexcLimIEEE1
    UnderexcitationLimiterDynamics <|-- UnderexcLimX2
    UnderexcitationLimiterDynamics <|-- UnderexcLim2Simplified
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this underexcitation limiter model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this underexcitation limiter model. |

