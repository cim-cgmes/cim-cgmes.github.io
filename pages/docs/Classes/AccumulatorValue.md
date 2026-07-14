# AccumulatorValue

AccumulatorValue represents an accumulated (counted) MeasurementValue.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    MeasurementValue <|-- AccumulatorValue
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
    click MeasurementValue href "MeasurementValue"
    AccumulatorValue : +Accumulator Accumulator[1]
    AccumulatorValue : +AccumulatorReset AccumulatorReset[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Accumulator | [Accumulator](Accumulator.md) | 1 | Measurement to which this value is connected. |
| AccumulatorReset | [AccumulatorReset](AccumulatorReset.md) | 0..1 | The command that resets the accumulator value. |

