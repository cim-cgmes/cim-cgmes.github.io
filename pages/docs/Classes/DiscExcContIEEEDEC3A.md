# DiscExcContIEEEDEC3A

IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing. Reference: IEEE 421.5-2005 12.4.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DiscontinuousExcitationControlDynamics <|-- DiscExcContIEEEDEC3A
    DiscontinuousExcitationControlDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    DiscontinuousExcitationControlDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click DiscontinuousExcitationControlDynamics href "DiscontinuousExcitationControlDynamics"
    DiscExcContIEEEDEC3A : +Float tdr[1..1]
    DiscExcContIEEEDEC3A : +Float vtmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| tdr | Float | 1..1 | Reset time delay (TDR) (>= 0). |
| vtmin | Float | 1..1 | Terminal undervoltage comparison level (VTMIN). |

