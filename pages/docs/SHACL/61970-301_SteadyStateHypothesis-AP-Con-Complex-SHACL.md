# 61970-301_SteadyStateHypothesis-AP-Con-Complex-SHACL

## ssh:ActivePowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ActivePowerLimit

**Nested Properties:**

### ssh:ActivePowerLimit.value-valueRange

**Path:** `cim:ActivePowerLimit.value`  
**Name:** C:301:SSH:ActivePowerLimit.value:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ApparentPowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ApparentPowerLimit

**Nested Properties:**

### ssh:ApparentPowerLimit.value-valueRange

**Path:** `cim:ApparentPowerLimit.value`  
**Name:** C:301:SSH:ApparentPowerLimit.value:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

**Nested Properties:**

### ssh:BatteryUnit.storedE-valueRange

**Path:** `cim:BatteryUnit.storedE`  
**Name:** C:301:SSH:BatteryUnit.storedE:valueRange  
The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ControlArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ControlArea

**Nested Properties:**

### ssh:ControlArea.pTolerance-valueRange

**Path:** `cim:ControlArea.pTolerance`  
**Name:** C:301:SSH:ControlArea.pTolerance:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### ssh:ACDCConverter.targetUdc-valueRange

**Path:** `cim:ACDCConverter.targetUdc`  
**Name:** C:301:SSH:ACDCConverter.targetUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetAlpha-valueRange

**Path:** `cim:CsConverter.targetAlpha`  
**Name:** C:301:SSH:CsConverter.targetAlpha:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetGamma-valueRange

**Path:** `cim:CsConverter.targetGamma`  
**Name:** C:301:SSH:CsConverter.targetGamma:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetIdc-valueRange

**Path:** `cim:CsConverter.targetIdc`  
**Name:** C:301:SSH:CsConverter.targetIdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:CurrentLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurrentLimit

**Nested Properties:**

### ssh:CurrentLimit.value-valueRange

**Path:** `cim:CurrentLimit.value`  
**Name:** C:301:SSH:CurrentLimit.value:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:EnergySource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergySource

**Nested Properties:**

### ssh:EnergySource.voltageAngle-valueRange

**Path:** `cim:EnergySource.voltageAngle`  
**Name:** C:301:SSH:EnergySource.voltageAngle:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:EnergySource.voltageMagnitude-valueRange

**Path:** `cim:EnergySource.voltageMagnitude`  
**Name:** C:301:SSH:EnergySource.voltageMagnitude:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### ssh:EquivalentInjection.regulationTarget-valueRange

**Path:** `cim:EquivalentInjection.regulationTarget`  
**Name:** C:301:SSH:EquivalentInjection.regulationTarget:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### ssh:ShuntCompensator.sections-valueRange

**Path:** `cim:ShuntCompensator.sections`  
**Name:** C:301:SSH:ShuntCompensator.sections:valueRange  
The attribute shall be a positive value or zero. 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### ssh:ShuntCompensator.sections-valueRange

**Path:** `cim:ShuntCompensator.sections`  
**Name:** C:301:SSH:ShuntCompensator.sections:valueRange  
The attribute shall be a positive value or zero. 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-valueRange

**Path:** `cim:RegulatingControl.targetDeadband`  
**Name:** C:301:SSH:RegulatingControl.targetDeadband:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-valueRange

**Path:** `cim:RegulatingControl.targetDeadband`  
**Name:** C:301:SSH:RegulatingControl.targetDeadband:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:VoltageLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageLimit

**Nested Properties:**

### ssh:VoltageLimit.value-valueRange

**Path:** `cim:VoltageLimit.value`  
**Name:** C:301:SSH:VoltageLimit.value:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### ssh:ACDCConverter.targetUdc-valueRange

**Path:** `cim:ACDCConverter.targetUdc`  
**Name:** C:301:SSH:ACDCConverter.targetUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.droop-valueRange

**Path:** `cim:VsConverter.droop`  
**Name:** C:301:SSH:VsConverter.droop:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.droopCompensation-valueRange

**Path:** `cim:VsConverter.droopCompensation`  
**Name:** C:301:SSH:VsConverter.droopCompensation:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.qShare-valueRange

**Path:** `cim:VsConverter.qShare`  
**Name:** C:301:SSH:VsConverter.qShare:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPWMfactor-valueRange

**Path:** `cim:VsConverter.targetPWMfactor`  
**Name:** C:301:SSH:VsConverter.targetPWMfactor:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPhasePcc-valueRange

**Path:** `cim:VsConverter.targetPhasePcc`  
**Name:** C:301:SSH:VsConverter.targetPhasePcc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPowerFactorPcc-valueRange

**Path:** `cim:VsConverter.targetPowerFactorPcc`  
**Name:** C:301:SSH:VsConverter.targetPowerFactorPcc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetUpcc-valueRange

**Path:** `cim:VsConverter.targetUpcc`  
**Name:** C:301:SSH:VsConverter.targetUpcc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
**Name:** C:301:SSH:GeneratingUnit.normalPF:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

