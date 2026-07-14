# 61970-301_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL

## ssh301n:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

## ssh301n:ControlArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ControlArea

**Nested Properties:**

### ssh301n:ControlArea-netInterchangeCalculation

**Path:** `rdf:type`  
**Name:** C:301:SSH:ControlArea:netInterchangeCalculation  
Control area constraints in power flow are represented as a set of area control equality constraints of the form: Control Area Net Interchange = SUM (control area flow into the area on each tie)

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value ?sump
			WHERE {
        $this cim:ControlArea.type cim:ControlAreaTypeKind.Interchange .
        $this cim:ControlArea.netInterchange ?value .
        {
        SELECT $this (SUM(?p) AS ?sump)
        WHERE {
              ?term ^cim:TieFlow.Terminal/cim:TieFlow.ControlArea $this  .
              ?term cim:Terminal.ConnectivityNode/^eu:BoundaryPoint.ConnectivityNode/rdf:type eu:BoundaryPoint .
              ?term cim:Terminal.ConductingEquipment/rdf:type cim:EquivalentInjection .
              ?term rdf:type ?termtype.
              ?term cim:Terminal.ConductingEquipment/cim:EquivalentInjection.p ?p .
          }
        GROUP BY $this ?termtype
        }
        FILTER (?value!=?sump) .
			} 
```
  - Messages: `["The sum of the EquivalentInjections which are connected to the BoundaryPoint-s differes from the ControlArea.netInterchange. ControlArea.netInterchange= {?value}. Sum of the EquivalentInjections= {?sump}."]`

## ssh301n:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### ssh301n:CsConverter.targetAlpha-applicability

**Path:** `cim:CsConverter.targetAlpha`  
**Name:** C:301:SSH:CsConverter.targetAlpha:applicability  
It is only applicable for rectifier if continuous tap changer control is used.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        #OPTIONAL {$this $PATH ?value}.
        $this $PATH ?value.
        $this cim:CsConverter.operatingMode ?opermode .
        #OPTIONAL {$this cim:ACDCConverter.PccTerminal ?pccterminal}.
        #OPTIONAL {?pccterminal cim:Terminal.ConductingEquipment ?condeq}. 
        #OPTIONAL {?condeq rdf:type ?condeqtype}.
        #OPTIONAL {?pccterminal cim:RegulatingControl.Terminal ?regcontrol}.
        #OPTIONAL {?regcontrol cim:RegulatingControl.discrete ?discrete}.
        
        OPTIONAL {$this cim:ACDCConverter.PccTerminal ?pccterminal .
                  ?pccterminal cim:Terminal.ConductingEquipment/rdf:type cim:PowerTransformer .
                  ?pccterminal ^cim:RegulatingControl.Terminal/cim:RegulatingControl.discrete ?discrete .
        } .
        
        
        #?regcontrol cim:RegulatingControl.Terminal ?pccterm .
        #FILTER (bound(?value) && (?opermode=cim:CsOperatingModeKind.inverter || (bound(?pccterminal) && ?condeqtype=cim:PowerTransformer && ?discrete=true && ?pccterm=?pccterminal))) .   
        FILTER ((?opermode=cim:CsOperatingModeKind.inverter || (bound(?pccterminal)  && ?discrete=true) || !bound(?discrete) )) .          
			}
```
  - Messages: `["CsConverter.targetAlpha is provided for an inverter or discrete tap changer control is used or RegulatingControl is not provided."]`

### ssh301n:CsConverter.targetGamma-applicability

**Path:** `cim:CsConverter.targetGamma`  
**Name:** C:301:SSH:CsConverter.targetGamma:applicability  
It is only applicable for inverter if continuous tap changer control is used.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        #OPTIONAL {$this $PATH ?value}.
        $this $PATH ?value.
        $this cim:CsConverter.operatingMode ?opermode .
        #OPTIONAL {$this cim:ACDCConverter.PccTerminal ?pccterminal}.
        #OPTIONAL {?pccterminal cim:Terminal.ConductingEquipment ?condeq}. 
        #OPTIONAL {?condeq rdf:type ?condeqtype}.
        #OPTIONAL {?pccterminal cim:RegulatingControl.Terminal ?regcontrol}.
        #OPTIONAL {?regcontrol cim:RegulatingControl.discrete ?discrete}.
        
        OPTIONAL {$this cim:ACDCConverter.PccTerminal ?pccterminal .
                  ?pccterminal cim:Terminal.ConductingEquipment/rdf:type cim:PowerTransformer .
                  ?pccterminal ^cim:RegulatingControl.Terminal/cim:RegulatingControl.discrete ?discrete .
        } .
        
        #?regcontrol cim:RegulatingControl.Terminal ?pccterm .
        #FILTER (bound(?value) && (?opermode=cim:CsOperatingModeKind.rectifier || (bound(?pccterminal) && ?condeqtype=cim:PowerTransformer && ?discrete=true && ?pccterm=?pccterminal))) . 
        FILTER ((?opermode=cim:CsOperatingModeKind.rectifier || (bound(?pccterminal) && ?discrete=true ) || !bound(?discrete))) .        
			}
```
  - Messages: `["CsConverter.targetGamma is provided for a rectifier or discrete tap changer control is used."]`

## ssh301n:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### ssh301n:ShuntCompensator.sections-valueLinear

**Path:** `cim:ShuntCompensator.sections`  
**Name:** C:301:SSH:ShuntCompensator.sections:valueLinear  
Non integer values are allowed to support continuous variables. For LinearShuntCompensator the value shall be between zero and ShuntCompensator.maximumSections. At value zero the shunt compensator conductance and admittance is zero.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ShuntCompensator.maximumSections ?maxsections .
        #OPTIONAL {$this cim:RegulatingCondEq.RegulatingControl ?contr}.
        #$this cim:RegulatingCondEq.controlEnabled ?contrenabled .
        
        #FILTER (bound(?contr) && ?contrenabled=true && !(?value>=0 && ?value<=?maxsections)) . 
        FILTER ( !(?value>=0 && ?value<=?maxsections)) .        
			}
```
  - Messages: `["The value is not between zero and ShuntCompensator.maximumSections."]`

## ssh301n:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### ssh301n:ShuntCompensator.sections-valueNonLinear

**Path:** `cim:ShuntCompensator.sections`  
**Name:** C:301:SSH:ShuntCompensator.sections:valueNonLinear  
For NonlinearShuntCompensator-s shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value (COUNT(?type) AS ?types) ?typesall
			WHERE {
        {
        SELECT $this (COUNT(?typeall) AS ?typesall)
        WHERE {
            ?nscpointsall cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator  $this .
            ?nscpointsall rdf:type ?typeall .
          }
        GROUP BY $this ?typesall
        }
        $this $PATH ?value .
        #OPTIONAL {$this cim:RegulatingCondEq.RegulatingControl ?contr}.
        #$this cim:RegulatingCondEq.controlEnabled ?contrenabled .
        ?nscpoints cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator  $this .
        ?nscpoints rdf:type ?type .
        ?nscpoints cim:NonlinearShuntCompensatorPoint.sectionNumber ?sectionnumber .  
        #FILTER (bound(?contr) && ?contrenabled=true && ?value!=?sectionnumber) .
        FILTER (?value!=?sectionnumber) .
			}
      GROUP BY $this ?value ?types ?typesall
      HAVING(?types=?typesall)
      
```
  - Messages: `["The value does not equal one of the NonlinearShuntCompenstorPoint.sectionNumber."]`

## ssh301n:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

## ssh301n:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

## ssh301n:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

## ssh301n:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

## ssh301n:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

## ssh301n:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl
- targetClass: cim:TapChangerControl

**Nested Properties:**

### ssh301n:RegulatingControl-requiredAttributes

**Path:** `cim:RegulatingControl.mode`  
**Name:** C:301:SSH:RegulatingControl:requiredAttributes  
The attribute minAllowedTargetValue and maxAllowedTargetValue are required in the following cases: - For a power generating module operated in power factor control mode to specify maximum and minimum power factor values; - ....

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this 
			WHERE {
        #$this $PATH ?value .
        $this $PATH cim:RegulatingControlModeKind.powerFactor .
        OPTIONAL {$this cim:RegulatingControl.minAllowedTargetValue ?minvalue}.
        OPTIONAL {$this cim:RegulatingControl.maxAllowedTargetValue ?maxvalue}. 
        #FILTER (?value=cim:RegulatingControlModeKind.powerFactor && (!bound(?minvalue) || !bound(?maxvalue))) .
        FILTER (!bound(?minvalue) || !bound(?maxvalue)) .        
			}
```
  - Messages: `["Both minAllowedTargetValue and maxAllowedTargetValue are not provided for RegulatingControl in mode powerFactor."]`

## ssh301n:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerTabular

**Nested Properties:**

### ssh301n:TapChanger.step-valueType

**Path:** `cim:TapChanger.step`  
**Name:** C:301:SSH:TapChanger.step:valueType  
Non integer values are allowed to support continuous tap variables.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.discrete true.
        #OPTIONAL {$this cim:TapChanger.TapChangerControl ?contr}.
        #?contr cim:RegulatingControl.discrete ?discrete . 
        #FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i") && bound(?contr) && ?discrete=true) .  
        FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")) .        
			}
```
  - Messages: `["Non-integer value for a discrete TapChangerControl."]`

