# LoadArea

The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Inheritance

```mermaid
classDiagram
    EnergyArea <|-- LoadArea
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| SubLoadAreas | [SubLoadArea](SubLoadArea.md) | 1..n | The SubLoadAreas in the LoadArea. |

