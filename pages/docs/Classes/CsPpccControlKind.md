# CsPpccControlKind (Enumeration)

Active power control modes for HVDC line operating as Current Source Converter.

## Values

| Label | Comment |
|-------|---------|
| activePower | Control is active power control at AC side, at point of common coupling. Target is provided by ACDCConverter.targetPpcc. |
| dcVoltage | Control is DC voltage with target value provided by ACDCConverter.targetUdc. |
| dcCurrent | Control is DC current with target value provided by CsConverter.targetIdc. |

