# 61970-457_Dynamics-AP-Con-Complex-Explicit-CrossProfile-SHACL

## dy457cpe:AsynchronousMachineDynamics.AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy457cpe:AsynchronousMachineDynamics.AsynchronousMachine-valueType

**Path:** `cim:AsynchronousMachineDynamics.AsynchronousMachine / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class AsynchronousMachine or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AsynchronousMachine]` 

## dy457cpe:CSCDynamics.CSConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CSCUserDefined

**Nested Properties:**

### dy457cpe:CSCDynamics.CSConverter-valueType

**Path:** `cim:CSCDynamics.CSConverter / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class CSConverter or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:CSConverter]` 

## dy457cpe:EnergyConsumer.LoadDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergyConsumer
- targetClass: cim:StationSupply
- targetClass: cim:ConformLoad
- targetClass: cim:NonConformLoad

**Nested Properties:**

### dy457cpe:EnergyConsumer.LoadDynamics-valueType

**Path:** `cim:EnergyConsumer.LoadDynamics / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class LoadDynamics or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:LoadComposite cim:LoadGenericNonLinear cim:LoadUserDefined cim:LoadAggregate]` 

## dy457cpe:RemoteInputSignal.Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RemoteInputSignal

**Nested Properties:**

### dy457cpe:RemoteInputSignal.Terminal-valueType

**Path:** `cim:RemoteInputSignal.Terminal / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Terminal or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Terminal]` 

## dy457cpe:StaticVarCompensatorDynamics.StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SVCUserDefined

**Nested Properties:**

### dy457cpe:StaticVarCompensatorDynamics.StaticVarCompensator-valueType

**Path:** `cim:StaticVarCompensatorDynamics.StaticVarCompensator / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class StaticVarCompensator or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StaticVarCompensator]` 

## dy457cpe:SynchronousMachineDynamics.SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineSimplified
- targetClass: cim:SynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy457cpe:SynchronousMachineDynamics.SynchronousMachine-valueType

**Path:** `cim:SynchronousMachineDynamics.SynchronousMachine / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class SynchronousMachine or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:SynchronousMachine]` 

## dy457cpe:VSCDynamics.VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VSCUserDefined

**Nested Properties:**

### dy457cpe:VSCDynamics.VsConverter-valueType

**Path:** `cim:VSCDynamics.VsConverter / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class VsConverter or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VsConverter]` 

## dy457cpe:WindTurbineType3or4Dynamics.PowerElectronicsConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindTurbineType4aIEC
- targetClass: cim:WindType3or4UserDefined
- targetClass: cim:WindTurbineType3IEC
- targetClass: cim:WindTurbineType4bIEC

**Nested Properties:**

### dy457cpe:WindTurbineType3or4Dynamics.PowerElectronicsConnection-valueType

**Path:** `cim:WindTurbineType3or4Dynamics.PowerElectronicsConnection / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerElectronicsConnection or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PowerElectronicsConnection]` 

