# VoltageAdjusterDynamics

Voltage adjuster function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- VoltageAdjusterDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    VoltageAdjusterDynamics <|-- VoltageAdjusterUserDefined
    VoltageAdjusterUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    VoltageAdjusterUserDefined : +Boolean proprietary[1..1]
    click VoltageAdjusterUserDefined href "VoltageAdjusterUserDefined"
    VoltageAdjusterDynamics <|-- VAdjIEEE
    VAdjIEEE : +Float adjslew[1..1]
    VAdjIEEE : +Float taoff[1..1]
    VAdjIEEE : +Float taon[1..1]
    VAdjIEEE : +Float vadjf[1..1]
    VAdjIEEE : +Float vadjmax[1..1]
    VAdjIEEE : +Float vadjmin[1..1]
    click VAdjIEEE href "VAdjIEEE"
    VoltageAdjusterDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PFVArControllerType1Dynamics | [PFVArControllerType1Dynamics](PFVArControllerType1Dynamics.md) | 1 | Power factor or VAr controller type 1 model with which this voltage adjuster is associated. |

