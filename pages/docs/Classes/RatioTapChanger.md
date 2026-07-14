# RatioTapChanger

A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer. Angle sign convention (general): Positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TapChanger <|-- RatioTapChanger
    TapChanger : +SvTapStep SvTapStep[0..1]
    TapChanger : +TapChangerControl TapChangerControl[0..1]
    TapChanger : +TapSchedule TapSchedules[0..n]
    TapChanger : +Boolean controlEnabled[1..1]
    TapChanger : +Integer highStep[1..1]
    TapChanger : +Integer lowStep[1..1]
    TapChanger : +Boolean ltcFlag[1..1]
    TapChanger : +Integer neutralStep[1..1]
    TapChanger : +Float neutralU[1..1]
    TapChanger : +Integer normalStep[1..1]
    TapChanger : +Float step[1..1]
    click TapChanger href "TapChanger"
    RatioTapChanger : +RatioTapChangerTable RatioTapChangerTable[0..1]
    RatioTapChanger : +TransformerEnd TransformerEnd[1]
    RatioTapChanger : +Float stepVoltageIncrement[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RatioTapChangerTable | [RatioTapChangerTable](RatioTapChangerTable.md) | 0..1 | The tap ratio table for this ratio tap changer. |
| TransformerEnd | [TransformerEnd](TransformerEnd.md) | 1 | Transformer end to which this ratio tap changer belongs. |
| stepVoltageIncrement | Float | 1..1 | Tap step increment, in per cent of rated voltage of the power transformer end, per step position. When the increment is negative, the voltage decreases when the tap step increases. |

