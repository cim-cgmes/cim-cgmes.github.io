# DCGround

A ground within a DC system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCConductingEquipment <|-- DCGround
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
    click DCConductingEquipment href "DCConductingEquipment"
    DCGround : +Float inductance[0..1]
    DCGround : +Float r[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| inductance | Float | 0..1 | Inductance to ground. |
| r | Float | 0..1 | Resistance to ground. |

