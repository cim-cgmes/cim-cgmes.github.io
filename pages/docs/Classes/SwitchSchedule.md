# SwitchSchedule

A schedule of switch positions. If RegularTimePoint.value1 is 0, the switch is open. If 1, the switch is closed.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SeasonDayTypeSchedule <|-- SwitchSchedule
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
    click SeasonDayTypeSchedule href "SeasonDayTypeSchedule"
    SwitchSchedule : +Switch Switch[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Switch | [Switch](Switch.md) | 1 | A SwitchSchedule is associated with a Switch. |

