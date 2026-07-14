# SubLoadArea

The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EnergyArea <|-- SubLoadArea
    EnergyArea : +ControlArea ControlArea[0..1]
    click EnergyArea href "EnergyArea"
    SubLoadArea : +LoadArea LoadArea[1]
    SubLoadArea : +LoadGroup LoadGroups[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| LoadArea | [LoadArea](LoadArea.md) | 1 | The LoadArea where the SubLoadArea belongs. |
| LoadGroups | [LoadGroup](LoadGroup.md) | 1..n | The Loadgroups in the SubLoadArea. |

