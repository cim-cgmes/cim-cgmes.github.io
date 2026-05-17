# 61970-301_ShortCircuit-AP-Con-Complex-NotSolvedMAS-SHACL

## sc301n:MutualCoupling

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MutualCoupling

**Nested Properties:**

### sc301n:MutualCoupling-terminalsAssignment

**Path:** `rdf:type`  
Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?typeline1 ?typeline2
			WHERE {
        #$this cim:MutualCoupling.First_Terminal ?firstterminal .
        #$this cim:MutualCoupling.Second_Terminal ?secondterminal .
        #?firstterminal cim:Terminal.ConductingEquipment ?line1 . 
        #?secondterminal cim:Terminal.ConductingEquipment ?line2 . 
        $this cim:MutualCoupling.First_Terminal/cim:Terminal.ConductingEquipment ?line1 .
        $this cim:MutualCoupling.Second_Terminal/cim:Terminal.ConductingEquipment ?line2 .
        ?line1 rdf:type ?typeline1 .
        ?line2 rdf:type ?typeline2 .
				FILTER (?typeline1 NOT IN (cim:ACLineSegment, cim:Equipment) || ?typeline2 NOT IN (cim:ACLineSegment, cim:Equipment) || ?line1=?line2) .
			}
```
  - Messages: `["The terminals are either not related to ACLineSegment or the first and the second terminal associations are not pointing to different ACLineSegments. Type line 1: {?typeline1}. Type line 2: {?typeline2}."]`

