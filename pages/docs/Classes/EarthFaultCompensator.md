# EarthFaultCompensator

A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults. An earth fault compensator device modelled with a single terminal implies a second terminal solidly connected to ground. If two terminals are modelled, the ground is not assumed and normal connection rules apply.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConductingEquipment <|-- EarthFaultCompensator
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
    click ConductingEquipment href "ConductingEquipment"
    EarthFaultCompensator <|-- PetersenCoil
    PetersenCoil : +PetersenCoilModeKind mode[1..1]
    PetersenCoil : +Float nominalU[1..1]
    PetersenCoil : +Float offsetCurrent[0..1]
    PetersenCoil : +Float positionCurrent[0..1]
    PetersenCoil : +Float xGroundMax[1..1]
    PetersenCoil : +Float xGroundMin[1..1]
    PetersenCoil : +Float xGroundNominal[1..1]
    click PetersenCoil href "PetersenCoil"
    EarthFaultCompensator <|-- GroundingImpedance
    GroundingImpedance : +Float x[1..1]
    click GroundingImpedance href "GroundingImpedance"
    EarthFaultCompensator : +Float r[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| r | Float | 0..1 | Nominal resistance of device. |

