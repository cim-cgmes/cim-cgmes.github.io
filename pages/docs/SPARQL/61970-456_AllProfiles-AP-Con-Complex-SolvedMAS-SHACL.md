# 61970-456_AllProfiles-AP-Con-Complex-SolvedMAS-SHACL

## mas456sol:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:AngleReference

**Nested Properties:**

### mas456sol:Model-angleReference

**Path:** `rdf:type`  
Angle reference: In cases where it is required to exchange a solved model and compare power flow results (assuming identical/comparable calculation methods and initial conditions) it is required that the angle reference slack is placed within the exported model. The slack generator is the SynchronousMachine connected to the TopologicalNode referenced by TopologicalIsland.AngleRefTopologicalNode and which has the highest SynchronousMachine.referencePriority in the exported MAS’s SSH.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

    	SELECT $this ?sm1 ?tn ?value ?tn1
			WHERE {
          {
          #SELECT $this (COUNT(?smrp) as ?count)
          SELECT $this (COUNT(?type) as ?count)
          WHERE {
              #?sm cim:SynchronousMachine.referencePriority ?smrp .
              ?sm cim:SynchronousMachine.referencePriority 1 .
              ?sm rdf:type cim:SynchronousMachine .
              ?sm rdf:type ?type .
              #FILTER (?smrp=1).
            }
            GROUP BY $this ?type
          }
          ?sm1 cim:SynchronousMachine.referencePriority 1 .
          ?sm1 rdf:type cim:SynchronousMachine .
          
          
          OPTIONAL {?sm1 ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode ?tn .
                    ?tn ^cim:TopologicalIsland.TopologicalNodes ?ti .
                    }.
          OPTIONAL {?ti2 cim:TopologicalIsland.AngleRefTopologicalNode ?tn1 .
                     ?tn1 ^cim:TopologicalIsland.TopologicalNodes ?ti1 .
                     }.
          
          #OPTIONAL {?sm1 ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?ti }.
          #OPTIONAL {?ti cim:TopologicalIsland.AngleRefTopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?ti1 .
          
          #OPTIONAL {?tn ^cim:TopologicalIsland.TopologicalNodes ?ti }.
          #OPTIONAL {?tn1 ^cim:TopologicalIsland.TopologicalNodes ?ti1 }.
          
          BIND("" as ?value).
      
          FILTER (?count!=1 || !bound(?ti) || !bound(?ti1) || (bound(?ti) && bound(?ti1) && ?ti!=?ti1)).
      } 
      LIMIT 1
      
```
  - Messages: `["The angle reference slack is located outside the model or the SynchronousMachine with the highest SynchronousMachine.referencePriority (ID: {?sm1}) is not in the SSH or the TopologicalNode (ID: {?tn}) is not the one referenced by TopologicalIsland.AngleRefTopologicalNode (TopologicalNode ID: {?tn1}) or there are multiple machines with SynchronousMachine.referencePriority=1."]`

