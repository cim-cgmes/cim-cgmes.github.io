# DCTerminal

An electrical connection point to generic DC conducting equipment.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCBaseTerminal <|-- DCTerminal
    DCBaseTerminal : +DCNode DCNode[0..1]
    DCBaseTerminal : +DCTopologicalNode DCTopologicalNode[1]
    click DCBaseTerminal href "DCBaseTerminal"
    DCTerminal : +DCConductingEquipment DCConductingEquipment[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCConductingEquipment | [DCConductingEquipment](DCConductingEquipment.md) | 1 | An DC terminal belong to a DC conducting equipment. |

