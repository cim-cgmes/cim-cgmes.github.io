# IOPoint

The class describe a measurement or control value. The purpose is to enable having attributes and associations common for measurement and control.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- IOPoint
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    IOPoint <|-- Control
    Control : +PowerSystemResource PowerSystemResource[0..1]
    Control : +String controlType[1..1]
    Control : +Boolean operationInProgress[0..1]
    Control : +DateTime timeStamp[0..1]
    Control : +UnitMultiplier unitMultiplier[0..1]
    Control : +UnitSymbol unitSymbol[0..1]
    click Control href "Control"
    IOPoint <|-- MeasurementValue
    MeasurementValue : +MeasurementValueQuality MeasurementValueQuality[0..1]
    MeasurementValue : +MeasurementValueSource MeasurementValueSource[1]
    MeasurementValue : +Float sensorAccuracy[0..1]
    MeasurementValue : +DateTime timeStamp[0..1]
    click MeasurementValue href "MeasurementValue"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

