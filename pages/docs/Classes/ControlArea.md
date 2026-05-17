# ControlArea

A control area is a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be used for a variety of purposes including automatic generation control, power flow solution area interchange control specification, and input to load forecasting. All generation and load within the area defined by the terminals on the border are considered in the area interchange control. Note that any number of overlapping control area specifications can be superimposed on the physical model. The following general principles apply to ControlArea: 1. The control area orientation for net interchange is positive for an import, negative for an export. 2. The control area net interchange is determined by summing flows in Terminals. The Terminals are identified by creating a set of TieFlow objects associated with a ControlArea object. Each TieFlow object identifies one Terminal. 3. In a single network model, a tie between two control areas must be modelled in both control area specifications, such that the two representations of the tie flow sum to zero. 4. The normal orientation of Terminal flow is positive for flow into the conducting equipment that owns the Terminal. (i.e. flow from a bus into a device is positive.) However, the orientation of each flow in the control area specification must align with the control area convention, i.e. import is positive. If the orientation of the Terminal flow referenced by a TieFlow is positive into the control area, then this is confirmed by setting TieFlow.positiveFlowIn flag TRUE. If not, the orientation must be reversed by setting the TieFlow.positiveFlowIn flag FALSE.

## Inheritance

```mermaid
classDiagram
    PowerSystemResource <|-- ControlArea
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ControlAreaGeneratingUnit | [ControlAreaGeneratingUnit](ControlAreaGeneratingUnit.md) | 0..n | The generating unit specifications for the control area. |
| EnergyArea | [EnergyArea](EnergyArea.md) | 1 | The energy area that is forecast from this control area specification. |
| TieFlow | [TieFlow](TieFlow.md) | 0..n | The tie flows associated with the control area. |
| netInterchange | Float | 1..1 | The specified positive net interchange into the control area, i.e. positive sign means flow into the area. |
| pTolerance | Float | 0..1 | Active power net interchange tolerance. The attribute shall be a positive value or zero. |
| type | [ControlAreaTypeKind](ControlAreaTypeKind.md) | 1..1 | The primary type of control area definition used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. A control area specified with primary type of automatic generation control could still be forecast and used as an interchange area in power flow analysis. |

