# ConformLoad

ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EnergyConsumer <|-- ConformLoad
    EnergyConsumer : +LoadDynamics LoadDynamics[0..1]
    EnergyConsumer : +LoadResponseCharacteristic LoadResponse[0..1]
    EnergyConsumer : +Float p[1..1]
    EnergyConsumer : +Float pfixed[0..1]
    EnergyConsumer : +Float pfixedPct[0..1]
    EnergyConsumer : +Float q[1..1]
    EnergyConsumer : +Float qfixed[0..1]
    EnergyConsumer : +Float qfixedPct[0..1]
    click EnergyConsumer href "EnergyConsumer"
    ConformLoad : +ConformLoadGroup LoadGroup[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| LoadGroup | [ConformLoadGroup](ConformLoadGroup.md) | 1 | Group of this ConformLoad. |

