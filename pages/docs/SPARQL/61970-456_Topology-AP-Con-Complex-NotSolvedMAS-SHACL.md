# 61970-456_Topology-AP-Con-Complex-NotSolvedMAS-SHACL

## tp456n:Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Switch
- targetClass: cim:Disconnector
- targetClass: cim:Jumper
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Cut
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch

**Nested Properties:**

### tp456n:Switch-sameTopologicalNode

**Path:** `cim:Switch.retained`  
**Name:** C:456:TP:Terminal:switch  
The Terminal-s of the two sides of a retained Switch (Switch.retained=true) or any of its subclasses shall not be connected to the same TopologicalNode.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value ?cntn1 ?tn1
			WHERE {
             $this $PATH ?value .
             ?terminal1 cim:Terminal.ConductingEquipment $this .
             ?terminal1 cim:ACDCTerminal.sequenceNumber 1 .
             OPTIONAL {?terminal1 cim:Terminal.ConnectivityNode ?cn1}.
             OPTIONAL {?terminal1 cim:Terminal.TopologicalNode ?tn1}.
             ?cn1 cim:ConnectivityNode.TopologicalNode ?cntn1 .
             
             ?terminal2 cim:Terminal.ConductingEquipment $this .
             ?terminal2 cim:ACDCTerminal.sequenceNumber 2 .
             OPTIONAL {?terminal2 cim:Terminal.ConnectivityNode ?cn2}.
             OPTIONAL {?terminal2 cim:Terminal.TopologicalNode ?tn2}.
             ?cn2 cim:ConnectivityNode.TopologicalNode ?cntn2 .          
				FILTER (?value=true && (?terminal1!=?terminal2 && (?tn1=?tn2 || ?cntn1=?cntn2))) .
			}
```
  - Messages: `["Terminal-s of retained Switch (or its subclasses) connect same TopologicalNode (ID via cim:ConnectivityNode.TopologicalNode: {?cntn1}; ID via cim:Terminal.TopologicalNode: {?tn1})."]`

