# TurbineLoadControllerDynamics

Turbine load controller function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- TurbineLoadControllerDynamics
    TurbineLoadControllerDynamics <|-- TurbLCFB1
    TurbineLoadControllerDynamics <|-- TurbineLoadControllerUserDefined
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TurbineGovernorDynamics | [TurbineGovernorDynamics](TurbineGovernorDynamics.md) | 1 | Turbine-governor controlled by this turbine load controller. |

