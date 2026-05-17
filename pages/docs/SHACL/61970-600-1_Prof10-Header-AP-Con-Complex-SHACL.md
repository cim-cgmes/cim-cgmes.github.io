# 61970-600-1_Prof10-Header-AP-Con-Complex-SHACL

## prof10:DiffModel-DY

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DY profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:HasValueConstraintComponent map[Value:http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0]}]]` 

## prof10:DiffModel-EQ

**Severity:** sh:Violation

**Nested Properties:**

### prof10:PROF10-EQ

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Info

**Messages:**
- "The EQ does not have reference to EQBD. The file header dependencies cardinalities and types for EQ profile are not according to PROF10."

**Constraints:**

- **sh:HasValueConstraintComponent** (Severity: sh:Info)
  - Value: `http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0` 

## prof10:DiffModel-GL

**Severity:** sh:Violation

**Nested Properties:**

### prof10:PROF10-GL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for GL profile are not according to PROF10."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]` 

## prof10:DiffModel-OP

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for OP profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:InConstraintComponent map[Values:[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]]}]]` 

## prof10:DiffModel-SC

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SC profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:InConstraintComponent map[Values:[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]]}]]` 

## prof10:FullModel-DL

**Severity:** sh:Violation

**Nested Properties:**

### prof10:PROF10-DL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DL profile are not according to PROF10."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[http://iec.ch/TC57/ns/CIM/Dynamics-EU/1.0 http://iec.ch/TC57/ns/CIM/Topology-EU/3.0 http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]` 

## prof10:FullModel-EQ

**Severity:** sh:Violation

**Nested Properties:**

### prof10:PROF10-EQ

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Info

**Messages:**
- "The EQ does not have reference to EQBD. The file header dependencies cardinalities and types for EQ profile are not according to PROF10."

**Constraints:**

- **sh:HasValueConstraintComponent** (Severity: sh:Info)
  - Value: `http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0` 

## prof10:FullModel-GL

**Severity:** sh:Violation

**Nested Properties:**

### prof10:PROF10-GL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for GL profile are not according to PROF10."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]` 

## prof10:PROF10-DY

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DY profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:HasValueConstraintComponent map[Value:http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0]}]]` 

## prof10:PROF10-OP

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for OP profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:InConstraintComponent map[Values:[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]]}]]` 

## prof10:PROF10-SC

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SC profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:InConstraintComponent map[Values:[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]]}]]` 

## prof10:PROF10-SSH

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SSH profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:HasValueConstraintComponent map[Value:http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0]}]]` 

## prof10:PROF10-SV

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SV profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]} {[mdc:Model.DependentOn] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:HasValueConstraintComponent map[Value:http://iec.ch/TC57/ns/CIM/Topology-EU/3.0]}]]` 

## prof10:PROF10-TP

CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for TP profile are not according to PROF10."

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[mdc:Model.DependentOn] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}] [{[mdc:Model.DependentOn mdc:Model.profile] sh:Violation    sh:HasValueConstraintComponent map[Value:http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU/3.0]}]]` 

