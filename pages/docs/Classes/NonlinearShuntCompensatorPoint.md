# NonlinearShuntCompensatorPoint

A non linear shunt compensator bank or section admittance value. The number of NonlinearShuntCompenstorPoint instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections. ShuntCompensator.sections shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no interpolation between NonlinearShuntCompenstorPoint-s.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| NonlinearShuntCompensator | [NonlinearShuntCompensator](NonlinearShuntCompensator.md) | 1 | Non-linear shunt compensator owning this point. |
| b | Float | 1..1 | Positive sequence shunt (charging) susceptance per section. |
| b0 | Float | 1..1 | Zero sequence shunt (charging) susceptance per section. |
| g | Float | 1..1 | Positive sequence shunt (charging) conductance per section. |
| g0 | Float | 1..1 | Zero sequence shunt (charging) conductance per section. |
| sectionNumber | Integer | 1..1 | The number of the section. |

