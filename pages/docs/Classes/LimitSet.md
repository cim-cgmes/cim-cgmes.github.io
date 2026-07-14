# LimitSet

Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- LimitSet
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    LimitSet <|-- AnalogLimitSet
    AnalogLimitSet : +AnalogLimit Limits[0..n]
    AnalogLimitSet : +Analog Measurements[1..n]
    click AnalogLimitSet href "AnalogLimitSet"
    LimitSet <|-- AccumulatorLimitSet
    AccumulatorLimitSet : +AccumulatorLimit Limits[1..n]
    AccumulatorLimitSet : +Accumulator Measurements[1..n]
    click AccumulatorLimitSet href "AccumulatorLimitSet"
    LimitSet : +Boolean isPercentageLimits[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| isPercentageLimits | Boolean | 0..1 | Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. |

