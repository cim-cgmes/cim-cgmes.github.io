# MeasurementValue

The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IOPoint <|-- MeasurementValue
    click IOPoint href "IOPoint"
    MeasurementValue <|-- DiscreteValue
    DiscreteValue : +Command Command[0..1]
    DiscreteValue : +Discrete Discrete[1]
    click DiscreteValue href "DiscreteValue"
    MeasurementValue <|-- StringMeasurementValue
    StringMeasurementValue : +StringMeasurement StringMeasurement[1]
    click StringMeasurementValue href "StringMeasurementValue"
    MeasurementValue <|-- AccumulatorValue
    AccumulatorValue : +Accumulator Accumulator[1]
    AccumulatorValue : +AccumulatorReset AccumulatorReset[0..1]
    click AccumulatorValue href "AccumulatorValue"
    MeasurementValue <|-- AnalogValue
    AnalogValue : +Analog Analog[1]
    AnalogValue : +AnalogControl AnalogControl[0..1]
    click AnalogValue href "AnalogValue"
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| MeasurementValueQuality | [MeasurementValueQuality](MeasurementValueQuality.md) | 0..1 | A MeasurementValue has a MeasurementValueQuality associated with it. |
| MeasurementValueSource | [MeasurementValueSource](MeasurementValueSource.md) | 1 | A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301. |
| sensorAccuracy | Float | 0..1 | The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under reference conditions. |
| timeStamp | DateTime | 0..1 | The time when the value was last updated. |

