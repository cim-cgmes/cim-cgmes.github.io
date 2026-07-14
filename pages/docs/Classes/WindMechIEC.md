# WindMechIEC

Two mass model. Reference: IEC 61400-27-1:2015, 5.6.2.1.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindMechIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindMechIEC : +WindTurbineType1or2IEC WindTurbineType1or2IEC[0..1]
    WindMechIEC : +WindTurbineType3IEC WindTurbineType3IEC[0..1]
    WindMechIEC : +WindTurbineType4bIEC WindTurbineType4bIEC[0..1]
    WindMechIEC : +Float cdrt[1..1]
    WindMechIEC : +Float hgen[1..1]
    WindMechIEC : +Float hwtr[1..1]
    WindMechIEC : +Float kdrt[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindTurbineType1or2IEC | [WindTurbineType1or2IEC](WindTurbineType1or2IEC.md) | 0..1 | Wind generator type 1 or type 2 model with which this wind mechanical model is associated. |
| WindTurbineType3IEC | [WindTurbineType3IEC](WindTurbineType3IEC.md) | 0..1 | Wind turbine type 3 model with which this wind mechanical model is associated. |
| WindTurbineType4bIEC | [WindTurbineType4bIEC](WindTurbineType4bIEC.md) | 0..1 | Wind turbine type 4B model with which this wind mechanical model is associated. |
| cdrt | Float | 1..1 | Drive train damping (cdrt). It is a type-dependent parameter. |
| hgen | Float | 1..1 | Inertia constant of generator (Hgen) (>= 0). It is a type-dependent parameter. |
| hwtr | Float | 1..1 | Inertia constant of wind turbine rotor (HWTR) (>= 0). It is a type-dependent parameter. |
| kdrt | Float | 1..1 | Drive train stiffness (kdrt). It is a type-dependent parameter. |

