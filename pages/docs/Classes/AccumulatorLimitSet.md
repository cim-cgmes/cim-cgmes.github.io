# AccumulatorLimitSet

An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    LimitSet <|-- AccumulatorLimitSet
    LimitSet : +Boolean isPercentageLimits[0..1]
    click LimitSet href "LimitSet"
    AccumulatorLimitSet : +AccumulatorLimit Limits[1..n]
    AccumulatorLimitSet : +Accumulator Measurements[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Limits | [AccumulatorLimit](AccumulatorLimit.md) | 1..n | The limit values used for supervision of Measurements. |
| Measurements | [Accumulator](Accumulator.md) | 1..n | The Measurements using the LimitSet. |

