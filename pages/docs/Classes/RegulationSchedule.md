# RegulationSchedule

A pre-established pattern over time for a controlled variable, e.g., busbar voltage.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SeasonDayTypeSchedule <|-- RegulationSchedule
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
    click SeasonDayTypeSchedule href "SeasonDayTypeSchedule"
    RegulationSchedule : +RegulatingControl RegulatingControl[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RegulatingControl | [RegulatingControl](RegulatingControl.md) | 1 | Regulating controls that have this schedule. |

