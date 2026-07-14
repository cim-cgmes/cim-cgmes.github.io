# ReactiveCapabilityCurve

Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure. The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Curve <|-- ReactiveCapabilityCurve
    Curve : +CurveData CurveDatas[1..n]
    Curve : +CurveStyle curveStyle[1..1]
    Curve : +UnitSymbol xUnit[1..1]
    Curve : +UnitSymbol y1Unit[1..1]
    Curve : +UnitSymbol y2Unit[0..1]
    click Curve href "Curve"
    ReactiveCapabilityCurve : +EquivalentInjection EquivalentInjection[0..n]
    ReactiveCapabilityCurve : +SynchronousMachine InitiallyUsedBySynchronousMachines[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| EquivalentInjection | [EquivalentInjection](EquivalentInjection.md) | 0..n | The equivalent injection using this reactive capability curve. |
| InitiallyUsedBySynchronousMachines | [SynchronousMachine](SynchronousMachine.md) | 1..n | Synchronous machines using this curve as default. |

