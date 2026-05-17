# 61970-456_StateVariables-AP-Con-Complex-Explicit-CrossProfile-SHACL

## sv456cpe:DCTopologicalIsland.DCTopologicalNodes

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCTopologicalIsland

**Nested Properties:**

### sv456cpe:DCTopologicalIsland.DCTopologicalNodes-valueType

**Path:** `cim:DCTopologicalIsland.DCTopologicalNodes / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class DCTopologicalNode or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCTopologicalNode]` 

## sv456cpe:SvInjection.TopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvInjection

**Nested Properties:**

### sv456cpe:SvInjection.TopologicalNode-valueType

**Path:** `cim:SvInjection.TopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class TopologicalNode or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

## sv456cpe:SvPowerFlow.Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvPowerFlow

**Nested Properties:**

### sv456cpe:SvPowerFlow.Terminal-valueType

**Path:** `cim:SvPowerFlow.Terminal / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Terminal or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Terminal]` 

## sv456cpe:SvShuntCompensatorSections.ShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvShuntCompensatorSections

**Nested Properties:**

### sv456cpe:SvShuntCompensatorSections.ShuntCompensator-valueType

**Path:** `cim:SvShuntCompensatorSections.ShuntCompensator / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class ShuntCompensator or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:LinearShuntCompensator cim:NonlinearShuntCompensator]` 

## sv456cpe:SvStatus.ConductingEquipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvStatus

**Nested Properties:**

### sv456cpe:SvStatus.ConductingEquipment-valueType

**Path:** `cim:SvStatus.ConductingEquipment / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class ConductingEquipment or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:NonConformLoad cim:Jumper cim:EquivalentShunt cim:Fuse cim:Cut cim:Junction cim:PowerElectronicsConnection cim:CsConverter cim:EnergyConsumer cim:AsynchronousMachine cim:SynchronousMachine cim:EquivalentBranch cim:Clamp cim:DisconnectingCircuitBreaker cim:EquivalentInjection cim:StationSupply cim:BusbarSection cim:ACLineSegment cim:StaticVarCompensator cim:Disconnector cim:GroundingImpedance cim:LoadBreakSwitch cim:PowerTransformer cim:PetersenCoil cim:Switch cim:LinearShuntCompensator cim:Ground cim:SeriesCompensator cim:GroundDisconnector cim:VsConverter cim:Breaker cim:EnergySource cim:NonlinearShuntCompensator cim:ExternalNetworkInjection cim:ConformLoad cim:Equipment]` 

## sv456cpe:SvSwitch.Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvSwitch

**Nested Properties:**

### sv456cpe:SvSwitch.Switch-valueType

**Path:** `cim:SvSwitch.Switch / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Switch or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Switch cim:Disconnector cim:Jumper cim:DisconnectingCircuitBreaker cim:Breaker cim:LoadBreakSwitch cim:Cut cim:Fuse cim:GroundDisconnector cim:Equipment]` 

## sv456cpe:SvTapStep.TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvTapStep

**Nested Properties:**

### sv456cpe:SvTapStep.TapChanger-valueType

**Path:** `cim:SvTapStep.TapChanger / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class TapChanger or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:RatioTapChanger cim:PhaseTapChangerLinear cim:PhaseTapChangerTabular cim:PhaseTapChangerAsymmetrical cim:PhaseTapChangerSymmetrical]` 

## sv456cpe:SvVoltage.TopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvVoltage

**Nested Properties:**

### sv456cpe:SvVoltage.TopologicalNode-valueType

**Path:** `cim:SvVoltage.TopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class TopologicalNode or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

## sv456cpe:TopologicalIsland.AngleRefTopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalIsland

**Nested Properties:**

### sv456cpe:TopologicalIsland.AngleRefTopologicalNode-valueType

**Path:** `cim:TopologicalIsland.AngleRefTopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class TopologicalNode or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

## sv456cpe:TopologicalIsland.TopologicalNodes

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalIsland

**Nested Properties:**

### sv456cpe:TopologicalIsland.TopologicalNodes-valueType

**Path:** `cim:TopologicalIsland.TopologicalNodes / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class TopologicalNode or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

