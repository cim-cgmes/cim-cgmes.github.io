# NonConformLoad

NonConformLoad represents loads that do not follow a daily load change pattern and whose changes are not correlated with the daily load change pattern.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EnergyConsumer <|-- NonConformLoad
    EnergyConsumer : +LoadDynamics LoadDynamics[0..1]
    EnergyConsumer : +LoadResponseCharacteristic LoadResponse[0..1]
    EnergyConsumer : +Float p[1..1]
    EnergyConsumer : +Float pfixed[0..1]
    EnergyConsumer : +Float pfixedPct[0..1]
    EnergyConsumer : +Float q[1..1]
    EnergyConsumer : +Float qfixed[0..1]
    EnergyConsumer : +Float qfixedPct[0..1]
    click EnergyConsumer href "EnergyConsumer"
    NonConformLoad : +NonConformLoadGroup LoadGroup[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| LoadGroup | [NonConformLoadGroup](NonConformLoadGroup.md) | 1 | Group of this ConformLoad. |

