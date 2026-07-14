# Sensor

This class describe devices that transform a measured quantity into signals that can be presented at displays, used in control or be recorded.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    AuxiliaryEquipment <|-- Sensor
    AuxiliaryEquipment : +Terminal Terminal[1]
    click AuxiliaryEquipment href "AuxiliaryEquipment"
    Sensor <|-- PostLineSensor
    click PostLineSensor href "PostLineSensor"
    Sensor <|-- CurrentTransformer
    click CurrentTransformer href "CurrentTransformer"
    Sensor <|-- PotentialTransformer
    click PotentialTransformer href "PotentialTransformer"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

