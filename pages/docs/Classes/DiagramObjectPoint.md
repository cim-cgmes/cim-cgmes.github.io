# DiagramObjectPoint

A point in a given space defined by 3 coordinates and associated to a diagram object. The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DiagramObject | [DiagramObject](DiagramObject.md) | 1 | The diagram object with which the points are associated. |
| DiagramObjectGluePoint | [DiagramObjectGluePoint](DiagramObjectGluePoint.md) | 0..1 | The 'glue' point to which this point is associated. |
| sequenceNumber | Integer | 0..1 | The sequence position of the point, used for defining the order of points for diagram objects acting as a polyline or polygon with more than one point. The attribute shall be a positive value. |
| xPosition | Float | 1..1 | The X coordinate of this point. |
| yPosition | Float | 1..1 | The Y coordinate of this point. |
| zPosition | Float | 0..1 | The Z coordinate of this point. |

