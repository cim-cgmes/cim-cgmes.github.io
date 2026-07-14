# WindProtectionIEC

The grid protection model includes protection against over- and under-voltage, and against over- and under-frequency. Reference: IEC 61400-27-1:2015, 5.6.6.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- WindProtectionIEC
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    WindProtectionIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindProtectionIEC : +WindTurbineType1or2IEC WindTurbineType1or2IEC[0..1]
    WindProtectionIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[0..1]
    WindProtectionIEC : +Float dfimax[1..1]
    WindProtectionIEC : +Float fover[1..1]
    WindProtectionIEC : +Float funder[1..1]
    WindProtectionIEC : +Boolean mzc[1..1]
    WindProtectionIEC : +Float tfma[1..1]
    WindProtectionIEC : +Float uover[1..1]
    WindProtectionIEC : +Float uunder[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindDynamicsLookupTable | [WindDynamicsLookupTable](WindDynamicsLookupTable.md) | 1..n | The wind dynamics lookup table associated with this grid protection model. |
| WindTurbineType1or2IEC | [WindTurbineType1or2IEC](WindTurbineType1or2IEC.md) | 0..1 | Wind generator type 1 or type 2 model with which this wind turbine protection model is associated. |
| WindTurbineType3or4IEC | [WindTurbineType3or4IEC](WindTurbineType3or4IEC.md) | 0..1 | Wind generator type 3 or type 4 model with which this wind turbine protection model is associated. |
| dfimax | Float | 1..1 | Maximum rate of change of frequency (dFmax). It is a type-dependent parameter. |
| fover | Float | 1..1 | Wind turbine over frequency protection activation threshold (fover). It is a project-dependent parameter. |
| funder | Float | 1..1 | Wind turbine under frequency protection activation threshold (funder). It is a project-dependent parameter. |
| mzc | Boolean | 1..1 | Zero crossing measurement mode (Mzc). It is a type-dependent parameter. true = WT protection system uses zero crossings to detect frequency (1 in the IEC model) false = WT protection system does not use zero crossings to detect frequency (0 in the IEC model). |
| tfma | Float | 1..1 | Time interval of moving average window (TfMA) (>= 0). It is a type-dependent parameter. |
| uover | Float | 1..1 | Wind turbine over voltage protection activation threshold (uover). It is a project-dependent parameter. |
| uunder | Float | 1..1 | Wind turbine under voltage protection activation threshold (uunder). It is a project-dependent parameter. |

