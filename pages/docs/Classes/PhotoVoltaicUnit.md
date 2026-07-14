# PhotoVoltaicUnit

A photovoltaic device or an aggregation of such devices.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerElectronicsUnit <|-- PhotoVoltaicUnit
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

