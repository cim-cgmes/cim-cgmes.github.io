# WindPowerPlant

Wind power plant.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemResource <|-- WindPowerPlant
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    WindPowerPlant : +WindGeneratingUnit WindGeneratingUnits[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindGeneratingUnits | [WindGeneratingUnit](WindGeneratingUnit.md) | 0..n | A wind generating unit or units may be a member of a wind power plant. |

