# WindGeneratingUnit

A wind driven generating unit, connected to the grid by means of a rotating machine. May be used to represent a single turbine or an aggregation.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    GeneratingUnit <|-- WindGeneratingUnit
    GeneratingUnit : +ControlAreaGeneratingUnit ControlAreaGeneratingUnit[0..n]
    GeneratingUnit : +GrossToNetActivePowerCurve GrossToNetActivePowerCurves[0..n]
    GeneratingUnit : +RotatingMachine RotatingMachine[1..n]
    GeneratingUnit : +GeneratorControlSource genControlSource[0..1]
    GeneratingUnit : +Float governorSCD[0..1]
    GeneratingUnit : +Float longPF[0..1]
    GeneratingUnit : +Float maxOperatingP[1..1]
    GeneratingUnit : +Float maximumAllowableSpinningReserve[0..1]
    GeneratingUnit : +Float minOperatingP[1..1]
    GeneratingUnit : +Float nominalP[0..1]
    GeneratingUnit : +Float normalPF[1..1]
    GeneratingUnit : +Float ratedGrossMaxP[0..1]
    GeneratingUnit : +Float ratedGrossMinP[0..1]
    GeneratingUnit : +Float ratedNetMaxP[0..1]
    GeneratingUnit : +Float shortPF[0..1]
    GeneratingUnit : +Float startupCost[0..1]
    GeneratingUnit : +Float startupTime[0..1]
    GeneratingUnit : +Float totalEfficiency[0..1]
    GeneratingUnit : +Float variableCost[0..1]
    click GeneratingUnit href "GeneratingUnit"
    WindGeneratingUnit : +WindPowerPlant WindPowerPlant[0..1]
    WindGeneratingUnit : +WindGenUnitKind windGenUnitType[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindPowerPlant | [WindPowerPlant](WindPowerPlant.md) | 0..1 | A wind power plant may have wind generating units. |
| windGenUnitType | [WindGenUnitKind](WindGenUnitKind.md) | 1..1 | The kind of wind generating unit. |

