# 61970-600_Topology-AP-Con-Complex-NotSolvedMAS-SHACL

## tp600n:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Terminal

**Nested Properties:**

### tp600n:Terminal-EXCH8TopologicalNode

**Path:** `rdf:type`  
**Name:** C:600:EQ:Terminal:EXCH8TopologicalNode  
The association end Terminal.TopologicalNode is required in cases where a RegulatingControl is associated with a Terminal.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this 
			WHERE {
             #OPTIONAL {$this ^cim:RegulatingControl.Terminal ?rc}.
             #OPTIONAL {$this cim:Terminal.TopologicalNode ?value}.
             #BIND(EXISTS{$this ^cim:RegulatingControl.Terminal/cim:RegulatingControl.enabled true} AS ?enable).
             BIND(EXISTS{$this ^cim:RegulatingControl.Terminal ?rc} AS ?rctrue).
             BIND(EXISTS{$this cim:Terminal.TopologicalNode ?v} AS ?val).
             #$this cim:Terminal.TopologicalNode ?value .
				#FILTER (!bound(?value) && bound(?rc)) .
        #FILTER (?val=false && ?enable=true) .
        FILTER (?val=false && ?rctrue=true) .
			}
```
  - Messages: `["The Terminal is referenced by a RegulatingControl but is not associated with a TopologicalNode."]`

