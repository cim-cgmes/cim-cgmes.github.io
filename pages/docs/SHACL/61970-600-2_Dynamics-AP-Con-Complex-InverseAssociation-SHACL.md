# 61970-600-2_Dynamics-AP-Con-Complex-InverseAssociation-SHACL

## dyia:AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### dyia:AsynchronousMachine.AsynchronousMachineDynamics-cardinality

**Path:** `^cim:AsynchronousMachineDynamics.AsynchronousMachine`  
**Name:** AsynchronousMachine.AsynchronousMachineDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:AsynchronousMachineDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineTimeConstantReactance

**Nested Properties:**

### dyia:AsynchronousMachineDynamics.MechanicalLoadDynamics-cardinality

**Path:** `^cim:MechanicalLoadDynamics.AsynchronousMachineDynamics`  
**Name:** AsynchronousMachineDynamics.MechanicalLoadDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:AsynchronousMachineDynamics.TurbineGovernorDynamics-cardinality

**Path:** `^cim:TurbineGovernorDynamics.AsynchronousMachineDynamics`  
**Name:** AsynchronousMachineDynamics.TurbineGovernorDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:AsynchronousMachineDynamics.WindTurbineType1or2Dynamics-cardinality

**Path:** `^cim:WindTurbineType1or2Dynamics.AsynchronousMachineDynamics`  
**Name:** AsynchronousMachineDynamics.WindTurbineType1or2Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### dyia:CsConverter.CSCDynamics-cardinality

**Path:** `^cim:CSCDynamics.CsConverter`  
**Name:** CsConverter.CSCDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:DiscontinuousExcitationControlDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscontinuousExcitationControlUserDefined
- targetClass: cim:DiscExcContIEEEDEC1A
- targetClass: cim:DiscExcContIEEEDEC2A
- targetClass: cim:DiscExcContIEEEDEC3A

**Nested Properties:**

### dyia:DiscontinuousExcitationControlDynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.DiscontinuousExcitationControlDynamics`  
**Name:** DiscontinuousExcitationControlDynamics.RemoteInputSignal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:ExcitationSystemDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR7
- targetClass: cim:ExcDC1A
- targetClass: cim:ExcNI
- targetClass: cim:ExcIEEEDC1A
- targetClass: cim:ExcOEX3T
- targetClass: cim:ExcAC4A
- targetClass: cim:ExcSCRX
- targetClass: cim:ExcSK
- targetClass: cim:ExcIEEEST6B
- targetClass: cim:ExcRQB
- targetClass: cim:ExcitationSystemUserDefined
- targetClass: cim:ExcIEEEAC4A
- targetClass: cim:ExcIEEEST1A
- targetClass: cim:ExcST6B
- targetClass: cim:ExcIEEEAC1A
- targetClass: cim:ExcIEEEAC2A
- targetClass: cim:ExcIEEEAC6A
- targetClass: cim:ExcIEEEDC3A
- targetClass: cim:ExcAC5A
- targetClass: cim:ExcSEXS
- targetClass: cim:ExcST3A
- targetClass: cim:ExcIEEEST7B
- targetClass: cim:ExcAVR1
- targetClass: cim:ExcDC3A
- targetClass: cim:ExcST2A
- targetClass: cim:ExcIEEEAC5A
- targetClass: cim:ExcIEEEAC7B
- targetClass: cim:ExcIEEEDC4B
- targetClass: cim:ExcAC3A
- targetClass: cim:ExcAVR4
- targetClass: cim:ExcHU
- targetClass: cim:ExcREXS
- targetClass: cim:ExcAC2A
- targetClass: cim:ExcIEEEAC3A
- targetClass: cim:ExcAVR3
- targetClass: cim:ExcIEEEST2A
- targetClass: cim:ExcDC2A
- targetClass: cim:ExcST7B
- targetClass: cim:ExcAVR5
- targetClass: cim:ExcCZ
- targetClass: cim:ExcELIN2
- targetClass: cim:ExcPIC
- targetClass: cim:ExcST1A
- targetClass: cim:ExcST4B
- targetClass: cim:ExcAC8B
- targetClass: cim:ExcIEEEST3A
- targetClass: cim:ExcAC6A
- targetClass: cim:ExcAVR2
- targetClass: cim:ExcBBC
- targetClass: cim:ExcDC3A1
- targetClass: cim:ExcELIN1
- targetClass: cim:ExcIEEEST5B
- targetClass: cim:ExcANS
- targetClass: cim:ExcIEEEAC8B
- targetClass: cim:ExcIEEEDC2A
- targetClass: cim:ExcAC1A
- targetClass: cim:ExcIEEEST4B

**Nested Properties:**

### dyia:ExcitationSystemDynamics.DiscontinuousExcitationControlDynamics-cardinality

**Path:** `^cim:DiscontinuousExcitationControlDynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.DiscontinuousExcitationControlDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.OverexcitationLimiterDynamics-cardinality

**Path:** `^cim:OverexcitationLimiterDynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.OverexcitationLimiterDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PFVArControllerType1Dynamics-cardinality

**Path:** `^cim:PFVArControllerType1Dynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.PFVArControllerType1Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PFVArControllerType2Dynamics-cardinality

**Path:** `^cim:PFVArControllerType2Dynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.PFVArControllerType2Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PowerSystemStabilizerDynamics-cardinality

**Path:** `^cim:PowerSystemStabilizerDynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.PowerSystemStabilizerDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.UnderexcitationLimiterDynamics-cardinality

**Path:** `^cim:UnderexcitationLimiterDynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.UnderexcitationLimiterDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.VoltageCompensatorDynamics-cardinality

**Path:** `^cim:VoltageCompensatorDynamics.ExcitationSystemDynamics`  
**Name:** ExcitationSystemDynamics.VoltageCompensatorDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:LoadAggregate

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadAggregate

**Nested Properties:**

### dyia:LoadAggregate.LoadMotor-cardinality

**Path:** `^cim:LoadMotor.LoadAggregate`  
**Name:** LoadAggregate.LoadMotor-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:LoadAggregate.LoadStatic-cardinality

**Path:** `^cim:LoadStatic.LoadAggregate`  
**Name:** LoadAggregate.LoadStatic-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:PFVArControllerType1Dynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PFVArControllerType2UserDefined
- targetClass: cim:PFVArType2IEEEPFController
- targetClass: cim:PFVArType2IEEEVArController
- targetClass: cim:PFVArType2Common1

**Nested Properties:**

### dyia:PFVArControllerType1Dynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.PFVArControllerType1Dynamics`  
**Name:** PFVArControllerType1Dynamics.RemoteInputSignal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:PFVArControllerType1Dynamics.VoltageAdjusterDynamics-cardinality

**Path:** `^cim:VoltageAdjusterDynamics.PFVArControllerType1Dynamics`  
**Name:** PFVArControllerType1Dynamics.VoltageAdjusterDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:PowerElectronicsConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerElectronicsConnection

**Nested Properties:**

### dyia:PowerElectronicsConnection.WindTurbineType3or4Dynamics-cardinality

**Path:** `^cim:WindTurbineType3or4Dynamics.PowerElectronicsConnection`  
**Name:** PowerElectronicsConnection.WindTurbineType3or4Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:RemoteInputSignal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RemoteInputSignal

**Nested Properties:**

### dyia:RemoteInputSignal.WindPlantDynamics-cardinality

**Path:** `^cim:WindPlantDynamics.RemoteInputSignal`  
**Name:** RemoteInputSignal.WindPlantDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:RemoteInputSignal.WindTurbineType1or2Dynamics-cardinality

**Path:** `^cim:WindTurbineType1or2Dynamics.RemoteInputSignal`  
**Name:** RemoteInputSignal.WindTurbineType1or2Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:RemoteInputSignal.WindTurbineType3or4Dynamics-cardinality

**Path:** `^cim:WindTurbineType3or4Dynamics.RemoteInputSignal`  
**Name:** RemoteInputSignal.WindTurbineType3or4Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator

**Nested Properties:**

### dyia:StaticVarCompensator.StaticVarCompensatorDynamics-cardinality

**Path:** `^cim:StaticVarCompensatorDynamics.StaticVarCompensator`  
**Name:** StaticVarCompensator.StaticVarCompensatorDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### dyia:SynchronousMachine.SynchronousMachineDynamics-cardinality

**Path:** `^cim:SynchronousMachineDynamics.SynchronousMachine`  
**Name:** SynchronousMachine.SynchronousMachineDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:SynchronousMachineDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineTimeConstantReactance
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:SynchronousMachineSimplified

**Nested Properties:**

### dyia:SynchronousMachineDynamics.CrossCompoundTurbineGovernorDyanmics-cardinality

**Path:** `^cim:CrossCompoundTurbineGovernorDyanmics.SynchronousMachineDynamics`  
**Name:** SynchronousMachineDynamics.CrossCompoundTurbineGovernorDyanmics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.CrossCompoundTurbineGovernorDynamics-cardinality

**Path:** `^cim:CrossCompoundTurbineGovernorDynamics.SynchronousMachineDynamics`  
**Name:** SynchronousMachineDynamics.CrossCompoundTurbineGovernorDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.ExcitationSystemDynamics-cardinality

**Path:** `^cim:ExcitationSystemDynamics.SynchronousMachineDynamics`  
**Name:** SynchronousMachineDynamics.ExcitationSystemDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.MechanicalLoadDynamics-cardinality

**Path:** `^cim:MechanicalLoadDynamics.SynchronousMachineDynamics`  
**Name:** SynchronousMachineDynamics.MechanicalLoadDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:TurbineGovernorDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TurbineGovernorUserDefined
- targetClass: cim:GovHydro4
- targetClass: cim:GovSteam1
- targetClass: cim:GovHydroIEEE1
- targetClass: cim:GovGAST4
- targetClass: cim:GovGASTWD
- targetClass: cim:GovHydro3
- targetClass: cim:GovSteamBB
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovHydroPID
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydroR
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovGAST1
- targetClass: cim:GovGAST2
- targetClass: cim:GovHydroDD
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovHydroFrancis
- targetClass: cim:GovSteamEU
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovHydro1
- targetClass: cim:GovGAST
- targetClass: cim:GovSteam2
- targetClass: cim:GovCT2
- targetClass: cim:GovGAST3
- targetClass: cim:GovHydro2
- targetClass: cim:GovHydroPelton
- targetClass: cim:GovSteam0
- targetClass: cim:GovSteamFV4
- targetClass: cim:GovCT1
- targetClass: cim:GovSteamCC

**Nested Properties:**

### dyia:TurbineGovernorDynamics.TurbineLoadControllerDynamics-cardinality

**Path:** `^cim:TurbineLoadControllerDynamics.TurbineGovernorDynamics`  
**Name:** TurbineGovernorDynamics.TurbineLoadControllerDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:UnderexcitationLimiterDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimIEEE2
- targetClass: cim:UnderexcLimIEEE1
- targetClass: cim:UnderexcitationLimiterUserDefined
- targetClass: cim:UnderexcLim2Simplified
- targetClass: cim:UnderexcLimX1
- targetClass: cim:UnderexcLimX2

**Nested Properties:**

### dyia:UnderexcitationLimiterDynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.UnderexcitationLimiterDynamics`  
**Name:** UnderexcitationLimiterDynamics.RemoteInputSignal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:VCompIEEEType2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VCompIEEEType2

**Nested Properties:**

### dyia:VCompIEEEType2.GenICompensationForGenJ-cardinality

**Path:** `^cim:GenICompensationForGenJ.VCompIEEEType2`  
**Name:** VCompIEEEType2.GenICompensationForGenJ-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 

## dyia:VoltageCompensatorDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageCompensatorUserDefined
- targetClass: cim:VCompIEEEType1
- targetClass: cim:VCompIEEEType2
- targetClass: cim:GenICompensationForGenJ

**Nested Properties:**

### dyia:VoltageCompensatorDynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.VoltageCompensatorDynamics`  
**Name:** VoltageCompensatorDynamics.RemoteInputSignal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### dyia:VsConverter.VSCDynamics-cardinality

**Path:** `^cim:VSCDynamics.VsConverter`  
**Name:** VsConverter.VSCDynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindAeroConstIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindAeroConstIEC

**Nested Properties:**

### dyia:WindAeroConstIEC.WindGenTurbineType1aIEC-cardinality

**Path:** `^cim:WindGenTurbineType1aIEC.WindAeroConstIEC`  
**Name:** WindAeroConstIEC.WindGenTurbineType1aIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindAeroOneDimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindAeroOneDimIEC

**Nested Properties:**

### dyia:WindAeroOneDimIEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindAeroOneDimIEC`  
**Name:** WindAeroOneDimIEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindAeroTwoDimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindAeroTwoDimIEC

**Nested Properties:**

### dyia:WindAeroTwoDimIEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindAeroTwoDimIEC`  
**Name:** WindAeroTwoDimIEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContCurrLimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContCurrLimIEC

**Nested Properties:**

### dyia:WindContCurrLimIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindContCurrLimIEC`  
**Name:** WindContCurrLimIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContCurrLimIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContCurrLimIEC`  
**Name:** WindContCurrLimIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContPType3IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType3IEC

**Nested Properties:**

### dyia:WindContPType3IEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindContPType3IEC`  
**Name:** WindContPType3IEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContPType3IEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindContPType3IEC`  
**Name:** WindContPType3IEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContPType4aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4aIEC

**Nested Properties:**

### dyia:WindContPType4aIEC.WindTurbineType4aIEC-cardinality

**Path:** `^cim:WindTurbineType4aIEC.WindContPType4aIEC`  
**Name:** WindContPType4aIEC.WindTurbineType4aIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContPType4bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4bIEC

**Nested Properties:**

### dyia:WindContPType4bIEC.WindTurbineType4bIEC-cardinality

**Path:** `^cim:WindTurbineType4bIEC.WindContPType4bIEC`  
**Name:** WindContPType4bIEC.WindTurbineType4bIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContPitchAngleIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPitchAngleIEC

**Nested Properties:**

### dyia:WindContPitchAngleIEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindContPitchAngleIEC`  
**Name:** WindContPitchAngleIEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContQIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQIEC

**Nested Properties:**

### dyia:WindContQIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContQIEC`  
**Name:** WindContQIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContQLimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQLimIEC

**Nested Properties:**

### dyia:WindContQLimIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContQLimIEC`  
**Name:** WindContQLimIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContQPQULimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQPQULimIEC

**Nested Properties:**

### dyia:WindContQPQULimIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindContQPQULimIEC`  
**Name:** WindContQPQULimIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContQPQULimIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContQPQULimIEC`  
**Name:** WindContQPQULimIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindContRotorRIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContRotorRIEC

**Nested Properties:**

### dyia:WindContRotorRIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindContRotorRIEC`  
**Name:** WindContRotorRIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContRotorRIEC.WindGenTurbineType2IEC-cardinality

**Path:** `^cim:WindGenTurbineType2IEC.WindContRotorRIEC`  
**Name:** WindContRotorRIEC.WindGenTurbineType2IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindGenType3IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3aIEC

**Nested Properties:**

### dyia:WindGenType3IEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindGenType3IEC`  
**Name:** WindGenType3IEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindGenType3aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3aIEC

**Nested Properties:**

### dyia:WindGenType3aIEC.WindTurbineType4IEC-cardinality

**Path:** `^cim:WindTurbineType4IEC.WindGenType3aIEC`  
**Name:** WindGenType3aIEC.WindTurbineType4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindGenType3bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3bIEC

**Nested Properties:**

### dyia:WindGenType3bIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindGenType3bIEC`  
**Name:** WindGenType3bIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## dyia:WindGenType4IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType4IEC

**Nested Properties:**

### dyia:WindGenType4IEC.WindTurbineType4aIEC-cardinality

**Path:** `^cim:WindTurbineType4aIEC.WindGenType4IEC`  
**Name:** WindGenType4IEC.WindTurbineType4aIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindGenType4IEC.WindTurbineType4bIEC-cardinality

**Path:** `^cim:WindTurbineType4bIEC.WindGenType4IEC`  
**Name:** WindGenType4IEC.WindTurbineType4bIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindMechIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindMechIEC

**Nested Properties:**

### dyia:WindMechIEC.WindTurbineType1or2IEC-cardinality

**Path:** `^cim:WindTurbineType1or2IEC.WindMechIEC`  
**Name:** WindMechIEC.WindTurbineType1or2IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindMechIEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindMechIEC`  
**Name:** WindMechIEC.WindTurbineType3IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindMechIEC.WindTurbineType4bIEC-cardinality

**Path:** `^cim:WindTurbineType4bIEC.WindMechIEC`  
**Name:** WindMechIEC.WindTurbineType4bIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindPitchContPowerIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPitchContPowerIEC

**Nested Properties:**

### dyia:WindPitchContPowerIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindPitchContPowerIEC`  
**Name:** WindPitchContPowerIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPitchContPowerIEC.WindGenTurbineType1bIEC-cardinality

**Path:** `^cim:WindGenTurbineType1bIEC.WindPitchContPowerIEC`  
**Name:** WindPitchContPowerIEC.WindGenTurbineType1bIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindPitchContPowerIEC.WindGenTurbineType2IEC-cardinality

**Path:** `^cim:WindGenTurbineType2IEC.WindPitchContPowerIEC`  
**Name:** WindPitchContPowerIEC.WindGenTurbineType2IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindPlantDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantUserDefined
- targetClass: cim:WindPlantIEC

**Nested Properties:**

### dyia:WindPlantDynamics.WindTurbineType3or4Dynamics-cardinality

**Path:** `^cim:WindTurbineType3or4Dynamics.WindPlantDynamics`  
**Name:** WindPlantDynamics.WindTurbineType3or4Dynamics-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## dyia:WindPlantFreqPcontrolIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantFreqPcontrolIEC

**Nested Properties:**

### dyia:WindPlantFreqPcontrolIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindPlantFreqPcontrolIEC`  
**Name:** WindPlantFreqPcontrolIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPlantFreqPcontrolIEC.WindPlantIEC-cardinality

**Path:** `^cim:WindPlantIEC.WindPlantFreqPcontrolIEC`  
**Name:** WindPlantFreqPcontrolIEC.WindPlantIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindPlantReactiveControlIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantReactiveControlIEC

**Nested Properties:**

### dyia:WindPlantReactiveControlIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindPlantReactiveControlIEC`  
**Name:** WindPlantReactiveControlIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPlantReactiveControlIEC.WindPlantIEC-cardinality

**Path:** `^cim:WindPlantIEC.WindPlantReactiveControlIEC`  
**Name:** WindPlantReactiveControlIEC.WindPlantIEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindProtectionIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindProtectionIEC

**Nested Properties:**

### dyia:WindProtectionIEC.WindDynamicsLookupTable-cardinality

**Path:** `^cim:WindDynamicsLookupTable.WindProtectionIEC`  
**Name:** WindProtectionIEC.WindDynamicsLookupTable-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindProtectionIEC.WindTurbineType1or2IEC-cardinality

**Path:** `^cim:WindTurbineType1or2IEC.WindProtectionIEC`  
**Name:** WindProtectionIEC.WindTurbineType1or2IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindProtectionIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindProtectionIEC`  
**Name:** WindProtectionIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## dyia:WindRefFrameRotIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindRefFrameRotIEC

**Nested Properties:**

### dyia:WindRefFrameRotIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindRefFrameRotIEC`  
**Name:** WindRefFrameRotIEC.WindTurbineType3or4IEC-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

