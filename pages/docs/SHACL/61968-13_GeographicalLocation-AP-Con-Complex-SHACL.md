# 61968-13_GeographicalLocation-AP-Con-Complex-SHACL

## gl:CoordinateSystem

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CoordinateSystem

**Nested Properties:**

### gl:CoordinateSystem.crsUrn-epsg

**Path:** `cim:CoordinateSystem.crsUrn`  
**Name:** C:13:GL:CoordinateSystem.crsUrn:epsg  
CoordinateSystem.crsUrn: If not specified elsewhere, the CoordinateSystem.crsUrn uses WGS84 (latitude, longitude), i.e. urn:ogc:def:crs:EPSG::4326.

**Severity:** sh:Info

**Messages:**
- "The value is different from the default value: urn:ogc:def:crs:EPSG::4326."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Info)
  - Values: `[urn:ogc:def:crs:EPSG::4326]` 

