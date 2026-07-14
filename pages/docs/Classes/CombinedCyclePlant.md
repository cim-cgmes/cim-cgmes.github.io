# CombinedCyclePlant

A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemResource <|-- CombinedCyclePlant
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    CombinedCyclePlant : +ThermalGeneratingUnit ThermalGeneratingUnits[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ThermalGeneratingUnits | [ThermalGeneratingUnit](ThermalGeneratingUnit.md) | 0..n | A thermal generating unit may be a member of a combined cycle plant. |

