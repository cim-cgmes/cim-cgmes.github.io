# DCSeriesDevice

A series device within the DC system, typically a reactor used for filtering or smoothing. Needed for transient and short circuit studies.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCConductingEquipment <|-- DCSeriesDevice
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
    click DCConductingEquipment href "DCConductingEquipment"
    DCSeriesDevice : +Float inductance[1..1]
    DCSeriesDevice : +Float resistance[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| inductance | Float | 1..1 | Inductance of the device. |
| resistance | Float | 1..1 | Resistance of the DC device. |

