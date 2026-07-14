# AccumulatorReset

This command resets the counter value to zero.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Control <|-- AccumulatorReset
    Control : +PowerSystemResource PowerSystemResource[0..1]
    Control : +String controlType[1..1]
    Control : +Boolean operationInProgress[0..1]
    Control : +DateTime timeStamp[0..1]
    Control : +UnitMultiplier unitMultiplier[0..1]
    Control : +UnitSymbol unitSymbol[0..1]
    click Control href "Control"
    AccumulatorReset : +AccumulatorValue AccumulatorValue[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AccumulatorValue | [AccumulatorValue](AccumulatorValue.md) | 1 | The accumulator value that is reset by the command. |

