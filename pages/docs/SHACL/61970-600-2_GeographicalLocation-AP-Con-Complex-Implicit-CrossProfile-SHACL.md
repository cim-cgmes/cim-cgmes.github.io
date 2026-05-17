# 61970-600-2_GeographicalLocation-AP-Con-Complex-Implicit-CrossProfile-SHACL

## gl13cpi:Location.PowerSystemResources

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Location

**Nested Properties:**

### gl13cpi:Location.PowerSystemResources-valueType

**Path:** `cim:Location.PowerSystemResources`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:PowerSystemResource` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

