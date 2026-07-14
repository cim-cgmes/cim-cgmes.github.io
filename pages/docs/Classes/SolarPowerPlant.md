# SolarPowerPlant

Solar power plant.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemResource <|-- SolarPowerPlant
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    SolarPowerPlant : +SolarGeneratingUnit SolarGeneratingUnits[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| SolarGeneratingUnits | [SolarGeneratingUnit](SolarGeneratingUnit.md) | 0..n | A solar generating unit or units may be a member of a solar power plant. |

