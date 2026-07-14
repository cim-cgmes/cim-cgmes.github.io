# DayType

Group of similar days. For example it could be used to represent weekdays, weekend, or holidays.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- DayType
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    DayType : +SeasonDayTypeSchedule SeasonDayTypeSchedules[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| SeasonDayTypeSchedules | [SeasonDayTypeSchedule](SeasonDayTypeSchedule.md) | 0..n | Schedules that use this DayType. |

