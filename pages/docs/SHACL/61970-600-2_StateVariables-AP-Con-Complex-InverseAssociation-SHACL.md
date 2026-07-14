# 61970-600-2_StateVariables-AP-Con-Complex-InverseAssociation-SHACL

## sv301ia:ConductingEquipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator
- targetClass: cim:Jumper
- targetClass: cim:VsConverter
- targetClass: cim:ACLineSegment
- targetClass: cim:BusbarSection
- targetClass: cim:EnergyConsumer
- targetClass: cim:SynchronousMachine
- targetClass: cim:EquivalentShunt
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:CsConverter
- targetClass: cim:PetersenCoil
- targetClass: cim:ConformLoad
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:Ground
- targetClass: cim:GroundingImpedance
- targetClass: cim:StationSupply
- targetClass: cim:AsynchronousMachine
- targetClass: cim:PowerTransformer
- targetClass: cim:Junction
- targetClass: cim:EnergySource
- targetClass: cim:NonConformLoad
- targetClass: cim:Switch
- targetClass: cim:Breaker
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:EquivalentInjection
- targetClass: cim:SeriesCompensator
- targetClass: cim:Fuse
- targetClass: cim:Cut
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Clamp
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:EquivalentBranch
- targetClass: cim:GroundDisconnector
- targetClass: cim:Disconnector

**Nested Properties:**

### sv301ia:ConductingEquipment.SvStatus-cardinality

**Path:** `^cim:SvStatus.ConductingEquipment`  
**Name:** ConductingEquipment.SvStatus-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## sv301ia:DCTopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCTopologicalNode

**Nested Properties:**

### sv301ia:DCTopologicalNode.DCTopologicalIsland-cardinality

**Path:** `^cim:DCTopologicalIsland.DCTopologicalNodes`  
**Name:** DCTopologicalNode.DCTopologicalIsland-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## sv301ia:ShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### sv301ia:ShuntCompensator.SvShuntCompensatorSections-cardinality

**Path:** `^cim:SvShuntCompensatorSections.ShuntCompensator`  
**Name:** ShuntCompensator.SvShuntCompensatorSections-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## sv301ia:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### sv301ia:TapChanger.SvTapStep-cardinality

**Path:** `^cim:SvTapStep.TapChanger`  
**Name:** TapChanger.SvTapStep-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## sv301ia:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Terminal

**Nested Properties:**

### sv301ia:Terminal.SvPowerFlow-cardinality

**Path:** `^cim:SvPowerFlow.Terminal`  
**Name:** Terminal.SvPowerFlow-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## sv301ia:TopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### sv301ia:TopologicalNode.SvInjection-cardinality

**Path:** `^cim:SvInjection.TopologicalNode`  
**Name:** TopologicalNode.SvInjection-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.SvVoltage-cardinality

**Path:** `^cim:SvVoltage.TopologicalNode`  
**Name:** TopologicalNode.SvVoltage-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.AngleRefTopologicalIsland-cardinality

**Path:** `^cim:TopologicalIsland.AngleRefTopologicalNode`  
**Name:** TopologicalNode.AngleRefTopologicalIsland-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.TopologicalIsland-cardinality

**Path:** `^cim:TopologicalIsland.TopologicalNodes`  
**Name:** TopologicalNode.TopologicalIsland-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

