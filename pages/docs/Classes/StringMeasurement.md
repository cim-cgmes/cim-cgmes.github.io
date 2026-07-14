# StringMeasurement

StringMeasurement represents a measurement with values of type string.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Measurement <|-- StringMeasurement
    Measurement : +PowerSystemResource PowerSystemResource[1..1]
    Measurement : +ACDCTerminal Terminal[0..1]
    Measurement : +String measurementType[1..1]
    Measurement : +PhaseCode phases[0..1]
    Measurement : +UnitMultiplier unitMultiplier[1..1]
    Measurement : +UnitSymbol unitSymbol[1..1]
    click Measurement href "Measurement"
    StringMeasurement : +StringMeasurementValue StringMeasurementValues[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| StringMeasurementValues | [StringMeasurementValue](StringMeasurementValue.md) | 0..n | The values connected to this measurement. |

