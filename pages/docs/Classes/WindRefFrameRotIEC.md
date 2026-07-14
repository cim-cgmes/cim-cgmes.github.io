# WindRefFrameRotIEC

Reference frame rotation model. Reference: IEC 61400-27-1:2015, 5.6.3.5.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindRefFrameRotIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindRefFrameRotIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[1]
    WindRefFrameRotIEC : +Float tpll[1..1]
    WindRefFrameRotIEC : +Float upll1[1..1]
    WindRefFrameRotIEC : +Float upll2[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindTurbineType3or4IEC | [WindTurbineType3or4IEC](WindTurbineType3or4IEC.md) | 1 | Wind turbine type 3 or type 4 model with which this reference frame rotation model is associated. |
| tpll | Float | 1..1 | Time constant for PLL first order filter model (TPLL) (>= 0). It is a type-dependent parameter. |
| upll1 | Float | 1..1 | Voltage below which the angle of the voltage is filtered and possibly also frozen (uPLL1). It is a type-dependent parameter. |
| upll2 | Float | 1..1 | Voltage (uPLL2) below which the angle of the voltage is frozen if uPLL2 is smaller or equal to uPLL1 . It is a type-dependent parameter. |

