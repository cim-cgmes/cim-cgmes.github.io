# SvInjection

The SvInjection reports the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 1 | The topological node associated with the flow injection state variable. |
| pInjection | Float | 1..1 | The active power mismatch between calculated injection and initial injection. Positive sign means injection into the TopologicalNode (bus). |
| qInjection | Float | 0..1 | The reactive power mismatch between calculated injection and initial injection. Positive sign means injection into the TopologicalNode (bus). |

