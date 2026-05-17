# 61970-457_Dynamics-AP-Con-Complex-NotSolvedMAS-SHACL

## dy457n:TurbineGovernorDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovCT2
- targetClass: cim:GovHydro1
- targetClass: cim:GovHydro3
- targetClass: cim:GovHydroPID
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovSteam0
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovHydroIEEE2
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovHydro4
- targetClass: cim:GovHydroDD
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydroR
- targetClass: cim:GovSteamCC
- targetClass: cim:GovHydro2
- targetClass: cim:GovSteam1
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovGAST
- targetClass: cim:GovGAST1
- targetClass: cim:GovGAST2
- targetClass: cim:GovGASTWD
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovSteamEU
- targetClass: cim:GovCT1

**Nested Properties:**

### dy457n:TurbineGovernorDynamics-mbaseEquation

**Path:** `rdf:type`  
The vast majority of turbine-governor models have mwbase as a parameter. The parameter is specified explicitly in the turbine-governor models to support use of a different value by transient analysis tools, if needed. If this parameter is present it shall correspond to RotatingMachine.ratedPowerFactor * RotatingMachine.ratedS.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
          $this rdf:type ?type .
          OPTIONAL {$this cim:GovHydroIEEE0.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroIEEE2.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamIEEE1.mwbase ?value }.
          OPTIONAL {$this cim:GovCT1.mwbase ?value }.
          OPTIONAL {$this cim:GovCT2.mwbase ?value }.
          OPTIONAL {$this cim:GovGAST.mwbase ?value }.
          OPTIONAL {$this cim:GovGAST1.mwbase ?value }.
          OPTIONAL {$this cim:GovGAST2.mwbase ?value }.
          OPTIONAL {$this cim:GovGASTWD.mwbase ?value }.
          OPTIONAL {$this cim:GovHydro1.mwbase ?value }.
          OPTIONAL {$this cim:GovHydro2.mwbase ?value }.
          OPTIONAL {$this cim:GovHydro3.mwbase ?value }.
          OPTIONAL {$this cim:GovHydro4.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroDD.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroPID.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroPID2.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroR.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroWEH.mwbase ?value }.
          OPTIONAL {$this cim:GovHydroWPID.mwbase ?value }.
          OPTIONAL {$this cim:GovSteam1.mwbase ?value }.
          OPTIONAL {$this cim:GovSteam0.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamCC.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamEU.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamFV3.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamSGO.mwbase ?value }.
          OPTIONAL {$this cim:GovSteamFV2.mwbase ?value }.
          $this cim:TurbineGovernorDynamics.SynchronousMachineDynamics ?smd .
          ?smd cim:SynchronousMachineDynamics.SynchronousMachine ?sm .
          OPTIONAL {?sm cim:RotatingMachine.ratedPowerFactor ?ratedPowerFactor} .
          OPTIONAL {?sm cim:RotatingMachine.ratedS ?ratedS} .
        FILTER ((!bound(?ratedPowerFactor) || !bound(?ratedS)) || ?value!=?ratedPowerFactor*?ratedS ) . 
			}
```
  - Messages: `["The value does not equal RotatingMachine.ratedPowerFactor * RotatingMachine.ratedS or either both or one of the following attributes are not defined: .ratedPowerFactor, .ratedS."]`

