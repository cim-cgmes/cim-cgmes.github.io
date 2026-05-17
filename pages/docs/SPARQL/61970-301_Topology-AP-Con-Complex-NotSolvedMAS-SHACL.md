# 61970-301_Topology-AP-Con-Complex-NotSolvedMAS-SHACL

## tp301n:Terminal.phases

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### tp301n:Terminal.phases-consistencyTopologicalNode

**Path:** `rdf:type`  
The phase code on terminals connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two terminals shall be consistent.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value2 ?terms ?value1 ?value
			WHERE {
        {
        SELECT $this (COUNT(?typeterm) AS ?terms) ?value
        WHERE {
        $this ^cim:Terminal.TopologicalNode  ?value.
        ?value rdf:type ?typeterm .
        #FILTER (?typeterm=cim:Terminal).
        }
        GROUP BY $this ?typeterm ?value
        HAVING (?terms>1)
        }
      
        $this ^cim:Terminal.TopologicalNode ?term2  .
        ?value cim:Terminal.phases ?value1  .
        OPTIONAL {?term2 cim:Terminal.phases ?value2 } .
        
        #?term1 cim:Terminal.TopologicalNode $this  .
        #OPTIONAL {?term1 cim:Terminal.phases ?value2 } .
        #?term2 cim:Terminal.TopologicalNode $this  .
        #OPTIONAL {?term2 cim:Terminal.phases ?value1 } .        
        #FILTER ((?terms>1 && bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N) && (?value2!=cim:PhaseCode.ABCN && ?value2!=cim:PhaseCode.N)) ||
        #(?terms>1 && bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABC) && (?value2!=cim:PhaseCode.ABC)) ||
        #(?terms>1 && !bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N))
        #) .
        FILTER ((?value!=?term2 && bound(?value2) && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N) && (?value2!=cim:PhaseCode.ABCN && ?value2!=cim:PhaseCode.N)) ||
        (?value!=?term2 && bound(?value2) && (?value1=cim:PhaseCode.ABC) && (?value2!=cim:PhaseCode.ABC)) ||
        (?value!=?term2 && !bound(?value2) && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N))
        ) .
			}
```
  - Messages: `["The phase codes for the connected terminals are not consistent. Terminal 1 code:{?value1} Terminal 2 code: {?value2}."]`

