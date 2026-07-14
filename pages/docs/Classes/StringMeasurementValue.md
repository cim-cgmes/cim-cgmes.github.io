# StringMeasurementValue

StringMeasurementValue represents a measurement value of type string.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    MeasurementValue <|-- StringMeasurementValue
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
    click MeasurementValue href "MeasurementValue"
    StringMeasurementValue : +StringMeasurement StringMeasurement[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| StringMeasurement | [StringMeasurement](StringMeasurement.md) | 1 | Measurement to which this value is connected. |

