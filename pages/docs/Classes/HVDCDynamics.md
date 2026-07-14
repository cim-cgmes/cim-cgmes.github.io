# HVDCDynamics

HVDC whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- HVDCDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    HVDCDynamics <|-- VSCDynamics
    VSCDynamics : +VsConverter VsConverter[1]
    click VSCDynamics href "VSCDynamics"
    HVDCDynamics <|-- CSCDynamics
    CSCDynamics : +CsConverter CSConverter[1]
    click CSCDynamics href "CSCDynamics"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

