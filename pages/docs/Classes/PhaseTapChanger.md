# PhaseTapChanger

A transformer phase shifting tap model that controls the phase angle difference across the power transformer and potentially the active power flow through the power transformer. This phase tap model may also impact the voltage magnitude.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TapChanger <|-- PhaseTapChanger
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
    PhaseTapChanger <|-- PhaseTapChangerLinear
    PhaseTapChangerLinear : +Float stepPhaseShiftIncrement[1..1]
    PhaseTapChangerLinear : +Float xMax[1..1]
    PhaseTapChangerLinear : +Float xMin[1..1]
    click PhaseTapChangerLinear href "PhaseTapChangerLinear"
    PhaseTapChanger <|-- PhaseTapChangerNonLinear
    PhaseTapChangerNonLinear : +Float voltageStepIncrement[1..1]
    PhaseTapChangerNonLinear : +Float xMax[1..1]
    PhaseTapChangerNonLinear : +Float xMin[1..1]
    click PhaseTapChangerNonLinear href "PhaseTapChangerNonLinear"
    PhaseTapChanger <|-- PhaseTapChangerTabular
    PhaseTapChangerTabular : +PhaseTapChangerTable PhaseTapChangerTable[1]
    click PhaseTapChangerTabular href "PhaseTapChangerTabular"
    PhaseTapChanger : +TransformerEnd TransformerEnd[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TransformerEnd | [TransformerEnd](TransformerEnd.md) | 1 | Transformer end to which this phase tap changer belongs. |

