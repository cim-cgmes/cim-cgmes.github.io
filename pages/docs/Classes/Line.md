# Line

Contains equipment beyond a substation belonging to a power transmission line.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EquipmentContainer <|-- Line
    EquipmentContainer : +Equipment Equipments[0..n]
    click EquipmentContainer href "EquipmentContainer"
    Line : +SubGeographicalRegion Region[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Region | [SubGeographicalRegion](SubGeographicalRegion.md) | 0..1 | The sub-geographical region of the line. |

