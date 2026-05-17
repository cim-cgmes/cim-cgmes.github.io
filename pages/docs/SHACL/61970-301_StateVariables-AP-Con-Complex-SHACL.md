# 61970-301_StateVariables-AP-Con-Complex-SHACL

## sv:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### sv:ACDCConverter.poleLossP-valueRange

**Path:** `cim:ACDCConverter.poleLossP`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:ACDCConverter.uc-valueRange

**Path:** `cim:ACDCConverter.uc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:ACDCConverter.udc-valueRange

**Path:** `cim:ACDCConverter.udc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:CsConverter.alpha-valueRange

**Path:** `cim:CsConverter.alpha`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:CsConverter.gamma-valueRange

**Path:** `cim:CsConverter.gamma`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## sv:SvShuntCompensatorSections

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvShuntCompensatorSections

**Nested Properties:**

### sv:SvShuntCompensatorSections.sections-valueRange

**Path:** `cim:SvShuntCompensatorSections.sections`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## sv:SvVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvVoltage

**Nested Properties:**

### sv:SvVoltage.v-valueRange

**Path:** `cim:SvVoltage.v`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## sv:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### sv:ACDCConverter.poleLossP-valueRange

**Path:** `cim:ACDCConverter.poleLossP`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:ACDCConverter.uc-valueRange

**Path:** `cim:ACDCConverter.uc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:ACDCConverter.udc-valueRange

**Path:** `cim:ACDCConverter.udc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:VsConverter.delta-valueRange

**Path:** `cim:VsConverter.delta`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### sv:VsConverter.uv-valueRange

**Path:** `cim:VsConverter.uv`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

