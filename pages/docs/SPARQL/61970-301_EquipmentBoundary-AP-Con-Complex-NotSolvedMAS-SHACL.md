# 61970-301_EquipmentBoundary-AP-Con-Complex-NotSolvedMAS-SHACL

## eqbd301n:BoundaryPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim100:BoundaryPoint

**Nested Properties:**

### eqbd301n:BoundaryPoint.isExcludedFromAreaInterchange-requiredTieFlow

**Path:** `cim100:BoundaryPoint.isExcludedFromAreaInterchange`  
**Name:** C:301:EQBD:BoundaryPoint.isExcludedFromAreaInterchange:requiredTieFlow  
If true, this boundary point is on the interconnection that is excluded from control area interchange calculation and consequently has no related tie flows. Otherwise, the interconnection is included in control area interchange and a TieFlow is required at all sides of the boundary point (default).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value ?terminal ?tieflow
			WHERE {
             ?terminal1 cim:Terminal.ConductingEquipment ?condeq .
             ?terminal1 cim:ACDCTerminal.sequenceNumber 1 .
             ?terminal1 cim:Terminal.ConnectivityNode ?cn1 .
             
             OPTIONAL {?terminal2 cim:Terminal.ConductingEquipment ?condeq}.
             OPTIONAL {?terminal2 cim:ACDCTerminal.sequenceNumber 2}.
             OPTIONAL {?terminal2 cim:Terminal.ConnectivityNode ?cn2}.
             
             OPTIONAL {$this $PATH ?value}.
             $this eu:BoundaryPoint.ConnectivityNode ?cnbp .
             OPTIONAL {?terminal cim:Terminal.ConnectivityNode ?cnbp }.
             OPTIONAL {?tieflow cim:TieFlow.Terminal ?terminal }.
           
				FILTER ((bound(?value) && ?value=false && !bound(?tieflow) && (?cnbp=?cn1 || ?cnbp=?cn2) && bound(?terminal1) && bound(?terminal2) && ?cn1!=?cn2 && (?terminal=?terminal1 || ?terminal=?terminal2)) || (!bound(?value) && !bound(?tieflow) && (?cnbp=?cn1 || ?cnbp=?cn2) && bound(?terminal1) && bound(?terminal2) && ?cn1!=?cn2 && (?terminal=?terminal1 || ?terminal=?terminal2))|| (bound(?value) && ?value=true && bound(?tieflow) && (?cnbp=?cn1 || ?cnbp=?cn2) && bound(?terminal1) && bound(?terminal2) && ?cn1!=?cn2 && (?terminal=?terminal1 || ?terminal=?terminal2))) .
			}
```
  - Messages: `["There is either TieFlow modelled in case the value is true or there are no TieFlow modelled in case the value is false. Id of the Terminal: {?terminal}. ID of the TieFlow: {?tieflow}."]`

