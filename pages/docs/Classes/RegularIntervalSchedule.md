# RegularIntervalSchedule

The schedule has time points where the time between them is constant.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    BasicIntervalSchedule <|-- RegularIntervalSchedule
    BasicIntervalSchedule : +DateTime startTime[1..1]
    BasicIntervalSchedule : +UnitSymbol value1Unit[1..1]
    BasicIntervalSchedule : +UnitSymbol value2Unit[0..1]
    click BasicIntervalSchedule href "BasicIntervalSchedule"
    RegularIntervalSchedule <|-- SeasonDayTypeSchedule
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
    click SeasonDayTypeSchedule href "SeasonDayTypeSchedule"
    RegularIntervalSchedule : +RegularTimePoint TimePoints[1..n]
    RegularIntervalSchedule : +DateTime endTime[1..1]
    RegularIntervalSchedule : +Float timeStep[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TimePoints | [RegularTimePoint](RegularTimePoint.md) | 1..n | The regular interval time point data values that define this schedule. |
| endTime | DateTime | 1..1 | The time for the last time point. The value can be a time of day, not a specific date. |
| timeStep | Float | 1..1 | The time between each pair of subsequent regular time points in sequence order. |

