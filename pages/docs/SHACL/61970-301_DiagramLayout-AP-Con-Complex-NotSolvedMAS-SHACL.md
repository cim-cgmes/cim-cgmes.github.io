# 61970-301_DiagramLayout-AP-Con-Complex-NotSolvedMAS-SHACL

## dl301n:DiagramObject.IdentifiedObject-additionalValueType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TextDiagramObject
- targetClass: cim:DiagramObject

**Nested Properties:**

### dl301n:DiagramObject.IdentifiedObject-GeneratingUnitvalueType

**Path:** `cim:DiagramObject.IdentifiedObject`  
The DiagramObject should link to SynchronousMachine and not GeneratingUnit.

**Severity:** sh:Violation

**Messages:**
- "The association DiagramObject.IdentifiedObject points to a GeneratingUnit and not SynchronousMachine."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:NotConstraintComponent** (Severity: sh:Violation)

  **Constraints:**

  - **sh:ClassConstraintComponent**
    - Class: `cim:GeneratingUnit`

