# SetPoint

An analog control that issues a set point value.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    AnalogControl <|-- SetPoint
    AnalogControl : +AnalogValue AnalogValue[1]
    AnalogControl : +Float maxValue[1..1]
    AnalogControl : +Float minValue[1..1]
    click AnalogControl href "AnalogControl"
    SetPoint : +Float normalValue[1..1]
    SetPoint : +Float value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | Normal value for Control.value e.g. used for percentage scaling. |
| value | Float | 1..1 | The value representing the actuator output. |

