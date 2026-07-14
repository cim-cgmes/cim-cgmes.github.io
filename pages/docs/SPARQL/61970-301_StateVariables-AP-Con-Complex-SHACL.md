# 61970-301_StateVariables-AP-Con-Complex-SHACL

## sv:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### sv:CsConverter.alpha-valueRangeTypical

**Path:** `cim:CsConverter.alpha`  
**Name:** C:301:SV:CsConverter.alpha:valueRangeTypical  
Typical value between 10 degrees and 18 degrees for a rectifier. 

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.rectifier .
        $this $PATH ?value .
        FILTER (?value<10 || ?value>18) .        
			}
```
  - Messages: `["The value is outside the range: 10-18 degrees."]`

### sv:CsConverter.gamma-valueRangeTypical

**Path:** `cim:CsConverter.gamma`  
**Name:** C:301:SV:CsConverter.gamma:valueRangeTypical  
Typical value between 17 degrees and 20 degrees for an inverter. 

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.inverter .
        $this $PATH ?value .
        FILTER (?value<17 || ?value>20) .        
			}
```
  - Messages: `["The value is outside the range: 17-20 degrees."]`

## sv:SvShuntCompensatorSections

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvShuntCompensatorSections

## sv:SvVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvVoltage

## sv:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

