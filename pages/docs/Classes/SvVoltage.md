# SvVoltage

State variable for voltage.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 1 | The topological node associated with the voltage state. |
| angle | Float | 1..1 | The voltage angle of the topological node complex voltage with respect to system reference. |
| v | Float | 1..1 | The voltage magnitude at the topological node. The attribute shall be a positive value. |

