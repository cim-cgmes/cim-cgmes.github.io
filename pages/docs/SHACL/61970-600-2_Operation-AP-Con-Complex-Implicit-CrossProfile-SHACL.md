# 61970-600-2_Operation-AP-Con-Complex-Implicit-CrossProfile-SHACL

## op452cpi:Control.PowerSystemResource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Control

**Nested Properties:**

### op452cpi:Control.PowerSystemResource-valueType

**Path:** `cim:Control.PowerSystemResource`  
**Name:** Control.PowerSystemResource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:PowerSystemResource` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## op452cpi:Measurement.ACDCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Measurement

**Nested Properties:**

### op452cpi:Measurement.ACDCTerminal-valueType

**Path:** `cim:Measurement.Terminal`  
**Name:** Measurement.ACDCTerminal-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:ACDCTerminal` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## op452cpi:Measurement.PowerSystemResource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Measurement

**Nested Properties:**

### op452cpi:Measurement.PowerSystemResource-valueType

**Path:** `cim:Measurement.PowerSystemResource`  
**Name:** Measurement.PowerSystemResource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:PowerSystemResource` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

