# DCShunt

A shunt device within the DC system, typically used for filtering. Needed for transient and short circuit studies.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCConductingEquipment <|-- DCShunt
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
    click DCConductingEquipment href "DCConductingEquipment"
    DCShunt : +Float capacitance[1..1]
    DCShunt : +Float resistance[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| capacitance | Float | 1..1 | Capacitance of the DC shunt. |
| resistance | Float | 1..1 | Resistance of the DC device. |

