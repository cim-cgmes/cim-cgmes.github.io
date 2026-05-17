# PositionPoint

Set of spatial coordinates that determine a point, defined in the coordinate system specified in 'Location.CoordinateSystem'. Use a single position point instance to describe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Location | [Location](Location.md) | 1 | Location described by this position point. |
| sequenceNumber | Integer | 0..1 | Zero-relative sequence number of this point within a series of points. |
| xPosition | String | 1..1 | X axis position. |
| yPosition | String | 1..1 | Y axis position. |
| zPosition | String | 0..1 | (if applicable) Z axis position. |

