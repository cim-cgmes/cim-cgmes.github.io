# AnalogValue

AnalogValue represents an analog MeasurementValue.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    MeasurementValue <|-- AnalogValue
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
    click MeasurementValue href "MeasurementValue"
    AnalogValue : +Analog Analog[1]
    AnalogValue : +AnalogControl AnalogControl[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Analog | [Analog](Analog.md) | 1 | Measurement to which this value is connected. |
| AnalogControl | [AnalogControl](AnalogControl.md) | 0..1 | The Control variable associated with the MeasurementValue. |

