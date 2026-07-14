# DiscreteValue

DiscreteValue represents a discrete MeasurementValue.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    MeasurementValue <|-- DiscreteValue
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
    click MeasurementValue href "MeasurementValue"
    DiscreteValue : +Command Command[0..1]
    DiscreteValue : +Discrete Discrete[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Command | [Command](Command.md) | 0..1 | The Control variable associated with the MeasurementValue. |
| Discrete | [Discrete](Discrete.md) | 1 | Measurement to which this value is connected. |

