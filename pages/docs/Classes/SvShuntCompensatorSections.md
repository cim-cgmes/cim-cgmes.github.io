# SvShuntCompensatorSections

State variable for the number of sections in service for a shunt compensator.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ShuntCompensator | [ShuntCompensator](ShuntCompensator.md) | 1 | The shunt compensator for which the state applies. |
| sections | Float | 1..1 | The number of sections in service as a continuous variable. The attribute shall be a positive value or zero. To get integer value scale with ShuntCompensator.bPerSection. |

