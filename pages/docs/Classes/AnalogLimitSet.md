# AnalogLimitSet

An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

## Inheritance

```mermaid
classDiagram
    LimitSet <|-- AnalogLimitSet
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Limits | [AnalogLimit](AnalogLimit.md) | 0..n | The limit values used for supervision of Measurements. |
| Measurements | [Analog](Analog.md) | 1..n | The Measurements using the LimitSet. |

