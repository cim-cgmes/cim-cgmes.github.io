# CurveData

Multi-purpose data points for defining a curve. The use of this generic class is discouraged if a more specific class can be used to specify the X and Y axis values along with their specific data types.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Curve | [Curve](Curve.md) | 1 | The curve of this curve data point. |
| xvalue | Float | 1..1 | The data value of the X-axis variable, depending on the X-axis units. |
| y1value | Float | 1..1 | The data value of the first Y-axis variable, depending on the Y-axis units. |
| y2value | Float | 0..1 | The data value of the second Y-axis variable (if present), depending on the Y-axis units. |

