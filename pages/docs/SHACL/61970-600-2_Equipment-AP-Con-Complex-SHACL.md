# 61970-600-2_Equipment-AP-Con-Complex-SHACL

## eq600-2:GeographicalRegionCountShape

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:GeographicalRegion

**Nested Properties:**

### eq600-2:GeographicalRegion-EQ__4

**Path:** `^rdf:type`  
**Name:** C:600:EQ:GeographicalRegion:EQ__4  
Only one GeographicalRegion shall be exchanged per MAS. In case multiple Model Authority have a need to have the same GeographicalRegion (i.e. multiple TSOs in a country) the class GeographicalRegion shall be present in all Model Authority models and shall have different rdf:ID, but can have same name/description. There is no specific naming convention defined. Note that this is mainly applicable for exchanging transmission data. Additional clarifications when dealing with distribution data are not defined currently.

**Severity:** sh:Violation

**Messages:**
- "Muliple GeographicalRegion-s are present."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq600-2:ReactiveCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ReactiveCapabilityCurve

## eq600-2:RotatingMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### eq600-2:RotatingMachine.ratedS-required

**Path:** `cim:RotatingMachine.ratedS`  
**Name:** C:600:EQ:RotatingMachine.ratedS:required  
RotatingMachine.ratedS is required.

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq600-2:SubstationCountShape

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:SubstationCount

## eq600-2:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:PhaseTapChangerSymmetrical

