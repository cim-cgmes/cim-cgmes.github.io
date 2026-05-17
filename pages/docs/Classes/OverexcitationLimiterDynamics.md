# OverexcitationLimiterDynamics

Overexcitation limiter function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- OverexcitationLimiterDynamics
    OverexcitationLimiterDynamics <|-- OverexcLimX1
    OverexcitationLimiterDynamics <|-- OverexcitationLimiterUserDefined
    OverexcitationLimiterDynamics <|-- OverexcLimX2
    OverexcitationLimiterDynamics <|-- OverexcLimIEEE
    OverexcitationLimiterDynamics <|-- OverexcLim2
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this overexcitation limiter model is associated. |

