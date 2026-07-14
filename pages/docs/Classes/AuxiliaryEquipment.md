# AuxiliaryEquipment

AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function. AuxiliaryEquipment is attached to primary equipment via an association with Terminal.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Equipment <|-- AuxiliaryEquipment
    Equipment : +EquipmentContainer EquipmentContainer[0..1]
    Equipment : +OperationalLimitSet OperationalLimitSet[0..n]
    Equipment : +Boolean aggregate[0..1]
    Equipment : +Boolean inService[1..1]
    Equipment : +Boolean normallyInService[0..1]
    click Equipment href "Equipment"
    AuxiliaryEquipment <|-- FaultIndicator
    click FaultIndicator href "FaultIndicator"
    AuxiliaryEquipment <|-- Sensor
    click Sensor href "Sensor"
    AuxiliaryEquipment <|-- SurgeArrester
    click SurgeArrester href "SurgeArrester"
    AuxiliaryEquipment <|-- WaveTrap
    click WaveTrap href "WaveTrap"
    AuxiliaryEquipment : +Terminal Terminal[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Terminal | [Terminal](Terminal.md) | 1 | The Terminal at the equipment where the AuxiliaryEquipment is attached. |

