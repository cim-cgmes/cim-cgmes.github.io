# PowerSystemResource

A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- PowerSystemResource
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    PowerSystemResource <|-- WindPowerPlant
    WindPowerPlant : +WindGeneratingUnit WindGeneratingUnits[0..n]
    click WindPowerPlant href "WindPowerPlant"
    PowerSystemResource <|-- SolarPowerPlant
    SolarPowerPlant : +SolarGeneratingUnit SolarGeneratingUnits[0..n]
    click SolarPowerPlant href "SolarPowerPlant"
    PowerSystemResource <|-- ControlArea
    ControlArea : +ControlAreaGeneratingUnit ControlAreaGeneratingUnit[0..n]
    ControlArea : +EnergyArea EnergyArea[1]
    ControlArea : +TieFlow TieFlow[0..n]
    ControlArea : +Float netInterchange[1..1]
    ControlArea : +Float pTolerance[0..1]
    ControlArea : +ControlAreaTypeKind type[1..1]
    click ControlArea href "ControlArea"
    PowerSystemResource <|-- TapChanger
    TapChanger : +SvTapStep SvTapStep[0..1]
    TapChanger : +TapChangerControl TapChangerControl[0..1]
    TapChanger : +TapSchedule TapSchedules[0..n]
    TapChanger : +Boolean controlEnabled[1..1]
    TapChanger : +Integer highStep[1..1]
    TapChanger : +Integer lowStep[1..1]
    TapChanger : +Boolean ltcFlag[1..1]
    TapChanger : +Integer neutralStep[1..1]
    TapChanger : +Float neutralU[1..1]
    TapChanger : +Integer normalStep[1..1]
    TapChanger : +Float step[1..1]
    click TapChanger href "TapChanger"
    PowerSystemResource <|-- ConnectivityNodeContainer
    ConnectivityNodeContainer : +ConnectivityNode ConnectivityNodes[0..n]
    ConnectivityNodeContainer : +TopologicalNode TopologicalNode[0..n]
    click ConnectivityNodeContainer href "ConnectivityNodeContainer"
    PowerSystemResource <|-- CombinedCyclePlant
    CombinedCyclePlant : +ThermalGeneratingUnit ThermalGeneratingUnits[0..n]
    click CombinedCyclePlant href "CombinedCyclePlant"
    PowerSystemResource <|-- CogenerationPlant
    CogenerationPlant : +ThermalGeneratingUnit ThermalGeneratingUnits[0..n]
    click CogenerationPlant href "CogenerationPlant"
    PowerSystemResource <|-- BoundaryPoint
    BoundaryPoint : +ConnectivityNode ConnectivityNode[1]
    BoundaryPoint : +String fromEndIsoCode[1..1]
    BoundaryPoint : +String fromEndName[1..1]
    BoundaryPoint : +String fromEndNameTso[1..1]
    BoundaryPoint : +Boolean isDirectCurrent[0..1]
    BoundaryPoint : +Boolean isExcludedFromAreaInterchange[0..1]
    BoundaryPoint : +String toEndIsoCode[1..1]
    BoundaryPoint : +String toEndName[1..1]
    BoundaryPoint : +String toEndNameTso[1..1]
    click BoundaryPoint href "BoundaryPoint"
    PowerSystemResource <|-- Equipment
    Equipment : +EquipmentContainer EquipmentContainer[0..1]
    Equipment : +OperationalLimitSet OperationalLimitSet[0..n]
    Equipment : +Boolean aggregate[0..1]
    Equipment : +Boolean inService[1..1]
    Equipment : +Boolean normallyInService[0..1]
    click Equipment href "Equipment"
    PowerSystemResource <|-- CAESPlant
    CAESPlant : +ThermalGeneratingUnit ThermalGeneratingUnit[0..1]
    click CAESPlant href "CAESPlant"
    PowerSystemResource <|-- RegulatingControl
    RegulatingControl : +RegulatingCondEq RegulatingCondEq[0..n]
    RegulatingControl : +RegulationSchedule RegulationSchedule[0..n]
    RegulatingControl : +Terminal Terminal[1..1]
    RegulatingControl : +Boolean discrete[1..1]
    RegulatingControl : +Boolean enabled[1..1]
    RegulatingControl : +Float maxAllowedTargetValue[0..1]
    RegulatingControl : +Float minAllowedTargetValue[0..1]
    RegulatingControl : +RegulatingControlModeKind mode[1..1]
    RegulatingControl : +Float targetDeadband[0..1]
    RegulatingControl : +Float targetValue[1..1]
    RegulatingControl : +UnitMultiplier targetValueUnitMultiplier[1..1]
    click RegulatingControl href "RegulatingControl"
    PowerSystemResource <|-- HydroPowerPlant
    HydroPowerPlant : +HydroGeneratingUnit HydroGeneratingUnits[0..n]
    HydroPowerPlant : +HydroPump HydroPumps[0..n]
    HydroPowerPlant : +HydroPlantStorageKind hydroPlantStorageType[1..1]
    click HydroPowerPlant href "HydroPowerPlant"
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Controls | [Control](Control.md) | 0..n | The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator. |
| Location | [Location](Location.md) | 0..1 | Location of this power system resource. |
| Measurements | [Measurement](Measurement.md) | 0..n | The measurements associated with this power system resource. |

