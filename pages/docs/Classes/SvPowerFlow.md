# SvPowerFlow

State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Terminal | [Terminal](Terminal.md) | 1 | The terminal associated with the power flow state variable. |
| p | Float | 1..1 | The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. |
| q | Float | 1..1 | The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. |

