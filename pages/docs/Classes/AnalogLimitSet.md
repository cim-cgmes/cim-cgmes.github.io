# AnalogLimitSet

An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    LimitSet <|-- AnalogLimitSet
    LimitSet : +Boolean isPercentageLimits[0..1]
    click LimitSet href "LimitSet"
    AnalogLimitSet : +AnalogLimit Limits[0..n]
    AnalogLimitSet : +Analog Measurements[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Limits | [AnalogLimit](AnalogLimit.md) | 0..n | The limit values used for supervision of Measurements. |
| Measurements | [Analog](Analog.md) | 1..n | The Measurements using the LimitSet. |

