# PowerTransformerEnd

A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows. 1) for a two Terminal PowerTransformer the high voltage (TransformerEnd.endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0. Parameters are always provided, even if the PowerTransformerEnds have the same rated voltage. In this case, the parameters are provided at the PowerTransformerEnd which has TransformerEnd.endNumber equal to 1. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represent a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) For a three Terminal transformer each PowerTransformerEnd shall have g, g0, b and b0 values corresponding to the no load losses distributed on the three PowerTransformerEnds. The total no load loss shunt impedances may also be placed at one of the PowerTransformerEnds, preferably the end numbered 1, having the shunt values on end 1. This is the preferred way. 4) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers. Each PowerTransformerEnd must be contained by a PowerTransformer. Because a PowerTransformerEnd (or any other object) can not be contained by more than one parent, a PowerTransformerEnd can not have an association to an EquipmentContainer (Substation, VoltageLevel, etc).

## Inheritance

```mermaid
classDiagram
    TransformerEnd <|-- PowerTransformerEnd
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PowerTransformer | [PowerTransformer](PowerTransformer.md) | 1..1 | The power transformer of this power transformer end. |
| b | Float | 1..1 | Magnetizing branch susceptance (B mag). The value can be positive or negative. |
| b0 | Float | 1..1 | Zero sequence magnetizing branch susceptance. |
| connectionKind | [WindingConnection](WindingConnection.md) | 0..1 | Kind of connection. |
| g | Float | 0..1 | Magnetizing branch conductance. |
| g0 | Float | 1..1 | Zero sequence magnetizing branch conductance (star-model). |
| phaseAngleClock | Integer | 1..1 | Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The valid values are 0 to 11. For example, for the secondary side end of a transformer with vector group code of 'Dyn11', specify the connection kind as wye with neutral and specify the phase angle of the clock as 11. The clock value of the transformer end number specified as 1, is assumed to be zero. Note the transformer end number is not assumed to be the same as the terminal sequence number. |
| r | Float | 1..1 | Resistance (star-model) of the transformer end. The attribute shall be equal to or greater than zero for non-equivalent transformers. |
| r0 | Float | 1..1 | Zero sequence series resistance (star-model) of the transformer end. |
| ratedS | Float | 0..1 | Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the values for the high and low voltage sides shall be identical. |
| ratedU | Float | 1..1 | Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is greater than or equal to ratedU for the lower voltage sides. The attribute shall be a positive value. |
| x | Float | 1..1 | Positive sequence series reactance (star-model) of the transformer end. |
| x0 | Float | 1..1 | Zero sequence series reactance of the transformer end. |

