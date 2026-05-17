# VsQpccControlKind (Enumeration)

Kind of reactive power control at point of common coupling for a voltage source converter.

## Values

| Label | Comment |
|-------|---------|
| reactivePcc | Control is reactive power at point of common coupling. Target is provided by VsConverter.targetQpcc. |
| voltagePcc | Control is voltage at point of common coupling. Target is provided by VsConverter.targetUpcc. |
| powerFactorPcc | Control is power factor at point of common coupling. Target is provided by VsConverter.targetPowerFactorPcc. |
| pulseWidthModulation | No explicit control. Pulse-modulation factor is directly set in magnitude (VsConverter.targetPWMfactor) and phase (VsConverter.targetPhasePcc). |

