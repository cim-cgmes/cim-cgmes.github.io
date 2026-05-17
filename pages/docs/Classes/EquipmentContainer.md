# EquipmentContainer

A modelling construct to provide a root class for containing equipment.

## Inheritance

```mermaid
classDiagram
    ConnectivityNodeContainer <|-- EquipmentContainer
    EquipmentContainer <|-- DCEquipmentContainer
    EquipmentContainer <|-- Line
    EquipmentContainer <|-- Bay
    EquipmentContainer <|-- Substation
    EquipmentContainer <|-- VoltageLevel
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Equipments | [Equipment](Equipment.md) | 0..n | Contained equipment. |

