# 61970-301_DiagramLayout-AP-Con-Complex-SHACL

## dl:DiagramObject.IdentifiedObject-additionalValueType

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:TextDiagramObjectDiagramObject

**Nested Properties:**

### dl:DiagramObject.IdentifiedObject-DLvalueType

**Path:** `rdf:type`  
The association end role description stated that: The domain object to which this diagram object is associated. Therefore, the association cannot point to cim:Diagram, cim:DiagramObject, cim:VisibilityLayer, cim:DiagramStyle, cim:DiagramObjectStyle or cim:TextDiagramObject.

**Severity:** sh:Violation

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 

## dl:DiagramObjectPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramObjectPoint

**Nested Properties:**

### dl:DiagramObjectPoint.sequenceNumber-valueRange

**Path:** `cim:DiagramObjectPoint.sequenceNumber`  
The property (attribute) shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

