# WindTurbineType4IEC

Parent class supporting relationships to IEC wind turbines type 4 including their control models.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType3or4IEC <|-- WindTurbineType4IEC
    WindTurbineType3or4IEC : +WindContQIEC WIndContQIEC[1]
    WindTurbineType3or4IEC : +WindContCurrLimIEC WindContCurrLimIEC[1]
    WindTurbineType3or4IEC : +WindContQLimIEC WindContQLimIEC[0..1]
    WindTurbineType3or4IEC : +WindContQPQULimIEC WindContQPQULimIEC[0..1]
    WindTurbineType3or4IEC : +WindProtectionIEC WindProtectionIEC[1]
    WindTurbineType3or4IEC : +WindRefFrameRotIEC WindRefFrameRotIEC[1]
    click WindTurbineType3or4IEC href "WindTurbineType3or4IEC"
    WindTurbineType4IEC <|-- WindTurbineType4aIEC
    WindTurbineType4aIEC : +WindContPType4aIEC WindContPType4aIEC[1]
    WindTurbineType4aIEC : +WindGenType4IEC WindGenType4IEC[0..1]
    click WindTurbineType4aIEC href "WindTurbineType4aIEC"
    WindTurbineType4IEC <|-- WindTurbineType4bIEC
    WindTurbineType4bIEC : +WindContPType4bIEC WindContPType4bIEC[1]
    WindTurbineType4bIEC : +WindGenType4IEC WindGenType4IEC[0..1]
    WindTurbineType4bIEC : +WindMechIEC WindMechIEC[1]
    click WindTurbineType4bIEC href "WindTurbineType4bIEC"
    WindTurbineType4IEC : +WindGenType3aIEC WindGenType3aIEC[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindGenType3aIEC | [WindGenType3aIEC](WindGenType3aIEC.md) | 0..1 | Wind generator type 3A model associated with this wind turbine type 4 model. |

