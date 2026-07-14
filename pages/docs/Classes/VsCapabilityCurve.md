# VsCapabilityCurve

The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and Qmax on Y1-axis and Y2-axis.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Curve <|-- VsCapabilityCurve
    Curve : +CurveData CurveDatas[1..n]
    Curve : +CurveStyle curveStyle[1..1]
    Curve : +UnitSymbol xUnit[1..1]
    Curve : +UnitSymbol y1Unit[1..1]
    Curve : +UnitSymbol y2Unit[0..1]
    click Curve href "Curve"
    VsCapabilityCurve : +VsConverter VsConverterDCSides[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| VsConverterDCSides | [VsConverter](VsConverter.md) | 0..n | All converters with this capability curve. |

