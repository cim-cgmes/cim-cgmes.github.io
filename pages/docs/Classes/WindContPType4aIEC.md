# WindContPType4aIEC

P control model type 4A. Reference: IEC 61400-27-1:2015, 5.6.5.5.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindContPType4aIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindContPType4aIEC : +WindTurbineType4aIEC WindTurbineType4aIEC[1]
    WindContPType4aIEC : +Float dpmaxp4a[1..1]
    WindContPType4aIEC : +Float tpordp4a[1..1]
    WindContPType4aIEC : +Float tufiltp4a[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindTurbineType4aIEC | [WindTurbineType4aIEC](WindTurbineType4aIEC.md) | 1 | Wind turbine type 4A model with which this wind control P type 4A model is associated. |
| dpmaxp4a | Float | 1..1 | Maximum wind turbine power ramp rate (dpmaxp4A). It is a project-dependent parameter. |
| tpordp4a | Float | 1..1 | Time constant in power order lag (Tpordp4A) (>= 0). It is a type-dependent parameter. |
| tufiltp4a | Float | 1..1 | Voltage measurement filter time constant (Tufiltp4A) (>= 0). It is a type-dependent parameter. |

