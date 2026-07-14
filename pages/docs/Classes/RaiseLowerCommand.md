# RaiseLowerCommand

An analog control that increases or decreases a set point value with pulses. Unless otherwise specified, one pulse moves the set point by one.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    AnalogControl <|-- RaiseLowerCommand
    AnalogControl : +AnalogValue AnalogValue[1]
    AnalogControl : +Float maxValue[1..1]
    AnalogControl : +Float minValue[1..1]
    click AnalogControl href "AnalogControl"
    RaiseLowerCommand : +ValueAliasSet ValueAliasSet[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ValueAliasSet | [ValueAliasSet](ValueAliasSet.md) | 0..1 | The ValueAliasSet used for translation of a Control value to a name. |

