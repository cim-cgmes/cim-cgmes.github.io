# DCConductingEquipment

The parts of the DC power system that are designed to carry current or that are conductively connected through DC terminals.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Equipment <|-- DCConductingEquipment
    Equipment : +EquipmentContainer EquipmentContainer[0..1]
    Equipment : +OperationalLimitSet OperationalLimitSet[0..n]
    Equipment : +Boolean aggregate[0..1]
    Equipment : +Boolean inService[1..1]
    Equipment : +Boolean normallyInService[0..1]
    click Equipment href "Equipment"
    DCConductingEquipment <|-- DCSwitch
    click DCSwitch href "DCSwitch"
    DCConductingEquipment <|-- DCSeriesDevice
    DCSeriesDevice : +Float inductance[1..1]
    DCSeriesDevice : +Float resistance[1..1]
    click DCSeriesDevice href "DCSeriesDevice"
    DCConductingEquipment <|-- DCGround
    DCGround : +Float inductance[0..1]
    DCGround : +Float r[0..1]
    click DCGround href "DCGround"
    DCConductingEquipment <|-- DCChopper
    click DCChopper href "DCChopper"
    DCConductingEquipment <|-- DCShunt
    DCShunt : +Float capacitance[1..1]
    DCShunt : +Float resistance[1..1]
    click DCShunt href "DCShunt"
    DCConductingEquipment <|-- DCBusbar
    click DCBusbar href "DCBusbar"
    DCConductingEquipment <|-- DCLineSegment
    DCLineSegment : +Float capacitance[1..1]
    DCLineSegment : +Float inductance[1..1]
    DCLineSegment : +Float length[0..1]
    DCLineSegment : +Float resistance[1..1]
    click DCLineSegment href "DCLineSegment"
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCTerminals | [DCTerminal](DCTerminal.md) | 0..n | A DC conducting equipment has DC terminals. |
| ratedUdc | Float | 1..1 | Rated DC device voltage. The attribute shall be a positive value. It is configuration data used in power flow. |

