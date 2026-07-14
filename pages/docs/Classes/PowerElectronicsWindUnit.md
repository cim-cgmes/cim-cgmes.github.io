# PowerElectronicsWindUnit

A wind generating unit that connects to the AC network with power electronics rather than rotating machines or an aggregation of such units.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerElectronicsUnit <|-- PowerElectronicsWindUnit
    PowerElectronicsUnit : +PowerElectronicsConnection PowerElectronicsConnection[1]
    PowerElectronicsUnit : +Float maxP[0..1]
    PowerElectronicsUnit : +Float minP[0..1]
    click PowerElectronicsUnit href "PowerElectronicsUnit"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

