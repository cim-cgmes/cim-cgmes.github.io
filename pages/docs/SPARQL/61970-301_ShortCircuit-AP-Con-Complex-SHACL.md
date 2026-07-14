# 61970-301_ShortCircuit-AP-Con-Complex-SHACL

## sc:MutualCoupling

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MutualCoupling

## sc:PetersenCoil

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PetersenCoil

## sc:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

## sc:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

**Nested Properties:**

### sc:SeriesCompensator.varistorRatedCurrent-usage

**Path:** `cim:SeriesCompensator.varistorRatedCurrent`  
**Name:** C:301:SC:SeriesCompensator.varistorRatedCurrent:usage  
It is used for short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }. 
        $this cim:SeriesCompensator.varistorPresent ?varpresent .
        FILTER (bound(?value) && ?varpresent=false) .        
			}
```
  - Messages: `["The attribute is present and SeriesCompensator.varistorPresent is false."]`

### sc:SeriesCompensator.varistorVoltageThreshold-usage

**Path:** `cim:SeriesCompensator.varistorVoltageThreshold`  
**Name:** C:301:SC:SeriesCompensator.varistorVoltageThreshold:usage  
It is used for short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }. 
        $this cim:SeriesCompensator.varistorPresent ?varpresent .
        FILTER (bound(?value) && ?varpresent=false) .        
			}
```
  - Messages: `["The attribute is present and SeriesCompensator.varistorPresent is false."]`

