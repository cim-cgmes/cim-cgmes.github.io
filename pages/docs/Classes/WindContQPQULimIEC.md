# WindContQPQULimIEC

QP and QU limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.10.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindContQPQULimIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindContQPQULimIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindContQPQULimIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[0..1]
    WindContQPQULimIEC : +Float tpfiltql[1..1]
    WindContQPQULimIEC : +Float tufiltql[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindDynamicsLookupTable | [WindDynamicsLookupTable](WindDynamicsLookupTable.md) | 1..n | The wind dynamics lookup table associated with this QP and QU limitation model. |
| WindTurbineType3or4IEC | [WindTurbineType3or4IEC](WindTurbineType3or4IEC.md) | 0..1 | Wind generator type 3 or type 4 model with which this QP and QU limitation model is associated. |
| tpfiltql | Float | 1..1 | Power measurement filter time constant for Q capacity (Tpfiltql) (>= 0). It is a type-dependent parameter. |
| tufiltql | Float | 1..1 | Voltage measurement filter time constant for Q capacity (Tufiltql) (>= 0). It is a type-dependent parameter. |

