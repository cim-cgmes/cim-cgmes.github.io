# Curve

A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- Curve
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    Curve <|-- ReactiveCapabilityCurve
    ReactiveCapabilityCurve : +EquivalentInjection EquivalentInjection[0..n]
    ReactiveCapabilityCurve : +SynchronousMachine InitiallyUsedBySynchronousMachines[1..n]
    click ReactiveCapabilityCurve href "ReactiveCapabilityCurve"
    Curve <|-- VsCapabilityCurve
    VsCapabilityCurve : +VsConverter VsConverterDCSides[0..n]
    click VsCapabilityCurve href "VsCapabilityCurve"
    Curve <|-- GrossToNetActivePowerCurve
    GrossToNetActivePowerCurve : +GeneratingUnit GeneratingUnit[1]
    click GrossToNetActivePowerCurve href "GrossToNetActivePowerCurve"
    Curve : +CurveData CurveDatas[1..n]
    Curve : +CurveStyle curveStyle[1..1]
    Curve : +UnitSymbol xUnit[1..1]
    Curve : +UnitSymbol y1Unit[1..1]
    Curve : +UnitSymbol y2Unit[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| CurveDatas | [CurveData](CurveData.md) | 1..n | The point data values that define this curve. |
| curveStyle | [CurveStyle](CurveStyle.md) | 1..1 | The style or shape of the curve. |
| xUnit | [UnitSymbol](UnitSymbol.md) | 1..1 | The X-axis units of measure. |
| y1Unit | [UnitSymbol](UnitSymbol.md) | 1..1 | The Y1-axis units of measure. |
| y2Unit | [UnitSymbol](UnitSymbol.md) | 0..1 | The Y2-axis units of measure. |

