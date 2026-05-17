# 61970-600-2_Dynamics-AP-Con-Complex-InverseAssociation-SHACL

## dyia:AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### dyia:AsynchronousMachine.AsynchronousMachineDynamics-cardinality

**Path:** `^cim:AsynchronousMachineDynamics.AsynchronousMachine`  
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
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineTimeConstantReactance
- targetClass: cim:AsynchronousMachineEquivalentCircuit

**Nested Properties:**

### dyia:AsynchronousMachineDynamics.MechanicalLoadDynamics-cardinality

**Path:** `^cim:MechanicalLoadDynamics.AsynchronousMachineDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:AsynchronousMachineDynamics.TurbineGovernorDynamics-cardinality

**Path:** `^cim:TurbineGovernorDynamics.AsynchronousMachineDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:AsynchronousMachineDynamics.WindTurbineType1or2Dynamics-cardinality

**Path:** `^cim:WindTurbineType1or2Dynamics.AsynchronousMachineDynamics`  
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
- targetClass: cim:ExcIEEEST4B
- targetClass: cim:ExcIEEEST6B
- targetClass: cim:ExcAC1A
- targetClass: cim:ExcAC3A
- targetClass: cim:ExcDC2A
- targetClass: cim:ExcIEEEAC1A
- targetClass: cim:ExcAVR7
- targetClass: cim:ExcNI
- targetClass: cim:ExcPIC
- targetClass: cim:ExcREXS
- targetClass: cim:ExcANS
- targetClass: cim:ExcBBC
- targetClass: cim:ExcST1A
- targetClass: cim:ExcIEEEAC8B
- targetClass: cim:ExcIEEEST3A
- targetClass: cim:ExcIEEEST5B
- targetClass: cim:ExcAVR5
- targetClass: cim:ExcST4B
- targetClass: cim:ExcAVR1
- targetClass: cim:ExcIEEEST1A
- targetClass: cim:ExcELIN1
- targetClass: cim:ExcST3A
- targetClass: cim:ExcIEEEAC2A
- targetClass: cim:ExcIEEEDC2A
- targetClass: cim:ExcIEEEAC5A
- targetClass: cim:ExcAC2A
- targetClass: cim:ExcAC4A
- targetClass: cim:ExcDC3A
- targetClass: cim:ExcRQB
- targetClass: cim:ExcIEEEAC7B
- targetClass: cim:ExcIEEEDC4B
- targetClass: cim:ExcAC5A
- targetClass: cim:ExcIEEEAC4A
- targetClass: cim:ExcIEEEAC6A
- targetClass: cim:ExcIEEEST2A
- targetClass: cim:ExcSEXS
- targetClass: cim:ExcIEEEST7B
- targetClass: cim:ExcIEEEDC3A
- targetClass: cim:ExcAVR4
- targetClass: cim:ExcOEX3T
- targetClass: cim:ExcST6B
- targetClass: cim:ExcAC8B
- targetClass: cim:ExcIEEEAC3A
- targetClass: cim:ExcDC1A
- targetClass: cim:ExcHU
- targetClass: cim:ExcAVR2
- targetClass: cim:ExcELIN2
- targetClass: cim:ExcAVR3
- targetClass: cim:ExcST2A
- targetClass: cim:ExcIEEEDC1A
- targetClass: cim:ExcSCRX
- targetClass: cim:ExcSK
- targetClass: cim:ExcAC6A
- targetClass: cim:ExcCZ
- targetClass: cim:ExcDC3A1
- targetClass: cim:ExcST7B
- targetClass: cim:ExcitationSystemUserDefined

**Nested Properties:**

### dyia:ExcitationSystemDynamics.DiscontinuousExcitationControlDynamics-cardinality

**Path:** `^cim:DiscontinuousExcitationControlDynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.OverexcitationLimiterDynamics-cardinality

**Path:** `^cim:OverexcitationLimiterDynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PFVArControllerType1Dynamics-cardinality

**Path:** `^cim:PFVArControllerType1Dynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PFVArControllerType2Dynamics-cardinality

**Path:** `^cim:PFVArControllerType2Dynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.PowerSystemStabilizerDynamics-cardinality

**Path:** `^cim:PowerSystemStabilizerDynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.UnderexcitationLimiterDynamics-cardinality

**Path:** `^cim:UnderexcitationLimiterDynamics.ExcitationSystemDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:ExcitationSystemDynamics.VoltageCompensatorDynamics-cardinality

**Path:** `^cim:VoltageCompensatorDynamics.ExcitationSystemDynamics`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:LoadAggregate.LoadStatic-cardinality

**Path:** `^cim:LoadStatic.LoadAggregate`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:PFVArControllerType1Dynamics.VoltageAdjusterDynamics-cardinality

**Path:** `^cim:VoltageAdjusterDynamics.PFVArControllerType1Dynamics`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:RemoteInputSignal.WindTurbineType1or2Dynamics-cardinality

**Path:** `^cim:WindTurbineType1or2Dynamics.RemoteInputSignal`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:RemoteInputSignal.WindTurbineType3or4Dynamics-cardinality

**Path:** `^cim:WindTurbineType3or4Dynamics.RemoteInputSignal`  
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
- targetClass: cim:SynchronousMachineSimplified
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineTimeConstantReactance
- targetClass: cim:SynchronousMachineEquivalentCircuit

**Nested Properties:**

### dyia:SynchronousMachineDynamics.CrossCompoundTurbineGovernorDyanmics-cardinality

**Path:** `^cim:CrossCompoundTurbineGovernorDyanmics.SynchronousMachineDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.CrossCompoundTurbineGovernorDynamics-cardinality

**Path:** `^cim:CrossCompoundTurbineGovernorDynamics.SynchronousMachineDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.ExcitationSystemDynamics-cardinality

**Path:** `^cim:ExcitationSystemDynamics.SynchronousMachineDynamics`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:SynchronousMachineDynamics.MechanicalLoadDynamics-cardinality

**Path:** `^cim:MechanicalLoadDynamics.SynchronousMachineDynamics`  
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
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovHydroDD
- targetClass: cim:GovSteam0
- targetClass: cim:GovHydroIEEE1
- targetClass: cim:GovGAST4
- targetClass: cim:TurbineGovernorUserDefined
- targetClass: cim:GovHydroFrancis
- targetClass: cim:GovSteamCC
- targetClass: cim:GovSteamEU
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovCT2
- targetClass: cim:GovSteam2
- targetClass: cim:GovHydro3
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovSteamBB
- targetClass: cim:GovCT1
- targetClass: cim:GovGAST
- targetClass: cim:GovGAST2
- targetClass: cim:GovHydro1
- targetClass: cim:GovHydro2
- targetClass: cim:GovHydroPelton
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovGAST1
- targetClass: cim:GovGAST3
- targetClass: cim:GovHydro4
- targetClass: cim:GovHydroR
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovGASTWD
- targetClass: cim:GovHydroPID
- targetClass: cim:GovSteam1
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovSteamFV4

**Nested Properties:**

### dyia:TurbineGovernorDynamics.TurbineLoadControllerDynamics-cardinality

**Path:** `^cim:TurbineLoadControllerDynamics.TurbineGovernorDynamics`  
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
- targetClass: cim:UnderexcLimIEEE1
- targetClass: cim:UnderexcitationLimiterUserDefined
- targetClass: cim:UnderexcLim2Simplified
- targetClass: cim:UnderexcLimX1
- targetClass: cim:UnderexcLimX2
- targetClass: cim:UnderexcLimIEEE2

**Nested Properties:**

### dyia:UnderexcitationLimiterDynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.UnderexcitationLimiterDynamics`  
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
- targetClass: cim:GenICompensationForGenJ
- targetClass: cim:VoltageCompensatorUserDefined
- targetClass: cim:VCompIEEEType1
- targetClass: cim:VCompIEEEType2

**Nested Properties:**

### dyia:VoltageCompensatorDynamics.RemoteInputSignal-cardinality

**Path:** `^cim:RemoteInputSignal.VoltageCompensatorDynamics`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContCurrLimIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContCurrLimIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContPType3IEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindContPType3IEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContQPQULimIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindContQPQULimIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindContRotorRIEC.WindGenTurbineType2IEC-cardinality

**Path:** `^cim:WindGenTurbineType2IEC.WindContRotorRIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindGenType4IEC.WindTurbineType4bIEC-cardinality

**Path:** `^cim:WindTurbineType4bIEC.WindGenType4IEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindMechIEC.WindTurbineType3IEC-cardinality

**Path:** `^cim:WindTurbineType3IEC.WindMechIEC`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindMechIEC.WindTurbineType4bIEC-cardinality

**Path:** `^cim:WindTurbineType4bIEC.WindMechIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPitchContPowerIEC.WindGenTurbineType1bIEC-cardinality

**Path:** `^cim:WindGenTurbineType1bIEC.WindPitchContPowerIEC`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindPitchContPowerIEC.WindGenTurbineType2IEC-cardinality

**Path:** `^cim:WindGenTurbineType2IEC.WindPitchContPowerIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPlantFreqPcontrolIEC.WindPlantIEC-cardinality

**Path:** `^cim:WindPlantIEC.WindPlantFreqPcontrolIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindPlantReactiveControlIEC.WindPlantIEC-cardinality

**Path:** `^cim:WindPlantIEC.WindPlantReactiveControlIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### dyia:WindProtectionIEC.WindTurbineType1or2IEC-cardinality

**Path:** `^cim:WindTurbineType1or2IEC.WindProtectionIEC`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### dyia:WindProtectionIEC.WindTurbineType3or4IEC-cardinality

**Path:** `^cim:WindTurbineType3or4IEC.WindProtectionIEC`  
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
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

