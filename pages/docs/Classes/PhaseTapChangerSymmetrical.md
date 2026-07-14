# PhaseTapChangerSymmetrical

Describes a symmetrical phase shifting transformer tap model in which the voltage magnitude of both sides is the same. The difference voltage magnitude is the base in an equal-sided triangle where the sides corresponds to the primary and secondary voltages. The phase angle difference corresponds to the top angle and can be expressed as twice the arctangent of half the total difference voltage.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PhaseTapChangerNonLinear <|-- PhaseTapChangerSymmetrical
    PhaseTapChangerNonLinear : +Float voltageStepIncrement[1..1]
    PhaseTapChangerNonLinear : +Float xMax[1..1]
    PhaseTapChangerNonLinear : +Float xMin[1..1]
    click PhaseTapChangerNonLinear href "PhaseTapChangerNonLinear"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

