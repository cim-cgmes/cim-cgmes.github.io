# 61970-600-1_AllProfiles-AP-Con-Complex-SolvedMAS-SHACL

## mas600:DanglingReferences

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:DanglingReferences

**Nested Properties:**

### mas600:All-DanglingReferences

**Path:** `rdf:type`  
The CGMES requires that at the receiving end of the exchange all references in the instance files pointing to instance files from other profiles which are part of the exchange should be satisfied. Therefore, the complete set of instance files necessary for the grid model shall have fulfilled references (no dangling references are allowed).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value ?s 
			WHERE {
        #?s !(rdf:type | md:Model.DependentOn | md:Model.Supersedes) ?value .
        ?s !rdf:type ?value .
        BIND (str(?value) AS ?strvalue).
        #OPTIONAL{?s (!rdf:type)/rdf:type ?v} .
        #OPTIONAL{?value  rdf:type ?v}.
        
        #FILTER(!isLiteral(?value) && CONTAINS(str(?value),"_") &&
        #      !CONTAINS(str(?value),"FullModel") && !CONTAINS(str(?value),"DifferenceModel")).
        #FILTER(!isLiteral(?value) && !STRSTARTS(str(?value),"urn:uuid:") && (CONTAINS(str(?value),"#_") || STRLEN(STRAFTER(str(?value),"#"))<=1) &&
        #      !CONTAINS(str(?value),"FullModel") && !CONTAINS(str(?value),"DifferenceModel") ).  
        FILTER(isIRI(?value) && (CONTAINS(?strvalue,"#_") || STRSTARTS(?strvalue,"urn:uuid:") || STRENDS(?strvalue,"#"))).              
        #OPTIONAL{?value  rdf:type ?v}.
        #FILTER (!bound(?v) ).
        FILTER NOT EXISTS {?value rdf:type ?v }.
			}
```
  - Messages: `["Dangling reference is present in the model. The ID of the class is: {?s}."]`

## mas600:SvShuntCompensatorSections

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### mas600:SvShuntCompensatorSections.sections-SV__4

**Path:** `cim:ShuntCompensator.sections`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value ?svshuntsec
			WHERE {
        $this ^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService true .
        $this cim:RegulatingCondEq.controlEnabled ?controlen .
        $this  ^cim:SvShuntCompensatorSections.ShuntCompensator/cim:SvShuntCompensatorSections.sections  ?svshuntsec .
        $this $PATH ?value .
        OPTIONAL {$this  cim:RegulatingCondEq.RegulatingControl/cim:RegulatingControl.enabled ?rcenabled} .
        #OPTIONAL {$this  ^cim:SvShuntCompensatorSections.ShuntCompensator/cim:SvShuntCompensatorSections.sections  ?svshuntsec} .
        #FILTER (bound(?svshuntsec) && ((?controlen=false && ?svshuntsec!=?value) || (bound(?rcenabled) && ?rcenabled=false && ?svshuntsec!=?value) )  ).
        FILTER ((?controlen=false && ?svshuntsec!=?value) || (bound(?rcenabled) && ?rcenabled=false && ?svshuntsec!=?value)   ).
			}
```
  - Messages: `["SvShuntCompensatorSections.sections is not the same as ShuntCompensator.sections for non-regulating ShuntCompensator. SvShuntCompensatorSections.sections is: {?svshuntsec}; ShuntCompensator.sections is: {?value}."]`

### mas600:SvShuntCompensatorSections-SV__4

**Path:** `rdf:type`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value 
			WHERE {
        $this ^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService true .
        $this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland.
        $this rdf:type ?value .
        #OPTIONAL {$this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        OPTIONAL {$this  ^cim:SvShuntCompensatorSections.ShuntCompensator  ?svshuntcompsec} .
        #FILTER (bound(?topologicalisland) && !bound(?svshuntcompsec)  ).
        FILTER (!bound(?svshuntcompsec)  ).
			}
```
  - Messages: `["SvShuntCompensatorSections is not instantiated for a ShuntCompensator (or any of the subtypes) connected to a TopologicalNode which is referenced by a TopologicalIsland."]`

## mas600:SvStatus

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalIsland

**Nested Properties:**

### mas600:SvStatus-SV__4

**Path:** `rdf:type`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value 
			WHERE {
        $this cim:TopologicalIsland.TopologicalNodes ?tn.
        ?tn ^cim:ConnectivityNode.TopologicalNode/^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment ?value.
        OPTIONAL {?value  ^cim:SvStatus.ConductingEquipment  ?svstatus} .
        #$this rdf:type ?value .
        #OPTIONAL {$this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        #OPTIONAL {$this  ^cim:SvStatus.ConductingEquipment  ?svstatus} .
        #FILTER (bound(?topologicalisland) && !bound(?svstatus) && ?value!=cim:Equipment ).
        FILTER (!bound(?svstatus) && ?value!=cim:Equipment ).
			}
```
  - Messages: `["SvStatus is not instantiated for a ConductingEquipment connected to a TopologicalNode which is referenced by a TopologicalIsland."]`

## mas600:SvSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Switch
- targetClass: cim:GroundDisconnector
- targetClass: cim:Jumper
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:Disconnector
- targetClass: cim:Cut
- targetClass: cim:Fuse
- targetClass: cim:Breaker

**Nested Properties:**

### mas600:SvSwitch-SV__4

**Path:** `rdf:type`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value 
			WHERE {
        $this ^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService true .
        $this cim:Switch.retained true .
        $this rdf:type ?value .
        $this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland.
        #OPTIONAL {$this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        OPTIONAL {$this  ^cim:SvSwitch.Switch  ?svswitch} .
        #FILTER (bound(?topologicalisland) && !bound(?svswitch)  ).
        FILTER (!bound(?svswitch)  ).
			}
```
  - Messages: `["SvSwitch is not instantiated for a retained Switch (or any of the subtypes) connected to a TopologicalNode which is referenced by a TopologicalIsland."]`

## mas600:SvTapStep

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular

**Nested Properties:**

### mas600:SvTapStep.position-SV__4

**Path:** `cim:TapChanger.step`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value ?svtapsteppos
			WHERE {
        $this (cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.PowerTransformer/^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService)|(cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.PowerTransformer/^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService) true .
        $this cim:TapChanger.controlEnabled ?controlen .
        $this  ^cim:SvTapStep.TapChanger/cim:SvTapStep.position  ?svtapsteppos.
        $this $PATH ?value .
        OPTIONAL {$this  cim:TapChanger.TapChangerControl/cim:RegulatingControl.enabled ?rcenabled} .
        #OPTIONAL {$this  ^cim:SvTapStep.TapChanger/cim:SvTapStep.position  ?svtapsteppos} .
        #FILTER (bound(?svtapsteppos) && ((?controlen=false && ?svtapsteppos!=?value) || (bound(?rcenabled) && ?rcenabled=false && ?svtapsteppos!=?value) )  ).
        FILTER ((?controlen=false && ?svtapsteppos!=?value) || (bound(?rcenabled) && ?rcenabled=false && ?svtapsteppos!=?value)  ).
			}
```
  - Messages: `["SvTapStep.position is not the same as TapChanger.step for non-regulating TapChanger. SvTapStep.position is: {?svtapsteppos}; TapChanger.step is: {?value}."]`

### mas600:SvTapStep-SV__4

**Path:** `rdf:type`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  DISTINCT $this ?value 
			WHERE {
        $this (cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.PowerTransformer/^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService)|(cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.PowerTransformer/^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService) true .
        $this  (cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes)|(cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes)  ?topologicalisland .
        $this rdf:type ?value .
        #OPTIONAL {$this cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        #OPTIONAL {$this cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        OPTIONAL {$this  ^cim:SvTapStep.TapChanger  ?svtapstep} .
        #FILTER (bound(?topologicalisland) && !bound(?svtapstep)  ).
        FILTER (!bound(?svtapstep)  ).
			}
```
  - Messages: `["SvTapStep is not instantiated for a RatioTapChanger or PhaseTapChanger (or any of the subtypes)  connected to a TopologicalNode which is referenced by a TopologicalIsland."]`

## mas600:SvVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### mas600:SvVoltage-SV__4

**Path:** `rdf:type`  
All state variables shall be instantiated in the SV instance file (distribution) for all energized elements part of a TopologicalIsland independently of the regulating status of the elements (e.g. for a shunt compensator that is not regulating the SvShuntCompensatorSections.sections shall be the same as ShuntCompensator.sections). All instances shall be representing computed values obtained from a power flow calculation. For SvPowerFlow instances refer to profile constraint on the SvPowerFlow class.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX md: <http://iec.ch/TC57/61970-552/ModelDescription/1#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this
			WHERE {
        $this  ^cim:TopologicalIsland.TopologicalNodes ?topologicalisland.
        #OPTIONAL {$this  ^cim:TopologicalIsland.TopologicalNodes ?topologicalisland}.
        OPTIONAL {$this  ^cim:SvVoltage.TopologicalNode ?svvoltage} .

        FILTER (!bound(?svvoltage)).
        #FILTER (bound(?topologicalisland) && !bound(?svvoltage)).
			}
```
  - Messages: `["SvVoltage is not instantiated for a TopologicalNode which is referenced by a TopologicalIsland."]`

