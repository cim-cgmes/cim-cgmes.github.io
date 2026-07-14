# Discrete

Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker position.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Measurement <|-- Discrete
    Measurement : +PowerSystemResource PowerSystemResource[1..1]
    Measurement : +ACDCTerminal Terminal[0..1]
    Measurement : +String measurementType[1..1]
    Measurement : +PhaseCode phases[0..1]
    Measurement : +UnitMultiplier unitMultiplier[1..1]
    Measurement : +UnitSymbol unitSymbol[1..1]
    click Measurement href "Measurement"
    Discrete : +DiscreteValue DiscreteValues[0..n]
    Discrete : +ValueAliasSet ValueAliasSet[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DiscreteValues | [DiscreteValue](DiscreteValue.md) | 0..n | The values connected to this measurement. |
| ValueAliasSet | [ValueAliasSet](ValueAliasSet.md) | 0..1 | The ValueAliasSet used for translation of a MeasurementValue.value to a name. |

