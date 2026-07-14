# StationSupply

Station supply with load derived from the station output.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EnergyConsumer <|-- StationSupply
    EnergyConsumer : +LoadDynamics LoadDynamics[0..1]
    EnergyConsumer : +LoadResponseCharacteristic LoadResponse[0..1]
    EnergyConsumer : +Float p[1..1]
    EnergyConsumer : +Float pfixed[0..1]
    EnergyConsumer : +Float pfixedPct[0..1]
    EnergyConsumer : +Float q[1..1]
    EnergyConsumer : +Float qfixed[0..1]
    EnergyConsumer : +Float qfixedPct[0..1]
    click EnergyConsumer href "EnergyConsumer"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

