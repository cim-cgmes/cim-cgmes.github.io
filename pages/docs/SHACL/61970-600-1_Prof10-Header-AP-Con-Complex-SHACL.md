# 61970-600-1_Prof10-Header-AP-Con-Complex-SHACL

## prof10:DiffModel-DY

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DY profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:HasValueConstraintComponent**
    - Value: `http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0`

## prof10:DiffModel-EQ

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

**Nested Properties:**

### prof10:PROF10-EQ

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Info

**Messages:**
- "The EQ does not have reference to EQBD. The file header dependencies cardinalities and types for EQ profile are not according to PROF10."

**Constraints:**

- **sh:HasValueConstraintComponent** (Severity: sh:Info)
  - Value: `http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0` 

## prof10:DiffModel-GL

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

**Nested Properties:**

### prof10:PROF10-GL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
**Name:** C:600:ALL:NA:PROF10  
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

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for OP profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:InConstraintComponent**
    - Values: `[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]`

## prof10:DiffModel-SC

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SC profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:InConstraintComponent**
    - Values: `[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]`

## prof10:FullModel-DL

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

**Nested Properties:**

### prof10:PROF10-DL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DL profile are not according to PROF10."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[http://iec.ch/TC57/ns/CIM/Dynamics-EU/1.0 http://iec.ch/TC57/ns/CIM/Topology-EU/3.0 http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]` 

## prof10:FullModel-EQ

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

**Nested Properties:**

### prof10:PROF10-EQ

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Info

**Messages:**
- "The EQ does not have reference to EQBD. The file header dependencies cardinalities and types for EQ profile are not according to PROF10."

**Constraints:**

- **sh:HasValueConstraintComponent** (Severity: sh:Info)
  - Value: `http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0` 

## prof10:FullModel-GL

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

**Nested Properties:**

### prof10:PROF10-GL

**Path:** `mdc:Model.DependentOn / mdc:Model.profile`  
**Name:** C:600:ALL:NA:PROF10  
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

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for DY profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:HasValueConstraintComponent**
    - Value: `http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0`

## prof10:PROF10-OP

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for OP profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:InConstraintComponent**
    - Values: `[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0]`

## prof10:PROF10-SC

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SC profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:InConstraintComponent**
    - Values: `[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0]`

## prof10:PROF10-SSH

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SSH profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:HasValueConstraintComponent**
    - Value: `http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0`

## prof10:PROF10-SV

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for SV profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:HasValueConstraintComponent**
    - Value: `http://iec.ch/TC57/ns/CIM/Topology-EU/3.0`

## prof10:PROF10-TP

**Name:** C:600:ALL:NA:PROF10  
CGMES instance file (distribution) dependency shall be declared by md:Model.DependentOn in the header according to Figure 1 and the associated rules.

**Severity:** sh:Violation

**Messages:**
- "The file header dependencies cardinalities and types for TP profile are not according to PROF10."

**Targets:**
- sparqlTarget: 

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:HasValueConstraintComponent**
    - Value: `http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU/3.0`

