# IdentifiedObject

This is a root class to provide common identification for all classes needing identification and naming attributes.

## Inheritance

```mermaid
classDiagram
    IdentifiedObject <|-- Location
    IdentifiedObject <|-- LoadResponseCharacteristic
    IdentifiedObject <|-- EnergyArea
    IdentifiedObject <|-- WindContPType4bIEC
    IdentifiedObject <|-- DCTopologicalNode
    IdentifiedObject <|-- BusNameMarker
    IdentifiedObject <|-- Diagram
    IdentifiedObject <|-- WindAeroOneDimIEC
    IdentifiedObject <|-- WindContQPQULimIEC
    IdentifiedObject <|-- ReportingGroup
    IdentifiedObject <|-- TopologicalIsland
    IdentifiedObject <|-- WindAeroConstIEC
    IdentifiedObject <|-- ControlAreaGeneratingUnit
    IdentifiedObject <|-- DCNode
    IdentifiedObject <|-- WindContQIEC
    IdentifiedObject <|-- LoadDynamics
    IdentifiedObject <|-- TieFlow
    IdentifiedObject <|-- WindContPType3IEC
    IdentifiedObject <|-- Limit
    IdentifiedObject <|-- Curve
    IdentifiedObject <|-- ConnectivityNode
    IdentifiedObject <|-- VisibilityLayer
    IdentifiedObject <|-- WindDynamicsLookupTable
    IdentifiedObject <|-- WindContQLimIEC
    IdentifiedObject <|-- GenICompensationForGenJ
    IdentifiedObject <|-- OperationalLimitType
    IdentifiedObject <|-- LoadStatic
    IdentifiedObject <|-- MeasurementValueSource
    IdentifiedObject <|-- ValueToAlias
    IdentifiedObject <|-- GeographicalRegion
    IdentifiedObject <|-- DayType
    IdentifiedObject <|-- CoordinateSystem
    IdentifiedObject <|-- LimitSet
    IdentifiedObject <|-- WindRefFrameRotIEC
    IdentifiedObject <|-- OperationalLimit
    IdentifiedObject <|-- ValueAliasSet
    IdentifiedObject <|-- DynamicsFunctionBlock
    IdentifiedObject <|-- SubGeographicalRegion
    IdentifiedObject <|-- BasicIntervalSchedule
    IdentifiedObject <|-- MutualCoupling
    IdentifiedObject <|-- FossilFuel
    IdentifiedObject <|-- PhaseTapChangerTable
    IdentifiedObject <|-- IOPoint
    IdentifiedObject <|-- WindProtectionIEC
    IdentifiedObject <|-- LoadMotor
    IdentifiedObject <|-- WindAeroTwoDimIEC
    IdentifiedObject <|-- DiagramObject
    IdentifiedObject <|-- WindMechIEC
    IdentifiedObject <|-- WindContPType4aIEC
    IdentifiedObject <|-- RatioTapChangerTable
    IdentifiedObject <|-- DCTopologicalIsland
    IdentifiedObject <|-- TopologicalNode
    IdentifiedObject <|-- OperationalLimitSet
    IdentifiedObject <|-- EnergySchedulingType
    IdentifiedObject <|-- WindContPitchAngleIEC
    IdentifiedObject <|-- WindPlantFreqPcontrolIEC
    IdentifiedObject <|-- DiagramObjectStyle
    IdentifiedObject <|-- TransformerEnd
    IdentifiedObject <|-- WindPlantReactiveControlIEC
    IdentifiedObject <|-- Measurement
    IdentifiedObject <|-- DiagramStyle
    IdentifiedObject <|-- WindGenType4IEC
    IdentifiedObject <|-- WindPitchContPowerIEC
    IdentifiedObject <|-- PowerSystemResource
    IdentifiedObject <|-- WindContCurrLimIEC
    IdentifiedObject <|-- WindGenType3IEC
    IdentifiedObject <|-- BaseVoltage
    IdentifiedObject <|-- LoadGroup
    IdentifiedObject <|-- RemoteInputSignal
    IdentifiedObject <|-- Season
    IdentifiedObject <|-- ACDCTerminal
    IdentifiedObject <|-- WindContRotorRIEC
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DiagramObjects | [DiagramObject](DiagramObject.md) | 0..n | The diagram objects that are associated with the domain object. |
| description | String | 0..1 | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. |
| energyIdentCodeEic | String | 0..1 | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. |
| mRID | String | 1..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. |
| name | String | 1..1 | The name is any free human readable and possibly non unique text naming the object. |
| shortName | String | 0..1 | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. |

