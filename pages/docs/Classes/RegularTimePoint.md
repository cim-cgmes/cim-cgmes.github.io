# RegularTimePoint

Time point for a schedule where the time between the consecutive points is constant.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| IntervalSchedule | [RegularIntervalSchedule](RegularIntervalSchedule.md) | 1 | Regular interval schedule containing this time point. |
| sequenceNumber | Integer | 1..1 | The position of the regular time point in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the associated regular interval schedule's time step with the regular time point sequence number and adding the associated schedules start time. To specify values for the start time, use sequence number 0. The sequence number cannot be negative. |
| value1 | Float | 1..1 | The first value at the time. The meaning of the value is defined by the derived type of the associated schedule. |
| value2 | Float | 0..1 | The second value at the time. The meaning of the value is defined by the derived type of the associated schedule. |

