# 61970-600-2_GeographicalLocation-AP-Con-Complex-SHACL

## gl600-2:Location-position

IEC 61968-13 allows both PositionPoint and mainAddress to be exchanged. CGMES requires that PositionPoint is exchanged and mainAddress is not exchanged.

**Severity:** sh:Violation

**Messages:**
- "Either Location.mainAddress is provided or the Location is not referenced by a PositionPoint."

**Targets:**
- targetClass: cim:Location

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[cim:Location.mainAddress] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:0]}] [{[^cim:PositionPoint.Location] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}]]` 

