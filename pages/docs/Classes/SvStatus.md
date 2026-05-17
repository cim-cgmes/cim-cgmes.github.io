# SvStatus

State variable for status.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ConductingEquipment | [ConductingEquipment](ConductingEquipment.md) | 1 | The conducting equipment associated with the status state variable. |
| inService | Boolean | 1..1 | The in service status as a result of topology processing. It indicates if the equipment is considered as energized by the power flow. It reflects if the equipment is connected within a solvable island. It does not necessarily reflect whether or not the island was solved by the power flow. |

