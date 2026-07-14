# Conductor

Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConductingEquipment <|-- Conductor
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
    click ConductingEquipment href "ConductingEquipment"
    Conductor <|-- ACLineSegment
    ACLineSegment : +Clamp Clamp[0..n]
    ACLineSegment : +Cut Cut[0..n]
    ACLineSegment : +Float b0ch[1..1]
    ACLineSegment : +Float bch[1..1]
    ACLineSegment : +Float g0ch[1..1]
    ACLineSegment : +Float gch[0..1]
    ACLineSegment : +Float r[1..1]
    ACLineSegment : +Float r0[1..1]
    ACLineSegment : +Float shortCircuitEndTemperature[1..1]
    ACLineSegment : +Float x[1..1]
    ACLineSegment : +Float x0[1..1]
    click ACLineSegment href "ACLineSegment"
    Conductor : +Float length[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| length | Float | 0..1 | Segment length for calculating line section capabilities. |

