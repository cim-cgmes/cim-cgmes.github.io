# 61970-600-2_AllProfiles-AP-Con-Complex-SolvedMAS-SHACL

## mas600-2:RegulatingControl

**Severity:** sh:Violation

**Nested Properties:**

### mas600-2:RegulatingControl-samePoint

**Path:** `rdf:type`  
A RegulatingControl will have associations to one or more instances of RegulatingCondEq and an association to a Terminal. The ConnectivityNode associated with the Terminal is the regulated point. It is common to have cases where multiple pieces of equipment regulate ConnectivityNodes that under normal network topology are associated with the same TopologicalNode. In this case, the same instance of RegulatingControl should be used by all of those regulating equipment if possible. If it is not possible, such as the case where a SynchronousMachine and a RatioTapChanger are regulating the same point using associations to instances of RegulatingControl and TapChangerControl, the number of instances of RegulatingControl and TapChangerControl should be minimized. Additionally, the target and deadband values for the same regulated point should not be contradictory. Profile restriction: If multiple instances of RegulatingControl control the same regulation point, the targetValues must not be contradictory.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

    	SELECT $this ?count ?value ?rcfail
			WHERE {
          $this ^cim:Terminal.TopologicalNode/^cim:RegulatingControl.Terminal ?rcfail .
          ?rcfail cim:RegulatingControl.targetValue ?value .
      {
      SELECT $this (count(distinct ?val) as ?count)
      WHERE {
             $this ^cim:Terminal.TopologicalNode/^cim:RegulatingControl.Terminal ?rc .
             ?rc cim:RegulatingControl.enabled true .
             ?rc cim:RegulatingControl.mode ?mode .
             ?rc cim:RegulatingControl.targetValue ?val .   
      }
      GROUP BY $this ?mode
			}
      }
      HAVING (?count>1)
      #LIMIT 1
      
```
  - Messages: `["Enabled RegulatingControl-s of the same type associated with the same TopologicalNode have different target values. RegulatingControl ID: {?rcfail}."]`

## mas600-2:RegulatingControlPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl
- targetClass: cim:TapChangerControl

**Nested Properties:**

### mas600-2:RegulatingControl-point

**Path:** `rdf:type`  
The controlled point and the controlling equipment shall be located in the same TopologicalIsland. In cases where the controlling point is a TopologicalNode only one RegulatingControl shall be instantiated following the terms of constraint C:452:EQ:RegulatingControl:samePoint.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

    	SELECT $this ?topislandterminal ?topislandterminalratio ?topislandterminalphase ?topislandterminalcondeq
			WHERE {
          $this cim:RegulatingControl.enabled true .
          $this cim:RegulatingControl.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topislandterminal .
          #BIND(EXISTS{$this cim:RegulatingControl.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?tnisland } AS ?tni).
          OPTIONAL {$this ^cim:TapChanger.TapChangerControl/cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topislandterminalratio}.
          OPTIONAL {$this ^cim:TapChanger.TapChangerControl/cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topislandterminalphase}.
          OPTIONAL {$this ^cim:RegulatingCondEq.RegulatingControl/^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topislandterminalcondeq}.
          ##FILTER ( ?tni=true && ((bound(?topislandterminalratio) && !bound(?topislandterminalphase) && !bound(?topislandterminalcondeq) && ?topislandterminalratio!=?topislandterminal) ||
          #(!bound(?topislandterminalratio) && bound(?topislandterminalphase) && !bound(?topislandterminalcondeq) && ?topislandterminalphase!=?topislandterminal) ||
          #(!bound(?topislandterminalratio) && !bound(?topislandterminalphase) && bound(?topislandterminalcondeq) && ?topislandterminalcondeq!=?topislandterminal) )).
          FILTER ( ((bound(?topislandterminalratio) && !bound(?topislandterminalphase) && !bound(?topislandterminalcondeq) && ?topislandterminalratio!=?topislandterminal) ||
          (!bound(?topislandterminalratio) && bound(?topislandterminalphase) && !bound(?topislandterminalcondeq) && ?topislandterminalphase!=?topislandterminal) ||
          (!bound(?topislandterminalratio) && !bound(?topislandterminalphase) && bound(?topislandterminalcondeq) && ?topislandterminalcondeq!=?topislandterminal) )
          ).
      } 
```
  - Messages: `["The controlled point and the controlling equipment are not located in the same TopologicalIsland. TopologicalIsland ID (via RegulatingControl.Terminal):{?topislandterminal} TopologicalIsland ID (via RatioTapChanger):{?topislandterminalratio} TopologicalIsland ID (via PhaseTapChanger):{?topislandterminalphase} TopologicalIsland ID (via ConductingEquipment):{?topislandterminalcondeq}."]`

