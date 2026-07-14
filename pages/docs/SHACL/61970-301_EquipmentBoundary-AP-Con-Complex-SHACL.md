# 61970-301_EquipmentBoundary-AP-Con-Complex-SHACL

## eqbd:BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BaseVoltage

**Nested Properties:**

### eqbd:BaseVoltage.nominalVoltage-valueRange

**Path:** `cim:BaseVoltage.nominalVoltage`  
**Name:** C:301:EQBD:BaseVoltage.nominalVoltage:valueRange  
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

### eqbd:BoundaryPoint.fromEndIsoCode-valueValidity

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
**Name:** C:301:EQBD:BoundaryPoint.fromEndIsoCode:valueValidity  
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

### eqbd:BoundaryPoint.fromEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
**Name:** C:301:EQBD:BoundaryPoint.fromEndIsoCode:stringLength  
The length of the string is 2 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is not 2 characters."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 

### eqbd:BoundaryPoint.fromEndName-stringLength

**Path:** `cim100:BoundaryPoint.fromEndName`  
**Name:** C:301:EQBD:BoundaryPoint.fromEndName:stringLength  
A human readable name with length of the string 64 characters maximum. 

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.fromEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.fromEndNameTso`  
**Name:** C:301:EQBD:BoundaryPoint.fromEndNameTso:stringLength  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.toEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.toEndIsoCode`  
**Name:** C:301:EQBD:BoundaryPoint.toEndIsoCode:stringLength  
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
**Name:** C:301:EQBD:BoundaryPoint.toEndIsoCode:valueValidity  
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
**Name:** C:301:EQBD:BoundaryPoint.toEndName:stringLength  
A human readable name with length of the string 64 characters maximum. 

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eqbd:BoundaryPoint.toEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.toEndNameTso`  
**Name:** C:301:EQBD:BoundaryPoint.toEndNameTso:stringLength  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

