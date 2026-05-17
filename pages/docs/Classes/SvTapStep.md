# SvTapStep

State variable for transformer tap step.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TapChanger | [TapChanger](TapChanger.md) | 1 | The tap changer associated with the tap step state. |
| position | Float | 1..1 | The floating point tap position. This is not the tap ratio, but rather the tap step position as defined by the related tap changer model and normally is constrained to be within the range of minimum and maximum tap positions. |

