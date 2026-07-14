# DCLineSegment

A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DCConductingEquipment <|-- DCLineSegment
    DCConductingEquipment : +DCTerminal DCTerminals[0..n]
    DCConductingEquipment : +Float ratedUdc[1..1]
    click DCConductingEquipment href "DCConductingEquipment"
    DCLineSegment : +Float capacitance[1..1]
    DCLineSegment : +Float inductance[1..1]
    DCLineSegment : +Float length[0..1]
    DCLineSegment : +Float resistance[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| capacitance | Float | 1..1 | Capacitance of the DC line segment. Significant for cables only. |
| inductance | Float | 1..1 | Inductance of the DC line segment. Negligible compared with DCSeriesDevice used for smoothing. |
| length | Float | 0..1 | Segment length for calculating line section capabilities. |
| resistance | Float | 1..1 | Resistance of the DC line segment. |

