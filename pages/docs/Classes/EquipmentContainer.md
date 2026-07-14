# EquipmentContainer

A modelling construct to provide a root class for containing equipment.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConnectivityNodeContainer <|-- EquipmentContainer
    ConnectivityNodeContainer : +ConnectivityNode ConnectivityNodes[0..n]
    ConnectivityNodeContainer : +TopologicalNode TopologicalNode[0..n]
    click ConnectivityNodeContainer href "ConnectivityNodeContainer"
    EquipmentContainer <|-- DCEquipmentContainer
    DCEquipmentContainer : +DCNode DCNodes[0..n]
    DCEquipmentContainer : +DCTopologicalNode DCTopologicalNode[0..n]
    click DCEquipmentContainer href "DCEquipmentContainer"
    EquipmentContainer <|-- Bay
    Bay : +VoltageLevel VoltageLevel[1]
    click Bay href "Bay"
    EquipmentContainer <|-- Line
    Line : +SubGeographicalRegion Region[0..1]
    click Line href "Line"
    EquipmentContainer <|-- VoltageLevel
    VoltageLevel : +BaseVoltage BaseVoltage[1]
    VoltageLevel : +Bay Bays[0..n]
    VoltageLevel : +Substation Substation[1]
    VoltageLevel : +Float highVoltageLimit[0..1]
    VoltageLevel : +Float lowVoltageLimit[0..1]
    click VoltageLevel href "VoltageLevel"
    EquipmentContainer <|-- Substation
    Substation : +DCConverterUnit DCConverterUnit[0..n]
    Substation : +SubGeographicalRegion Region[1]
    Substation : +VoltageLevel VoltageLevels[0..n]
    click Substation href "Substation"
    EquipmentContainer : +Equipment Equipments[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Equipments | [Equipment](Equipment.md) | 0..n | Contained equipment. |

