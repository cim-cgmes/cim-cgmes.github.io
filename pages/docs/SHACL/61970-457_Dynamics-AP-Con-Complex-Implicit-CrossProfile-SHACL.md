# 61970-457_Dynamics-AP-Con-Complex-Implicit-CrossProfile-SHACL

## dy457cpi:AsynchronousMachineDynamics.AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy457cpi:AsynchronousMachineDynamics.AsynchronousMachine-valueType

**Path:** `cim:AsynchronousMachineDynamics.AsynchronousMachine`  
**Name:** AsynchronousMachineDynamics.AsynchronousMachine-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class AsynchronousMachine or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:AsynchronousMachine` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:CSCDynamics.CSConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CSCUserDefined

**Nested Properties:**

### dy457cpi:CSCDynamics.CSConverter-valueType

**Path:** `cim:CSCDynamics.CSConverter`  
**Name:** CSCDynamics.CSConverter-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class CSConverter or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:CSConverter` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:EnergyConsumer.LoadDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoad
- targetClass: cim:NonConformLoad
- targetClass: cim:EnergyConsumer
- targetClass: cim:StationSupply

**Nested Properties:**

### dy457cpi:EnergyConsumer.LoadDynamics-valueType

**Path:** `cim:EnergyConsumer.LoadDynamics`  
**Name:** EnergyConsumer.LoadDynamics-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class LoadDynamics or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:LoadDynamics` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:RemoteInputSignal.Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RemoteInputSignal

**Nested Properties:**

### dy457cpi:RemoteInputSignal.Terminal-valueType

**Path:** `cim:RemoteInputSignal.Terminal`  
**Name:** RemoteInputSignal.Terminal-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Terminal or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:StaticVarCompensatorDynamics.StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SVCUserDefined

**Nested Properties:**

### dy457cpi:StaticVarCompensatorDynamics.StaticVarCompensator-valueType

**Path:** `cim:StaticVarCompensatorDynamics.StaticVarCompensator`  
**Name:** StaticVarCompensatorDynamics.StaticVarCompensator-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class StaticVarCompensator or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:StaticVarCompensator` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:SynchronousMachineDynamics.SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineSimplified
- targetClass: cim:SynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy457cpi:SynchronousMachineDynamics.SynchronousMachine-valueType

**Path:** `cim:SynchronousMachineDynamics.SynchronousMachine`  
**Name:** SynchronousMachineDynamics.SynchronousMachine-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class SynchronousMachine or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:SynchronousMachine` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:VSCDynamics.VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VSCUserDefined

**Nested Properties:**

### dy457cpi:VSCDynamics.VsConverter-valueType

**Path:** `cim:VSCDynamics.VsConverter`  
**Name:** VSCDynamics.VsConverter-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class VsConverter or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:VsConverter` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dy457cpi:WindTurbineType3or4Dynamics.PowerElectronicsConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindTurbineType3IEC
- targetClass: cim:WindTurbineType4bIEC
- targetClass: cim:WindTurbineType4aIEC
- targetClass: cim:WindType3or4UserDefined

**Nested Properties:**

### dy457cpi:WindTurbineType3or4Dynamics.PowerElectronicsConnection-valueType

**Path:** `cim:WindTurbineType3or4Dynamics.PowerElectronicsConnection`  
**Name:** WindTurbineType3or4Dynamics.PowerElectronicsConnection-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerElectronicsConnection or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:PowerElectronicsConnection` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

