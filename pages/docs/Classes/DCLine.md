# DCLine

Overhead lines and/or cables connecting two or more HVDC substations.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCEquipmentContainer <|-- DCLine
    DCEquipmentContainer : +DCNode DCNodes[0..n]
    DCEquipmentContainer : +DCTopologicalNode DCTopologicalNode[0..n]
    click DCEquipmentContainer href "DCEquipmentContainer"
    DCLine : +SubGeographicalRegion Region[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Region | [SubGeographicalRegion](SubGeographicalRegion.md) | 0..1 | The SubGeographicalRegion containing the DC line. |

