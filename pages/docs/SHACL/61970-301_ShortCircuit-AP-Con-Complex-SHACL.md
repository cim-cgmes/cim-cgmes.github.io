# 61970-301_ShortCircuit-AP-Con-Complex-SHACL

## sc:MutualCoupling

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MutualCoupling

**Nested Properties:**

### sc:MutualCoupling.distance11-lengthValueRange

**Path:** `cim:MutualCoupling.distance11`  
**Name:** C:301:SC:MutualCoupling:lengthValueRange  
Length datatype defines that: It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sc:MutualCoupling.distance12-lengthValueRange

**Path:** `cim:MutualCoupling.distance12`  
**Name:** C:301:SC:MutualCoupling:lengthValueRange  
Length datatype defines that: It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sc:MutualCoupling.distance21-lengthValueRange

**Path:** `cim:MutualCoupling.distance21`  
**Name:** C:301:SC:MutualCoupling:lengthValueRange  
Length datatype defines that: It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sc:MutualCoupling.distance22-lengthValueRange

**Path:** `cim:MutualCoupling.distance22`  
**Name:** C:301:SC:MutualCoupling:lengthValueRange  
Length datatype defines that: It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## sc:PetersenCoil

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PetersenCoil

**Nested Properties:**

### sc:PetersenCoil.offsetCurrent-valueRangeTypical

**Path:** `cim:PetersenCoil.offsetCurrent`  
**Name:** C:301:SC:PetersenCoil.offsetCurrent:valueRangeTypical  
This is normally a fixed amount for which the controller is configured and could be positive or negative.  Typically 0 to 60 A depending on voltage and resonance conditions.

**Severity:** sh:Warning

**Messages:**
- "The value is outside the range: 0-60 A."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Warning)
  - Value: `0.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Warning)
  - Value: `60` 

### sc:PetersenCoil.positionCurrent-valueRangeTypical

**Path:** `cim:PetersenCoil.positionCurrent`  
**Name:** C:301:SC:PetersenCoil.positionCurrent:valueRangeTypical  
Typically in the range of 20 mA to 200 mA.

**Severity:** sh:Warning

**Messages:**
- "The value is outside the range: 20-200 mA."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Warning)
  - Value: `0.02` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Warning)
  - Value: `0.2` 

## sc:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### sc:PowerTransformerEnd.phaseAngleClock-valueRange

**Path:** `cim:PowerTransformerEnd.phaseAngleClock`  
**Name:** C:301:SC:PowerTransformerEnd.phaseAngleClock:valueRange  
The valid values are 0 to 11.

**Severity:** sh:Violation

**Messages:**
- "The value is outside the valid range: 0-11."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `11.0` 

## sc:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

**Nested Properties:**

### sc:SeriesCompensator.varistorRatedCurrent-valueRange

**Path:** `cim:SeriesCompensator.varistorRatedCurrent`  
**Name:** C:301:SC:SeriesCompensator.varistorRatedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

