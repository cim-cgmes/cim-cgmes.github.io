# 61970-600-1_AllProfiles-AP-Con-Complex-SolvedMAS-SHACL

## mas600:DanglingReferences

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:DanglingReferences

## mas600:SvShuntCompensatorSections

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:LinearShuntCompensator

## mas600:SvStatus

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalIsland

## mas600:SvSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Switch
- targetClass: cim:GroundDisconnector
- targetClass: cim:Jumper
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:Disconnector
- targetClass: cim:Cut
- targetClass: cim:Fuse
- targetClass: cim:Breaker

## mas600:SvTapStep

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular

## mas600:SvVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

