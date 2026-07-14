# WindAeroConstIEC

Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC 61400-27-1:2015, 5.6.1.1.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindAeroConstIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindAeroConstIEC : +WindGenTurbineType1aIEC WindGenTurbineType1aIEC[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindGenTurbineType1aIEC | [WindGenTurbineType1aIEC](WindGenTurbineType1aIEC.md) | 1 | Wind turbine type 1A model with which this wind aerodynamic model is associated. |

