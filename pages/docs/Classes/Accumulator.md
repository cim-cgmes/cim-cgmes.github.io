# Accumulator

Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Measurement <|-- Accumulator
    Measurement : +PowerSystemResource PowerSystemResource[1..1]
    Measurement : +ACDCTerminal Terminal[0..1]
    Measurement : +String measurementType[1..1]
    Measurement : +PhaseCode phases[0..1]
    Measurement : +UnitMultiplier unitMultiplier[1..1]
    Measurement : +UnitSymbol unitSymbol[1..1]
    click Measurement href "Measurement"
    Accumulator : +AccumulatorValue AccumulatorValues[0..n]
    Accumulator : +AccumulatorLimitSet LimitSets[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AccumulatorValues | [AccumulatorValue](AccumulatorValue.md) | 0..n | The values connected to this measurement. |
| LimitSets | [AccumulatorLimitSet](AccumulatorLimitSet.md) | 0..n | A measurement may have zero or more limit ranges defined for it. |

