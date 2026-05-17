# 61970-453_DiagramLayout-AP-Con-Complex-Implicit-CrossProfile-SHACL

## dl453cpi:DiagramObject.IdentifiedObject

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramObject

**Nested Properties:**

### dl453cpi:DiagramObject.IdentifiedObject-valueType

**Path:** `cim:DiagramObject.IdentifiedObject`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class IdentifiedObject or its subclass."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:IdentifiedObject` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

