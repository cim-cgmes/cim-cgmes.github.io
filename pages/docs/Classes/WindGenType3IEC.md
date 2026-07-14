# WindGenType3IEC

Parent class supporting relationships to IEC wind turbines type 3 generator models of IEC type 3A and 3B.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindGenType3IEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindGenType3IEC <|-- WindGenType3aIEC
    WindGenType3aIEC : +WindTurbineType4IEC WindTurbineType4IEC[0..1]
    WindGenType3aIEC : +Float kpc[1..1]
    WindGenType3aIEC : +Float tic[1..1]
    click WindGenType3aIEC href "WindGenType3aIEC"
    WindGenType3IEC <|-- WindGenType3bIEC
    WindGenType3bIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindGenType3bIEC : +Boolean mwtcwp[1..1]
    WindGenType3bIEC : +Float tg[1..1]
    WindGenType3bIEC : +Float two[1..1]
    click WindGenType3bIEC href "WindGenType3bIEC"
    WindGenType3IEC : +WindTurbineType3IEC WindTurbineType3IEC[0..1]
    WindGenType3IEC : +Float dipmax[1..1]
    WindGenType3IEC : +Float diqmax[1..1]
    WindGenType3IEC : +Float xs[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindTurbineType3IEC | [WindTurbineType3IEC](WindTurbineType3IEC.md) | 0..1 | Wind turbine type 3 model with which this wind generator type 3 is associated. |
| dipmax | Float | 1..1 | Maximum active current ramp rate (dipmax). It is a project-dependent parameter. |
| diqmax | Float | 1..1 | Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter. |
| xs | Float | 1..1 | Electromagnetic transient reactance (xS). It is a type-dependent parameter. |

