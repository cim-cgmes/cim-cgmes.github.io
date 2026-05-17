# 61970-301_EquipmentBoundary-AP-Con-Complex-SHACL

## eqbd:BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BaseVoltage

**Nested Properties:**

### eqbd:BaseVoltage.nominalVoltage-valueRange

**Path:** `cim:BaseVoltage.nominalVoltage`  
Shall be a positive value and not zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eqbd:BoundaryPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim100:BoundaryPoint

**Nested Properties:**

### eqbd:BoundaryPoint.fromEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
The length of the string is 2 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is not 2 characters."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 

### eqbd:BoundaryPoint.fromEndIsoCode-valueValidity

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes).

**Severity:** sh:Violation

**Messages:**
- "Not valid two-character ISO code for Europe."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[AL AT BE BG HR CY CZ DK EE FI FR DE GR HU IS IE IT LV LI LT LU MT MD ME NL NO PL PT RO RS SK SI ES SE CH TR UA MK GB]` 

### eqbd:BoundaryPoint.fromEndName-stringLength

**Path:** `cim100:BoundaryPoint.fromEndName`  
A human readable name with length of the string 64 characters maximum. 

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.fromEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.fromEndNameTso`  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.toEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.toEndIsoCode`  
The length of the string is 2 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is not 2 characters."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 

### eqbd:BoundaryPoint.toEndIsoCode-valueValidity

**Path:** `cim100:BoundaryPoint.toEndIsoCode`  
The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes).

**Severity:** sh:Violation

**Messages:**
- "Not valid two-character ISO code for Europe."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[AL AT BE BG HR CY CZ DK EE FI FR DE GR HU IS IE IT LV LI LT LU MT MD ME NL NO PL PT RO RS SK SI ES SE CH TR UA MK GB]` 

### eqbd:BoundaryPoint.toEndName-stringLength

**Path:** `cim100:BoundaryPoint.toEndName`  
A human readable name with length of the string 64 characters maximum. 

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.toEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.toEndNameTso`  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

