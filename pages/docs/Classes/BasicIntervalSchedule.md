# BasicIntervalSchedule

Schedule of values at points in time.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- BasicIntervalSchedule
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    BasicIntervalSchedule <|-- RegularIntervalSchedule
    RegularIntervalSchedule : +RegularTimePoint TimePoints[1..n]
    RegularIntervalSchedule : +DateTime endTime[1..1]
    RegularIntervalSchedule : +Float timeStep[1..1]
    click RegularIntervalSchedule href "RegularIntervalSchedule"
    BasicIntervalSchedule : +DateTime startTime[1..1]
    BasicIntervalSchedule : +UnitSymbol value1Unit[1..1]
    BasicIntervalSchedule : +UnitSymbol value2Unit[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| startTime | DateTime | 1..1 | The time for the first time point. The value can be a time of day, not a specific date. |
| value1Unit | [UnitSymbol](UnitSymbol.md) | 1..1 | Value1 units of measure. |
| value2Unit | [UnitSymbol](UnitSymbol.md) | 0..1 | Value2 units of measure. |

