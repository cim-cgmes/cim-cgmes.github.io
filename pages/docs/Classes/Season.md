# Season

A specified time period of the year.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- Season
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    Season : +SeasonDayTypeSchedule SeasonDayTypeSchedules[0..n]
    Season : +MonthDay endDate[1..1]
    Season : +MonthDay startDate[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| SeasonDayTypeSchedules | [SeasonDayTypeSchedule](SeasonDayTypeSchedule.md) | 0..n | Schedules that use this Season. |
| endDate | MonthDay | 1..1 | Date season ends. |
| startDate | MonthDay | 1..1 | Date season starts. |

