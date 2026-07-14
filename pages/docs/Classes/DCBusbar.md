# DCBusbar

A busbar within a DC system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCConductingEquipment <|-- DCBusbar
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
    click DCConductingEquipment href "DCConductingEquipment"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

