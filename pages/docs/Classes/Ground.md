# Ground

A point where the system is grounded used for connecting conducting equipment to ground. The power system model can have any number of grounds.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConductingEquipment <|-- Ground
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
    click ConductingEquipment href "ConductingEquipment"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

