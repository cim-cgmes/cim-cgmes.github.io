# ConductingEquipment

The parts of the AC power system that are designed to carry current or that are conductively connected through terminals.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Equipment <|-- ConductingEquipment
    Equipment : +EquipmentContainer EquipmentContainer[0..1]
    Equipment : +OperationalLimitSet OperationalLimitSet[0..n]
    Equipment : +Boolean aggregate[0..1]
    Equipment : +Boolean inService[1..1]
    Equipment : +Boolean normallyInService[0..1]
    click Equipment href "Equipment"
    ConductingEquipment <|-- EnergyConnection
    click EnergyConnection href "EnergyConnection"
    ConductingEquipment <|-- EarthFaultCompensator
    EarthFaultCompensator : +Float r[0..1]
    click EarthFaultCompensator href "EarthFaultCompensator"
    ConductingEquipment <|-- Ground
    click Ground href "Ground"
    ConductingEquipment <|-- SeriesCompensator
    SeriesCompensator : +Float r[1..1]
    SeriesCompensator : +Float r0[1..1]
    SeriesCompensator : +Boolean varistorPresent[1..1]
    SeriesCompensator : +Float varistorRatedCurrent[0..1]
    SeriesCompensator : +Float varistorVoltageThreshold[0..1]
    SeriesCompensator : +Float x[1..1]
    SeriesCompensator : +Float x0[1..1]
    click SeriesCompensator href "SeriesCompensator"
    ConductingEquipment <|-- EquivalentEquipment
    EquivalentEquipment : +EquivalentNetwork EquivalentNetwork[0..1]
    click EquivalentEquipment href "EquivalentEquipment"
    ConductingEquipment <|-- ACDCConverter
    ACDCConverter : +ACDCConverterDCTerminal DCTerminals[0..n]
    ACDCConverter : +Terminal PccTerminal[0..1]
    ACDCConverter : +Float baseS[0..1]
    ACDCConverter : +Float idc[1..1]
    ACDCConverter : +Float idleLoss[0..1]
    ACDCConverter : +Float maxP[0..1]
    ACDCConverter : +Float maxUdc[0..1]
    ACDCConverter : +Float minP[0..1]
    ACDCConverter : +Float minUdc[0..1]
    ACDCConverter : +Integer numberOfValves[0..1]
    ACDCConverter : +Float p[1..1]
    ACDCConverter : +Float poleLossP[1..1]
    ACDCConverter : +Float q[1..1]
    ACDCConverter : +Float ratedUdc[0..1]
    ACDCConverter : +Float resistiveLoss[0..1]
    ACDCConverter : +Float switchingLoss[0..1]
    ACDCConverter : +Float targetPpcc[0..1]
    ACDCConverter : +Float targetUdc[0..1]
    ACDCConverter : +Float uc[1..1]
    ACDCConverter : +Float udc[1..1]
    ACDCConverter : +Float valveU0[0..1]
    click ACDCConverter href "ACDCConverter"
    ConductingEquipment <|-- Conductor
    Conductor : +Float length[0..1]
    click Conductor href "Conductor"
    ConductingEquipment <|-- Clamp
    Clamp : +ACLineSegment ACLineSegment[1]
    Clamp : +Float lengthFromTerminal1[0..1]
    click Clamp href "Clamp"
    ConductingEquipment <|-- PowerTransformer
    PowerTransformer : +PowerTransformerEnd PowerTransformerEnd[0..n]
    PowerTransformer : +Float beforeShCircuitHighestOperatingCurrent[0..1]
    PowerTransformer : +Float beforeShCircuitHighestOperatingVoltage[0..1]
    PowerTransformer : +Float beforeShortCircuitAnglePf[0..1]
    PowerTransformer : +Float highSideMinOperatingU[0..1]
    PowerTransformer : +Boolean isPartOfGeneratorUnit[1..1]
    PowerTransformer : +Boolean operationalValuesConsidered[0..1]
    click PowerTransformer href "PowerTransformer"
    ConductingEquipment <|-- Switch
    Switch : +SvSwitch SvSwitch[0..n]
    Switch : +SwitchSchedule SwitchSchedules[0..n]
    Switch : +Boolean locked[1..1]
    Switch : +Boolean normalOpen[1..1]
    Switch : +Boolean open[1..1]
    Switch : +Float ratedCurrent[0..1]
    Switch : +Boolean retained[1..1]
    click Switch href "Switch"
    ConductingEquipment <|-- Connector
    click Connector href "Connector"
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| BaseVoltage | [BaseVoltage](BaseVoltage.md) | 0..1 | Base voltage of this conducting equipment. Use only when there is no voltage level container used and only one base voltage applies. For example, not used for transformers. |
| SvStatus | [SvStatus](SvStatus.md) | 0..1 | The status state variable associated with this conducting equipment. |
| Terminals | [Terminal](Terminal.md) | 0..n | Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. |

