# Command

A Command is a discrete control used for supervisory control.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Control <|-- Command
    Control : +PowerSystemResource PowerSystemResource[0..1]
    Control : +String controlType[1..1]
    Control : +Boolean operationInProgress[0..1]
    Control : +DateTime timeStamp[0..1]
    Control : +UnitMultiplier unitMultiplier[0..1]
    Control : +UnitSymbol unitSymbol[0..1]
    click Control href "Control"
    Command : +DiscreteValue DiscreteValue[1]
    Command : +ValueAliasSet ValueAliasSet[0..1]
    Command : +Integer normalValue[1..1]
    Command : +Integer value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DiscreteValue | [DiscreteValue](DiscreteValue.md) | 1 | The MeasurementValue that is controlled. |
| ValueAliasSet | [ValueAliasSet](ValueAliasSet.md) | 0..1 | The ValueAliasSet used for translation of a Control value to a name. |
| normalValue | Integer | 1..1 | Normal value for Control.value e.g. used for percentage scaling. |
| value | Integer | 1..1 | The value representing the actuator output. |

