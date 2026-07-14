# CAESPlant

Compressed air energy storage plant.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemResource <|-- CAESPlant
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    CAESPlant : +ThermalGeneratingUnit ThermalGeneratingUnit[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ThermalGeneratingUnit | [ThermalGeneratingUnit](ThermalGeneratingUnit.md) | 0..1 | A thermal generating unit may be a member of a compressed air energy storage plant. |

