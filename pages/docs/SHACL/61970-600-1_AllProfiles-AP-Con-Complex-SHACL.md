# 61970-600-1_AllProfiles-AP-Con-Complex-SHACL

## all600:Float

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:FloatSpecialValues

## all600:FullModel

**Severity:** sh:Violation

**Constraints:**

- **sh:OrConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[sh:targetNode mdc:FullModel sh:targetNode diff:DifferenceModel]` 

**Nested Properties:**

### all600:All-HGEN2

**Path:** `^rdf:type`  
**Name:** C:600:ALL:NA:HGEN2  
Each type of instance file (full or difference) shall have a file header. (IEC 61970-552:2016, Subclause 5.1)

**Severity:** sh:Violation

**Messages:**
- "File header is missing."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## all600:FullModelDateTime

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

## all600:FullModelProf11

**Severity:** sh:Violation

**Targets:**
- targetClass: diff:DifferenceModel
- targetClass: mdc:FullModel

**Nested Properties:**

### all600:Model.profile-allowedValues

**Path:** `mdc:Model.profile`  
**Name:** C:600:ALL:Model.profile:allowedValues  
The respective profile URI shall be declared in the file header. If the profile URI is not included in the header, all classes/attributes/associations part of the undeclared profile are considered optional. Therefore, the profile references in the file header specify which profiles validation the instance file data is valid for. The instance data file (distribution) can contain data from multiple profiles (such as Short-Circuit or Operation) without being declared in the header profile references. However, the data belonging to non-declared profiles does not need to be imported and re-exported as the profiles are not defined in the file header. The user shall be informed if the data is not imported. (refer also to R:452:ALL:NA:exchange3 and R:452:ALL:NA:exchange4)

**Severity:** sh:Violation

**Messages:**
- "The model does not include any of the  md:Model.profile defined for CGMES."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0 http://iec.ch/TC57/ns/CIM/Operation-EU/3.0 http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0 http://iec.ch/TC57/ns/CIM/DiagramLayout-EU/3.0 http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU/3.0 http://iec.ch/TC57/ns/CIM/Topology-EU/3.0 http://iec.ch/TC57/ns/CIM/StateVariables-EU/3.0 http://iec.ch/TC57/ns/CIM/Dynamics-EU/1.0 http://iec.ch/TC57/ns/CIM/GeographicalLocation-EU/3.0 http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0]` 

## all600:IDuniqueness

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:IDuniqueness

## all600:IDuuidCheck

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:IDchecks

## all600:MarpRule

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

