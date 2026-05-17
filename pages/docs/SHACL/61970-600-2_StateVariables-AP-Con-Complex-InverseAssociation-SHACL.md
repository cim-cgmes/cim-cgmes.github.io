# 61970-600-2_StateVariables-AP-Con-Complex-InverseAssociation-SHACL

## sv301ia:ConductingEquipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch
- targetClass: cim:EquivalentShunt
- targetClass: cim:Junction
- targetClass: cim:GroundingImpedance
- targetClass: cim:SynchronousMachine
- targetClass: cim:Fuse
- targetClass: cim:VsConverter
- targetClass: cim:EnergyConsumer
- targetClass: cim:StaticVarCompensator
- targetClass: cim:SeriesCompensator
- targetClass: cim:Jumper
- targetClass: cim:ACLineSegment
- targetClass: cim:StationSupply
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:PowerTransformer
- targetClass: cim:Breaker
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Clamp
- targetClass: cim:PetersenCoil
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:EquivalentInjection
- targetClass: cim:GroundDisconnector
- targetClass: cim:Disconnector
- targetClass: cim:Switch
- targetClass: cim:BusbarSection
- targetClass: cim:NonConformLoad
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:Ground
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:AsynchronousMachine
- targetClass: cim:Cut
- targetClass: cim:CsConverter
- targetClass: cim:EnergySource
- targetClass: cim:ConformLoad

**Nested Properties:**

### sv301ia:ConductingEquipment.SvStatus-cardinality

**Path:** `^cim:SvStatus.ConductingEquipment`  
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
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### sv301ia:TapChanger.SvTapStep-cardinality

**Path:** `^cim:SvTapStep.TapChanger`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.SvVoltage-cardinality

**Path:** `^cim:SvVoltage.TopologicalNode`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.AngleRefTopologicalIsland-cardinality

**Path:** `^cim:TopologicalIsland.AngleRefTopologicalNode`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### sv301ia:TopologicalNode.TopologicalIsland-cardinality

**Path:** `^cim:TopologicalIsland.TopologicalNodes`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

