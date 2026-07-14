# AnalogControl

An analog control used for supervisory control.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Control <|-- AnalogControl
    Control : +PowerSystemResource PowerSystemResource[0..1]
    Control : +String controlType[1..1]
    Control : +Boolean operationInProgress[0..1]
    Control : +DateTime timeStamp[0..1]
    Control : +UnitMultiplier unitMultiplier[0..1]
    Control : +UnitSymbol unitSymbol[0..1]
    click Control href "Control"
    AnalogControl <|-- RaiseLowerCommand
    RaiseLowerCommand : +ValueAliasSet ValueAliasSet[0..1]
    click RaiseLowerCommand href "RaiseLowerCommand"
    AnalogControl <|-- SetPoint
    SetPoint : +Float normalValue[1..1]
    SetPoint : +Float value[1..1]
    click SetPoint href "SetPoint"
    AnalogControl : +AnalogValue AnalogValue[1]
    AnalogControl : +Float maxValue[1..1]
    AnalogControl : +Float minValue[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AnalogValue | [AnalogValue](AnalogValue.md) | 1 | The MeasurementValue that is controlled. |
| maxValue | Float | 1..1 | Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. |
| minValue | Float | 1..1 | Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. |

