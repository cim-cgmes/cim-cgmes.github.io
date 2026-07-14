# 61970-600-2_ShortCircuit-AP-Con-Complex-SHACL

## sc600-2:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

**Nested Properties:**

### sc600-2:SeriesCompensator.varistorRatedCurrent-required

**Path:** `cim:SeriesCompensator.varistorRatedCurrent`  
**Name:** C:600:SC:SeriesCompensator.varistorRatedCurrent:required  
The SeriesCompensator.varistorRatedCurrent is requited if SeriesCompensator.varistorPresent is true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }. 
        $this cim:SeriesCompensator.varistorPresent ?varpresent .
        FILTER (!bound(?value) && ?varpresent=true) .        
			}
```
  - Messages: `["The attribute is missing when SeriesCompensator.varistorPresent is true."]`

### sc600-2:SeriesCompensator.varistorVoltageThreshold-required

**Path:** `cim:SeriesCompensator.varistorVoltageThreshold`  
**Name:** C:600:SC:SeriesCompensator.varistorVoltageThreshold:required  
The SeriesCompensator.varistorVoltageThreshold is requited if SeriesCompensator.varistorPresent is true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }. 
        $this cim:SeriesCompensator.varistorPresent ?varpresent .
        FILTER (!bound(?value) && ?varpresent=true) .        
			}
```
  - Messages: `["The attribute is missing when SeriesCompensator.varistorPresent is true."]`

