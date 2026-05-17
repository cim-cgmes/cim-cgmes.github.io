# PFVArControllerType2Dynamics

Power factor or VAr controller type 2 function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- PFVArControllerType2Dynamics
    PFVArControllerType2Dynamics <|-- PFVArType2IEEEPFController
    PFVArControllerType2Dynamics <|-- PFVArType2Common1
    PFVArControllerType2Dynamics <|-- PFVArType2IEEEVArController
    PFVArControllerType2Dynamics <|-- PFVArControllerType2UserDefined
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this power factor or VAr controller type 2 is associated. |

