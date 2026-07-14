# SeasonDayTypeSchedule

A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    RegularIntervalSchedule <|-- SeasonDayTypeSchedule
    RegularIntervalSchedule : +RegularTimePoint TimePoints[1..n]
    RegularIntervalSchedule : +DateTime endTime[1..1]
    RegularIntervalSchedule : +Float timeStep[1..1]
    click RegularIntervalSchedule href "RegularIntervalSchedule"
    SeasonDayTypeSchedule <|-- NonConformLoadSchedule
    NonConformLoadSchedule : +NonConformLoadGroup NonConformLoadGroup[1]
    click NonConformLoadSchedule href "NonConformLoadSchedule"
    SeasonDayTypeSchedule <|-- SwitchSchedule
    SwitchSchedule : +Switch Switch[1]
    click SwitchSchedule href "SwitchSchedule"
    SeasonDayTypeSchedule <|-- RegulationSchedule
    RegulationSchedule : +RegulatingControl RegulatingControl[1]
    click RegulationSchedule href "RegulationSchedule"
    SeasonDayTypeSchedule <|-- TapSchedule
    TapSchedule : +TapChanger TapChanger[1]
    click TapSchedule href "TapSchedule"
    SeasonDayTypeSchedule <|-- ConformLoadSchedule
    ConformLoadSchedule : +ConformLoadGroup ConformLoadGroup[1]
    click ConformLoadSchedule href "ConformLoadSchedule"
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DayType | [DayType](DayType.md) | 1..1 | DayType for the Schedule. |
| Season | [Season](Season.md) | 1..1 | Season for the Schedule. |

