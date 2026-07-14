# 61970-302_Dynamics-AP-Con-Complex-SHACL

## dy302c:AsynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineEquivalentCircuit

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:AsynchronousMachineTimeConstantReactance

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy302c:AsynchronousMachineTimeConstantReactance.tppo-valueRange

**Path:** `cim:AsynchronousMachineTimeConstantReactance.tppo`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.tppo:valueRange  
Subtransient rotor time constant (T''o) (> 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.tpo-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.tppo`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.tpo:valueRangePair  
Transient rotor time constant (T'o) (> AsynchronousMachineTimeConstantReactance.tppo).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.tpo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.tpo` 

### dy302c:AsynchronousMachineTimeConstantReactance.xs-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.xp`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xs:valueRangePair  
Synchronous reactance (Xs) (>= AsynchronousMachineTimeConstantReactance.xp).  Typical value = 1,8.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than AsynchronousMachineTimeConstantReactance.xs."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xs` 

### dy302c:AsynchronousMachineTimeConstantReactance.xp-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.xpp`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xp:valueRangePair  
Transient reactance (unsaturated) (X') (>= AsynchronousMachineTimeConstantReactance.xpp).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than AsynchronousMachineTimeConstantReactance.xp."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xp` 

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:AsynchronousMachineUserDefined

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineUserDefined

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:DiscExcContIEEEDEC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC1A

**Nested Properties:**

### dy302c:DiscExcContIEEEDEC1A.tan-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tan`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.tan:valueRange  
Discontinuous controller time constant (T<sub>AN</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.td-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.td`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.td:valueRange  
Time constant (T<sub>D</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tl1-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tl1`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.tl1:valueRange  
Time constant (T<sub>L</sub><sub>1</sub>) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tl2-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tl2`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.tl2:valueRange  
Time constant (T<sub>L</sub><sub>2</sub>) (>= 0).  Typical value = 1,25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tw5-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tw5`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.tw5:valueRange  
DEC washout time constant (T<sub>W</sub><sub>5</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.vomin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC1A.vomin`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.vomin:valueRangePair  
Limiter (V<sub>OMIN</sub>) (< DiscExcContIEEEDEC1A.vomax).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than DiscExcContIEEEDEC1A.vomax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:DiscExcContIEEEDEC1A.vomax` 

### dy302c:DiscExcContIEEEDEC1A.vsmin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC1A.vsmin`  
**Name:** C:302:DY:DiscExcContIEEEDEC1A.vsmin:valueRangePair  
Limiter (V<sub>SMIN</sub>) (< DiscExcContIEEEDEC1A.vsmax).  Typical value = -0,066.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than DiscExcContIEEEDEC1A.vsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:DiscExcContIEEEDEC1A.vsmax` 

## dy302c:DiscExcContIEEEDEC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC2A

**Nested Properties:**

### dy302c:DiscExcContIEEEDEC2A.td1-valueRange

**Path:** `cim:DiscExcContIEEEDEC2A.td1`  
**Name:** C:302:DY:DiscExcContIEEEDEC2A.td1:valueRange  
Discontinuous controller time constant (T<sub>D1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC2A.td2-valueRange

**Path:** `cim:DiscExcContIEEEDEC2A.td2`  
**Name:** C:302:DY:DiscExcContIEEEDEC2A.td2:valueRange  
Discontinuous controller washout time constant (T<sub>D2</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC2A.vdmin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC2A.vdmin`  
**Name:** C:302:DY:DiscExcContIEEEDEC2A.vdmin:valueRangePair  
Limiter (V<sub>DMIN</sub>) (< DiscExcContIEEEDEC2A.vdmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than DiscExcContIEEEDEC2A.vdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:DiscExcContIEEEDEC2A.vdmax` 

## dy302c:DiscExcContIEEEDEC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC3A

**Nested Properties:**

### dy302c:DiscExcContIEEEDEC3A.tdr-valueRange

**Path:** `cim:DiscExcContIEEEDEC3A.tdr`  
**Name:** C:302:DY:DiscExcContIEEEDEC3A.tdr:valueRange  
Reset time delay (T<sub>DR</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC1A

**Nested Properties:**

### dy302c:ExcAC1A.ka-valueRange

**Path:** `cim:ExcAC1A.ka`  
**Name:** C:302:DY:ExcAC1A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kc-valueRange

**Path:** `cim:ExcAC1A.kc`  
**Name:** C:302:DY:ExcAC1A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kd-valueRange

**Path:** `cim:ExcAC1A.kd`  
**Name:** C:302:DY:ExcAC1A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,38.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf-valueRange

**Path:** `cim:ExcAC1A.kf`  
**Name:** C:302:DY:ExcAC1A.kf:valueRange  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf1-valueRange

**Path:** `cim:ExcAC1A.kf1`  
**Name:** C:302:DY:ExcAC1A.kf1:valueRange  
Coefficient to allow different usage of the model (Kf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf2-valueRange

**Path:** `cim:ExcAC1A.kf2`  
**Name:** C:302:DY:ExcAC1A.kf2:valueRange  
Coefficient to allow different usage of the model (Kf2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ks-valueRange

**Path:** `cim:ExcAC1A.ks`  
**Name:** C:302:DY:ExcAC1A.ks:valueRange  
Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.seve1-valueRange

**Path:** `cim:ExcAC1A.seve1`  
**Name:** C:302:DY:ExcAC1A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.seve2-valueRange

**Path:** `cim:ExcAC1A.seve2`  
**Name:** C:302:DY:ExcAC1A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ta-valueRange

**Path:** `cim:ExcAC1A.ta`  
**Name:** C:302:DY:ExcAC1A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tb-valueRange

**Path:** `cim:ExcAC1A.tb`  
**Name:** C:302:DY:ExcAC1A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tc-valueRange

**Path:** `cim:ExcAC1A.tc`  
**Name:** C:302:DY:ExcAC1A.tc:valueRange  
Voltage regulator time constant (T<sub>c</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.te-valueRange

**Path:** `cim:ExcAC1A.te`  
**Name:** C:302:DY:ExcAC1A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tf-valueRange

**Path:** `cim:ExcAC1A.tf`  
**Name:** C:302:DY:ExcAC1A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vamax-valueRange

**Path:** `cim:ExcAC1A.vamax`  
**Name:** C:302:DY:ExcAC1A.vamax:valueRange  
Maximum voltage regulator output (V<sub>amax</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vamin-valueRange

**Path:** `cim:ExcAC1A.vamin`  
**Name:** C:302:DY:ExcAC1A.vamin:valueRange  
Minimum voltage regulator output (V<sub>amin</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ve1-valueRange

**Path:** `cim:ExcAC1A.ve1`  
**Name:** C:302:DY:ExcAC1A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).  Typical value = 4,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ve2-valueRange

**Path:** `cim:ExcAC1A.ve2`  
**Name:** C:302:DY:ExcAC1A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).  Typical value = 3,14.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vrmax-valueRange

**Path:** `cim:ExcAC1A.vrmax`  
**Name:** C:302:DY:ExcAC1A.vrmax:valueRange  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 6,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vrmin-valueRange

**Path:** `cim:ExcAC1A.vrmin`  
**Name:** C:302:DY:ExcAC1A.vrmin:valueRange  
Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -5,43.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC2A

**Nested Properties:**

### dy302c:ExcAC2A.ka-valueRange

**Path:** `cim:ExcAC2A.ka`  
**Name:** C:302:DY:ExcAC2A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kb-valueRange

**Path:** `cim:ExcAC2A.kb`  
**Name:** C:302:DY:ExcAC2A.kb:valueRange  
Second stage regulator gain (Kb) (> 0).  Exciter field current controller gain.  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kc-valueRange

**Path:** `cim:ExcAC2A.kc`  
**Name:** C:302:DY:ExcAC2A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,28.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kd-valueRange

**Path:** `cim:ExcAC2A.kd`  
**Name:** C:302:DY:ExcAC2A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kf-valueRange

**Path:** `cim:ExcAC2A.kf`  
**Name:** C:302:DY:ExcAC2A.kf:valueRange  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kh-valueRange

**Path:** `cim:ExcAC2A.kh`  
**Name:** C:302:DY:ExcAC2A.kh:valueRange  
Exciter field current feedback gain (Kh) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ks-valueRange

**Path:** `cim:ExcAC2A.ks`  
**Name:** C:302:DY:ExcAC2A.ks:valueRange  
Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.seve1-valueRange

**Path:** `cim:ExcAC2A.seve1`  
**Name:** C:302:DY:ExcAC2A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.seve2-valueRange

**Path:** `cim:ExcAC2A.seve2`  
**Name:** C:302:DY:ExcAC2A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ta-valueRange

**Path:** `cim:ExcAC2A.ta`  
**Name:** C:302:DY:ExcAC2A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tb-valueRange

**Path:** `cim:ExcAC2A.tb`  
**Name:** C:302:DY:ExcAC2A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tc-valueRange

**Path:** `cim:ExcAC2A.tc`  
**Name:** C:302:DY:ExcAC2A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.te-valueRange

**Path:** `cim:ExcAC2A.te`  
**Name:** C:302:DY:ExcAC2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tf-valueRange

**Path:** `cim:ExcAC2A.tf`  
**Name:** C:302:DY:ExcAC2A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vamax-valueRange

**Path:** `cim:ExcAC2A.vamax`  
**Name:** C:302:DY:ExcAC2A.vamax:valueRange  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vamin-valueRange

**Path:** `cim:ExcAC2A.vamin`  
**Name:** C:302:DY:ExcAC2A.vamin:valueRange  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -8.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ve1-valueRange

**Path:** `cim:ExcAC2A.ve1`  
**Name:** C:302:DY:ExcAC2A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ve2-valueRange

**Path:** `cim:ExcAC2A.ve2`  
**Name:** C:302:DY:ExcAC2A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vfemax-valueRange

**Path:** `cim:ExcAC2A.vfemax`  
**Name:** C:302:DY:ExcAC2A.vfemax:valueRange  
Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vlr-valueRange

**Path:** `cim:ExcAC2A.vlr`  
**Name:** C:302:DY:ExcAC2A.vlr:valueRange  
Maximum exciter field current (Vlr) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vrmax-valueRange

**Path:** `cim:ExcAC2A.vrmax`  
**Name:** C:302:DY:ExcAC2A.vrmax:valueRange  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 105.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vrmin-valueRange

**Path:** `cim:ExcAC2A.vrmin`  
**Name:** C:302:DY:ExcAC2A.vrmin:valueRange  
Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC3A

**Nested Properties:**

### dy302c:ExcAC3A.efdn-valueRange

**Path:** `cim:ExcAC3A.efdn`  
**Name:** C:302:DY:ExcAC3A.efdn:valueRange  
Value of Efd at which feedback gain changes (Efdn) (> 0).  Typical value = 2,36.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ka-valueRange

**Path:** `cim:ExcAC3A.ka`  
**Name:** C:302:DY:ExcAC3A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 45,62.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kc-valueRange

**Path:** `cim:ExcAC3A.kc`  
**Name:** C:302:DY:ExcAC3A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,104.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kd-valueRange

**Path:** `cim:ExcAC3A.kd`  
**Name:** C:302:DY:ExcAC3A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,499.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kf-valueRange

**Path:** `cim:ExcAC3A.kf`  
**Name:** C:302:DY:ExcAC3A.kf:valueRange  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kn-valueRange

**Path:** `cim:ExcAC3A.kn`  
**Name:** C:302:DY:ExcAC3A.kn:valueRange  
Excitation control system stabilizer gain (Kn) (>= 0).  Typical value =0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kr-valueRange

**Path:** `cim:ExcAC3A.kr`  
**Name:** C:302:DY:ExcAC3A.kr:valueRange  
Constant associated with regulator and alternator field power supply (Kr) (> 0).  Typical value =3,77.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.seve1-valueRange

**Path:** `cim:ExcAC3A.seve1`  
**Name:** C:302:DY:ExcAC3A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 1,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.seve2-valueRange

**Path:** `cim:ExcAC3A.seve2`  
**Name:** C:302:DY:ExcAC3A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ta-valueRange

**Path:** `cim:ExcAC3A.ta`  
**Name:** C:302:DY:ExcAC3A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,013.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tb-valueRange

**Path:** `cim:ExcAC3A.tb`  
**Name:** C:302:DY:ExcAC3A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tc-valueRange

**Path:** `cim:ExcAC3A.tc`  
**Name:** C:302:DY:ExcAC3A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.te-valueRange

**Path:** `cim:ExcAC3A.te`  
**Name:** C:302:DY:ExcAC3A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,17.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tf-valueRange

**Path:** `cim:ExcAC3A.tf`  
**Name:** C:302:DY:ExcAC3A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vamax-valueRange

**Path:** `cim:ExcAC3A.vamax`  
**Name:** C:302:DY:ExcAC3A.vamax:valueRange  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vamin-valueRange

**Path:** `cim:ExcAC3A.vamin`  
**Name:** C:302:DY:ExcAC3A.vamin:valueRange  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ve1-valueRange

**Path:** `cim:ExcAC3A.ve1`  
**Name:** C:302:DY:ExcAC3A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 6.24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ve2-valueRange

**Path:** `cim:ExcAC3A.ve2`  
**Name:** C:302:DY:ExcAC3A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 4,68.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vemin-valueRange

**Path:** `cim:ExcAC3A.vemin`  
**Name:** C:302:DY:ExcAC3A.vemin:valueRange  
Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vfemax-valueRange

**Path:** `cim:ExcAC3A.vfemax`  
**Name:** C:302:DY:ExcAC3A.vfemax:valueRange  
Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 16.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC4A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC4A

**Nested Properties:**

### dy302c:ExcAC4A.ka-valueRange

**Path:** `cim:ExcAC4A.ka`  
**Name:** C:302:DY:ExcAC4A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.kc-valueRange

**Path:** `cim:ExcAC4A.kc`  
**Name:** C:302:DY:ExcAC4A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.ta-valueRange

**Path:** `cim:ExcAC4A.ta`  
**Name:** C:302:DY:ExcAC4A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,015.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.tb-valueRange

**Path:** `cim:ExcAC4A.tb`  
**Name:** C:302:DY:ExcAC4A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.tc-valueRange

**Path:** `cim:ExcAC4A.tc`  
**Name:** C:302:DY:ExcAC4A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vimax-valueRange

**Path:** `cim:ExcAC4A.vimax`  
**Name:** C:302:DY:ExcAC4A.vimax:valueRange  
Maximum voltage regulator input limit (Vimax)  (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vimin-valueRange

**Path:** `cim:ExcAC4A.vimin`  
**Name:** C:302:DY:ExcAC4A.vimin:valueRange  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vrmax-valueRange

**Path:** `cim:ExcAC4A.vrmax`  
**Name:** C:302:DY:ExcAC4A.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5,64.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vrmin-valueRange

**Path:** `cim:ExcAC4A.vrmin`  
**Name:** C:302:DY:ExcAC4A.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,53.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC5A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC5A

**Nested Properties:**

### dy302c:ExcAC5A.efd1-valueRange

**Path:** `cim:ExcAC5A.efd1`  
**Name:** C:302:DY:ExcAC5A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 5,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.efd2-valueRange

**Path:** `cim:ExcAC5A.efd2`  
**Name:** C:302:DY:ExcAC5A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 4,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.ka-valueRange

**Path:** `cim:ExcAC5A.ka`  
**Name:** C:302:DY:ExcAC5A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.kf-valueRange

**Path:** `cim:ExcAC5A.kf`  
**Name:** C:302:DY:ExcAC5A.kf:valueRange  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.seefd1-valueRange

**Path:** `cim:ExcAC5A.seefd1`  
**Name:** C:302:DY:ExcAC5A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,86.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.seefd2-valueRange

**Path:** `cim:ExcAC5A.seefd2`  
**Name:** C:302:DY:ExcAC5A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.ta-valueRange

**Path:** `cim:ExcAC5A.ta`  
**Name:** C:302:DY:ExcAC5A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tb-valueRange

**Path:** `cim:ExcAC5A.tb`  
**Name:** C:302:DY:ExcAC5A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tc-valueRange

**Path:** `cim:ExcAC5A.tc`  
**Name:** C:302:DY:ExcAC5A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.te-valueRange

**Path:** `cim:ExcAC5A.te`  
**Name:** C:302:DY:ExcAC5A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf1-valueRange

**Path:** `cim:ExcAC5A.tf1`  
**Name:** C:302:DY:ExcAC5A.tf1:valueRange  
Excitation control system stabilizer time constant (Tf1) (> 0).  Typical value  = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf2-valueRange

**Path:** `cim:ExcAC5A.tf2`  
**Name:** C:302:DY:ExcAC5A.tf2:valueRange  
Excitation control system stabilizer time constant (Tf2) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf3-valueRange

**Path:** `cim:ExcAC5A.tf3`  
**Name:** C:302:DY:ExcAC5A.tf3:valueRange  
Excitation control system stabilizer time constant (Tf3) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.vrmax-valueRange

**Path:** `cim:ExcAC5A.vrmax`  
**Name:** C:302:DY:ExcAC5A.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.vrmin-valueRange

**Path:** `cim:ExcAC5A.vrmin`  
**Name:** C:302:DY:ExcAC5A.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value =-7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC6A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC6A

**Nested Properties:**

### dy302c:ExcAC6A.ka-valueRange

**Path:** `cim:ExcAC6A.ka`  
**Name:** C:302:DY:ExcAC6A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 536.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kc-valueRange

**Path:** `cim:ExcAC6A.kc`  
**Name:** C:302:DY:ExcAC6A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kd-valueRange

**Path:** `cim:ExcAC6A.kd`  
**Name:** C:302:DY:ExcAC6A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,91.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kh-valueRange

**Path:** `cim:ExcAC6A.kh`  
**Name:** C:302:DY:ExcAC6A.kh:valueRange  
Exciter field current limiter gain (Kh) (>= 0).  Typical value = 92.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.seve1-valueRange

**Path:** `cim:ExcAC6A.seve1`  
**Name:** C:302:DY:ExcAC6A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,214.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.seve2-valueRange

**Path:** `cim:ExcAC6A.seve2`  
**Name:** C:302:DY:ExcAC6A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,044.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ta-valueRange

**Path:** `cim:ExcAC6A.ta`  
**Name:** C:302:DY:ExcAC6A.ta:valueRange  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tb-valueRange

**Path:** `cim:ExcAC6A.tb`  
**Name:** C:302:DY:ExcAC6A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tc-valueRange

**Path:** `cim:ExcAC6A.tc`  
**Name:** C:302:DY:ExcAC6A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.te-valueRange

**Path:** `cim:ExcAC6A.te`  
**Name:** C:302:DY:ExcAC6A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.th-valueRange

**Path:** `cim:ExcAC6A.th`  
**Name:** C:302:DY:ExcAC6A.th:valueRange  
Exciter field current limiter time constant (Th) (> 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tj-valueRange

**Path:** `cim:ExcAC6A.tj`  
**Name:** C:302:DY:ExcAC6A.tj:valueRange  
Exciter field current limiter time constant (Tj) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tk-valueRange

**Path:** `cim:ExcAC6A.tk`  
**Name:** C:302:DY:ExcAC6A.tk:valueRange  
Voltage regulator time constant (Tk) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vamax-valueRange

**Path:** `cim:ExcAC6A.vamax`  
**Name:** C:302:DY:ExcAC6A.vamax:valueRange  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vamin-valueRange

**Path:** `cim:ExcAC6A.vamin`  
**Name:** C:302:DY:ExcAC6A.vamin:valueRange  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -75.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ve1-valueRange

**Path:** `cim:ExcAC6A.ve1`  
**Name:** C:302:DY:ExcAC6A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 7,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ve2-valueRange

**Path:** `cim:ExcAC6A.ve2`  
**Name:** C:302:DY:ExcAC6A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 5,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vfelim-valueRange

**Path:** `cim:ExcAC6A.vfelim`  
**Name:** C:302:DY:ExcAC6A.vfelim:valueRange  
Exciter field current limit reference (Vfelim) (> 0).  Typical value = 19.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vhmax-valueRange

**Path:** `cim:ExcAC6A.vhmax`  
**Name:** C:302:DY:ExcAC6A.vhmax:valueRange  
Maximum field current limiter signal reference (Vhmax) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vrmax-valueRange

**Path:** `cim:ExcAC6A.vrmax`  
**Name:** C:302:DY:ExcAC6A.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vrmin-valueRange

**Path:** `cim:ExcAC6A.vrmin`  
**Name:** C:302:DY:ExcAC6A.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -36.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAC8B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC8B

**Nested Properties:**

### dy302c:ExcAC8B.ka-valueRange

**Path:** `cim:ExcAC8B.ka`  
**Name:** C:302:DY:ExcAC8B.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kc-valueRange

**Path:** `cim:ExcAC8B.kc`  
**Name:** C:302:DY:ExcAC8B.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kd-valueRange

**Path:** `cim:ExcAC8B.kd`  
**Name:** C:302:DY:ExcAC8B.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kdr-valueRange

**Path:** `cim:ExcAC8B.kdr`  
**Name:** C:302:DY:ExcAC8B.kdr:valueRange  
Voltage regulator derivative gain (Kdr) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kir-valueRange

**Path:** `cim:ExcAC8B.kir`  
**Name:** C:302:DY:ExcAC8B.kir:valueRange  
Voltage regulator integral gain (Kir) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.seve1-valueRange

**Path:** `cim:ExcAC8B.seve1`  
**Name:** C:302:DY:ExcAC8B.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.seve2-valueRange

**Path:** `cim:ExcAC8B.seve2`  
**Name:** C:302:DY:ExcAC8B.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ta-valueRange

**Path:** `cim:ExcAC8B.ta`  
**Name:** C:302:DY:ExcAC8B.ta:valueRange  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.tdr-valueRange

**Path:** `cim:ExcAC8B.tdr`  
**Name:** C:302:DY:ExcAC8B.tdr:valueRange  
Lag time constant (Tdr) (> 0 if ExcAC8B.kdr > 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.te-valueRange

**Path:** `cim:ExcAC8B.te`  
**Name:** C:302:DY:ExcAC8B.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ve1-valueRange

**Path:** `cim:ExcAC8B.ve1`  
**Name:** C:302:DY:ExcAC8B.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 6,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ve2-valueRange

**Path:** `cim:ExcAC8B.ve2`  
**Name:** C:302:DY:ExcAC8B.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vemin-valueRange

**Path:** `cim:ExcAC8B.vemin`  
**Name:** C:302:DY:ExcAC8B.vemin:valueRange  
Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vimin-valueRangePair

**Path:** `cim:ExcAC8B.vimin`  
**Name:** C:302:DY:ExcAC8B.vimin:valueRangePair  
Input signal minimum (Vimin) (< ExcAC8B.vimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAC8B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAC8B.vimax` 

### dy302c:ExcAC8B.vpidmin-valueRangePair

**Path:** `cim:ExcAC8B.vpidmin`  
**Name:** C:302:DY:ExcAC8B.vpidmin:valueRangePair  
PID minimum controller output (Vpidmin) (< ExcAC8B.vpidmax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAC8B.vpidmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAC8B.vpidmax` 

### dy302c:ExcAC8B.vrmax-valueRange

**Path:** `cim:ExcAC8B.vrmax`  
**Name:** C:302:DY:ExcAC8B.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0). Typical value = 35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vrmin-valueRange

**Path:** `cim:ExcAC8B.vrmin`  
**Name:** C:302:DY:ExcAC8B.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcANS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcANS

**Nested Properties:**

### dy302c:ExcANS.t1-valueRange

**Path:** `cim:ExcANS.t1`  
**Name:** C:302:DY:ExcANS.t1:valueRange  
Time constant (T<sub>1</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.t2-valueRange

**Path:** `cim:ExcANS.t2`  
**Name:** C:302:DY:ExcANS.t2:valueRange  
Time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.t3-valueRange

**Path:** `cim:ExcANS.t3`  
**Name:** C:302:DY:ExcANS.t3:valueRange  
Time constant (T<sub>3</sub>) (>= 0).  Typical value = 1,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.tb-valueRange

**Path:** `cim:ExcANS.tb`  
**Name:** C:302:DY:ExcANS.tb:valueRange  
Exciter time constant (T<sub>B</sub>) (>= 0).  Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR1

**Nested Properties:**

### dy302c:ExcAVR1.ta-valueRange

**Path:** `cim:ExcAVR1.ta`  
**Name:** C:302:DY:ExcAVR1.ta:valueRange  
AVR time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.tb-valueRange

**Path:** `cim:ExcAVR1.tb`  
**Name:** C:302:DY:ExcAVR1.tb:valueRange  
AVR time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.te-valueRange

**Path:** `cim:ExcAVR1.te`  
**Name:** C:302:DY:ExcAVR1.te:valueRange  
Exciter time constant (T<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.tf-valueRange

**Path:** `cim:ExcAVR1.tf`  
**Name:** C:302:DY:ExcAVR1.tf:valueRange  
Rate feedback time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR2

**Nested Properties:**

### dy302c:ExcAVR2.ta-valueRange

**Path:** `cim:ExcAVR2.ta`  
**Name:** C:302:DY:ExcAVR2.ta:valueRange  
AVR time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tb-valueRange

**Path:** `cim:ExcAVR2.tb`  
**Name:** C:302:DY:ExcAVR2.tb:valueRange  
AVR time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.te-valueRange

**Path:** `cim:ExcAVR2.te`  
**Name:** C:302:DY:ExcAVR2.te:valueRange  
Exciter time constant (T<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tf1-valueRange

**Path:** `cim:ExcAVR2.tf1`  
**Name:** C:302:DY:ExcAVR2.tf1:valueRange  
Rate feedback time constant (T<sub>F1</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tf2-valueRange

**Path:** `cim:ExcAVR2.tf2`  
**Name:** C:302:DY:ExcAVR2.tf2:valueRange  
Rate feedback time constant (T<sub>F2</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR3

**Nested Properties:**

### dy302c:ExcAVR3.t1-valueRange

**Path:** `cim:ExcAVR3.t1`  
**Name:** C:302:DY:ExcAVR3.t1:valueRange  
AVR time constant (T<sub>1</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t2-valueRange

**Path:** `cim:ExcAVR3.t2`  
**Name:** C:302:DY:ExcAVR3.t2:valueRange  
AVR time constant (T<sub>2</sub>) (>= 0).  Typical value = 1,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t3-valueRange

**Path:** `cim:ExcAVR3.t3`  
**Name:** C:302:DY:ExcAVR3.t3:valueRange  
AVR time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,66.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t4-valueRange

**Path:** `cim:ExcAVR3.t4`  
**Name:** C:302:DY:ExcAVR3.t4:valueRange  
AVR time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,07.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.te-valueRange

**Path:** `cim:ExcAVR3.te`  
**Name:** C:302:DY:ExcAVR3.te:valueRange  
Exciter time constant (T<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR4

**Nested Properties:**

### dy302c:ExcAVR4.t1-valueRange

**Path:** `cim:ExcAVR4.t1`  
**Name:** C:302:DY:ExcAVR4.t1:valueRange  
AVR time constant (T<sub>1</sub>) (>= 0).  Typical value = 4,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t1if-valueRange

**Path:** `cim:ExcAVR4.t1if`  
**Name:** C:302:DY:ExcAVR4.t1if:valueRange  
Exciter current feedback time constant (T<sub>1IF</sub>) (>= 0).  Typical value = 60.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t2-valueRange

**Path:** `cim:ExcAVR4.t2`  
**Name:** C:302:DY:ExcAVR4.t2:valueRange  
AVR time constant (T<sub>2</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t3-valueRange

**Path:** `cim:ExcAVR4.t3`  
**Name:** C:302:DY:ExcAVR4.t3:valueRange  
AVR time constant (T<sub>3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t4-valueRange

**Path:** `cim:ExcAVR4.t4`  
**Name:** C:302:DY:ExcAVR4.t4:valueRange  
AVR time constant (T<sub>4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.tif-valueRange

**Path:** `cim:ExcAVR4.tif`  
**Name:** C:302:DY:ExcAVR4.tif:valueRange  
Exciter current feedback time constant (T<sub>IF</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR5

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR5

**Nested Properties:**

### dy302c:ExcAVR5.ta-valueRange

**Path:** `cim:ExcAVR5.ta`  
**Name:** C:302:DY:ExcAVR5.ta:valueRange  
Time constant (Ta) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcAVR7

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR7

**Nested Properties:**

### dy302c:ExcAVR7.t1-valueRange

**Path:** `cim:ExcAVR7.t1`  
**Name:** C:302:DY:ExcAVR7.t1:valueRange  
Lead time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t2-valueRange

**Path:** `cim:ExcAVR7.t2`  
**Name:** C:302:DY:ExcAVR7.t2:valueRange  
Lag time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t3-valueRange

**Path:** `cim:ExcAVR7.t3`  
**Name:** C:302:DY:ExcAVR7.t3:valueRange  
Lead time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t4-valueRange

**Path:** `cim:ExcAVR7.t4`  
**Name:** C:302:DY:ExcAVR7.t4:valueRange  
Lag time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t5-valueRange

**Path:** `cim:ExcAVR7.t5`  
**Name:** C:302:DY:ExcAVR7.t5:valueRange  
Lead time constant (T<sub>5</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t6-valueRange

**Path:** `cim:ExcAVR7.t6`  
**Name:** C:302:DY:ExcAVR7.t6:valueRange  
Lag time constant (T<sub>6</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.vmin1-valueRangePair

**Path:** `cim:ExcAVR7.vmin1`  
**Name:** C:302:DY:ExcAVR7.vmin1:valueRangePair  
Lead-lag minimum limit (Vmin1) (< ExcAVR7.vmax1).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAVR7.vmax1."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAVR7.vmax1` 

### dy302c:ExcAVR7.vmin3-valueRangePair

**Path:** `cim:ExcAVR7.vmin3`  
**Name:** C:302:DY:ExcAVR7.vmin3:valueRangePair  
Lead-lag minimum limit (Vmin3) (< ExcAVR7.vmax3).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAVR7.vmax3."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAVR7.vmax3` 

### dy302c:ExcAVR7.vmin5-valueRangePair

**Path:** `cim:ExcAVR7.vmin5`  
**Name:** C:302:DY:ExcAVR7.vmin5:valueRangePair  
Lead-lag minimum limit (Vmin5) (< ExcAVR7.vmax5).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAVR7.vmax5."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAVR7.vmax5` 

## dy302c:ExcBBC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcBBC

**Nested Properties:**

### dy302c:ExcBBC.efdmin-valueRangePair

**Path:** `cim:ExcBBC.efdmin`  
**Name:** C:302:DY:ExcBBC.efdmin:valueRangePair  
Minimum open circuit exciter voltage (Efdmin) (< ExcBBC.efdmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcBBC.efdmax` 

### dy302c:ExcBBC.t1-valueRange

**Path:** `cim:ExcBBC.t1`  
**Name:** C:302:DY:ExcBBC.t1:valueRange  
Controller time constant (T1) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t2-valueRange

**Path:** `cim:ExcBBC.t2`  
**Name:** C:302:DY:ExcBBC.t2:valueRange  
Controller time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t3-valueRange

**Path:** `cim:ExcBBC.t3`  
**Name:** C:302:DY:ExcBBC.t3:valueRange  
Lead/lag time constant (T3) (>= 0).  If = 0, block is bypassed.  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t4-valueRange

**Path:** `cim:ExcBBC.t4`  
**Name:** C:302:DY:ExcBBC.t4:valueRange  
Lead/lag time constant (T4) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.vrmin-valueRangePair

**Path:** `cim:ExcBBC.vrmin`  
**Name:** C:302:DY:ExcBBC.vrmin:valueRangePair  
Minimum control element output (Vrmin) (< ExcBBC.vrmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcBBC.vrmax` 

### dy302c:ExcBBC.xe-valueRange

**Path:** `cim:ExcBBC.xe`  
**Name:** C:302:DY:ExcBBC.xe:valueRange  
Effective excitation transformer reactance (Xe) (>= 0).  Xe models the regulation of the transformer/rectifier unit.  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcCZ

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcCZ

**Nested Properties:**

### dy302c:ExcCZ.efdmin-valueRangePair

**Path:** `cim:ExcCZ.efdmin`  
**Name:** C:302:DY:ExcCZ.efdmin:valueRangePair  
Exciter output minimum limit (Efdmin) (< ExcCZ.efdmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcCZ.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcCZ.efdmax` 

### dy302c:ExcCZ.ta-valueRange

**Path:** `cim:ExcCZ.ta`  
**Name:** C:302:DY:ExcCZ.ta:valueRange  
Regulator time constant (Ta) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.tc-valueRange

**Path:** `cim:ExcCZ.tc`  
**Name:** C:302:DY:ExcCZ.tc:valueRange  
Regulator integral time constant (Tc) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.te-valueRange

**Path:** `cim:ExcCZ.te`  
**Name:** C:302:DY:ExcCZ.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.vrmin-valueRangePair

**Path:** `cim:ExcCZ.vrmin`  
**Name:** C:302:DY:ExcCZ.vrmin:valueRangePair  
Voltage regulator minimum limit (Vrmin) (< ExcCZ.vrmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcCZ.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcCZ.vrmax` 

## dy302c:ExcDC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC1A

**Nested Properties:**

### dy302c:ExcDC1A.efd1-valueRange

**Path:** `cim:ExcDC1A.efd1`  
**Name:** C:302:DY:ExcDC1A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 3,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.efd2-valueRange

**Path:** `cim:ExcDC1A.efd2`  
**Name:** C:302:DY:ExcDC1A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 2,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.efdmin-valueRangePair

**Path:** `cim:ExcDC1A.efdmin`  
**Name:** C:302:DY:ExcDC1A.efdmin:valueRangePair  
Minimum voltage exciter output limiter (Efdmin) (< ExcDC1A.edfmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC1A.edfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC1A.edfmax` 

### dy302c:ExcDC1A.ka-valueRange

**Path:** `cim:ExcDC1A.ka`  
**Name:** C:302:DY:ExcDC1A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.kf-valueRange

**Path:** `cim:ExcDC1A.kf`  
**Name:** C:302:DY:ExcDC1A.kf:valueRange  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.seefd1-valueRange

**Path:** `cim:ExcDC1A.seefd1`  
**Name:** C:302:DY:ExcDC1A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Eefd<sub>1</sub>]) (>= 0).  Typical value = 0,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.seefd2-valueRange

**Path:** `cim:ExcDC1A.seefd2`  
**Name:** C:302:DY:ExcDC1A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Eefd<sub>2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.ta-valueRange

**Path:** `cim:ExcDC1A.ta`  
**Name:** C:302:DY:ExcDC1A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,06.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tb-valueRange

**Path:** `cim:ExcDC1A.tb`  
**Name:** C:302:DY:ExcDC1A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tc-valueRange

**Path:** `cim:ExcDC1A.tc`  
**Name:** C:302:DY:ExcDC1A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.te-valueRange

**Path:** `cim:ExcDC1A.te`  
**Name:** C:302:DY:ExcDC1A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tf-valueRange

**Path:** `cim:ExcDC1A.tf`  
**Name:** C:302:DY:ExcDC1A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.vrmin-valueRangePair

**Path:** `cim:ExcDC1A.vrmin`  
**Name:** C:302:DY:ExcDC1A.vrmin:valueRangePair  
Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC1A.vrmax).  Typical value = -0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC1A.vrmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC1A.vrmax` 

## dy302c:ExcDC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC2A

**Nested Properties:**

### dy302c:ExcDC2A.efd1-valueRange

**Path:** `cim:ExcDC2A.efd1`  
**Name:** C:302:DY:ExcDC2A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 3,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.efd2-valueRange

**Path:** `cim:ExcDC2A.efd2`  
**Name:** C:302:DY:ExcDC2A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 2,29.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.ka-valueRange

**Path:** `cim:ExcDC2A.ka`  
**Name:** C:302:DY:ExcDC2A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.kf-valueRange

**Path:** `cim:ExcDC2A.kf`  
**Name:** C:302:DY:ExcDC2A.kf:valueRange  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.seefd1-valueRange

**Path:** `cim:ExcDC2A.seefd1`  
**Name:** C:302:DY:ExcDC2A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,279.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.seefd2-valueRange

**Path:** `cim:ExcDC2A.seefd2`  
**Name:** C:302:DY:ExcDC2A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,117.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.ta-valueRange

**Path:** `cim:ExcDC2A.ta`  
**Name:** C:302:DY:ExcDC2A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tb-valueRange

**Path:** `cim:ExcDC2A.tb`  
**Name:** C:302:DY:ExcDC2A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tc-valueRange

**Path:** `cim:ExcDC2A.tc`  
**Name:** C:302:DY:ExcDC2A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.te-valueRange

**Path:** `cim:ExcDC2A.te`  
**Name:** C:302:DY:ExcDC2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tf-valueRange

**Path:** `cim:ExcDC2A.tf`  
**Name:** C:302:DY:ExcDC2A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tf1-valueRange

**Path:** `cim:ExcDC2A.tf1`  
**Name:** C:302:DY:ExcDC2A.tf1:valueRange  
Excitation control system stabilizer time constant (Tf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.vrmin-valueRangePair

**Path:** `cim:ExcDC2A.vrmin`  
**Name:** C:302:DY:ExcDC2A.vrmin:valueRangePair  
Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC2A.vrmax).  Typical value = -4,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC2A.vrmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC2A.vrmax` 

## dy302c:ExcDC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC3A

**Nested Properties:**

### dy302c:ExcDC3A.efd1-valueRange

**Path:** `cim:ExcDC3A.efd1`  
**Name:** C:302:DY:ExcDC3A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 2,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.efd2-valueRange

**Path:** `cim:ExcDC3A.efd2`  
**Name:** C:302:DY:ExcDC3A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 3,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.efdmin-valueRangePair

**Path:** `cim:ExcDC3A.efdmin`  
**Name:** C:302:DY:ExcDC3A.efdmin:valueRangePair  
Minimum voltage exciter output limiter (Efdmin) (< ExcDC3A.efdmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC3A.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC3A.efdmax` 

### dy302c:ExcDC3A.kv-valueRange

**Path:** `cim:ExcDC3A.kv`  
**Name:** C:302:DY:ExcDC3A.kv:valueRange  
Fast raise/lower contact setting (Kv) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.seefd1-valueRange

**Path:** `cim:ExcDC3A.seefd1`  
**Name:** C:302:DY:ExcDC3A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.seefd2-valueRange

**Path:** `cim:ExcDC3A.seefd2`  
**Name:** C:302:DY:ExcDC3A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.te-valueRange

**Path:** `cim:ExcDC3A.te`  
**Name:** C:302:DY:ExcDC3A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.trh-valueRange

**Path:** `cim:ExcDC3A.trh`  
**Name:** C:302:DY:ExcDC3A.trh:valueRange  
Rheostat travel time (Trh) (> 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.vrmax-valueRange

**Path:** `cim:ExcDC3A.vrmax`  
**Name:** C:302:DY:ExcDC3A.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.vrmin-valueRange

**Path:** `cim:ExcDC3A.vrmin`  
**Name:** C:302:DY:ExcDC3A.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcDC3A1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC3A1

**Nested Properties:**

### dy302c:ExcDC3A1.ka-valueRange

**Path:** `cim:ExcDC3A1.ka`  
**Name:** C:302:DY:ExcDC3A1.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.kf-valueRange

**Path:** `cim:ExcDC3A1.kf`  
**Name:** C:302:DY:ExcDC3A1.kf:valueRange  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.ki-valueRange

**Path:** `cim:ExcDC3A1.ki`  
**Name:** C:302:DY:ExcDC3A1.ki:valueRange  
Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 4,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.kp-valueRange

**Path:** `cim:ExcDC3A1.kp`  
**Name:** C:302:DY:ExcDC3A1.kp:valueRange  
Potential circuit gain coefficient (Kp) (>= 0).  Typical value = 4,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.ta-valueRange

**Path:** `cim:ExcDC3A1.ta`  
**Name:** C:302:DY:ExcDC3A1.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.te-valueRange

**Path:** `cim:ExcDC3A1.te`  
**Name:** C:302:DY:ExcDC3A1.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.tf-valueRange

**Path:** `cim:ExcDC3A1.tf`  
**Name:** C:302:DY:ExcDC3A1.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vb1max-valueRange

**Path:** `cim:ExcDC3A1.vb1max`  
**Name:** C:302:DY:ExcDC3A1.vb1max:valueRange  
Available exciter voltage limiter (Vb1max) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vbmax-valueRange

**Path:** `cim:ExcDC3A1.vbmax`  
**Name:** C:302:DY:ExcDC3A1.vbmax:valueRange  
Available exciter voltage limiter (Vbmax) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vrmin-valueRangePair

**Path:** `cim:ExcDC3A1.vrmin`  
**Name:** C:302:DY:ExcDC3A1.vrmin:valueRangePair  
Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC3A1.vrmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC3A1.vrmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC3A1.vrmax` 

## dy302c:ExcELIN1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcELIN1

**Nested Properties:**

### dy302c:ExcELIN1.efmin-valueRangePair

**Path:** `cim:ExcELIN1.efmin`  
**Name:** C:302:DY:ExcELIN1.efmin:valueRangePair  
Minimum open circuit excitation voltage (Efmin) (< ExcELIN1.efmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN1.efmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN1.efmax` 

### dy302c:ExcELIN1.tfi-valueRange

**Path:** `cim:ExcELIN1.tfi`  
**Name:** C:302:DY:ExcELIN1.tfi:valueRange  
Current transducer time constant (Tfi) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.tnu-valueRange

**Path:** `cim:ExcELIN1.tnu`  
**Name:** C:302:DY:ExcELIN1.tnu:valueRange  
Controller reset time constant (Tnu) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.ts1-valueRange

**Path:** `cim:ExcELIN1.ts1`  
**Name:** C:302:DY:ExcELIN1.ts1:valueRange  
Stabilizer phase lag time constant (Ts1) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.ts2-valueRange

**Path:** `cim:ExcELIN1.ts2`  
**Name:** C:302:DY:ExcELIN1.ts2:valueRange  
Stabilizer filter time constant (Ts2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.tsw-valueRange

**Path:** `cim:ExcELIN1.tsw`  
**Name:** C:302:DY:ExcELIN1.tsw:valueRange  
Stabilizer parameters (Tsw) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.xe-valueRange

**Path:** `cim:ExcELIN1.xe`  
**Name:** C:302:DY:ExcELIN1.xe:valueRange  
Excitation transformer effective reactance (Xe) (>= 0).  Xe represents the regulation of the transformer/rectifier unit.  Typical value = 0,06.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcELIN2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcELIN2

**Nested Properties:**

### dy302c:ExcELIN2.iefmin-valueRangePair

**Path:** `cim:ExcELIN2.iefmin`  
**Name:** C:302:DY:ExcELIN2.iefmin:valueRangePair  
Limiter (I<sub>efmin</sub>) (< ExcELIN2.iefmax).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN2.iefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN2.iefmax` 

### dy302c:ExcELIN2.seve1-valueRange

**Path:** `cim:ExcELIN2.seve1`  
**Name:** C:302:DY:ExcELIN2.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.seve2-valueRange

**Path:** `cim:ExcELIN2.seve2`  
**Name:** C:302:DY:ExcELIN2.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.tb1-valueRange

**Path:** `cim:ExcELIN2.tb1`  
**Name:** C:302:DY:ExcELIN2.tb1:valueRange  
Voltage controller derivative washout time constant (Tb1) (>= 0).  Typical value = 12,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.te-valueRange

**Path:** `cim:ExcELIN2.te`  
**Name:** C:302:DY:ExcELIN2.te:valueRange  
Time constant (Te) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.te2-valueRange

**Path:** `cim:ExcELIN2.te2`  
**Name:** C:302:DY:ExcELIN2.te2:valueRange  
Time Constant (T<sub>e2</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ti3-valueRange

**Path:** `cim:ExcELIN2.ti3`  
**Name:** C:302:DY:ExcELIN2.ti3:valueRange  
Time constant (T<sub>i3</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ti4-valueRange

**Path:** `cim:ExcELIN2.ti4`  
**Name:** C:302:DY:ExcELIN2.ti4:valueRange  
Time constant (T<sub>i4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.tr4-valueRange

**Path:** `cim:ExcELIN2.tr4`  
**Name:** C:302:DY:ExcELIN2.tr4:valueRange  
Time constant (T<sub>r4</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.upmin-valueRangePair

**Path:** `cim:ExcELIN2.upmin`  
**Name:** C:302:DY:ExcELIN2.upmin:valueRangePair  
Limiter (Upmin) (< ExcELIN2.upmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN2.upmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN2.upmax` 

### dy302c:ExcELIN2.ve1-valueRange

**Path:** `cim:ExcELIN2.ve1`  
**Name:** C:302:DY:ExcELIN2.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ve2-valueRange

**Path:** `cim:ExcELIN2.ve2`  
**Name:** C:302:DY:ExcELIN2.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcHU

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcHU

**Nested Properties:**

### dy302c:ExcHU.emin-valueRangePair

**Path:** `cim:ExcHU.emin`  
**Name:** C:302:DY:ExcHU.emin:valueRangePair  
Field voltage control signal lower limit on AVR base (Emin) (< ExcHU.emax).  Typical value = -0,866.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcHU.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcHU.emax` 

### dy302c:ExcHU.imin-valueRangePair

**Path:** `cim:ExcHU.imin`  
**Name:** C:302:DY:ExcHU.imin:valueRangePair  
Major loop PI tag output signal lower limit (Imin) (< ExcHU.imax).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcHU.imax` 

### dy302c:ExcHU.te-valueRange

**Path:** `cim:ExcHU.te`  
**Name:** C:302:DY:ExcHU.te:valueRange  
Major loop PI tag integration time constant (Te) (>= 0).  Typical value = 0,154.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcHU.ti-valueRange

**Path:** `cim:ExcHU.ti`  
**Name:** C:302:DY:ExcHU.ti:valueRange  
Minor loop PI control tag integration time constant (Ti) (>= 0).  Typical value = 0,01333.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcHU.tr-valueRange

**Path:** `cim:ExcHU.tr`  
**Name:** C:302:DY:ExcHU.tr:valueRange  
Filter time constant (Tr) (>= 0). If a voltage compensator is used in conjunction with this excitation system model, Tr should be set to 0.  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC1A

**Nested Properties:**

### dy302c:ExcIEEEAC1A.ka-valueRange

**Path:** `cim:ExcIEEEAC1A.ka`  
**Name:** C:302:DY:ExcIEEEAC1A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kc-valueRange

**Path:** `cim:ExcIEEEAC1A.kc`  
**Name:** C:302:DY:ExcIEEEAC1A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kd-valueRange

**Path:** `cim:ExcIEEEAC1A.kd`  
**Name:** C:302:DY:ExcIEEEAC1A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,38.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kf-valueRange

**Path:** `cim:ExcIEEEAC1A.kf`  
**Name:** C:302:DY:ExcIEEEAC1A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.seve1-valueRange

**Path:** `cim:ExcIEEEAC1A.seve1`  
**Name:** C:302:DY:ExcIEEEAC1A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.seve2-valueRange

**Path:** `cim:ExcIEEEAC1A.seve2`  
**Name:** C:302:DY:ExcIEEEAC1A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ta-valueRange

**Path:** `cim:ExcIEEEAC1A.ta`  
**Name:** C:302:DY:ExcIEEEAC1A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tb-valueRange

**Path:** `cim:ExcIEEEAC1A.tb`  
**Name:** C:302:DY:ExcIEEEAC1A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tc-valueRange

**Path:** `cim:ExcIEEEAC1A.tc`  
**Name:** C:302:DY:ExcIEEEAC1A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.te-valueRange

**Path:** `cim:ExcIEEEAC1A.te`  
**Name:** C:302:DY:ExcIEEEAC1A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tf-valueRange

**Path:** `cim:ExcIEEEAC1A.tf`  
**Name:** C:302:DY:ExcIEEEAC1A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vamax-valueRange

**Path:** `cim:ExcIEEEAC1A.vamax`  
**Name:** C:302:DY:ExcIEEEAC1A.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vamin-valueRange

**Path:** `cim:ExcIEEEAC1A.vamin`  
**Name:** C:302:DY:ExcIEEEAC1A.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ve1-valueRange

**Path:** `cim:ExcIEEEAC1A.ve1`  
**Name:** C:302:DY:ExcIEEEAC1A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 4,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ve2-valueRange

**Path:** `cim:ExcIEEEAC1A.ve2`  
**Name:** C:302:DY:ExcIEEEAC1A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,14.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC1A.vrmax`  
**Name:** C:302:DY:ExcIEEEAC1A.vrmax:valueRange  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 6,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC1A.vrmin`  
**Name:** C:302:DY:ExcIEEEAC1A.vrmin:valueRange  
Minimum voltage regulator outputs (V<sub>RMIN</sub>) (< 0).  Typical value = -5,43.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC2A

**Nested Properties:**

### dy302c:ExcIEEEAC2A.ka-valueRange

**Path:** `cim:ExcIEEEAC2A.ka`  
**Name:** C:302:DY:ExcIEEEAC2A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kb-valueRange

**Path:** `cim:ExcIEEEAC2A.kb`  
**Name:** C:302:DY:ExcIEEEAC2A.kb:valueRange  
Second stage regulator gain (K<sub>B</sub>) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kc-valueRange

**Path:** `cim:ExcIEEEAC2A.kc`  
**Name:** C:302:DY:ExcIEEEAC2A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,28.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kd-valueRange

**Path:** `cim:ExcIEEEAC2A.kd`  
**Name:** C:302:DY:ExcIEEEAC2A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ke-valueRange

**Path:** `cim:ExcIEEEAC2A.ke`  
**Name:** C:302:DY:ExcIEEEAC2A.ke:valueRange  
Exciter constant related to self-excited field (K<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kf-valueRange

**Path:** `cim:ExcIEEEAC2A.kf`  
**Name:** C:302:DY:ExcIEEEAC2A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kh-valueRange

**Path:** `cim:ExcIEEEAC2A.kh`  
**Name:** C:302:DY:ExcIEEEAC2A.kh:valueRange  
Exciter field current feedback gain (K<sub>H</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.seve1-valueRange

**Path:** `cim:ExcIEEEAC2A.seve1`  
**Name:** C:302:DY:ExcIEEEAC2A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.seve2-valueRange

**Path:** `cim:ExcIEEEAC2A.seve2`  
**Name:** C:302:DY:ExcIEEEAC2A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ta-valueRange

**Path:** `cim:ExcIEEEAC2A.ta`  
**Name:** C:302:DY:ExcIEEEAC2A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tb-valueRange

**Path:** `cim:ExcIEEEAC2A.tb`  
**Name:** C:302:DY:ExcIEEEAC2A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tc-valueRange

**Path:** `cim:ExcIEEEAC2A.tc`  
**Name:** C:302:DY:ExcIEEEAC2A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.te-valueRange

**Path:** `cim:ExcIEEEAC2A.te`  
**Name:** C:302:DY:ExcIEEEAC2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tf-valueRange

**Path:** `cim:ExcIEEEAC2A.tf`  
**Name:** C:302:DY:ExcIEEEAC2A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vamax-valueRange

**Path:** `cim:ExcIEEEAC2A.vamax`  
**Name:** C:302:DY:ExcIEEEAC2A.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vamin-valueRange

**Path:** `cim:ExcIEEEAC2A.vamin`  
**Name:** C:302:DY:ExcIEEEAC2A.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -8.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ve1-valueRange

**Path:** `cim:ExcIEEEAC2A.ve1`  
**Name:** C:302:DY:ExcIEEEAC2A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ve2-valueRange

**Path:** `cim:ExcIEEEAC2A.ve2`  
**Name:** C:302:DY:ExcIEEEAC2A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vfemax-valueRange

**Path:** `cim:ExcIEEEAC2A.vfemax`  
**Name:** C:302:DY:ExcIEEEAC2A.vfemax:valueRange  
Exciter field current limit reference (V<sub>FEMAX</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC2A.vrmax`  
**Name:** C:302:DY:ExcIEEEAC2A.vrmax:valueRange  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 105.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC2A.vrmin`  
**Name:** C:302:DY:ExcIEEEAC2A.vrmin:valueRange  
Minimum voltage regulator outputs (V<sub>RMIN</sub>) (< 0).  Typical value = -95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC3A

**Nested Properties:**

### dy302c:ExcIEEEAC3A.efdn-valueRange

**Path:** `cim:ExcIEEEAC3A.efdn`  
**Name:** C:302:DY:ExcIEEEAC3A.efdn:valueRange  
Value of Efd at which feedback gain changes (E<sub>FDN</sub>) (> 0).  Typical value = 2,36.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ka-valueRange

**Path:** `cim:ExcIEEEAC3A.ka`  
**Name:** C:302:DY:ExcIEEEAC3A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 45,62.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kc-valueRange

**Path:** `cim:ExcIEEEAC3A.kc`  
**Name:** C:302:DY:ExcIEEEAC3A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,104.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kd-valueRange

**Path:** `cim:ExcIEEEAC3A.kd`  
**Name:** C:302:DY:ExcIEEEAC3A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,499.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kf-valueRange

**Path:** `cim:ExcIEEEAC3A.kf`  
**Name:** C:302:DY:ExcIEEEAC3A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kn-valueRange

**Path:** `cim:ExcIEEEAC3A.kn`  
**Name:** C:302:DY:ExcIEEEAC3A.kn:valueRange  
Excitation control system stabilizer gain (K<sub>N</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kr-valueRange

**Path:** `cim:ExcIEEEAC3A.kr`  
**Name:** C:302:DY:ExcIEEEAC3A.kr:valueRange  
Constant associated with regulator and alternator field power supply (K<sub>R</sub>) (> 0).  Typical value = 3,77.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.seve1-valueRange

**Path:** `cim:ExcIEEEAC3A.seve1`  
**Name:** C:302:DY:ExcIEEEAC3A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 1,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.seve2-valueRange

**Path:** `cim:ExcIEEEAC3A.seve2`  
**Name:** C:302:DY:ExcIEEEAC3A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ta-valueRange

**Path:** `cim:ExcIEEEAC3A.ta`  
**Name:** C:302:DY:ExcIEEEAC3A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,013.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tb-valueRange

**Path:** `cim:ExcIEEEAC3A.tb`  
**Name:** C:302:DY:ExcIEEEAC3A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tc-valueRange

**Path:** `cim:ExcIEEEAC3A.tc`  
**Name:** C:302:DY:ExcIEEEAC3A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.te-valueRange

**Path:** `cim:ExcIEEEAC3A.te`  
**Name:** C:302:DY:ExcIEEEAC3A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,17.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tf-valueRange

**Path:** `cim:ExcIEEEAC3A.tf`  
**Name:** C:302:DY:ExcIEEEAC3A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vamax-valueRange

**Path:** `cim:ExcIEEEAC3A.vamax`  
**Name:** C:302:DY:ExcIEEEAC3A.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vamin-valueRange

**Path:** `cim:ExcIEEEAC3A.vamin`  
**Name:** C:302:DY:ExcIEEEAC3A.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ve1-valueRange

**Path:** `cim:ExcIEEEAC3A.ve1`  
**Name:** C:302:DY:ExcIEEEAC3A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ve2-valueRange

**Path:** `cim:ExcIEEEAC3A.ve2`  
**Name:** C:302:DY:ExcIEEEAC3A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 4,68.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vemin-valueRange

**Path:** `cim:ExcIEEEAC3A.vemin`  
**Name:** C:302:DY:ExcIEEEAC3A.vemin:valueRange  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vfemax-valueRange

**Path:** `cim:ExcIEEEAC3A.vfemax`  
**Name:** C:302:DY:ExcIEEEAC3A.vfemax:valueRange  
Exciter field current limit reference (V<sub>FEMAX</sub>) (>= 0).  Typical value = 16.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC4A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC4A

**Nested Properties:**

### dy302c:ExcIEEEAC4A.ka-valueRange

**Path:** `cim:ExcIEEEAC4A.ka`  
**Name:** C:302:DY:ExcIEEEAC4A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.kc-valueRange

**Path:** `cim:ExcIEEEAC4A.kc`  
**Name:** C:302:DY:ExcIEEEAC4A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.ta-valueRange

**Path:** `cim:ExcIEEEAC4A.ta`  
**Name:** C:302:DY:ExcIEEEAC4A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,015.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.tb-valueRange

**Path:** `cim:ExcIEEEAC4A.tb`  
**Name:** C:302:DY:ExcIEEEAC4A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.tc-valueRange

**Path:** `cim:ExcIEEEAC4A.tc`  
**Name:** C:302:DY:ExcIEEEAC4A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vimax-valueRange

**Path:** `cim:ExcIEEEAC4A.vimax`  
**Name:** C:302:DY:ExcIEEEAC4A.vimax:valueRange  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vimin-valueRange

**Path:** `cim:ExcIEEEAC4A.vimin`  
**Name:** C:302:DY:ExcIEEEAC4A.vimin:valueRange  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC4A.vrmax`  
**Name:** C:302:DY:ExcIEEEAC4A.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5,64.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC4A.vrmin`  
**Name:** C:302:DY:ExcIEEEAC4A.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -4,53.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC5A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC5A

**Nested Properties:**

### dy302c:ExcIEEEAC5A.efd1-valueRange

**Path:** `cim:ExcIEEEAC5A.efd1`  
**Name:** C:302:DY:ExcIEEEAC5A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 5,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.efd2-valueRange

**Path:** `cim:ExcIEEEAC5A.efd2`  
**Name:** C:302:DY:ExcIEEEAC5A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 4,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.ka-valueRange

**Path:** `cim:ExcIEEEAC5A.ka`  
**Name:** C:302:DY:ExcIEEEAC5A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.kf-valueRange

**Path:** `cim:ExcIEEEAC5A.kf`  
**Name:** C:302:DY:ExcIEEEAC5A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.seefd1-valueRange

**Path:** `cim:ExcIEEEAC5A.seefd1`  
**Name:** C:302:DY:ExcIEEEAC5A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,86.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.seefd2-valueRange

**Path:** `cim:ExcIEEEAC5A.seefd2`  
**Name:** C:302:DY:ExcIEEEAC5A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.ta-valueRange

**Path:** `cim:ExcIEEEAC5A.ta`  
**Name:** C:302:DY:ExcIEEEAC5A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.te-valueRange

**Path:** `cim:ExcIEEEAC5A.te`  
**Name:** C:302:DY:ExcIEEEAC5A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf1-valueRange

**Path:** `cim:ExcIEEEAC5A.tf1`  
**Name:** C:302:DY:ExcIEEEAC5A.tf1:valueRange  
Excitation control system stabilizer time constant (T<sub>F1</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf2-valueRange

**Path:** `cim:ExcIEEEAC5A.tf2`  
**Name:** C:302:DY:ExcIEEEAC5A.tf2:valueRange  
Excitation control system stabilizer time constant (T<sub>F2</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf3-valueRange

**Path:** `cim:ExcIEEEAC5A.tf3`  
**Name:** C:302:DY:ExcIEEEAC5A.tf3:valueRange  
Excitation control system stabilizer time constant (T<sub>F3</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC5A.vrmax`  
**Name:** C:302:DY:ExcIEEEAC5A.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC5A.vrmin`  
**Name:** C:302:DY:ExcIEEEAC5A.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC6A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC6A

**Nested Properties:**

### dy302c:ExcIEEEAC6A.ka-valueRange

**Path:** `cim:ExcIEEEAC6A.ka`  
**Name:** C:302:DY:ExcIEEEAC6A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 536.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kc-valueRange

**Path:** `cim:ExcIEEEAC6A.kc`  
**Name:** C:302:DY:ExcIEEEAC6A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kd-valueRange

**Path:** `cim:ExcIEEEAC6A.kd`  
**Name:** C:302:DY:ExcIEEEAC6A.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 1,91.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kh-valueRange

**Path:** `cim:ExcIEEEAC6A.kh`  
**Name:** C:302:DY:ExcIEEEAC6A.kh:valueRange  
Exciter field current limiter gain (K<sub>H</sub>) (>= 0).  Typical value = 92.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.seve1-valueRange

**Path:** `cim:ExcIEEEAC6A.seve1`  
**Name:** C:302:DY:ExcIEEEAC6A.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,214.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.seve2-valueRange

**Path:** `cim:ExcIEEEAC6A.seve2`  
**Name:** C:302:DY:ExcIEEEAC6A.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,044.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ta-valueRange

**Path:** `cim:ExcIEEEAC6A.ta`  
**Name:** C:302:DY:ExcIEEEAC6A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tb-valueRange

**Path:** `cim:ExcIEEEAC6A.tb`  
**Name:** C:302:DY:ExcIEEEAC6A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tc-valueRange

**Path:** `cim:ExcIEEEAC6A.tc`  
**Name:** C:302:DY:ExcIEEEAC6A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.te-valueRange

**Path:** `cim:ExcIEEEAC6A.te`  
**Name:** C:302:DY:ExcIEEEAC6A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.th-valueRange

**Path:** `cim:ExcIEEEAC6A.th`  
**Name:** C:302:DY:ExcIEEEAC6A.th:valueRange  
Exciter field current limiter time constant (T<sub>H</sub>) (> 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tj-valueRange

**Path:** `cim:ExcIEEEAC6A.tj`  
**Name:** C:302:DY:ExcIEEEAC6A.tj:valueRange  
Exciter field current limiter time constant (T<sub>J</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tk-valueRange

**Path:** `cim:ExcIEEEAC6A.tk`  
**Name:** C:302:DY:ExcIEEEAC6A.tk:valueRange  
Voltage regulator time constant (T<sub>K</sub>) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vamax-valueRange

**Path:** `cim:ExcIEEEAC6A.vamax`  
**Name:** C:302:DY:ExcIEEEAC6A.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vamin-valueRange

**Path:** `cim:ExcIEEEAC6A.vamin`  
**Name:** C:302:DY:ExcIEEEAC6A.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -75.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ve1-valueRange

**Path:** `cim:ExcIEEEAC6A.ve1`  
**Name:** C:302:DY:ExcIEEEAC6A.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 7,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ve2-valueRange

**Path:** `cim:ExcIEEEAC6A.ve2`  
**Name:** C:302:DY:ExcIEEEAC6A.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 5,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vfelim-valueRange

**Path:** `cim:ExcIEEEAC6A.vfelim`  
**Name:** C:302:DY:ExcIEEEAC6A.vfelim:valueRange  
Exciter field current limit reference (V<sub>FELIM</sub>) (> 0).  Typical value = 19.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vhmax-valueRange

**Path:** `cim:ExcIEEEAC6A.vhmax`  
**Name:** C:302:DY:ExcIEEEAC6A.vhmax:valueRange  
Maximum field current limiter signal reference (V<sub>HMAX</sub>) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC6A.vrmax`  
**Name:** C:302:DY:ExcIEEEAC6A.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC6A.vrmin`  
**Name:** C:302:DY:ExcIEEEAC6A.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -36.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC7B

**Nested Properties:**

### dy302c:ExcIEEEAC7B.kc-valueRange

**Path:** `cim:ExcIEEEAC7B.kc`  
**Name:** C:302:DY:ExcIEEEAC7B.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kd-valueRange

**Path:** `cim:ExcIEEEAC7B.kd`  
**Name:** C:302:DY:ExcIEEEAC7B.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kdr-valueRange

**Path:** `cim:ExcIEEEAC7B.kdr`  
**Name:** C:302:DY:ExcIEEEAC7B.kdr:valueRange  
Voltage regulator derivative gain (K<sub>DR</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf1-valueRange

**Path:** `cim:ExcIEEEAC7B.kf1`  
**Name:** C:302:DY:ExcIEEEAC7B.kf1:valueRange  
Excitation control system stabilizer gain (K<sub>F1</sub>) (>= 0).  Typical value = 0,212.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf2-valueRange

**Path:** `cim:ExcIEEEAC7B.kf2`  
**Name:** C:302:DY:ExcIEEEAC7B.kf2:valueRange  
Excitation control system stabilizer gain (K<sub>F2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf3-valueRange

**Path:** `cim:ExcIEEEAC7B.kf3`  
**Name:** C:302:DY:ExcIEEEAC7B.kf3:valueRange  
Excitation control system stabilizer gain (K<sub>F3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kia-valueRange

**Path:** `cim:ExcIEEEAC7B.kia`  
**Name:** C:302:DY:ExcIEEEAC7B.kia:valueRange  
Voltage regulator integral gain (K<sub>IA</sub>) (>= 0).  Typical value = 59,69.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kir-valueRange

**Path:** `cim:ExcIEEEAC7B.kir`  
**Name:** C:302:DY:ExcIEEEAC7B.kir:valueRange  
Voltage regulator integral gain (K<sub>IR</sub>) (>= 0).  Typical value = 4,24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kp-valueRange

**Path:** `cim:ExcIEEEAC7B.kp`  
**Name:** C:302:DY:ExcIEEEAC7B.kp:valueRange  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 4,96.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.seve1-valueRange

**Path:** `cim:ExcIEEEAC7B.seve1`  
**Name:** C:302:DY:ExcIEEEAC7B.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.seve2-valueRange

**Path:** `cim:ExcIEEEAC7B.seve2`  
**Name:** C:302:DY:ExcIEEEAC7B.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.tdr-valueRange

**Path:** `cim:ExcIEEEAC7B.tdr`  
**Name:** C:302:DY:ExcIEEEAC7B.tdr:valueRange  
Lag time constant (T<sub>DR</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.te-valueRange

**Path:** `cim:ExcIEEEAC7B.te`  
**Name:** C:302:DY:ExcIEEEAC7B.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.tf-valueRange

**Path:** `cim:ExcIEEEAC7B.tf`  
**Name:** C:302:DY:ExcIEEEAC7B.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vamax-valueRange

**Path:** `cim:ExcIEEEAC7B.vamax`  
**Name:** C:302:DY:ExcIEEEAC7B.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vamin-valueRange

**Path:** `cim:ExcIEEEAC7B.vamin`  
**Name:** C:302:DY:ExcIEEEAC7B.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.ve1-valueRange

**Path:** `cim:ExcIEEEAC7B.ve1`  
**Name:** C:302:DY:ExcIEEEAC7B.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.ve2-valueRange

**Path:** `cim:ExcIEEEAC7B.ve2`  
**Name:** C:302:DY:ExcIEEEAC7B.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vemin-valueRange

**Path:** `cim:ExcIEEEAC7B.vemin`  
**Name:** C:302:DY:ExcIEEEAC7B.vemin:valueRange  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vrmax-valueRange

**Path:** `cim:ExcIEEEAC7B.vrmax`  
**Name:** C:302:DY:ExcIEEEAC7B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5,79.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vrmin-valueRange

**Path:** `cim:ExcIEEEAC7B.vrmin`  
**Name:** C:302:DY:ExcIEEEAC7B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -5,79.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEAC8B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC8B

**Nested Properties:**

### dy302c:ExcIEEEAC8B.ka-valueRange

**Path:** `cim:ExcIEEEAC8B.ka`  
**Name:** C:302:DY:ExcIEEEAC8B.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kc-valueRange

**Path:** `cim:ExcIEEEAC8B.kc`  
**Name:** C:302:DY:ExcIEEEAC8B.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kd-valueRange

**Path:** `cim:ExcIEEEAC8B.kd`  
**Name:** C:302:DY:ExcIEEEAC8B.kd:valueRange  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kdr-valueRange

**Path:** `cim:ExcIEEEAC8B.kdr`  
**Name:** C:302:DY:ExcIEEEAC8B.kdr:valueRange  
Voltage regulator derivative gain (K<sub>DR</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kir-valueRange

**Path:** `cim:ExcIEEEAC8B.kir`  
**Name:** C:302:DY:ExcIEEEAC8B.kir:valueRange  
Voltage regulator integral gain (K<sub>IR</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.seve1-valueRange

**Path:** `cim:ExcIEEEAC8B.seve1`  
**Name:** C:302:DY:ExcIEEEAC8B.seve1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.seve2-valueRange

**Path:** `cim:ExcIEEEAC8B.seve2`  
**Name:** C:302:DY:ExcIEEEAC8B.seve2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ta-valueRange

**Path:** `cim:ExcIEEEAC8B.ta`  
**Name:** C:302:DY:ExcIEEEAC8B.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.tdr-valueRange

**Path:** `cim:ExcIEEEAC8B.tdr`  
**Name:** C:302:DY:ExcIEEEAC8B.tdr:valueRange  
Lag time constant (T<sub>DR</sub>) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.te-valueRange

**Path:** `cim:ExcIEEEAC8B.te`  
**Name:** C:302:DY:ExcIEEEAC8B.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ve1-valueRange

**Path:** `cim:ExcIEEEAC8B.ve1`  
**Name:** C:302:DY:ExcIEEEAC8B.ve1:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ve2-valueRange

**Path:** `cim:ExcIEEEAC8B.ve2`  
**Name:** C:302:DY:ExcIEEEAC8B.ve2:valueRange  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vemin-valueRange

**Path:** `cim:ExcIEEEAC8B.vemin`  
**Name:** C:302:DY:ExcIEEEAC8B.vemin:valueRange  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vrmax-valueRange

**Path:** `cim:ExcIEEEAC8B.vrmax`  
**Name:** C:302:DY:ExcIEEEAC8B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vrmin-valueRange

**Path:** `cim:ExcIEEEAC8B.vrmin`  
**Name:** C:302:DY:ExcIEEEAC8B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEDC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC1A

**Nested Properties:**

### dy302c:ExcIEEEDC1A.efd1-valueRange

**Path:** `cim:ExcIEEEDC1A.efd1`  
**Name:** C:302:DY:ExcIEEEDC1A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.efd2-valueRange

**Path:** `cim:ExcIEEEDC1A.efd2`  
**Name:** C:302:DY:ExcIEEEDC1A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.ka-valueRange

**Path:** `cim:ExcIEEEDC1A.ka`  
**Name:** C:302:DY:ExcIEEEDC1A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.kf-valueRange

**Path:** `cim:ExcIEEEDC1A.kf`  
**Name:** C:302:DY:ExcIEEEDC1A.kf:valueRange  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0.1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC1A.seefd1`  
**Name:** C:302:DY:ExcIEEEDC1A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0.33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC1A.seefd2`  
**Name:** C:302:DY:ExcIEEEDC1A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.ta-valueRange

**Path:** `cim:ExcIEEEDC1A.ta`  
**Name:** C:302:DY:ExcIEEEDC1A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,06.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tb-valueRange

**Path:** `cim:ExcIEEEDC1A.tb`  
**Name:** C:302:DY:ExcIEEEDC1A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tc-valueRange

**Path:** `cim:ExcIEEEDC1A.tc`  
**Name:** C:302:DY:ExcIEEEDC1A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.te-valueRange

**Path:** `cim:ExcIEEEDC1A.te`  
**Name:** C:302:DY:ExcIEEEDC1A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tf-valueRange

**Path:** `cim:ExcIEEEDC1A.tf`  
**Name:** C:302:DY:ExcIEEEDC1A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC1A.vrmin`  
**Name:** C:302:DY:ExcIEEEDC1A.vrmin:valueRangePair  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0 and < ExcIEEEDC1A.vrmax).  Typical value = -0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcIEEEDC1A.vrmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcIEEEDC1A.vrmax` 

## dy302c:ExcIEEEDC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC2A

**Nested Properties:**

### dy302c:ExcIEEEDC2A.efd1-valueRange

**Path:** `cim:ExcIEEEDC2A.efd1`  
**Name:** C:302:DY:ExcIEEEDC2A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.efd2-valueRange

**Path:** `cim:ExcIEEEDC2A.efd2`  
**Name:** C:302:DY:ExcIEEEDC2A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,29.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.ka-valueRange

**Path:** `cim:ExcIEEEDC2A.ka`  
**Name:** C:302:DY:ExcIEEEDC2A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.kf-valueRange

**Path:** `cim:ExcIEEEDC2A.kf`  
**Name:** C:302:DY:ExcIEEEDC2A.kf:valueRange  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC2A.seefd1`  
**Name:** C:302:DY:ExcIEEEDC2A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,279.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC2A.seefd2`  
**Name:** C:302:DY:ExcIEEEDC2A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,117.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.ta-valueRange

**Path:** `cim:ExcIEEEDC2A.ta`  
**Name:** C:302:DY:ExcIEEEDC2A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tb-valueRange

**Path:** `cim:ExcIEEEDC2A.tb`  
**Name:** C:302:DY:ExcIEEEDC2A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tc-valueRange

**Path:** `cim:ExcIEEEDC2A.tc`  
**Name:** C:302:DY:ExcIEEEDC2A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.te-valueRange

**Path:** `cim:ExcIEEEDC2A.te`  
**Name:** C:302:DY:ExcIEEEDC2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tf-valueRange

**Path:** `cim:ExcIEEEDC2A.tf`  
**Name:** C:302:DY:ExcIEEEDC2A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC2A.vrmin`  
**Name:** C:302:DY:ExcIEEEDC2A.vrmin:valueRangePair  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0 and < ExcIEEEDC2A.vrmax).  Typical value = -4,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcIEEEDC2A.vrmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcIEEEDC2A.vrmax` 

## dy302c:ExcIEEEDC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC3A

**Nested Properties:**

### dy302c:ExcIEEEDC3A.efd1-valueRange

**Path:** `cim:ExcIEEEDC3A.efd1`  
**Name:** C:302:DY:ExcIEEEDC3A.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,375.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.efd2-valueRange

**Path:** `cim:ExcIEEEDC3A.efd2`  
**Name:** C:302:DY:ExcIEEEDC3A.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 3,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.kv-valueRange

**Path:** `cim:ExcIEEEDC3A.kv`  
**Name:** C:302:DY:ExcIEEEDC3A.kv:valueRange  
Fast raise/lower contact setting (K<sub>V</sub>) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC3A.seefd1`  
**Name:** C:302:DY:ExcIEEEDC3A.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,267.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC3A.seefd2`  
**Name:** C:302:DY:ExcIEEEDC3A.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,068.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.te-valueRange

**Path:** `cim:ExcIEEEDC3A.te`  
**Name:** C:302:DY:ExcIEEEDC3A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.trh-valueRange

**Path:** `cim:ExcIEEEDC3A.trh`  
**Name:** C:302:DY:ExcIEEEDC3A.trh:valueRange  
Rheostat travel time (T<sub>RH</sub>) (> 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.vrmax-valueRange

**Path:** `cim:ExcIEEEDC3A.vrmax`  
**Name:** C:302:DY:ExcIEEEDC3A.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.vrmin-valueRange

**Path:** `cim:ExcIEEEDC3A.vrmin`  
**Name:** C:302:DY:ExcIEEEDC3A.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEDC4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC4B

**Nested Properties:**

### dy302c:ExcIEEEDC4B.efd1-valueRange

**Path:** `cim:ExcIEEEDC4B.efd1`  
**Name:** C:302:DY:ExcIEEEDC4B.efd1:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 1,75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.efd2-valueRange

**Path:** `cim:ExcIEEEDC4B.efd2`  
**Name:** C:302:DY:ExcIEEEDC4B.efd2:valueRange  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ka-valueRange

**Path:** `cim:ExcIEEEDC4B.ka`  
**Name:** C:302:DY:ExcIEEEDC4B.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kd-valueRange

**Path:** `cim:ExcIEEEDC4B.kd`  
**Name:** C:302:DY:ExcIEEEDC4B.kd:valueRange  
Regulator derivative gain (K<sub>D</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kf-valueRange

**Path:** `cim:ExcIEEEDC4B.kf`  
**Name:** C:302:DY:ExcIEEEDC4B.kf:valueRange  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ki-valueRange

**Path:** `cim:ExcIEEEDC4B.ki`  
**Name:** C:302:DY:ExcIEEEDC4B.ki:valueRange  
Regulator integral gain (K<sub>I</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kp-valueRange

**Path:** `cim:ExcIEEEDC4B.kp`  
**Name:** C:302:DY:ExcIEEEDC4B.kp:valueRange  
Regulator proportional gain (K<sub>P</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.seefd1-valueRange

**Path:** `cim:ExcIEEEDC4B.seefd1`  
**Name:** C:302:DY:ExcIEEEDC4B.seefd1:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.seefd2-valueRange

**Path:** `cim:ExcIEEEDC4B.seefd2`  
**Name:** C:302:DY:ExcIEEEDC4B.seefd2:valueRange  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,27.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ta-valueRange

**Path:** `cim:ExcIEEEDC4B.ta`  
**Name:** C:302:DY:ExcIEEEDC4B.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.te-valueRange

**Path:** `cim:ExcIEEEDC4B.te`  
**Name:** C:302:DY:ExcIEEEDC4B.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.tf-valueRange

**Path:** `cim:ExcIEEEDC4B.tf`  
**Name:** C:302:DY:ExcIEEEDC4B.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.vemin-valueRange

**Path:** `cim:ExcIEEEDC4B.vemin`  
**Name:** C:302:DY:ExcIEEEDC4B.vemin:valueRange  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC4B.vrmin`  
**Name:** C:302:DY:ExcIEEEDC4B.vrmin:valueRangePair  
Minimum voltage regulator output (V<sub>RMIN</sub>) (<= 0 and < ExcIEEEDC4B.vrmax).  Typical value = -0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcIEEEDC4B.vrmax; or positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcIEEEDC4B.vrmax` 

## dy302c:ExcIEEEST1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST1A

**Nested Properties:**

### dy302c:ExcIEEEST1A.ka-valueRange

**Path:** `cim:ExcIEEEST1A.ka`  
**Name:** C:302:DY:ExcIEEEST1A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 190.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.kc-valueRange

**Path:** `cim:ExcIEEEST1A.kc`  
**Name:** C:302:DY:ExcIEEEST1A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.kf-valueRange

**Path:** `cim:ExcIEEEST1A.kf`  
**Name:** C:302:DY:ExcIEEEST1A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.ta-valueRange

**Path:** `cim:ExcIEEEST1A.ta`  
**Name:** C:302:DY:ExcIEEEST1A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tb-valueRange

**Path:** `cim:ExcIEEEST1A.tb`  
**Name:** C:302:DY:ExcIEEEST1A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tb1-valueRange

**Path:** `cim:ExcIEEEST1A.tb1`  
**Name:** C:302:DY:ExcIEEEST1A.tb1:valueRange  
Voltage regulator time constant (T<sub>B1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tc-valueRange

**Path:** `cim:ExcIEEEST1A.tc`  
**Name:** C:302:DY:ExcIEEEST1A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tc1-valueRange

**Path:** `cim:ExcIEEEST1A.tc1`  
**Name:** C:302:DY:ExcIEEEST1A.tc1:valueRange  
Voltage regulator time constant (T<sub>C1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tf-valueRange

**Path:** `cim:ExcIEEEST1A.tf`  
**Name:** C:302:DY:ExcIEEEST1A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vamax-valueRange

**Path:** `cim:ExcIEEEST1A.vamax`  
**Name:** C:302:DY:ExcIEEEST1A.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vamin-valueRange

**Path:** `cim:ExcIEEEST1A.vamin`  
**Name:** C:302:DY:ExcIEEEST1A.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vimax-valueRange

**Path:** `cim:ExcIEEEST1A.vimax`  
**Name:** C:302:DY:ExcIEEEST1A.vimax:valueRange  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vimin-valueRange

**Path:** `cim:ExcIEEEST1A.vimin`  
**Name:** C:302:DY:ExcIEEEST1A.vimin:valueRange  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vrmax-valueRange

**Path:** `cim:ExcIEEEST1A.vrmax`  
**Name:** C:302:DY:ExcIEEEST1A.vrmax:valueRange  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 7,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vrmin-valueRange

**Path:** `cim:ExcIEEEST1A.vrmin`  
**Name:** C:302:DY:ExcIEEEST1A.vrmin:valueRange  
Minimum voltage regulator outputs (V<sub>RMIN</sub>) (< 0).  Typical value = -6,7.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST2A

**Nested Properties:**

### dy302c:ExcIEEEST2A.efdmax-valueRange

**Path:** `cim:ExcIEEEST2A.efdmax`  
**Name:** C:302:DY:ExcIEEEST2A.efdmax:valueRange  
Maximum field voltage (E<sub>FDMax</sub>) (>= 0).  Typical value = 99.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ka-valueRange

**Path:** `cim:ExcIEEEST2A.ka`  
**Name:** C:302:DY:ExcIEEEST2A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kc-valueRange

**Path:** `cim:ExcIEEEST2A.kc`  
**Name:** C:302:DY:ExcIEEEST2A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 1,82.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kf-valueRange

**Path:** `cim:ExcIEEEST2A.kf`  
**Name:** C:302:DY:ExcIEEEST2A.kf:valueRange  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ki-valueRange

**Path:** `cim:ExcIEEEST2A.ki`  
**Name:** C:302:DY:ExcIEEEST2A.ki:valueRange  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kp-valueRange

**Path:** `cim:ExcIEEEST2A.kp`  
**Name:** C:302:DY:ExcIEEEST2A.kp:valueRange  
Potential circuit gain coefficient (K<sub>P</sub>) (>= 0).  Typical value = 4,88.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ta-valueRange

**Path:** `cim:ExcIEEEST2A.ta`  
**Name:** C:302:DY:ExcIEEEST2A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.te-valueRange

**Path:** `cim:ExcIEEEST2A.te`  
**Name:** C:302:DY:ExcIEEEST2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.tf-valueRange

**Path:** `cim:ExcIEEEST2A.tf`  
**Name:** C:302:DY:ExcIEEEST2A.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.vrmax-valueRange

**Path:** `cim:ExcIEEEST2A.vrmax`  
**Name:** C:302:DY:ExcIEEEST2A.vrmax:valueRange  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.vrmin-valueRange

**Path:** `cim:ExcIEEEST2A.vrmin`  
**Name:** C:302:DY:ExcIEEEST2A.vrmin:valueRange  
Minimum voltage regulator outputs (V<sub>RMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST3A

**Nested Properties:**

### dy302c:ExcIEEEST3A.ka-valueRange

**Path:** `cim:ExcIEEEST3A.ka`  
**Name:** C:302:DY:ExcIEEEST3A.ka:valueRange  
Voltage regulator gain (K<sub>A</sub>) (> 0). This is parameter K in the IEEE standard. Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kc-valueRange

**Path:** `cim:ExcIEEEST3A.kc`  
**Name:** C:302:DY:ExcIEEEST3A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kg-valueRange

**Path:** `cim:ExcIEEEST3A.kg`  
**Name:** C:302:DY:ExcIEEEST3A.kg:valueRange  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.ki-valueRange

**Path:** `cim:ExcIEEEST3A.ki`  
**Name:** C:302:DY:ExcIEEEST3A.ki:valueRange  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.km-valueRange

**Path:** `cim:ExcIEEEST3A.km`  
**Name:** C:302:DY:ExcIEEEST3A.km:valueRange  
Forward gain constant of the inner loop field regulator (K<sub>M</sub>) (> 0).  Typical value = 7,93.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kp-valueRange

**Path:** `cim:ExcIEEEST3A.kp`  
**Name:** C:302:DY:ExcIEEEST3A.kp:valueRange  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 6,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.ta-valueRange

**Path:** `cim:ExcIEEEST3A.ta`  
**Name:** C:302:DY:ExcIEEEST3A.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tb-valueRange

**Path:** `cim:ExcIEEEST3A.tb`  
**Name:** C:302:DY:ExcIEEEST3A.tb:valueRange  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tc-valueRange

**Path:** `cim:ExcIEEEST3A.tc`  
**Name:** C:302:DY:ExcIEEEST3A.tc:valueRange  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tm-valueRange

**Path:** `cim:ExcIEEEST3A.tm`  
**Name:** C:302:DY:ExcIEEEST3A.tm:valueRange  
Forward time constant of inner loop field regulator (T<sub>M</sub>) (> 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vbmax-valueRange

**Path:** `cim:ExcIEEEST3A.vbmax`  
**Name:** C:302:DY:ExcIEEEST3A.vbmax:valueRange  
Maximum excitation voltage (V<sub>BMax</sub>) (> 0).  Typical value = 6,9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vgmax-valueRange

**Path:** `cim:ExcIEEEST3A.vgmax`  
**Name:** C:302:DY:ExcIEEEST3A.vgmax:valueRange  
Maximum inner loop feedback voltage (V<sub>GMax</sub>) (>= 0).  Typical value = 5,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vimax-valueRange

**Path:** `cim:ExcIEEEST3A.vimax`  
**Name:** C:302:DY:ExcIEEEST3A.vimax:valueRange  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vimin-valueRange

**Path:** `cim:ExcIEEEST3A.vimin`  
**Name:** C:302:DY:ExcIEEEST3A.vimin:valueRange  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vmmax-valueRange

**Path:** `cim:ExcIEEEST3A.vmmax`  
**Name:** C:302:DY:ExcIEEEST3A.vmmax:valueRange  
Maximum inner loop output (V<sub>MMax</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vmmin-valueRange

**Path:** `cim:ExcIEEEST3A.vmmin`  
**Name:** C:302:DY:ExcIEEEST3A.vmmin:valueRange  
Minimum inner loop output (V<sub>MMin</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vrmax-valueRange

**Path:** `cim:ExcIEEEST3A.vrmax`  
**Name:** C:302:DY:ExcIEEEST3A.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vrmin-valueRange

**Path:** `cim:ExcIEEEST3A.vrmin`  
**Name:** C:302:DY:ExcIEEEST3A.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.xl-valueRange

**Path:** `cim:ExcIEEEST3A.xl`  
**Name:** C:302:DY:ExcIEEEST3A.xl:valueRange  
Reactance associated with potential source (X<sub>L</sub>) (>= 0).  Typical value = 0,081.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST4B

**Nested Properties:**

### dy302c:ExcIEEEST4B.kc-valueRange

**Path:** `cim:ExcIEEEST4B.kc`  
**Name:** C:302:DY:ExcIEEEST4B.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,113.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.kg-valueRange

**Path:** `cim:ExcIEEEST4B.kg`  
**Name:** C:302:DY:ExcIEEEST4B.kg:valueRange  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.ki-valueRange

**Path:** `cim:ExcIEEEST4B.ki`  
**Name:** C:302:DY:ExcIEEEST4B.ki:valueRange  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.kp-valueRange

**Path:** `cim:ExcIEEEST4B.kp`  
**Name:** C:302:DY:ExcIEEEST4B.kp:valueRange  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 9,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.ta-valueRange

**Path:** `cim:ExcIEEEST4B.ta`  
**Name:** C:302:DY:ExcIEEEST4B.ta:valueRange  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vbmax-valueRange

**Path:** `cim:ExcIEEEST4B.vbmax`  
**Name:** C:302:DY:ExcIEEEST4B.vbmax:valueRange  
Maximum excitation voltage (V<sub>BMax</sub>) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vmmin-valueRangePair

**Path:** `cim:ExcIEEEST4B.vmmin`  
**Name:** C:302:DY:ExcIEEEST4B.vmmin:valueRangePair  
Minimum inner loop output (V<sub>MMin</sub>) (< ExcIEEEST4B.vmmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcIEEEST4B.vmmax; or positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcIEEEST4B.vmmax` 

### dy302c:ExcIEEEST4B.vrmax-valueRange

**Path:** `cim:ExcIEEEST4B.vrmax`  
**Name:** C:302:DY:ExcIEEEST4B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vrmin-valueRange

**Path:** `cim:ExcIEEEST4B.vrmin`  
**Name:** C:302:DY:ExcIEEEST4B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.xl-valueRange

**Path:** `cim:ExcIEEEST4B.xl`  
**Name:** C:302:DY:ExcIEEEST4B.xl:valueRange  
Reactance associated with potential source (X<sub>L</sub>) (>= 0).  Typical value = 0,124.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST5B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST5B

**Nested Properties:**

### dy302c:ExcIEEEST5B.kc-valueRange

**Path:** `cim:ExcIEEEST5B.kc`  
**Name:** C:302:DY:ExcIEEEST5B.kc:valueRange  
Rectifier regulation factor (K<sub>C</sub>) (>= 0).  Typical value = 0,004.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.kr-valueRange

**Path:** `cim:ExcIEEEST5B.kr`  
**Name:** C:302:DY:ExcIEEEST5B.kr:valueRange  
Regulator gain (K<sub>R</sub>) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.t1-valueRange

**Path:** `cim:ExcIEEEST5B.t1`  
**Name:** C:302:DY:ExcIEEEST5B.t1:valueRange  
Firing circuit time constant (T1) (>= 0).  Typical value = 0,004.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tb1-valueRange

**Path:** `cim:ExcIEEEST5B.tb1`  
**Name:** C:302:DY:ExcIEEEST5B.tb1:valueRange  
Regulator lag time constant (T<sub>B1</sub>) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tb2-valueRange

**Path:** `cim:ExcIEEEST5B.tb2`  
**Name:** C:302:DY:ExcIEEEST5B.tb2:valueRange  
Regulator lag time constant (T<sub>B2</sub>) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tc1-valueRange

**Path:** `cim:ExcIEEEST5B.tc1`  
**Name:** C:302:DY:ExcIEEEST5B.tc1:valueRange  
Regulator lead time constant (T<sub>C1</sub>) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tc2-valueRange

**Path:** `cim:ExcIEEEST5B.tc2`  
**Name:** C:302:DY:ExcIEEEST5B.tc2:valueRange  
Regulator lead time constant (T<sub>C2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tob1-valueRange

**Path:** `cim:ExcIEEEST5B.tob1`  
**Name:** C:302:DY:ExcIEEEST5B.tob1:valueRange  
OEL lag time constant (T<sub>OB1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tob2-valueRange

**Path:** `cim:ExcIEEEST5B.tob2`  
**Name:** C:302:DY:ExcIEEEST5B.tob2:valueRange  
OEL lag time constant (T<sub>OB2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.toc1-valueRange

**Path:** `cim:ExcIEEEST5B.toc1`  
**Name:** C:302:DY:ExcIEEEST5B.toc1:valueRange  
OEL lead time constant (T<sub>OC1</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.toc2-valueRange

**Path:** `cim:ExcIEEEST5B.toc2`  
**Name:** C:302:DY:ExcIEEEST5B.toc2:valueRange  
OEL lead time constant (T<sub>OC2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tub1-valueRange

**Path:** `cim:ExcIEEEST5B.tub1`  
**Name:** C:302:DY:ExcIEEEST5B.tub1:valueRange  
UEL lag time constant (T<sub>UB1</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tub2-valueRange

**Path:** `cim:ExcIEEEST5B.tub2`  
**Name:** C:302:DY:ExcIEEEST5B.tub2:valueRange  
UEL lag time constant (T<sub>UB2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tuc1-valueRange

**Path:** `cim:ExcIEEEST5B.tuc1`  
**Name:** C:302:DY:ExcIEEEST5B.tuc1:valueRange  
UEL lead time constant (T<sub>UC1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tuc2-valueRange

**Path:** `cim:ExcIEEEST5B.tuc2`  
**Name:** C:302:DY:ExcIEEEST5B.tuc2:valueRange  
UEL lead time constant (T<sub>UC2</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.vrmax-valueRange

**Path:** `cim:ExcIEEEST5B.vrmax`  
**Name:** C:302:DY:ExcIEEEST5B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.vrmin-valueRange

**Path:** `cim:ExcIEEEST5B.vrmin`  
**Name:** C:302:DY:ExcIEEEST5B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -4.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST6B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST6B

**Nested Properties:**

### dy302c:ExcIEEEST6B.ilr-valueRange

**Path:** `cim:ExcIEEEST6B.ilr`  
**Name:** C:302:DY:ExcIEEEST6B.ilr:valueRange  
Exciter output current limit reference (I<sub>LR</sub>) (> 0).  Typical value = 4,164.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kci-valueRange

**Path:** `cim:ExcIEEEST6B.kci`  
**Name:** C:302:DY:ExcIEEEST6B.kci:valueRange  
Exciter output current limit adjustment (K<sub>CI</sub>) (> 0).  Typical value = 1,0577.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kg-valueRange

**Path:** `cim:ExcIEEEST6B.kg`  
**Name:** C:302:DY:ExcIEEEST6B.kg:valueRange  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kia-valueRange

**Path:** `cim:ExcIEEEST6B.kia`  
**Name:** C:302:DY:ExcIEEEST6B.kia:valueRange  
Voltage regulator integral gain (K<sub>IA</sub>) (> 0).  Typical value = 45,094.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.klr-valueRange

**Path:** `cim:ExcIEEEST6B.klr`  
**Name:** C:302:DY:ExcIEEEST6B.klr:valueRange  
Exciter output current limiter gain (K<sub>LR</sub>) (> 0).  Typical value = 17,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kpa-valueRange

**Path:** `cim:ExcIEEEST6B.kpa`  
**Name:** C:302:DY:ExcIEEEST6B.kpa:valueRange  
Voltage regulator proportional gain (<u>K</u><u><sub>PA</sub></u>) (> 0).  Typical value = 18,038.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.tg-valueRange

**Path:** `cim:ExcIEEEST6B.tg`  
**Name:** C:302:DY:ExcIEEEST6B.tg:valueRange  
Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vamax-valueRange

**Path:** `cim:ExcIEEEST6B.vamax`  
**Name:** C:302:DY:ExcIEEEST6B.vamax:valueRange  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vamin-valueRange

**Path:** `cim:ExcIEEEST6B.vamin`  
**Name:** C:302:DY:ExcIEEEST6B.vamin:valueRange  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vrmax-valueRange

**Path:** `cim:ExcIEEEST6B.vrmax`  
**Name:** C:302:DY:ExcIEEEST6B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vrmin-valueRange

**Path:** `cim:ExcIEEEST6B.vrmin`  
**Name:** C:302:DY:ExcIEEEST6B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcIEEEST7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST7B

**Nested Properties:**

### dy302c:ExcIEEEST7B.kh-valueRange

**Path:** `cim:ExcIEEEST7B.kh`  
**Name:** C:302:DY:ExcIEEEST7B.kh:valueRange  
High-value gate feedback gain (K<sub>H</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kia-valueRange

**Path:** `cim:ExcIEEEST7B.kia`  
**Name:** C:302:DY:ExcIEEEST7B.kia:valueRange  
Voltage regulator integral gain (K<sub>IA</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kl-valueRange

**Path:** `cim:ExcIEEEST7B.kl`  
**Name:** C:302:DY:ExcIEEEST7B.kl:valueRange  
Low-value gate feedback gain (K<sub>L</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kpa-valueRange

**Path:** `cim:ExcIEEEST7B.kpa`  
**Name:** C:302:DY:ExcIEEEST7B.kpa:valueRange  
Voltage regulator proportional gain (K<sub>PA</sub>) (> 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tb-valueRange

**Path:** `cim:ExcIEEEST7B.tb`  
**Name:** C:302:DY:ExcIEEEST7B.tb:valueRange  
Regulator lag time constant (T<sub>B</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tc-valueRange

**Path:** `cim:ExcIEEEST7B.tc`  
**Name:** C:302:DY:ExcIEEEST7B.tc:valueRange  
Regulator lead time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tf-valueRange

**Path:** `cim:ExcIEEEST7B.tf`  
**Name:** C:302:DY:ExcIEEEST7B.tf:valueRange  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tg-valueRange

**Path:** `cim:ExcIEEEST7B.tg`  
**Name:** C:302:DY:ExcIEEEST7B.tg:valueRange  
Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>) (>= 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tia-valueRange

**Path:** `cim:ExcIEEEST7B.tia`  
**Name:** C:302:DY:ExcIEEEST7B.tia:valueRange  
Feedback time constant (T<sub>IA</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vmax-valueRange

**Path:** `cim:ExcIEEEST7B.vmax`  
**Name:** C:302:DY:ExcIEEEST7B.vmax:valueRange  
Maximum voltage reference signal (V<sub>MAX</sub>) (> 0 and > ExcIEEEST7B.vmin).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vmin-valueRangePair

**Path:** `cim:ExcIEEEST7B.vmin`  
**Name:** C:302:DY:ExcIEEEST7B.vmin:valueRangePair  
Minimum voltage reference signal (V<sub>MIN</sub>) (> 0 and < ExcIEEEST7B.vmax).  Typical value = 0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcIEEEST7B.vmax; or negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcIEEEST7B.vmax` 

### dy302c:ExcIEEEST7B.vrmax-valueRange

**Path:** `cim:ExcIEEEST7B.vrmax`  
**Name:** C:302:DY:ExcIEEEST7B.vrmax:valueRange  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vrmin-valueRange

**Path:** `cim:ExcIEEEST7B.vrmin`  
**Name:** C:302:DY:ExcIEEEST7B.vrmin:valueRange  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -4,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcNI

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcNI

**Nested Properties:**

### dy302c:ExcNI.ka-valueRange

**Path:** `cim:ExcNI.ka`  
**Name:** C:302:DY:ExcNI.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 210.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.kf-valueRange

**Path:** `cim:ExcNI.kf`  
**Name:** C:302:DY:ExcNI.kf:valueRange  
Excitation control system stabilizer gain (Kf) (> 0).  Typical value 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.r-valueRange

**Path:** `cim:ExcNI.r`  
**Name:** C:302:DY:ExcNI.r:valueRange  
rc / rfd (R) (>= 0). 
0 means exciter has negative current capability
> 0 means exciter does not have negative current capability.  
Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.ta-valueRange

**Path:** `cim:ExcNI.ta`  
**Name:** C:302:DY:ExcNI.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tf1-valueRange

**Path:** `cim:ExcNI.tf1`  
**Name:** C:302:DY:ExcNI.tf1:valueRange  
Excitation control system stabilizer time constant (Tf1) (> 0). Typical value = 1,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tf2-valueRange

**Path:** `cim:ExcNI.tf2`  
**Name:** C:302:DY:ExcNI.tf2:valueRange  
Excitation control system stabilizer time constant (Tf2) (> 0). Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tr-valueRange

**Path:** `cim:ExcNI.tr`  
**Name:** C:302:DY:ExcNI.tr:valueRange  
Time constant (Tr) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.vrmin-valueRangePair

**Path:** `cim:ExcNI.vrmin`  
**Name:** C:302:DY:ExcNI.vrmin:valueRangePair  
Minimum voltage regulator ouput (Vrmin) (< ExcNI.vrmax). Typical value = -2,0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcNI.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcNI.vrmax` 

## dy302c:ExcOEX3T

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcOEX3T

**Nested Properties:**

### dy302c:ExcOEX3T.t1-valueRange

**Path:** `cim:ExcOEX3T.t1`  
**Name:** C:302:DY:ExcOEX3T.t1:valueRange  
Time constant (T<sub>1</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t2-valueRange

**Path:** `cim:ExcOEX3T.t2`  
**Name:** C:302:DY:ExcOEX3T.t2:valueRange  
Time constant (T<sub>2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t3-valueRange

**Path:** `cim:ExcOEX3T.t3`  
**Name:** C:302:DY:ExcOEX3T.t3:valueRange  
Time constant (T<sub>3</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t4-valueRange

**Path:** `cim:ExcOEX3T.t4`  
**Name:** C:302:DY:ExcOEX3T.t4:valueRange  
Time constant (T<sub>4</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t5-valueRange

**Path:** `cim:ExcOEX3T.t5`  
**Name:** C:302:DY:ExcOEX3T.t5:valueRange  
Time constant (T<sub>5</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t6-valueRange

**Path:** `cim:ExcOEX3T.t6`  
**Name:** C:302:DY:ExcOEX3T.t6:valueRange  
Time constant (T<sub>6</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.te-valueRange

**Path:** `cim:ExcOEX3T.te`  
**Name:** C:302:DY:ExcOEX3T.te:valueRange  
Time constant (T<sub>E</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.tf-valueRange

**Path:** `cim:ExcOEX3T.tf`  
**Name:** C:302:DY:ExcOEX3T.tf:valueRange  
Time constant (T<sub>F</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.vrmin-valueRangePair

**Path:** `cim:ExcOEX3T.vrmin`  
**Name:** C:302:DY:ExcOEX3T.vrmin:valueRangePair  
Limiter (V<sub>RMIN</sub>) (< ExcOEX3T.vrmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcOEX3T.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcOEX3T.vrmax` 

## dy302c:ExcPIC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcPIC

**Nested Properties:**

### dy302c:ExcPIC.efdmin-valueRangePair

**Path:** `cim:ExcPIC.efdmin`  
**Name:** C:302:DY:ExcPIC.efdmin:valueRangePair  
Exciter minimum limit (E<sub>fdmin</sub>) (< ExcPIC.efdmax).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcPIC.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcPIC.efdmax` 

### dy302c:ExcPIC.ta1-valueRange

**Path:** `cim:ExcPIC.ta1`  
**Name:** C:302:DY:ExcPIC.ta1:valueRange  
PI controller time constant (T<sub>a1</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta2-valueRange

**Path:** `cim:ExcPIC.ta2`  
**Name:** C:302:DY:ExcPIC.ta2:valueRange  
Voltage regulator time constant (T<sub>a2</sub>) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta3-valueRange

**Path:** `cim:ExcPIC.ta3`  
**Name:** C:302:DY:ExcPIC.ta3:valueRange  
Lead time constant (T<sub>a3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta4-valueRange

**Path:** `cim:ExcPIC.ta4`  
**Name:** C:302:DY:ExcPIC.ta4:valueRange  
Lag time constant (T<sub>a4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.te-valueRange

**Path:** `cim:ExcPIC.te`  
**Name:** C:302:DY:ExcPIC.te:valueRange  
Exciter time constant (T<sub>e</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.tf1-valueRange

**Path:** `cim:ExcPIC.tf1`  
**Name:** C:302:DY:ExcPIC.tf1:valueRange  
Rate feedback time constant (T<sub>f1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.tf2-valueRange

**Path:** `cim:ExcPIC.tf2`  
**Name:** C:302:DY:ExcPIC.tf2:valueRange  
Rate feedback lag time constant (T<sub>f2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.vrmin-valueRangePair

**Path:** `cim:ExcPIC.vrmin`  
**Name:** C:302:DY:ExcPIC.vrmin:valueRangePair  
Voltage regulator minimum limit (V<sub>rmin</sub>) (< ExcPIC.vrmax).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcPIC.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcPIC.vrmax` 

## dy302c:ExcREXS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcREXS

**Nested Properties:**

### dy302c:ExcREXS.kf-valueRange

**Path:** `cim:ExcREXS.kf`  
**Name:** C:302:DY:ExcREXS.kf:valueRange  
Rate feedback gain (Kf) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.ta-valueRange

**Path:** `cim:ExcREXS.ta`  
**Name:** C:302:DY:ExcREXS.ta:valueRange  
Voltage regulator time constant (Ta) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tb1-valueRange

**Path:** `cim:ExcREXS.tb1`  
**Name:** C:302:DY:ExcREXS.tb1:valueRange  
Lag time constant (Tb1) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tb2-valueRange

**Path:** `cim:ExcREXS.tb2`  
**Name:** C:302:DY:ExcREXS.tb2:valueRange  
Lag time constant (Tb2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tc1-valueRange

**Path:** `cim:ExcREXS.tc1`  
**Name:** C:302:DY:ExcREXS.tc1:valueRange  
Lead time constant (Tc1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tc2-valueRange

**Path:** `cim:ExcREXS.tc2`  
**Name:** C:302:DY:ExcREXS.tc2:valueRange  
Lead time constant (Tc2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.te-valueRange

**Path:** `cim:ExcREXS.te`  
**Name:** C:302:DY:ExcREXS.te:valueRange  
Exciter field time constant (Te) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf-valueRange

**Path:** `cim:ExcREXS.tf`  
**Name:** C:302:DY:ExcREXS.tf:valueRange  
Rate feedback time constant (Tf) (>= 0).  If = 0, the feedback path is not used.  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf1-valueRange

**Path:** `cim:ExcREXS.tf1`  
**Name:** C:302:DY:ExcREXS.tf1:valueRange  
Feedback lead time constant (Tf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf2-valueRange

**Path:** `cim:ExcREXS.tf2`  
**Name:** C:302:DY:ExcREXS.tf2:valueRange  
Feedback lag time constant (Tf2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tp-valueRange

**Path:** `cim:ExcREXS.tp`  
**Name:** C:302:DY:ExcREXS.tp:valueRange  
Field current bridge time constant (Tp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.vfmin-valueRangePair

**Path:** `cim:ExcREXS.vfmin`  
**Name:** C:302:DY:ExcREXS.vfmin:valueRangePair  
Minimum exciter field current (Vfmin) (< ExcREXS.vfmax).  Typical value = -20.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcREXS.vfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcREXS.vfmax` 

### dy302c:ExcREXS.vrmin-valueRangePair

**Path:** `cim:ExcREXS.vrmin`  
**Name:** C:302:DY:ExcREXS.vrmin:valueRangePair  
Minimum controller output (Vrmin) (< ExcREXS.vrmax).  Typical value = -20.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcREXS.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcREXS.vrmax` 

## dy302c:ExcRQB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcRQB

**Nested Properties:**

### dy302c:ExcRQB.mesu-valueRange

**Path:** `cim:ExcRQB.mesu`  
**Name:** C:302:DY:ExcRQB.mesu:valueRange  
Voltage input time constant (MESU) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.t4m-valueRange

**Path:** `cim:ExcRQB.t4m`  
**Name:** C:302:DY:ExcRQB.t4m:valueRange  
Input time constant (T4M) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.tc-valueRange

**Path:** `cim:ExcRQB.tc`  
**Name:** C:302:DY:ExcRQB.tc:valueRange  
Lead lag time constant (TC) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.te-valueRange

**Path:** `cim:ExcRQB.te`  
**Name:** C:302:DY:ExcRQB.te:valueRange  
Lead lag time constant (TE) (>= 0).  Typical value = 0,22.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.tf-valueRange

**Path:** `cim:ExcRQB.tf`  
**Name:** C:302:DY:ExcRQB.tf:valueRange  
Exciter time constant (TF) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.ucmin-valueRangePair

**Path:** `cim:ExcRQB.ucmin`  
**Name:** C:302:DY:ExcRQB.ucmin:valueRangePair  
Minimum voltage reference limit (UCMIN) (< ExcRQB.ucmax).  Typical value = 0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcRQB.ucmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcRQB.ucmax` 

## dy302c:ExcSCRX

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSCRX

**Nested Properties:**

### dy302c:ExcSCRX.emin-valueRangePair

**Path:** `cim:ExcSCRX.emin`  
**Name:** C:302:DY:ExcSCRX.emin:valueRangePair  
Minimum field voltage output (Emin) (< ExcSCRX.emax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSCRX.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSCRX.emax` 

### dy302c:ExcSCRX.k-valueRange

**Path:** `cim:ExcSCRX.k`  
**Name:** C:302:DY:ExcSCRX.k:valueRange  
Gain (K) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSCRX.tb-valueRange

**Path:** `cim:ExcSCRX.tb`  
**Name:** C:302:DY:ExcSCRX.tb:valueRange  
Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSCRX.te-valueRange

**Path:** `cim:ExcSCRX.te`  
**Name:** C:302:DY:ExcSCRX.te:valueRange  
Time constant of gain block (Te) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcSEXS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSEXS

**Nested Properties:**

### dy302c:ExcSEXS.efdmin-valueRangePair

**Path:** `cim:ExcSEXS.efdmin`  
**Name:** C:302:DY:ExcSEXS.efdmin:valueRangePair  
Field voltage clipping minimum limit (Efdmin) (< ExcSEXS.efdmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSEXS.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSEXS.efdmax` 

### dy302c:ExcSEXS.emin-valueRangePair

**Path:** `cim:ExcSEXS.emin`  
**Name:** C:302:DY:ExcSEXS.emin:valueRangePair  
Minimum field voltage output (Emin) (< ExcSEXS.emax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSEXS.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSEXS.emax` 

### dy302c:ExcSEXS.k-valueRange

**Path:** `cim:ExcSEXS.k`  
**Name:** C:302:DY:ExcSEXS.k:valueRange  
Gain (K) (> 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.tb-valueRange

**Path:** `cim:ExcSEXS.tb`  
**Name:** C:302:DY:ExcSEXS.tb:valueRange  
Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.tc-valueRange

**Path:** `cim:ExcSEXS.tc`  
**Name:** C:302:DY:ExcSEXS.tc:valueRange  
PI controller phase lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.te-valueRange

**Path:** `cim:ExcSEXS.te`  
**Name:** C:302:DY:ExcSEXS.te:valueRange  
Time constant of gain block (Te) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcSK

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSK

**Nested Properties:**

### dy302c:ExcSK.efdmin-valueRangePair

**Path:** `cim:ExcSK.efdmin`  
**Name:** C:302:DY:ExcSK.efdmin:valueRangePair  
Field voltage clipping lower level limit (Efdmin) (< ExcSK.efdmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.efdmax` 

### dy302c:ExcSK.emin-valueRangePair

**Path:** `cim:ExcSK.emin`  
**Name:** C:302:DY:ExcSK.emin:valueRangePair  
Minimum field voltage output (Emin) (< ExcSK.emax).  Typical value = -20.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.emax` 

### dy302c:ExcSK.sbase-valueRange

**Path:** `cim:ExcSK.sbase`  
**Name:** C:302:DY:ExcSK.sbase:valueRange  
Apparent power of the unit (Sbase) (> 0).  Unit = MVA.  Typical value = 259.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tc-valueRange

**Path:** `cim:ExcSK.tc`  
**Name:** C:302:DY:ExcSK.tc:valueRange  
PI controller phase lead time constant (Tc) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.te-valueRange

**Path:** `cim:ExcSK.te`  
**Name:** C:302:DY:ExcSK.te:valueRange  
Time constant of gain block (Te) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.ti-valueRange

**Path:** `cim:ExcSK.ti`  
**Name:** C:302:DY:ExcSK.ti:valueRange  
PI controller phase lead time constant (Ti) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tp-valueRange

**Path:** `cim:ExcSK.tp`  
**Name:** C:302:DY:ExcSK.tp:valueRange  
Time constant (Tp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tr-valueRange

**Path:** `cim:ExcSK.tr`  
**Name:** C:302:DY:ExcSK.tr:valueRange  
Voltage transducer time constant (Tr) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.uimin-valueRangePair

**Path:** `cim:ExcSK.uimin`  
**Name:** C:302:DY:ExcSK.uimin:valueRangePair  
Minimum error (UImin) (< ExcSK.uimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.uimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.uimax` 

### dy302c:ExcSK.urmin-valueRangePair

**Path:** `cim:ExcSK.urmin`  
**Name:** C:302:DY:ExcSK.urmin:valueRangePair  
Minimum controller output (URmin) (< ExcSK.urmax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.urmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.urmax` 

### dy302c:ExcSK.vtmin-valueRangePair

**Path:** `cim:ExcSK.vtmin`  
**Name:** C:302:DY:ExcSK.vtmin:valueRangePair  
Minimum terminal voltage input (Vtmin) (< ExcSK.vtmax).  Determines the range of voltage deadband.  Typical value = 0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.vtmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.vtmax` 

## dy302c:ExcST1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST1A

**Nested Properties:**

### dy302c:ExcST1A.ka-valueRange

**Path:** `cim:ExcST1A.ka`  
**Name:** C:302:DY:ExcST1A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 190.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.kc-valueRange

**Path:** `cim:ExcST1A.kc`  
**Name:** C:302:DY:ExcST1A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.kf-valueRange

**Path:** `cim:ExcST1A.kf`  
**Name:** C:302:DY:ExcST1A.kf:valueRange  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.ta-valueRange

**Path:** `cim:ExcST1A.ta`  
**Name:** C:302:DY:ExcST1A.ta:valueRange  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tb-valueRange

**Path:** `cim:ExcST1A.tb`  
**Name:** C:302:DY:ExcST1A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tb1-valueRange

**Path:** `cim:ExcST1A.tb1`  
**Name:** C:302:DY:ExcST1A.tb1:valueRange  
Voltage regulator time constant (Tb1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tc-valueRange

**Path:** `cim:ExcST1A.tc`  
**Name:** C:302:DY:ExcST1A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tc1-valueRange

**Path:** `cim:ExcST1A.tc1`  
**Name:** C:302:DY:ExcST1A.tc1:valueRange  
Voltage regulator time constant (Tc1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tf-valueRange

**Path:** `cim:ExcST1A.tf`  
**Name:** C:302:DY:ExcST1A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vamax-valueRange

**Path:** `cim:ExcST1A.vamax`  
**Name:** C:302:DY:ExcST1A.vamax:valueRange  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vamin-valueRange

**Path:** `cim:ExcST1A.vamin`  
**Name:** C:302:DY:ExcST1A.vamin:valueRange  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vimax-valueRange

**Path:** `cim:ExcST1A.vimax`  
**Name:** C:302:DY:ExcST1A.vimax:valueRange  
Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vimin-valueRange

**Path:** `cim:ExcST1A.vimin`  
**Name:** C:302:DY:ExcST1A.vimin:valueRange  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vrmax-valueRange

**Path:** `cim:ExcST1A.vrmax`  
**Name:** C:302:DY:ExcST1A.vrmax:valueRange  
Maximum voltage regulator outputs (Vrmax) (> 0) .  Typical value = 7,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vrmin-valueRange

**Path:** `cim:ExcST1A.vrmin`  
**Name:** C:302:DY:ExcST1A.vrmin:valueRange  
Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -6,7.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcST2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST2A

**Nested Properties:**

### dy302c:ExcST2A.efdmax-valueRange

**Path:** `cim:ExcST2A.efdmax`  
**Name:** C:302:DY:ExcST2A.efdmax:valueRange  
Maximum field voltage (Efdmax) (>= 0).  Typical value = 99.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ka-valueRange

**Path:** `cim:ExcST2A.ka`  
**Name:** C:302:DY:ExcST2A.ka:valueRange  
Voltage regulator gain (Ka) (> 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kc-valueRange

**Path:** `cim:ExcST2A.kc`  
**Name:** C:302:DY:ExcST2A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 1,82.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kf-valueRange

**Path:** `cim:ExcST2A.kf`  
**Name:** C:302:DY:ExcST2A.kf:valueRange  
Excitation control system stabilizer gains (kf) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ki-valueRange

**Path:** `cim:ExcST2A.ki`  
**Name:** C:302:DY:ExcST2A.ki:valueRange  
Potential circuit gain coefficient (K<sub>i</sub>) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kp-valueRange

**Path:** `cim:ExcST2A.kp`  
**Name:** C:302:DY:ExcST2A.kp:valueRange  
Potential circuit gain coefficient (K<sub>p</sub>) (>= 0).  Typical value = 4,88.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ta-valueRange

**Path:** `cim:ExcST2A.ta`  
**Name:** C:302:DY:ExcST2A.ta:valueRange  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tb-valueRange

**Path:** `cim:ExcST2A.tb`  
**Name:** C:302:DY:ExcST2A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tc-valueRange

**Path:** `cim:ExcST2A.tc`  
**Name:** C:302:DY:ExcST2A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.te-valueRange

**Path:** `cim:ExcST2A.te`  
**Name:** C:302:DY:ExcST2A.te:valueRange  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tf-valueRange

**Path:** `cim:ExcST2A.tf`  
**Name:** C:302:DY:ExcST2A.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.vrmax-valueRange

**Path:** `cim:ExcST2A.vrmax`  
**Name:** C:302:DY:ExcST2A.vrmax:valueRange  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.vrmin-valueRange

**Path:** `cim:ExcST2A.vrmin`  
**Name:** C:302:DY:ExcST2A.vrmin:valueRange  
Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcST3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST3A

**Nested Properties:**

### dy302c:ExcST3A.efdmax-valueRange

**Path:** `cim:ExcST3A.efdmax`  
**Name:** C:302:DY:ExcST3A.efdmax:valueRange  
Maximum AVR output (Efdmax) (>= 0).  Typical value = 6,9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kc-valueRange

**Path:** `cim:ExcST3A.kc`  
**Name:** C:302:DY:ExcST3A.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kg-valueRange

**Path:** `cim:ExcST3A.kg`  
**Name:** C:302:DY:ExcST3A.kg:valueRange  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.ki-valueRange

**Path:** `cim:ExcST3A.ki`  
**Name:** C:302:DY:ExcST3A.ki:valueRange  
Potential circuit gain coefficient (K<sub>i</sub>) (>= 0).  Typical value = 4,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kj-valueRange

**Path:** `cim:ExcST3A.kj`  
**Name:** C:302:DY:ExcST3A.kj:valueRange  
AVR gain (Kj) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.km-valueRange

**Path:** `cim:ExcST3A.km`  
**Name:** C:302:DY:ExcST3A.km:valueRange  
Forward gain constant of the inner loop field regulator (Km) (> 0).  Typical value = 7,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kp-valueRange

**Path:** `cim:ExcST3A.kp`  
**Name:** C:302:DY:ExcST3A.kp:valueRange  
Potential source gain (K<sub>p</sub>) (> 0).  Typical value = 4,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tb-valueRange

**Path:** `cim:ExcST3A.tb`  
**Name:** C:302:DY:ExcST3A.tb:valueRange  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 6,67.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tc-valueRange

**Path:** `cim:ExcST3A.tc`  
**Name:** C:302:DY:ExcST3A.tc:valueRange  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tm-valueRange

**Path:** `cim:ExcST3A.tm`  
**Name:** C:302:DY:ExcST3A.tm:valueRange  
Forward time constant of inner loop field regulator (Tm) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vbmax-valueRange

**Path:** `cim:ExcST3A.vbmax`  
**Name:** C:302:DY:ExcST3A.vbmax:valueRange  
Maximum excitation voltage (Vbmax) (> 0).  Typical value = 8,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vgmax-valueRange

**Path:** `cim:ExcST3A.vgmax`  
**Name:** C:302:DY:ExcST3A.vgmax:valueRange  
Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 6,53.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vimax-valueRange

**Path:** `cim:ExcST3A.vimax`  
**Name:** C:302:DY:ExcST3A.vimax:valueRange  
Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vimin-valueRange

**Path:** `cim:ExcST3A.vimin`  
**Name:** C:302:DY:ExcST3A.vimin:valueRange  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vrmax-valueRange

**Path:** `cim:ExcST3A.vrmax`  
**Name:** C:302:DY:ExcST3A.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vrmin-valueRange

**Path:** `cim:ExcST3A.vrmin`  
**Name:** C:302:DY:ExcST3A.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.xl-valueRange

**Path:** `cim:ExcST3A.xl`  
**Name:** C:302:DY:ExcST3A.xl:valueRange  
Reactance associated with potential source (Xl) (>= 0).  Typical value = 0,09.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcST4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST4B

**Nested Properties:**

### dy302c:ExcST4B.kc-valueRange

**Path:** `cim:ExcST4B.kc`  
**Name:** C:302:DY:ExcST4B.kc:valueRange  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,113.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.kg-valueRange

**Path:** `cim:ExcST4B.kg`  
**Name:** C:302:DY:ExcST4B.kg:valueRange  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0). Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.ki-valueRange

**Path:** `cim:ExcST4B.ki`  
**Name:** C:302:DY:ExcST4B.ki:valueRange  
Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.kp-valueRange

**Path:** `cim:ExcST4B.kp`  
**Name:** C:302:DY:ExcST4B.kp:valueRange  
Potential circuit gain coefficient (Kp) (> 0).  Typical value = 9,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.ta-valueRange

**Path:** `cim:ExcST4B.ta`  
**Name:** C:302:DY:ExcST4B.ta:valueRange  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vbmax-valueRange

**Path:** `cim:ExcST4B.vbmax`  
**Name:** C:302:DY:ExcST4B.vbmax:valueRange  
Maximum excitation voltage (Vbmax) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vgmax-valueRange

**Path:** `cim:ExcST4B.vgmax`  
**Name:** C:302:DY:ExcST4B.vgmax:valueRange  
Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 5,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vmmin-valueRangePair

**Path:** `cim:ExcST4B.vmmin`  
**Name:** C:302:DY:ExcST4B.vmmin:valueRangePair  
Minimum inner loop output (Vmmin) (< ExcST4B.vmmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcST4B.vmmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcST4B.vmmax` 

### dy302c:ExcST4B.vrmax-valueRange

**Path:** `cim:ExcST4B.vrmax`  
**Name:** C:302:DY:ExcST4B.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vrmin-valueRange

**Path:** `cim:ExcST4B.vrmin`  
**Name:** C:302:DY:ExcST4B.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.xl-valueRange

**Path:** `cim:ExcST4B.xl`  
**Name:** C:302:DY:ExcST4B.xl:valueRange  
Reactance associated with potential source (Xl) (>= 0).  Typical value = 0,124.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcST6B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST6B

**Nested Properties:**

### dy302c:ExcST6B.ilr-valueRange

**Path:** `cim:ExcST6B.ilr`  
**Name:** C:302:DY:ExcST6B.ilr:valueRange  
Exciter output current limit reference (Ilr) (> 0).  Typical value = 4,164.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kcl-valueRange

**Path:** `cim:ExcST6B.kcl`  
**Name:** C:302:DY:ExcST6B.kcl:valueRange  
Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 1,0577.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kg-valueRange

**Path:** `cim:ExcST6B.kg`  
**Name:** C:302:DY:ExcST6B.kg:valueRange  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kia-valueRange

**Path:** `cim:ExcST6B.kia`  
**Name:** C:302:DY:ExcST6B.kia:valueRange  
Voltage regulator integral gain (Kia) (> 0).  Typical value = 45,094.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.klr-valueRange

**Path:** `cim:ExcST6B.klr`  
**Name:** C:302:DY:ExcST6B.klr:valueRange  
Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 17,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kpa-valueRange

**Path:** `cim:ExcST6B.kpa`  
**Name:** C:302:DY:ExcST6B.kpa:valueRange  
Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 18,038.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.tg-valueRange

**Path:** `cim:ExcST6B.tg`  
**Name:** C:302:DY:ExcST6B.tg:valueRange  
Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.ts-valueRange

**Path:** `cim:ExcST6B.ts`  
**Name:** C:302:DY:ExcST6B.ts:valueRange  
Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.tvd-valueRange

**Path:** `cim:ExcST6B.tvd`  
**Name:** C:302:DY:ExcST6B.tvd:valueRange  
Voltage regulator derivative gain (Tvd) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vamax-valueRange

**Path:** `cim:ExcST6B.vamax`  
**Name:** C:302:DY:ExcST6B.vamax:valueRange  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vamin-valueRange

**Path:** `cim:ExcST6B.vamin`  
**Name:** C:302:DY:ExcST6B.vamin:valueRange  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vimin-valueRangePair

**Path:** `cim:ExcST6B.vimin`  
**Name:** C:302:DY:ExcST6B.vimin:valueRangePair  
Minimum voltage regulator input limit (Vimin) (< ExcST6B.vimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcST6B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcST6B.vimax` 

### dy302c:ExcST6B.vrmax-valueRange

**Path:** `cim:ExcST6B.vrmax`  
**Name:** C:302:DY:ExcST6B.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vrmin-valueRange

**Path:** `cim:ExcST6B.vrmin`  
**Name:** C:302:DY:ExcST6B.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:ExcST7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST7B

**Nested Properties:**

### dy302c:ExcST7B.kh-valueRange

**Path:** `cim:ExcST7B.kh`  
**Name:** C:302:DY:ExcST7B.kh:valueRange  
High-value gate feedback gain (Kh) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kia-valueRange

**Path:** `cim:ExcST7B.kia`  
**Name:** C:302:DY:ExcST7B.kia:valueRange  
Voltage regulator integral gain (Kia) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kl-valueRange

**Path:** `cim:ExcST7B.kl`  
**Name:** C:302:DY:ExcST7B.kl:valueRange  
Low-value gate feedback gain (Kl) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kpa-valueRange

**Path:** `cim:ExcST7B.kpa`  
**Name:** C:302:DY:ExcST7B.kpa:valueRange  
Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tb-valueRange

**Path:** `cim:ExcST7B.tb`  
**Name:** C:302:DY:ExcST7B.tb:valueRange  
Regulator lag time constant (Tb) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tc-valueRange

**Path:** `cim:ExcST7B.tc`  
**Name:** C:302:DY:ExcST7B.tc:valueRange  
Regulator lead time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tf-valueRange

**Path:** `cim:ExcST7B.tf`  
**Name:** C:302:DY:ExcST7B.tf:valueRange  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tg-valueRange

**Path:** `cim:ExcST7B.tg`  
**Name:** C:302:DY:ExcST7B.tg:valueRange  
Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tia-valueRange

**Path:** `cim:ExcST7B.tia`  
**Name:** C:302:DY:ExcST7B.tia:valueRange  
Feedback time constant (Tia) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.ts-valueRange

**Path:** `cim:ExcST7B.ts`  
**Name:** C:302:DY:ExcST7B.ts:valueRange  
Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vmax-valueRange

**Path:** `cim:ExcST7B.vmax`  
**Name:** C:302:DY:ExcST7B.vmax:valueRange  
Maximum voltage reference signal (Vmax) (> 0 and > ExcST7B.vmin)).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vmin-valueRangePair

**Path:** `cim:ExcST7B.vmin`  
**Name:** C:302:DY:ExcST7B.vmin:valueRangePair  
Minimum voltage reference signal (Vmin) (> 0 and < ExcST7B.vmax).  Typical value = 0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcST7B.vmax; or negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcST7B.vmax` 

### dy302c:ExcST7B.vrmax-valueRange

**Path:** `cim:ExcST7B.vrmax`  
**Name:** C:302:DY:ExcST7B.vrmax:valueRange  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vrmin-valueRange

**Path:** `cim:ExcST7B.vrmin`  
**Name:** C:302:DY:ExcST7B.vrmin:valueRange  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovCT1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovCT1

**Nested Properties:**

### dy302c:GovCT1.kturb-valueRange

**Path:** `cim:GovCT1.kturb`  
**Name:** C:302:DY:GovCT1.kturb:valueRange  
Turbine gain (Kturb) (> 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.minerr-valueRangePair

**Path:** `cim:GovCT1.minerr`  
**Name:** C:302:DY:GovCT1.minerr:valueRangePair  
Minimum value for speed error signal (minerr) (< GovCT1.maxerr).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT1.maxerr."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT1.maxerr` 

### dy302c:GovCT1.mwbase-valueRange

**Path:** `cim:GovCT1.mwbase`  
**Name:** C:302:DY:GovCT1.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.ta-valueRange

**Path:** `cim:GovCT1.ta`  
**Name:** C:302:DY:GovCT1.ta:valueRange  
Acceleration limiter time constant (Ta) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tact-valueRange

**Path:** `cim:GovCT1.tact`  
**Name:** C:302:DY:GovCT1.tact:valueRange  
Actuator time constant (Tact) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tb-valueRange

**Path:** `cim:GovCT1.tb`  
**Name:** C:302:DY:GovCT1.tb:valueRange  
Turbine lag time constant (Tb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tc-valueRange

**Path:** `cim:GovCT1.tc`  
**Name:** C:302:DY:GovCT1.tc:valueRange  
Turbine lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tdgov-valueRange

**Path:** `cim:GovCT1.tdgov`  
**Name:** C:302:DY:GovCT1.tdgov:valueRange  
Governor derivative controller time constant (Tdgov) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.teng-valueRange

**Path:** `cim:GovCT1.teng`  
**Name:** C:302:DY:GovCT1.teng:valueRange  
Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng) (>= 0).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tfload-valueRange

**Path:** `cim:GovCT1.tfload`  
**Name:** C:302:DY:GovCT1.tfload:valueRange  
Load-limiter time constant (Tfload) (> 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tpelec-valueRange

**Path:** `cim:GovCT1.tpelec`  
**Name:** C:302:DY:GovCT1.tpelec:valueRange  
Electrical power transducer time constant (Tpelec) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tsa-valueRange

**Path:** `cim:GovCT1.tsa`  
**Name:** C:302:DY:GovCT1.tsa:valueRange  
Temperature detection lead time constant (Tsa) (>= 0).  Typical value = 4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tsb-valueRange

**Path:** `cim:GovCT1.tsb`  
**Name:** C:302:DY:GovCT1.tsb:valueRange  
Temperature detection lag time constant (Tsb) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.vmin-valueRangePair

**Path:** `cim:GovCT1.vmin`  
**Name:** C:302:DY:GovCT1.vmin:valueRangePair  
Minimum valve position limit (Vmin) (< GovCT1.vmax).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT1.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT1.vmax` 

## dy302c:GovCT2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovCT2

**Nested Properties:**

### dy302c:GovCT2.minerr-valueRangePair

**Path:** `cim:GovCT2.minerr`  
**Name:** C:302:DY:GovCT2.minerr:valueRangePair  
Minimum value for speed error signal (Minerr) (< GovCT2.maxerr).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT2.maxerr."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT2.maxerr` 

### dy302c:GovCT2.mwbase-valueRange

**Path:** `cim:GovCT2.mwbase`  
**Name:** C:302:DY:GovCT2.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.ta-valueRange

**Path:** `cim:GovCT2.ta`  
**Name:** C:302:DY:GovCT2.ta:valueRange  
Acceleration limiter time constant (Ta) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tact-valueRange

**Path:** `cim:GovCT2.tact`  
**Name:** C:302:DY:GovCT2.tact:valueRange  
Actuator time constant (Tact) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tb-valueRange

**Path:** `cim:GovCT2.tb`  
**Name:** C:302:DY:GovCT2.tb:valueRange  
Turbine lag time constant (Tb) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tc-valueRange

**Path:** `cim:GovCT2.tc`  
**Name:** C:302:DY:GovCT2.tc:valueRange  
Turbine lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tdgov-valueRange

**Path:** `cim:GovCT2.tdgov`  
**Name:** C:302:DY:GovCT2.tdgov:valueRange  
Governor derivative controller time constant (Tdgov) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.teng-valueRange

**Path:** `cim:GovCT2.teng`  
**Name:** C:302:DY:GovCT2.teng:valueRange  
Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng) (>= 0).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tfload-valueRange

**Path:** `cim:GovCT2.tfload`  
**Name:** C:302:DY:GovCT2.tfload:valueRange  
Load limiter time constant (Tfload) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tpelec-valueRange

**Path:** `cim:GovCT2.tpelec`  
**Name:** C:302:DY:GovCT2.tpelec:valueRange  
Electrical power transducer time constant (Tpelec) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tsa-valueRange

**Path:** `cim:GovCT2.tsa`  
**Name:** C:302:DY:GovCT2.tsa:valueRange  
Temperature detection lead time constant (Tsa) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tsb-valueRange

**Path:** `cim:GovCT2.tsb`  
**Name:** C:302:DY:GovCT2.tsb:valueRange  
Temperature detection lag time constant (Tsb) (>= 0).  Typical value = 50.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.vmin-valueRangePair

**Path:** `cim:GovCT2.vmin`  
**Name:** C:302:DY:GovCT2.vmin:valueRangePair  
Minimum valve position limit (Vmin) (< GovCT2.vmax).  Typical value = 0,175.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT2.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT2.vmax` 

## dy302c:GovGAST

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST

**Nested Properties:**

### dy302c:GovGAST.mwbase-valueRange

**Path:** `cim:GovGAST.mwbase`  
**Name:** C:302:DY:GovGAST.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.r-valueRange

**Path:** `cim:GovGAST.r`  
**Name:** C:302:DY:GovGAST.r:valueRange  
Permanent droop (R) (>0). Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t1-valueRange

**Path:** `cim:GovGAST.t1`  
**Name:** C:302:DY:GovGAST.t1:valueRange  
Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t2-valueRange

**Path:** `cim:GovGAST.t2`  
**Name:** C:302:DY:GovGAST.t2:valueRange  
Turbine power time constant (T2) (>= 0).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power turbine of an aero-derivative unit, for example.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t3-valueRange

**Path:** `cim:GovGAST.t3`  
**Name:** C:302:DY:GovGAST.t3:valueRange  
Turbine exhaust temperature time constant (T3) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.vmin-valueRangePair

**Path:** `cim:GovGAST.vmin`  
**Name:** C:302:DY:GovGAST.vmin:valueRangePair  
Minimum turbine power, PU of MWbase (Vmin) (< GovGAST.vmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGAST.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGAST.vmax` 

## dy302c:GovGAST1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST1

**Nested Properties:**

### dy302c:GovGAST1.b-valueRange

**Path:** `cim:GovGAST1.b`  
**Name:** C:302:DY:GovGAST1.b:valueRange  
Turbine power time constant denominator scale factor (b) (>0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.mwbase-valueRange

**Path:** `cim:GovGAST1.mwbase`  
**Name:** C:302:DY:GovGAST1.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.r-valueRange

**Path:** `cim:GovGAST1.r`  
**Name:** C:302:DY:GovGAST1.r:valueRange  
Permanent droop (R) (>0).  Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t1-valueRange

**Path:** `cim:GovGAST1.t1`  
**Name:** C:302:DY:GovGAST1.t1:valueRange  
Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t2-valueRange

**Path:** `cim:GovGAST1.t2`  
**Name:** C:302:DY:GovGAST1.t2:valueRange  
Turbine power time constant (T2) (>= 0). T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t3-valueRange

**Path:** `cim:GovGAST1.t3`  
**Name:** C:302:DY:GovGAST1.t3:valueRange  
Turbine exhaust temperature time constant (T3) (>= 0).  T3 represents delay in the exhaust temperature and load limiting system. Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t4-valueRange

**Path:** `cim:GovGAST1.t4`  
**Name:** C:302:DY:GovGAST1.t4:valueRange  
Governor lead time constant (T4) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t5-valueRange

**Path:** `cim:GovGAST1.t5`  
**Name:** C:302:DY:GovGAST1.t5:valueRange  
Governor lag time constant (T5) (>= 0).  If = 0, entire gain and lead-lag block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.tltr-valueRange

**Path:** `cim:GovGAST1.tltr`  
**Name:** C:302:DY:GovGAST1.tltr:valueRange  
Valve position averaging time constant (Tltr) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.vmin-valueRangePair

**Path:** `cim:GovGAST1.vmin`  
**Name:** C:302:DY:GovGAST1.vmin:valueRangePair  
Minimum turbine power, PU of MWbase (Vmin) (< GovGAST1.vmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGAST1.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGAST1.vmax` 

## dy302c:GovGAST2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST2

**Nested Properties:**

### dy302c:GovGAST2.ecr-valueRange

**Path:** `cim:GovGAST2.ecr`  
**Name:** C:302:DY:GovGAST2.ecr:valueRange  
Combustion reaction time delay (Ecr) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.etd-valueRange

**Path:** `cim:GovGAST2.etd`  
**Name:** C:302:DY:GovGAST2.etd:valueRange  
Turbine and exhaust delay (Etd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.mwbase-valueRange

**Path:** `cim:GovGAST2.mwbase`  
**Name:** C:302:DY:GovGAST2.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t-valueRange

**Path:** `cim:GovGAST2.t`  
**Name:** C:302:DY:GovGAST2.t:valueRange  
Fuel control time constant (T) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t3-valueRange

**Path:** `cim:GovGAST2.t3`  
**Name:** C:302:DY:GovGAST2.t3:valueRange  
Radiation shield time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t4-valueRange

**Path:** `cim:GovGAST2.t4`  
**Name:** C:302:DY:GovGAST2.t4:valueRange  
Thermocouple time constant (T4) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t5-valueRange

**Path:** `cim:GovGAST2.t5`  
**Name:** C:302:DY:GovGAST2.t5:valueRange  
Temperature control time constant (T5) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tcd-valueRange

**Path:** `cim:GovGAST2.tcd`  
**Name:** C:302:DY:GovGAST2.tcd:valueRange  
Compressor discharge time constant (Tcd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tf-valueRange

**Path:** `cim:GovGAST2.tf`  
**Name:** C:302:DY:GovGAST2.tf:valueRange  
Fuel system time constant (Tf) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tmin-valueRangePair

**Path:** `cim:GovGAST2.tmin`  
**Name:** C:302:DY:GovGAST2.tmin:valueRangePair  
Minimum turbine limit (Tmin) (< GovGAST2.tmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGAST2.tmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGAST2.tmax` 

### dy302c:GovGAST2.tt-valueRange

**Path:** `cim:GovGAST2.tt`  
**Name:** C:302:DY:GovGAST2.tt:valueRange  
Temperature controller integration rate (Tt) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.x-valueRange

**Path:** `cim:GovGAST2.x`  
**Name:** C:302:DY:GovGAST2.x:valueRange  
Governor lead time constant (X) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.y-valueRange

**Path:** `cim:GovGAST2.y`  
**Name:** C:302:DY:GovGAST2.y:valueRange  
Governor lag time constant (Y) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovGAST3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST3

**Nested Properties:**

### dy302c:GovGAST3.tac-valueRange

**Path:** `cim:GovGAST3.tac`  
**Name:** C:302:DY:GovGAST3.tac:valueRange  
Fuel control time constant (Tac) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tc-valueRange

**Path:** `cim:GovGAST3.tc`  
**Name:** C:302:DY:GovGAST3.tc:valueRange  
Compressor discharge volume time constant (Tc) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.td-valueRange

**Path:** `cim:GovGAST3.td`  
**Name:** C:302:DY:GovGAST3.td:valueRange  
Temperature controller derivative gain (Td) (>= 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tg-valueRange

**Path:** `cim:GovGAST3.tg`  
**Name:** C:302:DY:GovGAST3.tg:valueRange  
Time constant of speed governor (Tg) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tsi-valueRange

**Path:** `cim:GovGAST3.tsi`  
**Name:** C:302:DY:GovGAST3.tsi:valueRange  
Time constant of radiation shield (Tsi) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.ttc-valueRange

**Path:** `cim:GovGAST3.ttc`  
**Name:** C:302:DY:GovGAST3.ttc:valueRange  
Time constant of thermocouple (Ttc) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.ty-valueRange

**Path:** `cim:GovGAST3.ty`  
**Name:** C:302:DY:GovGAST3.ty:valueRange  
Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovGAST4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST4

**Nested Properties:**

### dy302c:GovGAST4.ta-valueRange

**Path:** `cim:GovGAST4.ta`  
**Name:** C:302:DY:GovGAST4.ta:valueRange  
Maximum gate opening velocity (TA) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tc-valueRange

**Path:** `cim:GovGAST4.tc`  
**Name:** C:302:DY:GovGAST4.tc:valueRange  
Maximum gate closing velocity (TC) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tcm-valueRange

**Path:** `cim:GovGAST4.tcm`  
**Name:** C:302:DY:GovGAST4.tcm:valueRange  
Fuel control time constant (Tcm) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tm-valueRange

**Path:** `cim:GovGAST4.tm`  
**Name:** C:302:DY:GovGAST4.tm:valueRange  
Compressor discharge volume time constant (Tm) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.ty-valueRange

**Path:** `cim:GovGAST4.ty`  
**Name:** C:302:DY:GovGAST4.ty:valueRange  
Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovGASTWD

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGASTWD

**Nested Properties:**

### dy302c:GovGASTWD.ecr-valueRange

**Path:** `cim:GovGASTWD.ecr`  
**Name:** C:302:DY:GovGASTWD.ecr:valueRange  
Combustion reaction time delay (Ecr) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.etd-valueRange

**Path:** `cim:GovGASTWD.etd`  
**Name:** C:302:DY:GovGASTWD.etd:valueRange  
Turbine and exhaust delay (Etd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.kdroop-valueRange

**Path:** `cim:GovGASTWD.kdroop`  
**Name:** C:302:DY:GovGASTWD.kdroop:valueRange  
(Kdroop) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.mwbase-valueRange

**Path:** `cim:GovGASTWD.mwbase`  
**Name:** C:302:DY:GovGASTWD.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t-valueRange

**Path:** `cim:GovGASTWD.t`  
**Name:** C:302:DY:GovGASTWD.t:valueRange  
Fuel control time constant (T) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t3-valueRange

**Path:** `cim:GovGASTWD.t3`  
**Name:** C:302:DY:GovGASTWD.t3:valueRange  
Radiation shield time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t4-valueRange

**Path:** `cim:GovGASTWD.t4`  
**Name:** C:302:DY:GovGASTWD.t4:valueRange  
Thermocouple time constant (T4) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t5-valueRange

**Path:** `cim:GovGASTWD.t5`  
**Name:** C:302:DY:GovGASTWD.t5:valueRange  
Temperature control time constant (T5) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tcd-valueRange

**Path:** `cim:GovGASTWD.tcd`  
**Name:** C:302:DY:GovGASTWD.tcd:valueRange  
Compressor discharge time constant (Tcd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.td-valueRange

**Path:** `cim:GovGASTWD.td`  
**Name:** C:302:DY:GovGASTWD.td:valueRange  
Power transducer time constant (Td) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tf-valueRange

**Path:** `cim:GovGASTWD.tf`  
**Name:** C:302:DY:GovGASTWD.tf:valueRange  
Fuel system time constant (Tf) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tmin-valueRangePair

**Path:** `cim:GovGASTWD.tmin`  
**Name:** C:302:DY:GovGASTWD.tmin:valueRangePair  
Minimum turbine limit (Tmin) (< GovGASTWD.tmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGASTWD.tmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGASTWD.tmax` 

### dy302c:GovGASTWD.tt-valueRange

**Path:** `cim:GovGASTWD.tt`  
**Name:** C:302:DY:GovGASTWD.tt:valueRange  
Temperature controller integration rate (Tt) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydro1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro1

**Nested Properties:**

### dy302c:GovHydro1.at-valueRange

**Path:** `cim:GovHydro1.at`  
**Name:** C:302:DY:GovHydro1.at:valueRange  
Turbine gain (At) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.dturb-valueRange

**Path:** `cim:GovHydro1.dturb`  
**Name:** C:302:DY:GovHydro1.dturb:valueRange  
Turbine damping factor (Dturb) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.gmin-valueRangePair

**Path:** `cim:GovHydro1.gmin`  
**Name:** C:302:DY:GovHydro1.gmin:valueRangePair  
Minimum gate opening (Gmin) (>= 0 and < GovHydro1.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro1.gmax; or negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro1.gmax` 

### dy302c:GovHydro1.mwbase-valueRange

**Path:** `cim:GovHydro1.mwbase`  
**Name:** C:302:DY:GovHydro1.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.qnl-valueRange

**Path:** `cim:GovHydro1.qnl`  
**Name:** C:302:DY:GovHydro1.qnl:valueRange  
No-load flow at nominal head (qnl) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.rperm-valueRange

**Path:** `cim:GovHydro1.rperm`  
**Name:** C:302:DY:GovHydro1.rperm:valueRange  
Permanent droop (R) (> 0).  Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.rperm-valueRangePair

**Path:** `cim:GovHydro1.rperm`  
**Name:** C:302:DY:GovHydro1.rtemp:valueRangePair  
Temporary droop (r) (GovHydro1.rtemp > GovHydro1.rperm).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value of GovHydro1.rperm is either equal to or greater than GovHydro1.rtemp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro1.rtemp` 

### dy302c:GovHydro1.tf-valueRange

**Path:** `cim:GovHydro1.tf`  
**Name:** C:302:DY:GovHydro1.tf:valueRange  
Filter time constant (Tf) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tg-valueRange

**Path:** `cim:GovHydro1.tg`  
**Name:** C:302:DY:GovHydro1.tg:valueRange  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tr-valueRange

**Path:** `cim:GovHydro1.tr`  
**Name:** C:302:DY:GovHydro1.tr:valueRange  
Washout time constant (Tr) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tw-valueRange

**Path:** `cim:GovHydro1.tw`  
**Name:** C:302:DY:GovHydro1.tw:valueRange  
Water inertia time constant (Tw) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.velm-valueRange

**Path:** `cim:GovHydro1.velm`  
**Name:** C:302:DY:GovHydro1.velm:valueRange  
Maximum gate velocity (Vlem) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydro2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro2

**Nested Properties:**

### dy302c:GovHydro2.bturb-valueRange

**Path:** `cim:GovHydro2.bturb`  
**Name:** C:302:DY:GovHydro2.bturb:valueRange  
Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.mwbase-valueRange

**Path:** `cim:GovHydro2.mwbase`  
**Name:** C:302:DY:GovHydro2.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.pmin-valueRangePair

**Path:** `cim:GovHydro2.pmin`  
**Name:** C:302:DY:GovHydro2.pmin:valueRangePair  
Minimum gate opening (Pmin) (< GovHydro2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro2.pmax` 

### dy302c:GovHydro2.tg-valueRange

**Path:** `cim:GovHydro2.tg`  
**Name:** C:302:DY:GovHydro2.tg:valueRange  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tp-valueRange

**Path:** `cim:GovHydro2.tp`  
**Name:** C:302:DY:GovHydro2.tp:valueRange  
Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tr-valueRange

**Path:** `cim:GovHydro2.tr`  
**Name:** C:302:DY:GovHydro2.tr:valueRange  
Dashpot time constant (Tr) (>= 0).  Typical value = 12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tw-valueRange

**Path:** `cim:GovHydro2.tw`  
**Name:** C:302:DY:GovHydro2.tw:valueRange  
Water inertia time constant (Tw) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.uc-valueRange

**Path:** `cim:GovHydro2.uc`  
**Name:** C:302:DY:GovHydro2.uc:valueRange  
Maximum gate closing velocity (Uc) (< 0).  Unit = PU / s.   Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydro3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro3

**Nested Properties:**

### dy302c:GovHydro3.at-valueRange

**Path:** `cim:GovHydro3.at`  
**Name:** C:302:DY:GovHydro3.at:valueRange  
Turbine gain (At) (>0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.mwbase-valueRange

**Path:** `cim:GovHydro3.mwbase`  
**Name:** C:302:DY:GovHydro3.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.pmin-valueRangePair

**Path:** `cim:GovHydro3.pmin`  
**Name:** C:302:DY:GovHydro3.pmin:valueRangePair  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydro3.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro3.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro3.pmax` 

### dy302c:GovHydro3.td-valueRange

**Path:** `cim:GovHydro3.td`  
**Name:** C:302:DY:GovHydro3.td:valueRange  
Input filter time constant (Td) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tf-valueRange

**Path:** `cim:GovHydro3.tf`  
**Name:** C:302:DY:GovHydro3.tf:valueRange  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tp-valueRange

**Path:** `cim:GovHydro3.tp`  
**Name:** C:302:DY:GovHydro3.tp:valueRange  
Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tt-valueRange

**Path:** `cim:GovHydro3.tt`  
**Name:** C:302:DY:GovHydro3.tt:valueRange  
Power feedback time constant (Tt) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tw-valueRange

**Path:** `cim:GovHydro3.tw`  
**Name:** C:302:DY:GovHydro3.tw:valueRange  
Water inertia time constant (Tw) (>= 0).  If = 0, block is bypassed.  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydro4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro4

**Nested Properties:**

### dy302c:GovHydro4.gmin-valueRangePair

**Path:** `cim:GovHydro4.gmin`  
**Name:** C:302:DY:GovHydro4.gmin:valueRangePair  
Minimum gate opening, PU of MWbase (Gmin) (< GovHydro4.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro4.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro4.gmax` 

### dy302c:GovHydro4.mwbase-valueRange

**Path:** `cim:GovHydro4.mwbase`  
**Name:** C:302:DY:GovHydro4.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.rperm-valueRange

**Path:** `cim:GovHydro4.rperm`  
**Name:** C:302:DY:GovHydro4.rperm:valueRange  
Permanent droop (Rperm) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.rtemp-valueRange

**Path:** `cim:GovHydro4.rtemp`  
**Name:** C:302:DY:GovHydro4.rtemp:valueRange  
Temporary droop (Rtemp) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tblade-valueRange

**Path:** `cim:GovHydro4.tblade`  
**Name:** C:302:DY:GovHydro4.tblade:valueRange  
Blade servo time constant (Tblade) (>= 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tg-valueRange

**Path:** `cim:GovHydro4.tg`  
**Name:** C:302:DY:GovHydro4.tg:valueRange  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tp-valueRange

**Path:** `cim:GovHydro4.tp`  
**Name:** C:302:DY:GovHydro4.tp:valueRange  
Pilot servo time constant (Tp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tr-valueRange

**Path:** `cim:GovHydro4.tr`  
**Name:** C:302:DY:GovHydro4.tr:valueRange  
Dashpot time constant (Tr) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tw-valueRange

**Path:** `cim:GovHydro4.tw`  
**Name:** C:302:DY:GovHydro4.tw:valueRange  
Water inertia time constant (Tw) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroDD

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroDD

**Nested Properties:**

### dy302c:GovHydroDD.gmin-valueRangePair

**Path:** `cim:GovHydroDD.gmin`  
**Name:** C:302:DY:GovHydroDD.gmin:valueRangePair  
Minimum gate opening (Gmin) (< GovHydroDD.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroDD.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroDD.gmax` 

### dy302c:GovHydroDD.mwbase-valueRange

**Path:** `cim:GovHydroDD.mwbase`  
**Name:** C:302:DY:GovHydroDD.mwbase:valueRange  
Base for power values (MWbase) (>0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.pmin-valueRangePair

**Path:** `cim:GovHydroDD.pmin`  
**Name:** C:302:DY:GovHydroDD.pmin:valueRangePair  
Minimum gate opening, PU of MWbase (Pmin) (> GovHydroDD.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroDD.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroDD.pmax` 

### dy302c:GovHydroDD.td-valueRange

**Path:** `cim:GovHydroDD.td`  
**Name:** C:302:DY:GovHydroDD.td:valueRange  
Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tf-valueRange

**Path:** `cim:GovHydroDD.tf`  
**Name:** C:302:DY:GovHydroDD.tf:valueRange  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tp-valueRange

**Path:** `cim:GovHydroDD.tp`  
**Name:** C:302:DY:GovHydroDD.tp:valueRange  
Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tt-valueRange

**Path:** `cim:GovHydroDD.tt`  
**Name:** C:302:DY:GovHydroDD.tt:valueRange  
Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tturb-valueRange

**Path:** `cim:GovHydroDD.tturb`  
**Name:** C:302:DY:GovHydroDD.tturb:valueRange  
Turbine time constant (Tturb)  (>= 0).  See parameter detail 3.  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroFrancis

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroFrancis

**Nested Properties:**

### dy302c:GovHydroFrancis.ta-valueRange

**Path:** `cim:GovHydroFrancis.ta`  
**Name:** C:302:DY:GovHydroFrancis.ta:valueRange  
Derivative gain (Ta) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.td-valueRange

**Path:** `cim:GovHydroFrancis.td`  
**Name:** C:302:DY:GovHydroFrancis.td:valueRange  
Washout time constant (Td) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.ts-valueRange

**Path:** `cim:GovHydroFrancis.ts`  
**Name:** C:302:DY:GovHydroFrancis.ts:valueRange  
Gate servo time constant (Ts) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.twnc-valueRange

**Path:** `cim:GovHydroFrancis.twnc`  
**Name:** C:302:DY:GovHydroFrancis.twnc:valueRange  
Water inertia time constant (Twnc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.twng-valueRange

**Path:** `cim:GovHydroFrancis.twng`  
**Name:** C:302:DY:GovHydroFrancis.twng:valueRange  
Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.tx-valueRange

**Path:** `cim:GovHydroFrancis.tx`  
**Name:** C:302:DY:GovHydroFrancis.tx:valueRange  
Derivative feedback gain (Tx) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.valvmin-valueRangePair

**Path:** `cim:GovHydroFrancis.valvmin`  
**Name:** C:302:DY:GovHydroFrancis.valvmin:valueRangePair  
Minimum gate opening (ValvMin) (< GovHydroFrancis.valvmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroFrancis.valvmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroFrancis.valvmax` 

## dy302c:GovHydroIEEE0

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroIEEE0

**Nested Properties:**

### dy302c:GovHydroIEEE0.mwbase-valueRange

**Path:** `cim:GovHydroIEEE0.mwbase`  
**Name:** C:302:DY:GovHydroIEEE0.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.pmin-valueRangePair

**Path:** `cim:GovHydroIEEE0.pmin`  
**Name:** C:302:DY:GovHydroIEEE0.pmin:valueRangePair  
Gate minimum (Pmin) (< GovHydroIEEE.pmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroIEEE.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroIEEE.pmax` 

### dy302c:GovHydroIEEE0.t1-valueRange

**Path:** `cim:GovHydroIEEE0.t1`  
**Name:** C:302:DY:GovHydroIEEE0.t1:valueRange  
Governor lag time constant (T1) (>= 0).  Typical value = 0,25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t2-valueRange

**Path:** `cim:GovHydroIEEE0.t2`  
**Name:** C:302:DY:GovHydroIEEE0.t2:valueRange  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t3-valueRange

**Path:** `cim:GovHydroIEEE0.t3`  
**Name:** C:302:DY:GovHydroIEEE0.t3:valueRange  
Gate actuator time constant (T3) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t4-valueRange

**Path:** `cim:GovHydroIEEE0.t4`  
**Name:** C:302:DY:GovHydroIEEE0.t4:valueRange  
Water starting time (T4) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroIEEE2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroIEEE2

**Nested Properties:**

### dy302c:GovHydroIEEE2.bturb-valueRange

**Path:** `cim:GovHydroIEEE2.bturb`  
**Name:** C:302:DY:GovHydroIEEE2.bturb:valueRange  
Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.mwbase-valueRange

**Path:** `cim:GovHydroIEEE2.mwbase`  
**Name:** C:302:DY:GovHydroIEEE2.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.pmin-valueRangePair

**Path:** `cim:GovHydroIEEE2.pmin`  
**Name:** C:302:DY:GovHydroIEEE2.pmin:valueRangePair  
Minimum gate opening (Pmin) (<GovHydroIEEE2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroIEEE2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroIEEE2.pmax` 

### dy302c:GovHydroIEEE2.tg-valueRange

**Path:** `cim:GovHydroIEEE2.tg`  
**Name:** C:302:DY:GovHydroIEEE2.tg:valueRange  
Gate servo time constant (Tg) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tp-valueRange

**Path:** `cim:GovHydroIEEE2.tp`  
**Name:** C:302:DY:GovHydroIEEE2.tp:valueRange  
Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tr-valueRange

**Path:** `cim:GovHydroIEEE2.tr`  
**Name:** C:302:DY:GovHydroIEEE2.tr:valueRange  
Dashpot time constant (Tr) (>= 0).  Typical value = 12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tw-valueRange

**Path:** `cim:GovHydroIEEE2.tw`  
**Name:** C:302:DY:GovHydroIEEE2.tw:valueRange  
Water inertia time constant (Tw) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.uc-valueRange

**Path:** `cim:GovHydroIEEE2.uc`  
**Name:** C:302:DY:GovHydroIEEE2.uc:valueRange  
Maximum gate closing velocity (Uc) (<0).  Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroPID

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPID

**Nested Properties:**

### dy302c:GovHydroPID.mwbase-valueRange

**Path:** `cim:GovHydroPID.mwbase`  
**Name:** C:302:DY:GovHydroPID.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.pmin-valueRangePair

**Path:** `cim:GovHydroPID.pmin`  
**Name:** C:302:DY:GovHydroPID.pmin:valueRangePair  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydroPID.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPID.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPID.pmax` 

### dy302c:GovHydroPID.td-valueRange

**Path:** `cim:GovHydroPID.td`  
**Name:** C:302:DY:GovHydroPID.td:valueRange  
Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tf-valueRange

**Path:** `cim:GovHydroPID.tf`  
**Name:** C:302:DY:GovHydroPID.tf:valueRange  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tp-valueRange

**Path:** `cim:GovHydroPID.tp`  
**Name:** C:302:DY:GovHydroPID.tp:valueRange  
Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tt-valueRange

**Path:** `cim:GovHydroPID.tt`  
**Name:** C:302:DY:GovHydroPID.tt:valueRange  
Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tturb-valueRange

**Path:** `cim:GovHydroPID.tturb`  
**Name:** C:302:DY:GovHydroPID.tturb:valueRange  
Turbine time constant (Tturb) (>= 0). See Parameter detail 3.  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroPID2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPID2

**Nested Properties:**

### dy302c:GovHydroPID2.gmin-valueRangePair

**Path:** `cim:GovHydroPID2.gmin`  
**Name:** C:302:DY:GovHydroPID2.gmin:valueRangePair  
Minimum gate opening (Gmin) (> GovHydroPID2.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPID2.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPID2.gmax` 

### dy302c:GovHydroPID2.mwbase-valueRange

**Path:** `cim:GovHydroPID2.mwbase`  
**Name:** C:302:DY:GovHydroPID2.mwbase:valueRange  
Base for power values (MWbase) (>0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.ta-valueRange

**Path:** `cim:GovHydroPID2.ta`  
**Name:** C:302:DY:GovHydroPID2.ta:valueRange  
Controller time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.tb-valueRange

**Path:** `cim:GovHydroPID2.tb`  
**Name:** C:302:DY:GovHydroPID2.tb:valueRange  
Gate servo time constant (Tb) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.treg-valueRange

**Path:** `cim:GovHydroPID2.treg`  
**Name:** C:302:DY:GovHydroPID2.treg:valueRange  
Speed detector time constant (Treg) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.tw-valueRange

**Path:** `cim:GovHydroPID2.tw`  
**Name:** C:302:DY:GovHydroPID2.tw:valueRange  
Water inertia time constant (Tw) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.velmax-valueRangePair

**Path:** `cim:GovHydroPID2.velmax`  
**Name:** C:302:DY:GovHydroPID2.velmax:valueRangePair  
Maximum gate opening velocity (Velmax) (< GovHydroPID2.velmin).  Unit = PU / s.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPID2.velmin."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPID2.velmin` 

## dy302c:GovHydroPelton

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPelton

**Nested Properties:**

### dy302c:GovHydroPelton.ta-valueRange

**Path:** `cim:GovHydroPelton.ta`  
**Name:** C:302:DY:GovHydroPelton.ta:valueRange  
Derivative gain (accelerometer time constant) (Ta) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.ts-valueRange

**Path:** `cim:GovHydroPelton.ts`  
**Name:** C:302:DY:GovHydroPelton.ts:valueRange  
Gate servo time constant (Ts) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.tv-valueRange

**Path:** `cim:GovHydroPelton.tv`  
**Name:** C:302:DY:GovHydroPelton.tv:valueRange  
Servomotor integrator time constant (Tv) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.twnc-valueRange

**Path:** `cim:GovHydroPelton.twnc`  
**Name:** C:302:DY:GovHydroPelton.twnc:valueRange  
Water inertia time constant (Twnc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.twng-valueRange

**Path:** `cim:GovHydroPelton.twng`  
**Name:** C:302:DY:GovHydroPelton.twng:valueRange  
Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.tx-valueRange

**Path:** `cim:GovHydroPelton.tx`  
**Name:** C:302:DY:GovHydroPelton.tx:valueRange  
Electronic integrator time constant (Tx) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.valvmin-valueRangePair

**Path:** `cim:GovHydroPelton.valvmin`  
**Name:** C:302:DY:GovHydroPelton.valvmin:valueRangePair  
Minimum gate opening (ValvMin) (< GovHydroPelton.valvmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPelton.valvmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPelton.valvmax` 

## dy302c:GovHydroR

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroR

**Nested Properties:**

### dy302c:GovHydroR.gmin-valueRangePair

**Path:** `cim:GovHydroR.gmin`  
**Name:** C:302:DY:GovHydroR.gmin:valueRangePair  
Minimum governor output (Gmin) (< GovHydroR.gmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroR.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroR.gmax` 

### dy302c:GovHydroR.mwbase-valueRange

**Path:** `cim:GovHydroR.mwbase`  
**Name:** C:302:DY:GovHydroR.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.pmin-valueRangePair

**Path:** `cim:GovHydroR.pmin`  
**Name:** C:302:DY:GovHydroR.pmin:valueRangePair  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydroR.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroR.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroR.pmax` 

### dy302c:GovHydroR.t1-valueRange

**Path:** `cim:GovHydroR.t1`  
**Name:** C:302:DY:GovHydroR.t1:valueRange  
Lead time constant 1 (T1) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t2-valueRange

**Path:** `cim:GovHydroR.t2`  
**Name:** C:302:DY:GovHydroR.t2:valueRange  
Lag time constant 1 (T2) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t3-valueRange

**Path:** `cim:GovHydroR.t3`  
**Name:** C:302:DY:GovHydroR.t3:valueRange  
Lead time constant 2 (T3) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t4-valueRange

**Path:** `cim:GovHydroR.t4`  
**Name:** C:302:DY:GovHydroR.t4:valueRange  
Lag time constant 2 (T4) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t5-valueRange

**Path:** `cim:GovHydroR.t5`  
**Name:** C:302:DY:GovHydroR.t5:valueRange  
Lead time constant 3 (T5) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t6-valueRange

**Path:** `cim:GovHydroR.t6`  
**Name:** C:302:DY:GovHydroR.t6:valueRange  
Lag time constant 3 (T6) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t7-valueRange

**Path:** `cim:GovHydroR.t7`  
**Name:** C:302:DY:GovHydroR.t7:valueRange  
Lead time constant 4 (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t8-valueRange

**Path:** `cim:GovHydroR.t8`  
**Name:** C:302:DY:GovHydroR.t8:valueRange  
Lag time constant 4 (T8) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.td-valueRange

**Path:** `cim:GovHydroR.td`  
**Name:** C:302:DY:GovHydroR.td:valueRange  
Input filter time constant (Td) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tp-valueRange

**Path:** `cim:GovHydroR.tp`  
**Name:** C:302:DY:GovHydroR.tp:valueRange  
Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tt-valueRange

**Path:** `cim:GovHydroR.tt`  
**Name:** C:302:DY:GovHydroR.tt:valueRange  
Power feedback time constant (Tt) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tw-valueRange

**Path:** `cim:GovHydroR.tw`  
**Name:** C:302:DY:GovHydroR.tw:valueRange  
Water inertia time constant (Tw) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroWEH

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroWEH

**Nested Properties:**

### dy302c:GovHydroWEH.gmin-valueRangePair

**Path:** `cim:GovHydroWEH.gmin`  
**Name:** C:302:DY:GovHydroWEH.gmin:valueRangePair  
Minimum gate position (Gmin) (< GovHydroWEH.gmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWEH.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWEH.gmax` 

### dy302c:GovHydroWEH.mwbase-valueRange

**Path:** `cim:GovHydroWEH.mwbase`  
**Name:** C:302:DY:GovHydroWEH.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.td-valueRange

**Path:** `cim:GovHydroWEH.td`  
**Name:** C:302:DY:GovHydroWEH.td:valueRange  
Derivative controller time constant (Td) (>= 0).  Limits the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tdv-valueRange

**Path:** `cim:GovHydroWEH.tdv`  
**Name:** C:302:DY:GovHydroWEH.tdv:valueRange  
Distributive valve time lag time constant (Tdv) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tg-valueRange

**Path:** `cim:GovHydroWEH.tg`  
**Name:** C:302:DY:GovHydroWEH.tg:valueRange  
Value to allow the distribution valve controller to advance beyond the gate movement rate limit (Tg) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tp-valueRange

**Path:** `cim:GovHydroWEH.tp`  
**Name:** C:302:DY:GovHydroWEH.tp:valueRange  
Pilot valve time lag time constant (Tp) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tpe-valueRange

**Path:** `cim:GovHydroWEH.tpe`  
**Name:** C:302:DY:GovHydroWEH.tpe:valueRange  
Electrical power droop time constant (Tpe) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tw-valueRange

**Path:** `cim:GovHydroWEH.tw`  
**Name:** C:302:DY:GovHydroWEH.tw:valueRange  
Water inertia time constant (Tw) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovHydroWPID

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroWPID

**Nested Properties:**

### dy302c:GovHydroWPID.gatmin-valueRangePair

**Path:** `cim:GovHydroWPID.gatmin`  
**Name:** C:302:DY:GovHydroWPID.gatmin:valueRangePair  
Gate opening limit minimum (Gatmin) (< GovHydroWPID.gatmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWPID.gatmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWPID.gatmax` 

### dy302c:GovHydroWPID.mwbase-valueRange

**Path:** `cim:GovHydroWPID.mwbase`  
**Name:** C:302:DY:GovHydroWPID.mwbase:valueRange  
Base for power values  (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.pmin-valueRangePair

**Path:** `cim:GovHydroWPID.pmin`  
**Name:** C:302:DY:GovHydroWPID.pmin:valueRangePair  
Minimum power output (Pmin) (< GovHydroWPID.pmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWPID.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWPID.pmax` 

### dy302c:GovHydroWPID.ta-valueRange

**Path:** `cim:GovHydroWPID.ta`  
**Name:** C:302:DY:GovHydroWPID.ta:valueRange  
Controller time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.tb-valueRange

**Path:** `cim:GovHydroWPID.tb`  
**Name:** C:302:DY:GovHydroWPID.tb:valueRange  
Gate servo time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.treg-valueRange

**Path:** `cim:GovHydroWPID.treg`  
**Name:** C:302:DY:GovHydroWPID.treg:valueRange  
Speed detector time constant (Treg) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.tw-valueRange

**Path:** `cim:GovHydroWPID.tw`  
**Name:** C:302:DY:GovHydroWPID.tw:valueRange  
Water inertia time constant (Tw) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.velmin-valueRangePair

**Path:** `cim:GovHydroWPID.velmin`  
**Name:** C:302:DY:GovHydroWPID.velmin:valueRangePair  
Maximum gate closing velocity (Velmin) (< GovHydroWPID.velmax).  Unit = PU / s.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWPID.velmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWPID.velmax` 

## dy302c:GovSteam0

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam0

**Nested Properties:**

### dy302c:GovSteam0.mwbase-valueRange

**Path:** `cim:GovSteam0.mwbase`  
**Name:** C:302:DY:GovSteam0.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t1-valueRange

**Path:** `cim:GovSteam0.t1`  
**Name:** C:302:DY:GovSteam0.t1:valueRange  
Steam bowl time constant (T1) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t2-valueRange

**Path:** `cim:GovSteam0.t2`  
**Name:** C:302:DY:GovSteam0.t2:valueRange  
Numerator time constant of T2/T3 block (T2) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t3-valueRange

**Path:** `cim:GovSteam0.t3`  
**Name:** C:302:DY:GovSteam0.t3:valueRange  
Reheater time constant (T3) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.vmin-valueRangePair

**Path:** `cim:GovSteam0.vmin`  
**Name:** C:302:DY:GovSteam0.vmin:valueRangePair  
Minimum valve position, PU of mwcap (Vmin) (< GovSteam0.vmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteam0.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteam0.vmax` 

## dy302c:GovSteam1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam1

**Nested Properties:**

### dy302c:GovSteam1.k-valueRange

**Path:** `cim:GovSteam1.k`  
**Name:** C:302:DY:GovSteam1.k:valueRange  
Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.mwbase-valueRange

**Path:** `cim:GovSteam1.mwbase`  
**Name:** C:302:DY:GovSteam1.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.pmin-valueRangePair

**Path:** `cim:GovSteam1.pmin`  
**Name:** C:302:DY:GovSteam1.pmin:valueRangePair  
Minimum valve opening (Pmin) (>= 0 and < GovSteam1.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteam1.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteam1.pmax` 

### dy302c:GovSteam1.t1-valueRange

**Path:** `cim:GovSteam1.t1`  
**Name:** C:302:DY:GovSteam1.t1:valueRange  
Governor lag time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t2-valueRange

**Path:** `cim:GovSteam1.t2`  
**Name:** C:302:DY:GovSteam1.t2:valueRange  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t3-valueRange

**Path:** `cim:GovSteam1.t3`  
**Name:** C:302:DY:GovSteam1.t3:valueRange  
Valve positioner time constant (T3) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t4-valueRange

**Path:** `cim:GovSteam1.t4`  
**Name:** C:302:DY:GovSteam1.t4:valueRange  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t5-valueRange

**Path:** `cim:GovSteam1.t5`  
**Name:** C:302:DY:GovSteam1.t5:valueRange  
Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t6-valueRange

**Path:** `cim:GovSteam1.t6`  
**Name:** C:302:DY:GovSteam1.t6:valueRange  
Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t7-valueRange

**Path:** `cim:GovSteam1.t7`  
**Name:** C:302:DY:GovSteam1.t7:valueRange  
Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.uc-valueRange

**Path:** `cim:GovSteam1.uc`  
**Name:** C:302:DY:GovSteam1.uc:valueRange  
Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.uo-valueRange

**Path:** `cim:GovSteam1.uo`  
**Name:** C:302:DY:GovSteam1.uo:valueRange  
Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteam2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam2

**Nested Properties:**

### dy302c:GovSteam2.pmin-valueRangePair

**Path:** `cim:GovSteam2.pmin`  
**Name:** C:302:DY:GovSteam2.pmin:valueRangePair  
Minimum fuel flow (P<sub>MIN</sub>) (< GovSteam2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteam2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteam2.pmax` 

### dy302c:GovSteam2.t1-valueRange

**Path:** `cim:GovSteam2.t1`  
**Name:** C:302:DY:GovSteam2.t1:valueRange  
Governor lag time constant (T<sub>1</sub>) (> 0).  Typical value = 0,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam2.t2-valueRange

**Path:** `cim:GovSteam2.t2`  
**Name:** C:302:DY:GovSteam2.t2:valueRange  
Governor lead time constant (T<sub>2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamBB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamBB

**Nested Properties:**

### dy302c:GovSteamBB.fcut-valueRange

**Path:** `cim:GovSteamBB.fcut`  
**Name:** C:302:DY:GovSteamBB.fcut:valueRange  
Frequency deadband (f<sub>cut</sub>) (>= 0).  Typical value = 0,002.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.kls-valueRange

**Path:** `cim:GovSteamBB.kls`  
**Name:** C:302:DY:GovSteamBB.kls:valueRange  
Gain (Kls) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.pmin-valueRangePair

**Path:** `cim:GovSteamBB.pmin`  
**Name:** C:302:DY:GovSteamBB.pmin:valueRangePair  
Low power limit (Pmin) (< GovSteamBB.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamBB.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamBB.pmax` 

### dy302c:GovSteamBB.td-valueRange

**Path:** `cim:GovSteamBB.td`  
**Name:** C:302:DY:GovSteamBB.td:valueRange  
Time constant (Td) (> 0).  Typical value = 1,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.tn-valueRange

**Path:** `cim:GovSteamBB.tn`  
**Name:** C:302:DY:GovSteamBB.tn:valueRange  
Time constant (Tn) (> 0).  Typical value = 1,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamCC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamCC

**Nested Properties:**

### dy302c:GovSteamCC.mwbase-valueRange

**Path:** `cim:GovSteamCC.mwbase`  
**Name:** C:302:DY:GovSteamCC.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.rhp-valueRange

**Path:** `cim:GovSteamCC.rhp`  
**Name:** C:302:DY:GovSteamCC.rhp:valueRange  
HP governor droop (Rhp) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.rlp-valueRange

**Path:** `cim:GovSteamCC.rlp`  
**Name:** C:302:DY:GovSteamCC.rlp:valueRange  
LP governor droop (Rlp) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t1hp-valueRange

**Path:** `cim:GovSteamCC.t1hp`  
**Name:** C:302:DY:GovSteamCC.t1hp:valueRange  
HP governor time constant (T1hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t1lp-valueRange

**Path:** `cim:GovSteamCC.t1lp`  
**Name:** C:302:DY:GovSteamCC.t1lp:valueRange  
LP governor time constant (T1lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t3hp-valueRange

**Path:** `cim:GovSteamCC.t3hp`  
**Name:** C:302:DY:GovSteamCC.t3hp:valueRange  
HP turbine time constant (T3hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t3lp-valueRange

**Path:** `cim:GovSteamCC.t3lp`  
**Name:** C:302:DY:GovSteamCC.t3lp:valueRange  
LP turbine time constant (T3lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t4hp-valueRange

**Path:** `cim:GovSteamCC.t4hp`  
**Name:** C:302:DY:GovSteamCC.t4hp:valueRange  
HP turbine time constant (T4hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t4lp-valueRange

**Path:** `cim:GovSteamCC.t4lp`  
**Name:** C:302:DY:GovSteamCC.t4lp:valueRange  
LP turbine time constant (T4lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t5hp-valueRange

**Path:** `cim:GovSteamCC.t5hp`  
**Name:** C:302:DY:GovSteamCC.t5hp:valueRange  
HP reheater time constant (T5hp) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t5lp-valueRange

**Path:** `cim:GovSteamCC.t5lp`  
**Name:** C:302:DY:GovSteamCC.t5lp:valueRange  
LP reheater time constant (T5lp) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamEU

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamEU

**Nested Properties:**

### dy302c:GovSteamEU.mwbase-valueRange

**Path:** `cim:GovSteamEU.mwbase`  
**Name:** C:302:DY:GovSteamEU.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tb-valueRange

**Path:** `cim:GovSteamEU.tb`  
**Name:** C:302:DY:GovSteamEU.tb:valueRange  
Boiler time constant (Tb) (>= 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tdp-valueRange

**Path:** `cim:GovSteamEU.tdp`  
**Name:** C:302:DY:GovSteamEU.tdp:valueRange  
Derivative time constant of the power controller (Tdp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.ten-valueRange

**Path:** `cim:GovSteamEU.ten`  
**Name:** C:302:DY:GovSteamEU.ten:valueRange  
Electro hydraulic transducer (Ten) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tf-valueRange

**Path:** `cim:GovSteamEU.tf`  
**Name:** C:302:DY:GovSteamEU.tf:valueRange  
Frequency transducer time constant (Tf) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tfp-valueRange

**Path:** `cim:GovSteamEU.tfp`  
**Name:** C:302:DY:GovSteamEU.tfp:valueRange  
Time constant of the power controller (Tfp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.thp-valueRange

**Path:** `cim:GovSteamEU.thp`  
**Name:** C:302:DY:GovSteamEU.thp:valueRange  
High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,31.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tip-valueRange

**Path:** `cim:GovSteamEU.tip`  
**Name:** C:302:DY:GovSteamEU.tip:valueRange  
Integral time constant of the power controller (Tip) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tlp-valueRange

**Path:** `cim:GovSteamEU.tlp`  
**Name:** C:302:DY:GovSteamEU.tlp:valueRange  
Low pressure (LP) time constant of the turbine (Tlp) (>= 0).  Typical value = 0,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tp-valueRange

**Path:** `cim:GovSteamEU.tp`  
**Name:** C:302:DY:GovSteamEU.tp:valueRange  
Power transducer time constant (Tp) (>= 0).  Typical value = 0,07.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.trh-valueRange

**Path:** `cim:GovSteamEU.trh`  
**Name:** C:302:DY:GovSteamEU.trh:valueRange  
Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tvhp-valueRange

**Path:** `cim:GovSteamEU.tvhp`  
**Name:** C:302:DY:GovSteamEU.tvhp:valueRange  
Control valves servo time constant (Tvhp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tvip-valueRange

**Path:** `cim:GovSteamEU.tvip`  
**Name:** C:302:DY:GovSteamEU.tvip:valueRange  
Intercept valves servo time constant (Tvip) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tw-valueRange

**Path:** `cim:GovSteamEU.tw`  
**Name:** C:302:DY:GovSteamEU.tw:valueRange  
Speed transducer time constant (Tw) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.wfmin-valueRangePair

**Path:** `cim:GovSteamEU.wfmin`  
**Name:** C:302:DY:GovSteamEU.wfmin:valueRangePair  
Lower limit for frequency correction (Wfmin) (< GovSteamEU.wfmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamEU.wfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamEU.wfmax` 

### dy302c:GovSteamEU.wwmin-valueRangePair

**Path:** `cim:GovSteamEU.wwmin`  
**Name:** C:302:DY:GovSteamEU.wwmin:valueRangePair  
Lower limit for the speed governor frequency correction (Wwmin) (< GovSteamEU.wwmax).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamEU.wwmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamEU.wwmax` 

## dy302c:GovSteamFV2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV2

**Nested Properties:**

### dy302c:GovSteamFV2.mwbase-valueRange

**Path:** `cim:GovSteamFV2.mwbase`  
**Name:** C:302:DY:GovSteamFV2.mwbase:valueRange  
Alternate base used instead of machine base in equipment model if necessary (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.t1-valueRange

**Path:** `cim:GovSteamFV2.t1`  
**Name:** C:302:DY:GovSteamFV2.t1:valueRange  
Governor time constant (T1) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.t3-valueRange

**Path:** `cim:GovSteamFV2.t3`  
**Name:** C:302:DY:GovSteamFV2.t3:valueRange  
Reheater time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.ta-valueRange

**Path:** `cim:GovSteamFV2.ta`  
**Name:** C:302:DY:GovSteamFV2.ta:valueRange  
Time after initial time for valve to close (Ta) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tb-valueRange

**Path:** `cim:GovSteamFV2.tb`  
**Name:** C:302:DY:GovSteamFV2.tb:valueRange  
Time after initial time for valve to begin opening (Tb) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tc-valueRange

**Path:** `cim:GovSteamFV2.tc`  
**Name:** C:302:DY:GovSteamFV2.tc:valueRange  
Time after initial time for valve to become fully open (Tc) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tt-valueRange

**Path:** `cim:GovSteamFV2.tt`  
**Name:** C:302:DY:GovSteamFV2.tt:valueRange  
Time constant with which power falls off after intercept valve closure (Tt) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.vmin-valueRangePair

**Path:** `cim:GovSteamFV2.vmin`  
**Name:** C:302:DY:GovSteamFV2.vmin:valueRangePair  
(Vmin) (< GovSteamFV2.vmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamFV2.vmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamFV2.vmax` 

## dy302c:GovSteamFV3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV3

**Nested Properties:**

### dy302c:GovSteamFV3.mwbase-valueRange

**Path:** `cim:GovSteamFV3.mwbase`  
**Name:** C:302:DY:GovSteamFV3.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.pmin-valueRangePair

**Path:** `cim:GovSteamFV3.pmin`  
**Name:** C:302:DY:GovSteamFV3.pmin:valueRangePair  
Minimum valve opening, PU of MWbase (Pmin) (< GovSteamFV3.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamFV3.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamFV3.pmax` 

### dy302c:GovSteamFV3.t1-valueRange

**Path:** `cim:GovSteamFV3.t1`  
**Name:** C:302:DY:GovSteamFV3.t1:valueRange  
Governor lead time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t2-valueRange

**Path:** `cim:GovSteamFV3.t2`  
**Name:** C:302:DY:GovSteamFV3.t2:valueRange  
Governor lag time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t3-valueRange

**Path:** `cim:GovSteamFV3.t3`  
**Name:** C:302:DY:GovSteamFV3.t3:valueRange  
Valve positioner time constant (T3) (> 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t4-valueRange

**Path:** `cim:GovSteamFV3.t4`  
**Name:** C:302:DY:GovSteamFV3.t4:valueRange  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t6-valueRange

**Path:** `cim:GovSteamFV3.t6`  
**Name:** C:302:DY:GovSteamFV3.t6:valueRange  
Time constant of crossover or third boiler pass (T6) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.ta-valueRange

**Path:** `cim:GovSteamFV3.ta`  
**Name:** C:302:DY:GovSteamFV3.ta:valueRange  
Time to close intercept valve (IV) (Ta) (>= 0).  Typical value = 0,97.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.tb-valueRange

**Path:** `cim:GovSteamFV3.tb`  
**Name:** C:302:DY:GovSteamFV3.tb:valueRange  
Time until IV starts to reopen (Tb) (>= 0).  Typical value = 0,98.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.tc-valueRange

**Path:** `cim:GovSteamFV3.tc`  
**Name:** C:302:DY:GovSteamFV3.tc:valueRange  
Time until IV is fully open (Tc) (>= 0).  Typical value = 0,99.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamFV4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV4

**Nested Properties:**

### dy302c:GovSteamFV4.ta-valueRange

**Path:** `cim:GovSteamFV4.ta`  
**Name:** C:302:DY:GovSteamFV4.ta:valueRange  
Control valves rate opening time (Ta) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tam-valueRange

**Path:** `cim:GovSteamFV4.tam`  
**Name:** C:302:DY:GovSteamFV4.tam:valueRange  
Intercept valves rate opening time (Tam) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tc-valueRange

**Path:** `cim:GovSteamFV4.tc`  
**Name:** C:302:DY:GovSteamFV4.tc:valueRange  
Control valves rate closing time (Tc) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tcm-valueRange

**Path:** `cim:GovSteamFV4.tcm`  
**Name:** C:302:DY:GovSteamFV4.tcm:valueRange  
Intercept valves rate closing time (Tcm) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tdc-valueRange

**Path:** `cim:GovSteamFV4.tdc`  
**Name:** C:302:DY:GovSteamFV4.tdc:valueRange  
Derivative time constant of pressure regulator (Tdc) (>= 0).  Typical value = 90.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tf1-valueRange

**Path:** `cim:GovSteamFV4.tf1`  
**Name:** C:302:DY:GovSteamFV4.tf1:valueRange  
Time constant of fuel regulation (Tf1) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tf2-valueRange

**Path:** `cim:GovSteamFV4.tf2`  
**Name:** C:302:DY:GovSteamFV4.tf2:valueRange  
Time constant of steam chest (Tf2) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.thp-valueRange

**Path:** `cim:GovSteamFV4.thp`  
**Name:** C:302:DY:GovSteamFV4.thp:valueRange  
High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tmp-valueRange

**Path:** `cim:GovSteamFV4.tmp`  
**Name:** C:302:DY:GovSteamFV4.tmp:valueRange  
Low pressure (LP) time constant of the turbine (Tmp) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.trh-valueRange

**Path:** `cim:GovSteamFV4.trh`  
**Name:** C:302:DY:GovSteamFV4.trh:valueRange  
Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tv-valueRange

**Path:** `cim:GovSteamFV4.tv`  
**Name:** C:302:DY:GovSteamFV4.tv:valueRange  
Boiler time constant (Tv) (>= 0).  Typical value = 60.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.ty-valueRange

**Path:** `cim:GovSteamFV4.ty`  
**Name:** C:302:DY:GovSteamFV4.ty:valueRange  
Control valves servo time constant (Ty) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamIEEE1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamIEEE1

**Nested Properties:**

### dy302c:GovSteamIEEE1.k-valueRange

**Path:** `cim:GovSteamIEEE1.k`  
**Name:** C:302:DY:GovSteamIEEE1.k:valueRange  
Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.mwbase-valueRange

**Path:** `cim:GovSteamIEEE1.mwbase`  
**Name:** C:302:DY:GovSteamIEEE1.mwbase:valueRange  
Base for power values (MWbase) (> 0). Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.pmin-valueRangePair

**Path:** `cim:GovSteamIEEE1.pmin`  
**Name:** C:302:DY:GovSteamIEEE1.pmin:valueRangePair  
Minimum valve opening (Pmin) (>= 0 and < GovSteamIEEE1.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamIEEE1.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamIEEE1.pmax` 

### dy302c:GovSteamIEEE1.t1-valueRange

**Path:** `cim:GovSteamIEEE1.t1`  
**Name:** C:302:DY:GovSteamIEEE1.t1:valueRange  
Governor lag time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t2-valueRange

**Path:** `cim:GovSteamIEEE1.t2`  
**Name:** C:302:DY:GovSteamIEEE1.t2:valueRange  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t3-valueRange

**Path:** `cim:GovSteamIEEE1.t3`  
**Name:** C:302:DY:GovSteamIEEE1.t3:valueRange  
Valve positioner time constant (T3) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t4-valueRange

**Path:** `cim:GovSteamIEEE1.t4`  
**Name:** C:302:DY:GovSteamIEEE1.t4:valueRange  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t5-valueRange

**Path:** `cim:GovSteamIEEE1.t5`  
**Name:** C:302:DY:GovSteamIEEE1.t5:valueRange  
Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t6-valueRange

**Path:** `cim:GovSteamIEEE1.t6`  
**Name:** C:302:DY:GovSteamIEEE1.t6:valueRange  
Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t7-valueRange

**Path:** `cim:GovSteamIEEE1.t7`  
**Name:** C:302:DY:GovSteamIEEE1.t7:valueRange  
Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.uc-valueRange

**Path:** `cim:GovSteamIEEE1.uc`  
**Name:** C:302:DY:GovSteamIEEE1.uc:valueRange  
Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.uo-valueRange

**Path:** `cim:GovSteamIEEE1.uo`  
**Name:** C:302:DY:GovSteamIEEE1.uo:valueRange  
Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:GovSteamSGO

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamSGO

**Nested Properties:**

### dy302c:GovSteamSGO.mwbase-valueRange

**Path:** `cim:GovSteamSGO.mwbase`  
**Name:** C:302:DY:GovSteamSGO.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.pmin-valueRangePair

**Path:** `cim:GovSteamSGO.pmin`  
**Name:** C:302:DY:GovSteamSGO.pmin:valueRangePair  
Lower power limit (Pmin) (>= 0 and < GovSteamSGO.pmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamSGO.pmax; or negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamSGO.pmax` 

### dy302c:GovSteamSGO.t1-valueRange

**Path:** `cim:GovSteamSGO.t1`  
**Name:** C:302:DY:GovSteamSGO.t1:valueRange  
Controller lag (T1) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t2-valueRange

**Path:** `cim:GovSteamSGO.t2`  
**Name:** C:302:DY:GovSteamSGO.t2:valueRange  
Controller lead compensation (T2) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t3-valueRange

**Path:** `cim:GovSteamSGO.t3`  
**Name:** C:302:DY:GovSteamSGO.t3:valueRange  
Governor lag (T3) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t4-valueRange

**Path:** `cim:GovSteamSGO.t4`  
**Name:** C:302:DY:GovSteamSGO.t4:valueRange  
Delay due to steam inlet volumes associated with steam chest and inlet piping (T4) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t5-valueRange

**Path:** `cim:GovSteamSGO.t5`  
**Name:** C:302:DY:GovSteamSGO.t5:valueRange  
Reheater delay including hot and cold leads (T5) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t6-valueRange

**Path:** `cim:GovSteamSGO.t6`  
**Name:** C:302:DY:GovSteamSGO.t6:valueRange  
Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:LoadComposite

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadComposite

**Nested Properties:**

### dy302c:LoadComposite.h-valueRange

**Path:** `cim:LoadComposite.h`  
**Name:** C:302:DY:LoadComposite.h:valueRange  
Inertia constant (H) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadComposite.pfrac-valueRange

**Path:** `cim:LoadComposite.pfrac`  
**Name:** C:302:DY:LoadComposite.pfrac:valueRange  
Fraction of constant-power load to be represented by this motor model (P<sub>FRAC</sub>) (>= 0,0 and <= 1,0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is outside the range [0,1]."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `1.0` 

## dy302c:LoadGenericNonLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadGenericNonLinear

**Nested Properties:**

### dy302c:LoadGenericNonLinear.tp-valueRange

**Path:** `cim:LoadGenericNonLinear.tp`  
**Name:** C:302:DY:LoadGenericNonLinear.tp:valueRange  
Time constant of lag function of active power (T<sub>P</sub>) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadGenericNonLinear.tq-valueRange

**Path:** `cim:LoadGenericNonLinear.tq`  
**Name:** C:302:DY:LoadGenericNonLinear.tq:valueRange  
Time constant of lag function of reactive power (T<sub>Q</sub>) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:LoadMotor

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadMotor

**Nested Properties:**

### dy302c:LoadMotor.h-valueRange

**Path:** `cim:LoadMotor.h`  
**Name:** C:302:DY:LoadMotor.h:valueRange  
Inertia constant (H) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.pfrac-valueRange

**Path:** `cim:LoadMotor.pfrac`  
**Name:** C:302:DY:LoadMotor.pfrac:valueRange  
Fraction of constant-power load to be represented by this motor model (Pfrac) (>= 0,0 and <= 1,0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is outside the range [0,1]."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `1.0` 

### dy302c:LoadMotor.tbkr-valueRange

**Path:** `cim:LoadMotor.tbkr`  
**Name:** C:302:DY:LoadMotor.tbkr:valueRange  
Circuit breaker operating time (Tbkr) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tpo-valueRange

**Path:** `cim:LoadMotor.tpo`  
**Name:** C:302:DY:LoadMotor.tpo:valueRange  
Transient rotor time constant (Tpo) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tppo-valueRange

**Path:** `cim:LoadMotor.tppo`  
**Name:** C:302:DY:LoadMotor.tppo:valueRange  
Subtransient rotor time constant (Tppo) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tv-valueRange

**Path:** `cim:LoadMotor.tv`  
**Name:** C:302:DY:LoadMotor.tv:valueRange  
Voltage trip pickup time (Tv) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:LoadStatic

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadStatic

## dy302c:MechanicalLoadDynamics

**Name:** C:302:DY:MechanicalLoadDynamics:associationsCondition  
MechanicalLoadDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:MechanicalLoadUserDefined
- targetClass: cim:MechLoad1

**Constraints:**

- **sh:XoneConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1`

## dy302c:OverexcLim2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLim2

**Nested Properties:**

### dy302c:OverexcLim2.voimin-valueRangePair

**Path:** `cim:OverexcLim2.voimin`  
**Name:** C:302:DY:OverexcLim2.voimin:valueRangePair  
Minimum error signal (V<sub>OIMIN</sub>) (< OverexcLim2.voimax).  Typical value = -9999.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than OverexcLim2.voimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:OverexcLim2.voimax` 

## dy302c:OverexcLimX1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLimX1

**Nested Properties:**

### dy302c:OverexcLimX1.t1-valueRange

**Path:** `cim:OverexcLimX1.t1`  
**Name:** C:302:DY:OverexcLimX1.t1:valueRange  
Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME<sub>1</sub>) (>= 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.t2-valueRange

**Path:** `cim:OverexcLimX1.t2`  
**Name:** C:302:DY:OverexcLimX1.t2:valueRange  
Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME<sub>2</sub>) (>= 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.t3-valueRange

**Path:** `cim:OverexcLimX1.t3`  
**Name:** C:302:DY:OverexcLimX1.t3:valueRange  
Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME<sub>3</sub>) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.vlow-valueRange

**Path:** `cim:OverexcLimX1.vlow`  
**Name:** C:302:DY:OverexcLimX1.vlow:valueRange  
Low voltage limit (V<sub>LOW</sub>) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:OverexcLimX2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLimX2

**Nested Properties:**

### dy302c:OverexcLimX2.t1-valueRange

**Path:** `cim:OverexcLimX2.t1`  
**Name:** C:302:DY:OverexcLimX2.t1:valueRange  
Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME<sub>1</sub>) (>= 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.t2-valueRange

**Path:** `cim:OverexcLimX2.t2`  
**Name:** C:302:DY:OverexcLimX2.t2:valueRange  
Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME<sub>2</sub>) (>= 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.t3-valueRange

**Path:** `cim:OverexcLimX2.t3`  
**Name:** C:302:DY:OverexcLimX2.t3:valueRange  
Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME<sub>3</sub>) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.vlow-valueRange

**Path:** `cim:OverexcLimX2.vlow`  
**Name:** C:302:DY:OverexcLimX2.vlow:valueRange  
Low voltage limit (V<sub>LOW</sub>) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PFVArType1IEEEPFController

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PFVArType1IEEEPFController

**Nested Properties:**

### dy302c:PFVArType1IEEEPFController.tpfc-valueRange

**Path:** `cim:PFVArType1IEEEPFController.tpfc`  
**Name:** C:302:DY:PFVArType1IEEEPFController.tpfc:valueRange  
PF controller time delay (T<sub>PFC</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PFVArType1IEEEPFController.vvtmin-valueRangePair

**Path:** `cim:PFVArType1IEEEPFController.vvtmin`  
**Name:** C:302:DY:PFVArType1IEEEPFController.vvtmin:valueRangePair  
Minimum machine terminal voltage needed to enable pf/var controller (V<sub>VTMIN</sub>) (< PFVArType1IEEEPFController.vvtmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PFVArType1IEEEPFController.vvtmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PFVArType1IEEEPFController.vvtmax` 

## dy302c:PFVArType1IEEEVArController

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PFVArType1IEEEVArController

**Nested Properties:**

### dy302c:PFVArType1IEEEVArController.tvarc-valueRange

**Path:** `cim:PFVArType1IEEEVArController.tvarc`  
**Name:** C:302:DY:PFVArType1IEEEVArController.tvarc:valueRange  
Var controller time delay (T<sub>VARC</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PFVArType1IEEEVArController.vvtmin-valueRangePair

**Path:** `cim:PFVArType1IEEEVArController.vvtmin`  
**Name:** C:302:DY:PFVArType1IEEEVArController.vvtmin:valueRangePair  
Minimum machine terminal voltage needed to enable pf/var controller (V<sub>VTMIN</sub>) (< PVFArType1IEEEVArController.vvtmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PVFArType1IEEEVArController.vvtmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PVFArType1IEEEVArController.vvtmax` 

## dy302c:Pss1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss1

**Nested Properties:**

### dy302c:Pss1.t10-valueRange

**Path:** `cim:Pss1.t10`  
**Name:** C:302:DY:Pss1.t10:valueRange  
Lead/lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t5-valueRange

**Path:** `cim:Pss1.t5`  
**Name:** C:302:DY:Pss1.t5:valueRange  
Washout (T<sub>5</sub>) (>= 0).  Typical value = 3,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t6-valueRange

**Path:** `cim:Pss1.t6`  
**Name:** C:302:DY:Pss1.t6:valueRange  
Filter time constant (T<sub>6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t7-valueRange

**Path:** `cim:Pss1.t7`  
**Name:** C:302:DY:Pss1.t7:valueRange  
Lead/lag time constant (T<sub>7</sub>) (>= 0). If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t8-valueRange

**Path:** `cim:Pss1.t8`  
**Name:** C:302:DY:Pss1.t8:valueRange  
Lead/lag time constant (T<sub>8</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t9-valueRange

**Path:** `cim:Pss1.t9`  
**Name:** C:302:DY:Pss1.t9:valueRange  
Lead/lag time constant (T<sub>9</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.tpe-valueRange

**Path:** `cim:Pss1.tpe`  
**Name:** C:302:DY:Pss1.tpe:valueRange  
Electric power filter time constant (T<sub>PE</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:Pss1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss1A

**Nested Properties:**

### dy302c:Pss1A.t1-valueRange

**Path:** `cim:Pss1A.t1`  
**Name:** C:302:DY:Pss1A.t1:valueRange  
Lead/lag time constant (T<sub>1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t2-valueRange

**Path:** `cim:Pss1A.t2`  
**Name:** C:302:DY:Pss1A.t2:valueRange  
Lead/lag time constant (T<sub>2</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t3-valueRange

**Path:** `cim:Pss1A.t3`  
**Name:** C:302:DY:Pss1A.t3:valueRange  
Lead/lag time constant (T<sub>3</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t4-valueRange

**Path:** `cim:Pss1A.t4`  
**Name:** C:302:DY:Pss1A.t4:valueRange  
Lead/lag time constant (T<sub>4</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t5-valueRange

**Path:** `cim:Pss1A.t5`  
**Name:** C:302:DY:Pss1A.t5:valueRange  
Washout time constant (T<sub>5</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t6-valueRange

**Path:** `cim:Pss1A.t6`  
**Name:** C:302:DY:Pss1A.t6:valueRange  
Transducer time constant (T<sub>6</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.tdelay-valueRange

**Path:** `cim:Pss1A.tdelay`  
**Name:** C:302:DY:Pss1A.tdelay:valueRange  
Time constant (Tdelay) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.vrmin-valueRangePair

**Path:** `cim:Pss1A.vrmin`  
**Name:** C:302:DY:Pss1A.vrmin:valueRangePair  
Minimum stabilizer output (Vrmin) (< Pss1A.vrmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss1A.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss1A.vrmax` 

## dy302c:Pss2B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss2B

**Nested Properties:**

### dy302c:Pss2B.t1-valueRange

**Path:** `cim:Pss2B.t1`  
**Name:** C:302:DY:Pss2B.t1:valueRange  
Lead/lag time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t10-valueRange

**Path:** `cim:Pss2B.t10`  
**Name:** C:302:DY:Pss2B.t10:valueRange  
Lead/lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t11-valueRange

**Path:** `cim:Pss2B.t11`  
**Name:** C:302:DY:Pss2B.t11:valueRange  
Lead/lag time constant (T<sub>11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t2-valueRange

**Path:** `cim:Pss2B.t2`  
**Name:** C:302:DY:Pss2B.t2:valueRange  
Lead/lag time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t3-valueRange

**Path:** `cim:Pss2B.t3`  
**Name:** C:302:DY:Pss2B.t3:valueRange  
Lead/lag time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t4-valueRange

**Path:** `cim:Pss2B.t4`  
**Name:** C:302:DY:Pss2B.t4:valueRange  
Lead/lag time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t6-valueRange

**Path:** `cim:Pss2B.t6`  
**Name:** C:302:DY:Pss2B.t6:valueRange  
Time constant on signal #1 (T<sub>6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t7-valueRange

**Path:** `cim:Pss2B.t7`  
**Name:** C:302:DY:Pss2B.t7:valueRange  
Time constant on signal #2 (T<sub>7</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t8-valueRange

**Path:** `cim:Pss2B.t8`  
**Name:** C:302:DY:Pss2B.t8:valueRange  
Lead of ramp tracking filter (T<sub>8</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t9-valueRange

**Path:** `cim:Pss2B.t9`  
**Name:** C:302:DY:Pss2B.t9:valueRange  
Lag of ramp tracking filter (T<sub>9</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.ta-valueRange

**Path:** `cim:Pss2B.ta`  
**Name:** C:302:DY:Pss2B.ta:valueRange  
Lead constant (T<sub>a</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tb-valueRange

**Path:** `cim:Pss2B.tb`  
**Name:** C:302:DY:Pss2B.tb:valueRange  
Lag time constant (T<sub>b</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw1-valueRange

**Path:** `cim:Pss2B.tw1`  
**Name:** C:302:DY:Pss2B.tw1:valueRange  
First washout on signal #1 (T<sub>w1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw2-valueRange

**Path:** `cim:Pss2B.tw2`  
**Name:** C:302:DY:Pss2B.tw2:valueRange  
Second washout on signal #1 (T<sub>w2</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw3-valueRange

**Path:** `cim:Pss2B.tw3`  
**Name:** C:302:DY:Pss2B.tw3:valueRange  
First washout on signal #2 (T<sub>w3</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw4-valueRange

**Path:** `cim:Pss2B.tw4`  
**Name:** C:302:DY:Pss2B.tw4:valueRange  
Second washout on signal #2 (T<sub>w4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.vsi1min-valueRangePair

**Path:** `cim:Pss2B.vsi1min`  
**Name:** C:302:DY:Pss2B.vsi1min:valueRangePair  
Input signal #1 minimum limit (Vsi1min) (< Pss2B.vsi1max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2B.vsi1max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2B.vsi1max` 

### dy302c:Pss2B.vsi2min-valueRangePair

**Path:** `cim:Pss2B.vsi2min`  
**Name:** C:302:DY:Pss2B.vsi2min:valueRangePair  
Input signal #2 minimum limit (Vsi2min) (< Pss2B.vsi2max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2B.vsi2max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2B.vsi2max` 

### dy302c:Pss2B.vstmin-valueRangePair

**Path:** `cim:Pss2B.vstmin`  
**Name:** C:302:DY:Pss2B.vstmin:valueRangePair  
Stabilizer output minimum limit (Vstmin) (< Pss2B.vstmax).  Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2B.vstmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2B.vstmax` 

## dy302c:Pss2ST

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss2ST

**Nested Properties:**

### dy302c:Pss2ST.inputSignal1Type-allowedValues

**Path:** `cim:Pss2ST.inputSignal1Type`  
**Name:** C:302:DY:Pss2ST.inputSignal1Type:allowedValues  
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:Pss2ST.inputSignal2Type-allowedValues

**Path:** `cim:Pss2ST.inputSignal2Type`  
**Name:** C:302:DY:Pss2ST.inputSignal2Type:allowedValues  
Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative - shall be different than Pss2ST.inputSignal1Type).  Typical value = busVoltageDerivative.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:Pss2ST.lsmin-valueRangePair

**Path:** `cim:Pss2ST.lsmin`  
**Name:** C:302:DY:Pss2ST.lsmin:valueRangePair  
Limiter (L<sub>SMIN</sub>) (< Pss2ST.lsmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2ST.lsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2ST.lsmax` 

### dy302c:Pss2ST.t1-valueRange

**Path:** `cim:Pss2ST.t1`  
**Name:** C:302:DY:Pss2ST.t1:valueRange  
Time constant (T<sub>1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t10-valueRange

**Path:** `cim:Pss2ST.t10`  
**Name:** C:302:DY:Pss2ST.t10:valueRange  
Time constant (T<sub>10</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t2-valueRange

**Path:** `cim:Pss2ST.t2`  
**Name:** C:302:DY:Pss2ST.t2:valueRange  
Time constant (T<sub>2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t3-valueRange

**Path:** `cim:Pss2ST.t3`  
**Name:** C:302:DY:Pss2ST.t3:valueRange  
Time constant (T<sub>3</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t4-valueRange

**Path:** `cim:Pss2ST.t4`  
**Name:** C:302:DY:Pss2ST.t4:valueRange  
Time constant (T<sub>4</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t5-valueRange

**Path:** `cim:Pss2ST.t5`  
**Name:** C:302:DY:Pss2ST.t5:valueRange  
Time constant (T<sub>5</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t6-valueRange

**Path:** `cim:Pss2ST.t6`  
**Name:** C:302:DY:Pss2ST.t6:valueRange  
Time constant (T<sub>6</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t7-valueRange

**Path:** `cim:Pss2ST.t7`  
**Name:** C:302:DY:Pss2ST.t7:valueRange  
Time constant (T<sub>7</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t8-valueRange

**Path:** `cim:Pss2ST.t8`  
**Name:** C:302:DY:Pss2ST.t8:valueRange  
Time constant (T<sub>8</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t9-valueRange

**Path:** `cim:Pss2ST.t9`  
**Name:** C:302:DY:Pss2ST.t9:valueRange  
Time constant (T<sub>9</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:Pss5

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss5

**Nested Properties:**

### dy302c:Pss5.tl1-valueRange

**Path:** `cim:Pss5.tl1`  
**Name:** C:302:DY:Pss5.tl1:valueRange  
Lead/lag time constant (T<sub>L1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl2-valueRange

**Path:** `cim:Pss5.tl2`  
**Name:** C:302:DY:Pss5.tl2:valueRange  
Lead/lag time constant (T<sub>L2</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl3-valueRange

**Path:** `cim:Pss5.tl3`  
**Name:** C:302:DY:Pss5.tl3:valueRange  
Lead/lag time constant (T<sub>L3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl4-valueRange

**Path:** `cim:Pss5.tl4`  
**Name:** C:302:DY:Pss5.tl4:valueRange  
Lead/lag time constant (T<sub>L4</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tpe-valueRange

**Path:** `cim:Pss5.tpe`  
**Name:** C:302:DY:Pss5.tpe:valueRange  
Electric power filter time constant (T<sub>PE</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tw1-valueRange

**Path:** `cim:Pss5.tw1`  
**Name:** C:302:DY:Pss5.tw1:valueRange  
First washout (T<sub>W1</sub>) (>= 0).  Typical value = 3,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tw2-valueRange

**Path:** `cim:Pss5.tw2`  
**Name:** C:302:DY:Pss5.tw2:valueRange  
Second washout (T<sub>W2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PssELIN2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssELIN2

**Nested Properties:**

### dy302c:PssELIN2.ppss-valueRange

**Path:** `cim:PssELIN2.ppss`  
**Name:** C:302:DY:PssELIN2.ppss:valueRange  
Coefficient (p_PSS) (>= 0 and <= 4).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is outside the range [0,4]."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `4.0` 

### dy302c:PssELIN2.ts1-valueRange

**Path:** `cim:PssELIN2.ts1`  
**Name:** C:302:DY:PssELIN2.ts1:valueRange  
Time constant (Ts1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts2-valueRange

**Path:** `cim:PssELIN2.ts2`  
**Name:** C:302:DY:PssELIN2.ts2:valueRange  
Time constant (Ts2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts3-valueRange

**Path:** `cim:PssELIN2.ts3`  
**Name:** C:302:DY:PssELIN2.ts3:valueRange  
Time constant (Ts3) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts4-valueRange

**Path:** `cim:PssELIN2.ts4`  
**Name:** C:302:DY:PssELIN2.ts4:valueRange  
Time constant (Ts4) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts5-valueRange

**Path:** `cim:PssELIN2.ts5`  
**Name:** C:302:DY:PssELIN2.ts5:valueRange  
Time constant (Ts5) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts6-valueRange

**Path:** `cim:PssELIN2.ts6`  
**Name:** C:302:DY:PssELIN2.ts6:valueRange  
Time constant (Ts6) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PssIEEE1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE1A

**Nested Properties:**

### dy302c:PssIEEE1A.inputSignalType-allowedValues

**Path:** `cim:PssIEEE1A.inputSignalType`  
**Name:** C:302:DY:PssIEEE1A.inputSignalType:allowedValues  
Type of input signal (rotorAngularFrequencyDeviation, generatorElectricalPower, or busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssIEEE1A.t1-valueRange

**Path:** `cim:PssIEEE1A.t1`  
**Name:** C:302:DY:PssIEEE1A.t1:valueRange  
Lead/lag time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t2-valueRange

**Path:** `cim:PssIEEE1A.t2`  
**Name:** C:302:DY:PssIEEE1A.t2:valueRange  
Lead/lag time constant (T2) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t3-valueRange

**Path:** `cim:PssIEEE1A.t3`  
**Name:** C:302:DY:PssIEEE1A.t3:valueRange  
Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t4-valueRange

**Path:** `cim:PssIEEE1A.t4`  
**Name:** C:302:DY:PssIEEE1A.t4:valueRange  
Lead/lag time constant (T4) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t5-valueRange

**Path:** `cim:PssIEEE1A.t5`  
**Name:** C:302:DY:PssIEEE1A.t5:valueRange  
Washout time constant (T5) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t6-valueRange

**Path:** `cim:PssIEEE1A.t6`  
**Name:** C:302:DY:PssIEEE1A.t6:valueRange  
Transducer time constant (T6) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.vrmin-valueRangePair

**Path:** `cim:PssIEEE1A.vrmin`  
**Name:** C:302:DY:PssIEEE1A.vrmin:valueRangePair  
Minimum stabilizer output (Vrmin) (< PssIEEE1A.vrmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE1A.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE1A.vrmax` 

## dy302c:PssIEEE2B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE2B

**Nested Properties:**

### dy302c:PssIEEE2B.inputSignal1Type-allowedValues

**Path:** `cim:PssIEEE2B.inputSignal1Type`  
**Name:** C:302:DY:PssIEEE2B.inputSignal1Type:allowedValues  
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssIEEE2B.inputSignal2Type-allowedValues

**Path:** `cim:PssIEEE2B.inputSignal2Type`  
**Name:** C:302:DY:PssIEEE2B.inputSignal2Type:allowedValues  
Type of input signal #2 (generatorElectricalPower).  Typical value = generatorElectricalPower.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.generatorElectricalPower]` 

### dy302c:PssIEEE2B.t1-valueRange

**Path:** `cim:PssIEEE2B.t1`  
**Name:** C:302:DY:PssIEEE2B.t1:valueRange  
Lead/lag time constant (T1) (>= 0).  Typical value = 0,12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t10-valueRange

**Path:** `cim:PssIEEE2B.t10`  
**Name:** C:302:DY:PssIEEE2B.t10:valueRange  
Lead/lag time constant (T10) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t11-valueRange

**Path:** `cim:PssIEEE2B.t11`  
**Name:** C:302:DY:PssIEEE2B.t11:valueRange  
Lead/lag time constant (T11) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t2-valueRange

**Path:** `cim:PssIEEE2B.t2`  
**Name:** C:302:DY:PssIEEE2B.t2:valueRange  
Lead/lag time constant (T2) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t3-valueRange

**Path:** `cim:PssIEEE2B.t3`  
**Name:** C:302:DY:PssIEEE2B.t3:valueRange  
Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t4-valueRange

**Path:** `cim:PssIEEE2B.t4`  
**Name:** C:302:DY:PssIEEE2B.t4:valueRange  
Lead/lag time constant (T4) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t6-valueRange

**Path:** `cim:PssIEEE2B.t6`  
**Name:** C:302:DY:PssIEEE2B.t6:valueRange  
Time constant on signal #1 (T6) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t7-valueRange

**Path:** `cim:PssIEEE2B.t7`  
**Name:** C:302:DY:PssIEEE2B.t7:valueRange  
Time constant on signal #2 (T7) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t8-valueRange

**Path:** `cim:PssIEEE2B.t8`  
**Name:** C:302:DY:PssIEEE2B.t8:valueRange  
Lead of ramp tracking filter (T8) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t9-valueRange

**Path:** `cim:PssIEEE2B.t9`  
**Name:** C:302:DY:PssIEEE2B.t9:valueRange  
Lag of ramp tracking filter (T9) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw1-valueRange

**Path:** `cim:PssIEEE2B.tw1`  
**Name:** C:302:DY:PssIEEE2B.tw1:valueRange  
First washout on signal #1 (Tw1) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw2-valueRange

**Path:** `cim:PssIEEE2B.tw2`  
**Name:** C:302:DY:PssIEEE2B.tw2:valueRange  
Second washout on signal #1 (Tw2) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw3-valueRange

**Path:** `cim:PssIEEE2B.tw3`  
**Name:** C:302:DY:PssIEEE2B.tw3:valueRange  
First washout on signal #2 (Tw3) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw4-valueRange

**Path:** `cim:PssIEEE2B.tw4`  
**Name:** C:302:DY:PssIEEE2B.tw4:valueRange  
Second washout on signal #2 (Tw4) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.vsi1min-valueRangePair

**Path:** `cim:PssIEEE2B.vsi1min`  
**Name:** C:302:DY:PssIEEE2B.vsi1min:valueRangePair  
Input signal #1 minimum limit (Vsi1min) (< PssIEEE2B.vsi1max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE2B.vsi1max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE2B.vsi1max` 

### dy302c:PssIEEE2B.vsi2min-valueRangePair

**Path:** `cim:PssIEEE2B.vsi2min`  
**Name:** C:302:DY:PssIEEE2B.vsi2min:valueRangePair  
Input signal #2 minimum limit (Vsi2min) (< PssIEEE2B.vsi2max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE2B.vsi2max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE2B.vsi2max` 

### dy302c:PssIEEE2B.vstmin-valueRangePair

**Path:** `cim:PssIEEE2B.vstmin`  
**Name:** C:302:DY:PssIEEE2B.vstmin:valueRangePair  
Stabilizer output minimum limit (Vstmin) (< PssIEEE2B.vstmax).  Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE2B.vstmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE2B.vstmax` 

## dy302c:PssIEEE3B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE3B

**Nested Properties:**

### dy302c:PssIEEE3B.t1-valueRange

**Path:** `cim:PssIEEE3B.t1`  
**Name:** C:302:DY:PssIEEE3B.t1:valueRange  
Transducer time constant (T1) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.t2-valueRange

**Path:** `cim:PssIEEE3B.t2`  
**Name:** C:302:DY:PssIEEE3B.t2:valueRange  
Transducer time constant (T2) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw1-valueRange

**Path:** `cim:PssIEEE3B.tw1`  
**Name:** C:302:DY:PssIEEE3B.tw1:valueRange  
Washout time constant (Tw1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw2-valueRange

**Path:** `cim:PssIEEE3B.tw2`  
**Name:** C:302:DY:PssIEEE3B.tw2:valueRange  
Washout time constant (Tw2) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw3-valueRange

**Path:** `cim:PssIEEE3B.tw3`  
**Name:** C:302:DY:PssIEEE3B.tw3:valueRange  
Washout time constant (Tw3) (>= 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.vstmin-valueRangePair

**Path:** `cim:PssIEEE3B.vstmin`  
**Name:** C:302:DY:PssIEEE3B.vstmin:valueRangePair  
Stabilizer output minimum limit (Vstmin) (< PssIEEE3B.vstmax).  Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE3B.vstmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE3B.vstmax` 

## dy302c:PssIEEE4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE4B

**Nested Properties:**

### dy302c:PssIEEE4B.th1-valueRange

**Path:** `cim:PssIEEE4B.th1`  
**Name:** C:302:DY:PssIEEE4B.th1:valueRange  
High band time constant (T<sub>H1</sub>) (>= 0).  Typical value = 0,01513.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th10-valueRange

**Path:** `cim:PssIEEE4B.th10`  
**Name:** C:302:DY:PssIEEE4B.th10:valueRange  
High band time constant (T<sub>H10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th11-valueRange

**Path:** `cim:PssIEEE4B.th11`  
**Name:** C:302:DY:PssIEEE4B.th11:valueRange  
High band time constant (T<sub>H11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th12-valueRange

**Path:** `cim:PssIEEE4B.th12`  
**Name:** C:302:DY:PssIEEE4B.th12:valueRange  
High band time constant (T<sub>H12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th2-valueRange

**Path:** `cim:PssIEEE4B.th2`  
**Name:** C:302:DY:PssIEEE4B.th2:valueRange  
High band time constant (T<sub>H2</sub>) (>= 0).  Typical value = 0,01816.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th3-valueRange

**Path:** `cim:PssIEEE4B.th3`  
**Name:** C:302:DY:PssIEEE4B.th3:valueRange  
High band time constant (T<sub>H3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th4-valueRange

**Path:** `cim:PssIEEE4B.th4`  
**Name:** C:302:DY:PssIEEE4B.th4:valueRange  
High band time constant (T<sub>H4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th5-valueRange

**Path:** `cim:PssIEEE4B.th5`  
**Name:** C:302:DY:PssIEEE4B.th5:valueRange  
High band time constant (T<sub>H5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th6-valueRange

**Path:** `cim:PssIEEE4B.th6`  
**Name:** C:302:DY:PssIEEE4B.th6:valueRange  
High band time constant (T<sub>H6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th7-valueRange

**Path:** `cim:PssIEEE4B.th7`  
**Name:** C:302:DY:PssIEEE4B.th7:valueRange  
High band time constant (T<sub>H7</sub>) (>= 0).  Typical value = 0,01816.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th8-valueRange

**Path:** `cim:PssIEEE4B.th8`  
**Name:** C:302:DY:PssIEEE4B.th8:valueRange  
High band time constant (T<sub>H8</sub>) (>= 0).  Typical value = 0,02179.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th9-valueRange

**Path:** `cim:PssIEEE4B.th9`  
**Name:** C:302:DY:PssIEEE4B.th9:valueRange  
High band time constant (T<sub>H9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti1-valueRange

**Path:** `cim:PssIEEE4B.ti1`  
**Name:** C:302:DY:PssIEEE4B.ti1:valueRange  
Intermediate band time constant (T<sub>I1</sub>) (>= 0).  Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti10-valueRange

**Path:** `cim:PssIEEE4B.ti10`  
**Name:** C:302:DY:PssIEEE4B.ti10:valueRange  
Intermediate band time constant (T<sub>I10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti11-valueRange

**Path:** `cim:PssIEEE4B.ti11`  
**Name:** C:302:DY:PssIEEE4B.ti11:valueRange  
Intermediate band time constant (T<sub>I11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti12-valueRange

**Path:** `cim:PssIEEE4B.ti12`  
**Name:** C:302:DY:PssIEEE4B.ti12:valueRange  
Intermediate band time constant (T<sub>I12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti2-valueRange

**Path:** `cim:PssIEEE4B.ti2`  
**Name:** C:302:DY:PssIEEE4B.ti2:valueRange  
Intermediate band time constant (T<sub>I2</sub>) (>= 0).  Typical value = 0,2075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti3-valueRange

**Path:** `cim:PssIEEE4B.ti3`  
**Name:** C:302:DY:PssIEEE4B.ti3:valueRange  
Intermediate band time constant (T<sub>I3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti4-valueRange

**Path:** `cim:PssIEEE4B.ti4`  
**Name:** C:302:DY:PssIEEE4B.ti4:valueRange  
Intermediate band time constant (T<sub>I4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti5-valueRange

**Path:** `cim:PssIEEE4B.ti5`  
**Name:** C:302:DY:PssIEEE4B.ti5:valueRange  
Intermediate band time constant (T<sub>I5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti6-valueRange

**Path:** `cim:PssIEEE4B.ti6`  
**Name:** C:302:DY:PssIEEE4B.ti6:valueRange  
Intermediate band time constant (T<sub>I6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti7-valueRange

**Path:** `cim:PssIEEE4B.ti7`  
**Name:** C:302:DY:PssIEEE4B.ti7:valueRange  
Intermediate band time constant (T<sub>I7</sub>) (>= 0).  Typical value = 0,2075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti8-valueRange

**Path:** `cim:PssIEEE4B.ti8`  
**Name:** C:302:DY:PssIEEE4B.ti8:valueRange  
Intermediate band time constant (T<sub>I8</sub>) (>= 0).  Typical value = 0,2491.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti9-valueRange

**Path:** `cim:PssIEEE4B.ti9`  
**Name:** C:302:DY:PssIEEE4B.ti9:valueRange  
Intermediate band time constant (T<sub>I9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl1-valueRange

**Path:** `cim:PssIEEE4B.tl1`  
**Name:** C:302:DY:PssIEEE4B.tl1:valueRange  
Low band time constant (T<sub>L1</sub>) (>= 0).  Typical value = 1,73.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl10-valueRange

**Path:** `cim:PssIEEE4B.tl10`  
**Name:** C:302:DY:PssIEEE4B.tl10:valueRange  
Low band time constant (T<sub>L10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl11-valueRange

**Path:** `cim:PssIEEE4B.tl11`  
**Name:** C:302:DY:PssIEEE4B.tl11:valueRange  
Low band time constant (T<sub>L11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl12-valueRange

**Path:** `cim:PssIEEE4B.tl12`  
**Name:** C:302:DY:PssIEEE4B.tl12:valueRange  
Low band time constant (T<sub>L12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl2-valueRange

**Path:** `cim:PssIEEE4B.tl2`  
**Name:** C:302:DY:PssIEEE4B.tl2:valueRange  
Low band time constant (T<sub>L2</sub>) (>= 0).  Typical value = 2,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl3-valueRange

**Path:** `cim:PssIEEE4B.tl3`  
**Name:** C:302:DY:PssIEEE4B.tl3:valueRange  
Low band time constant (T<sub>L3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl4-valueRange

**Path:** `cim:PssIEEE4B.tl4`  
**Name:** C:302:DY:PssIEEE4B.tl4:valueRange  
Low band time constant (T<sub>L4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl5-valueRange

**Path:** `cim:PssIEEE4B.tl5`  
**Name:** C:302:DY:PssIEEE4B.tl5:valueRange  
Low band time constant (T<sub>L5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl6-valueRange

**Path:** `cim:PssIEEE4B.tl6`  
**Name:** C:302:DY:PssIEEE4B.tl6:valueRange  
Low band time constant (T<sub>L6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl7-valueRange

**Path:** `cim:PssIEEE4B.tl7`  
**Name:** C:302:DY:PssIEEE4B.tl7:valueRange  
Low band time constant (T<sub>L7</sub>) (>= 0).  Typical value = 2,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl8-valueRange

**Path:** `cim:PssIEEE4B.tl8`  
**Name:** C:302:DY:PssIEEE4B.tl8:valueRange  
Low band time constant (T<sub>L8</sub>) (>= 0).  Typical value = 2,491.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl9-valueRange

**Path:** `cim:PssIEEE4B.tl9`  
**Name:** C:302:DY:PssIEEE4B.tl9:valueRange  
Low band time constant (T<sub>L9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.vhmin-valueRangePair

**Path:** `cim:PssIEEE4B.vhmin`  
**Name:** C:302:DY:PssIEEE4B.vhmin:valueRangePair  
High band output minimum limit (V<sub>Hmin</sub>) (< PssIEEE4V.vhmax).  Typical value = -0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4V.vhmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4V.vhmax` 

### dy302c:PssIEEE4B.vimin-valueRangePair

**Path:** `cim:PssIEEE4B.vimin`  
**Name:** C:302:DY:PssIEEE4B.vimin:valueRangePair  
Intermediate band output minimum limit (V<sub>Imin</sub>) (< PssIEEE4B.vimax).  Typical value = -0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4B.vimax` 

### dy302c:PssIEEE4B.vlmin-valueRangePair

**Path:** `cim:PssIEEE4B.vlmin`  
**Name:** C:302:DY:PssIEEE4B.vlmin:valueRangePair  
Low band output minimum limit (V<sub>Lmin</sub>) (< PssIEEE4B.vlmax).  Typical value = -0,075.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4B.vlmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4B.vlmax` 

### dy302c:PssIEEE4B.vstmin-valueRangePair

**Path:** `cim:PssIEEE4B.vstmin`  
**Name:** C:302:DY:PssIEEE4B.vstmin:valueRangePair  
PSS output minimum limit (V<sub>STmin</sub>) (< PssIEEE4B.vstmax).  Typical value = -0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4B.vstmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4B.vstmax` 

## dy302c:PssPTIST1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssPTIST1

**Nested Properties:**

### dy302c:PssPTIST1.dtc-valueRange

**Path:** `cim:PssPTIST1.dtc`  
**Name:** C:302:DY:PssPTIST1.dtc:valueRange  
Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.dtf-valueRange

**Path:** `cim:PssPTIST1.dtf`  
**Name:** C:302:DY:PssPTIST1.dtf:valueRange  
Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.dtp-valueRange

**Path:** `cim:PssPTIST1.dtp`  
**Name:** C:302:DY:PssPTIST1.dtp:valueRange  
Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t1-valueRange

**Path:** `cim:PssPTIST1.t1`  
**Name:** C:302:DY:PssPTIST1.t1:valueRange  
Time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t2-valueRange

**Path:** `cim:PssPTIST1.t2`  
**Name:** C:302:DY:PssPTIST1.t2:valueRange  
Time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t3-valueRange

**Path:** `cim:PssPTIST1.t3`  
**Name:** C:302:DY:PssPTIST1.t3:valueRange  
Time constant (T3) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t4-valueRange

**Path:** `cim:PssPTIST1.t4`  
**Name:** C:302:DY:PssPTIST1.t4:valueRange  
Time constant (T4) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.tf-valueRange

**Path:** `cim:PssPTIST1.tf`  
**Name:** C:302:DY:PssPTIST1.tf:valueRange  
Time constant (Tf) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.tp-valueRange

**Path:** `cim:PssPTIST1.tp`  
**Name:** C:302:DY:PssPTIST1.tp:valueRange  
Time constant (Tp) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PssPTIST3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssPTIST3

**Nested Properties:**

### dy302c:PssPTIST3.dtc-valueRange

**Path:** `cim:PssPTIST3.dtc`  
**Name:** C:302:DY:PssPTIST3.dtc:valueRange  
Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.dtf-valueRange

**Path:** `cim:PssPTIST3.dtf`  
**Name:** C:302:DY:PssPTIST3.dtf:valueRange  
Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.dtp-valueRange

**Path:** `cim:PssPTIST3.dtp`  
**Name:** C:302:DY:PssPTIST3.dtp:valueRange  
Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125  (0,015 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.nav-valueRange

**Path:** `cim:PssPTIST3.nav`  
**Name:** C:302:DY:PssPTIST3.nav:valueRange  
Number of control outputs to average (NAV) (1 <=  NAV <= 16).  Typical value = 4.

**Severity:** sh:Violation

**Messages:**
- "The value is outside the range [1,16]."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `1.0` 
- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `16.0` 

### dy302c:PssPTIST3.ncl-valueRange

**Path:** `cim:PssPTIST3.ncl`  
**Name:** C:302:DY:PssPTIST3.ncl:valueRange  
Number of counts at limit to active limit function (NCL) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t1-valueRange

**Path:** `cim:PssPTIST3.t1`  
**Name:** C:302:DY:PssPTIST3.t1:valueRange  
Time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t2-valueRange

**Path:** `cim:PssPTIST3.t2`  
**Name:** C:302:DY:PssPTIST3.t2:valueRange  
Time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t3-valueRange

**Path:** `cim:PssPTIST3.t3`  
**Name:** C:302:DY:PssPTIST3.t3:valueRange  
Time constant (T3) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t4-valueRange

**Path:** `cim:PssPTIST3.t4`  
**Name:** C:302:DY:PssPTIST3.t4:valueRange  
Time constant (T4) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t5-valueRange

**Path:** `cim:PssPTIST3.t5`  
**Name:** C:302:DY:PssPTIST3.t5:valueRange  
Time constant (T5) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t6-valueRange

**Path:** `cim:PssPTIST3.t6`  
**Name:** C:302:DY:PssPTIST3.t6:valueRange  
Time constant (T6) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.tf-valueRange

**Path:** `cim:PssPTIST3.tf`  
**Name:** C:302:DY:PssPTIST3.tf:valueRange  
Time constant (Tf) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.tp-valueRange

**Path:** `cim:PssPTIST3.tp`  
**Name:** C:302:DY:PssPTIST3.tp:valueRange  
Time constant (Tp) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PssRQB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssRQB

**Nested Properties:**

### dy302c:PssRQB.t4f-valueRange

**Path:** `cim:PssRQB.t4f`  
**Name:** C:302:DY:PssRQB.t4f:valueRange  
Lead lag time constant (T4F) (>= 0). Typical value = 0,045.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.t4m-valueRange

**Path:** `cim:PssRQB.t4m`  
**Name:** C:302:DY:PssRQB.t4m:valueRange  
Input time constant (T4M) (>= 0). Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.t4mom-valueRange

**Path:** `cim:PssRQB.t4mom`  
**Name:** C:302:DY:PssRQB.t4mom:valueRange  
Speed time constant (T4MOM) (>= 0). Typical value = 1,27.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.tomd-valueRange

**Path:** `cim:PssRQB.tomd`  
**Name:** C:302:DY:PssRQB.tomd:valueRange  
Speed delay (TOMD) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.tomsl-valueRange

**Path:** `cim:PssRQB.tomsl`  
**Name:** C:302:DY:PssRQB.tomsl:valueRange  
Speed time constant (TOMSL) (>= 0). Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:PssSB4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSB4

**Nested Properties:**

### dy302c:PssSB4.ta-valueRange

**Path:** `cim:PssSB4.ta`  
**Name:** C:302:DY:PssSB4.ta:valueRange  
Time constant (Ta) (>= 0).  Typical value = 0,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tb-valueRange

**Path:** `cim:PssSB4.tb`  
**Name:** C:302:DY:PssSB4.tb:valueRange  
Time constant (Tb) (>= 0).  Typical value = 0,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tc-valueRange

**Path:** `cim:PssSB4.tc`  
**Name:** C:302:DY:PssSB4.tc:valueRange  
Time constant (Tc) (>= 0).  Typical value = 0,035.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.td-valueRange

**Path:** `cim:PssSB4.td`  
**Name:** C:302:DY:PssSB4.td:valueRange  
Time constant (Td) (>= 0).  Typical value = 0,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.te-valueRange

**Path:** `cim:PssSB4.te`  
**Name:** C:302:DY:PssSB4.te:valueRange  
Time constant (Te) (>= 0).  Typical value = 0,0169.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tt-valueRange

**Path:** `cim:PssSB4.tt`  
**Name:** C:302:DY:PssSB4.tt:valueRange  
Time constant (Tt) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tx1-valueRange

**Path:** `cim:PssSB4.tx1`  
**Name:** C:302:DY:PssSB4.tx1:valueRange  
Reset time constant (Tx1) (>= 0).  Typical value = 0,035.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tx2-valueRange

**Path:** `cim:PssSB4.tx2`  
**Name:** C:302:DY:PssSB4.tx2:valueRange  
Time constant (Tx2) (>= 0).  Typical value = 5,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.vsmin-valueRangePair

**Path:** `cim:PssSB4.vsmin`  
**Name:** C:302:DY:PssSB4.vsmin:valueRangePair  
Limiter (Vsmin) (< PssSB4.vsmax).  Typical value = -0,062.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssSB4.vsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssSB4.vsmax` 

## dy302c:PssSH

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSH

**Nested Properties:**

### dy302c:PssSH.t1-valueRange

**Path:** `cim:PssSH.t1`  
**Name:** C:302:DY:PssSH.t1:valueRange  
Time constant 1 (T1) (> 0).  Typical value = 0,076.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t2-valueRange

**Path:** `cim:PssSH.t2`  
**Name:** C:302:DY:PssSH.t2:valueRange  
Time constant 2 (T2) (> 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t3-valueRange

**Path:** `cim:PssSH.t3`  
**Name:** C:302:DY:PssSH.t3:valueRange  
Time constant 3 (T3) (> 0).   Typical value = 1,068.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t4-valueRange

**Path:** `cim:PssSH.t4`  
**Name:** C:302:DY:PssSH.t4:valueRange  
Time constant 4 (T4) (> 0).  Typical value = 1,913.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.td-valueRange

**Path:** `cim:PssSH.td`  
**Name:** C:302:DY:PssSH.td:valueRange  
Input time constant (T<sub>d</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.vsmin-valueRangePair

**Path:** `cim:PssSH.vsmin`  
**Name:** C:302:DY:PssSH.vsmin:valueRangePair  
Output minimum limit (Vsmin) (< PssSH.vsmax).  Typical value = -0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssSH.vsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssSH.vsmax` 

## dy302c:PssSK

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSK

**Nested Properties:**

### dy302c:PssSK.t1-valueRange

**Path:** `cim:PssSK.t1`  
**Name:** C:302:DY:PssSK.t1:valueRange  
Denominator time constant (T<sub>1</sub>) (> 0,005).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t2-valueRange

**Path:** `cim:PssSK.t2`  
**Name:** C:302:DY:PssSK.t2:valueRange  
Filter time constant (T<sub>2</sub>) (> 0,005).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t3-valueRange

**Path:** `cim:PssSK.t3`  
**Name:** C:302:DY:PssSK.t3:valueRange  
Denominator time constant (T<sub>3</sub>) (> 0,005).  Typical value = 0,22.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t4-valueRange

**Path:** `cim:PssSK.t4`  
**Name:** C:302:DY:PssSK.t4:valueRange  
Filter time constant (T<sub>4</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t5-valueRange

**Path:** `cim:PssSK.t5`  
**Name:** C:302:DY:PssSK.t5:valueRange  
Denominator time constant (T<sub>5</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t6-valueRange

**Path:** `cim:PssSK.t6`  
**Name:** C:302:DY:PssSK.t6:valueRange  
Filter time constant (T<sub>6</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.vsmin-valueRangePair

**Path:** `cim:PssSK.vsmin`  
**Name:** C:302:DY:PssSK.vsmin:valueRangePair  
Stabilizer output minimum limit (V<sub>SMIN</sub>) (< PssSK.vsmax).  Typical value = -0.4.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssSK.vsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssSK.vsmax` 

## dy302c:PssWECC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssWECC

**Nested Properties:**

### dy302c:PssWECC.inputSignal1Type-allowedValues

**Path:** `cim:PssWECC.inputSignal1Type`  
**Name:** C:302:DY:PssWECC.inputSignal1Type:allowedValues  
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssWECC.inputSignal2Type-allowedValues

**Path:** `cim:PssWECC.inputSignal2Type`  
**Name:** C:302:DY:PssWECC.inputSignal2Type:allowedValues  
Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, busVoltageDerivative - shall be different than PssWECC.inputSignal1Type).  Typical value = busVoltageDerivative.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssWECC.t1-valueRange

**Path:** `cim:PssWECC.t1`  
**Name:** C:302:DY:PssWECC.t1:valueRange  
Input signal 1 transducer time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t10-valueRange

**Path:** `cim:PssWECC.t10`  
**Name:** C:302:DY:PssWECC.t10:valueRange  
Lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t2-valueRange

**Path:** `cim:PssWECC.t2`  
**Name:** C:302:DY:PssWECC.t2:valueRange  
Input signal 2 transducer time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t3-valueRange

**Path:** `cim:PssWECC.t3`  
**Name:** C:302:DY:PssWECC.t3:valueRange  
Stabilizer washout time constant (T<sub>3</sub>) (>= 0).  Typical value = 9,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t4-valueRange

**Path:** `cim:PssWECC.t4`  
**Name:** C:302:DY:PssWECC.t4:valueRange  
Stabilizer washout time lag constant (T<sub>4</sub>) (>= 0).  Typical value = 9,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t5-valueRange

**Path:** `cim:PssWECC.t5`  
**Name:** C:302:DY:PssWECC.t5:valueRange  
Lead time constant (T<sub>5</sub>) (>= 0).  Typical value = 1,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t6-valueRange

**Path:** `cim:PssWECC.t6`  
**Name:** C:302:DY:PssWECC.t6:valueRange  
Lag time constant (T<sub>6</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t7-valueRange

**Path:** `cim:PssWECC.t7`  
**Name:** C:302:DY:PssWECC.t7:valueRange  
Lead time constant (T<sub>7</sub>) (>= 0).  Typical value = 1,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t8-valueRange

**Path:** `cim:PssWECC.t8`  
**Name:** C:302:DY:PssWECC.t8:valueRange  
Lag time constant (T<sub>8</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t9-valueRange

**Path:** `cim:PssWECC.t9`  
**Name:** C:302:DY:PssWECC.t9:valueRange  
Lead time constant (T<sub>9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.vsmin-valueRangePair

**Path:** `cim:PssWECC.vsmin`  
**Name:** C:302:DY:PssWECC.vsmin:valueRangePair  
Minimum output signal (Vsmin) (< PssWECC.vsmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssWECC.vsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssWECC.vsmax` 

## dy302c:RotatingMachineDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineTimeConstantReactance
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineTimeConstantReactance
- targetClass: cim:AsynchronousMachineEquivalentCircuit

## dy302c:SynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineEquivalentCircuit

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.efdBaseRatio-valueRange

**Path:** `cim:SynchronousMachineDetailed.efdBaseRatio`  
**Name:** C:302:DY:SynchronousMachineDetailed.efdBaseRatio:valueRange  
Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.saturationFactorQAxis-valueRange

**Path:** `cim:SynchronousMachineDetailed.saturationFactorQAxis`  
**Name:** C:302:DY:SynchronousMachineDetailed.saturationFactorQAxis:valueRange  
Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:SynchronousMachineSimplified

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineSimplified

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:SynchronousMachineTimeConstantReactance

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.efdBaseRatio-valueRange

**Path:** `cim:SynchronousMachineDetailed.efdBaseRatio`  
**Name:** C:302:DY:SynchronousMachineDetailed.efdBaseRatio:valueRange  
Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.saturationFactorQAxis-valueRange

**Path:** `cim:SynchronousMachineDetailed.saturationFactorQAxis`  
**Name:** C:302:DY:SynchronousMachineDetailed.saturationFactorQAxis:valueRange  
Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.ks-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.ks`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.ks:valueRange  
Saturation loading correction factor (Ks) (>= 0).  Used only by type J model.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tc-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tc`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.tc:valueRange  
Damping time constant for “Canay” reactance (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tpdo-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppdo`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.tpdo:valueRangePair  
Direct-axis transient rotor time constant (T'do) (> SynchronousMachineTimeConstantReactance.tppdo).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.tpdo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.tpdo` 

### dy302c:SynchronousMachineTimeConstantReactance.tppdo-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppdo`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.tppdo:valueRange  
Direct-axis subtransient rotor time constant (T''do) (> 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tppqo-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppqo`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.tppqo:valueRange  
Quadrature-axis subtransient rotor time constant (T''qo) (> 0). Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tpqo-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppqo`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.tpqo:valueRangePair  
Quadrature-axis transient rotor time constant (T'qo) (> SynchronousMachineTimeConstantReactance.tppqo). Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.tpqo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.tpqo` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectTrans-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectTrans:valueRangePair  
Direct-axis transient reactance (unsaturated) (X'd) (>= SynchronousMachineTimeConstantReactance.xDirectSubtrans).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xDirectTrans."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectTrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSync-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xDirectTrans`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSync:valueRangePair  
Direct-axis synchronous reactance (Xd) (>= SynchronousMachineTimeConstantReactance.xDirectTrans). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed.  Typical value = 1,8.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xDirectSync."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSync` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadTrans-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadTrans:valueRangePair  
Quadrature-axis transient reactance (X'q) (>= SynchronousMachineTimeConstantReactance.xQuadSubtrans).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xQuadTrans."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadTrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSync-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xQuadTrans`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSync:valueRangePair  
Quadrature-axis synchronous reactance (Xq) (>= SynchronousMachineTimeConstantReactance.xQuadTrans).
The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical value = 1,6.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xQuadSync."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSync` 

## dy302c:SynchronousMachineUserDefined

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineUserDefined

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
**Name:** C:302:DY:RotatingMachineDynamics.damping:valueRange  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
**Name:** C:302:DY:RotatingMachineDynamics.inertia:valueRange  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor:valueRange  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:AsynchronousMachineTimeConstantReactance.xpp:valueRangePair  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xQuadSubtrans:valueRangePair  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:SynchronousMachineTimeConstantReactance.xDirectSubtrans:valueRangePair  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorLeakageReactance:valueRange  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
**Name:** C:302:DY:RotatingMachineDynamics.statorResistance:valueRange  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:TurbLCFB1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TurbLCFB1

**Nested Properties:**

### dy302c:TurbLCFB1.mwbase-valueRange

**Path:** `cim:TurbLCFB1.mwbase`  
**Name:** C:302:DY:TurbLCFB1.mwbase:valueRange  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:TurbLCFB1.tpelec-valueRange

**Path:** `cim:TurbLCFB1.tpelec`  
**Name:** C:302:DY:TurbLCFB1.tpelec:valueRange  
Power transducer time constant (Tpelec) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:TurbineGovernorDynamics

**Name:** C:302:DY:TurbineGovernorDynamics:associationsCondition  
TurbineGovernorDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:GovGAST4
- targetClass: cim:GovGAST3
- targetClass: cim:GovGAST
- targetClass: cim:GovSteam1
- targetClass: cim:GovGASTWD
- targetClass: cim:GovHydro1
- targetClass: cim:TurbineGovernorUserDefined
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovHydroFrancis
- targetClass: cim:GovSteam0
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovHydroPelton
- targetClass: cim:GovSteamEU
- targetClass: cim:GovHydro3
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovSteamBB
- targetClass: cim:GovGAST2
- targetClass: cim:GovHydroIEEE2
- targetClass: cim:GovHydro2
- targetClass: cim:GovHydroPID
- targetClass: cim:GovHydro4
- targetClass: cim:GovSteam2
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovCT1
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydroDD
- targetClass: cim:GovSteamFV4
- targetClass: cim:GovGAST1
- targetClass: cim:GovCT2
- targetClass: cim:GovHydroR

**Constraints:**

- **sh:XoneConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1`

## dy302c:UnderexcLim2Simplified

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLim2Simplified

**Nested Properties:**

### dy302c:UnderexcLim2Simplified.vuimin-valueRangePair

**Path:** `cim:UnderexcLim2Simplified.vuimin`  
**Name:** C:302:DY:UnderexcLim2Simplified.vuimin:valueRangePair  
Minimum error signal (V<sub>UIMIN</sub>) (< UnderexcLim2Simplified.vuimax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLim2Simplified.vuimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLim2Simplified.vuimax` 

## dy302c:UnderexcLimIEEE1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimIEEE1

**Nested Properties:**

### dy302c:UnderexcLimIEEE1.tu1-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu1`  
**Name:** C:302:DY:UnderexcLimIEEE1.tu1:valueRange  
UEL lead time constant (T<sub>U1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu2-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu2`  
**Name:** C:302:DY:UnderexcLimIEEE1.tu2:valueRange  
UEL lag time constant (T<sub>U2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu3-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu3`  
**Name:** C:302:DY:UnderexcLimIEEE1.tu3:valueRange  
UEL lead time constant (T<sub>U3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu4-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu4`  
**Name:** C:302:DY:UnderexcLimIEEE1.tu4:valueRange  
UEL lag time constant (T<sub>U4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.vuimin-valueRangePair

**Path:** `cim:UnderexcLimIEEE1.vuimin`  
**Name:** C:302:DY:UnderexcLimIEEE1.vuimin:valueRangePair  
UEL integrator output minimum limit (V<sub>UIMIN</sub>) (< UnderexcLimIEEE1.vuimax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE1.vuimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE1.vuimax` 

### dy302c:UnderexcLimIEEE1.vulmin-valueRangePair

**Path:** `cim:UnderexcLimIEEE1.vulmin`  
**Name:** C:302:DY:UnderexcLimIEEE1.vulmin:valueRangePair  
UEL output minimum limit (V<sub>ULMIN</sub>) (< UnderexcLimIEEE1.vulmax).  Typical value = -18.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE1.vulmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE1.vulmax` 

## dy302c:UnderexcLimIEEE2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimIEEE2

**Nested Properties:**

### dy302c:UnderexcLimIEEE2.tu1-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu1`  
**Name:** C:302:DY:UnderexcLimIEEE2.tu1:valueRange  
UEL lead time constant (T<sub>U1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu2-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu2`  
**Name:** C:302:DY:UnderexcLimIEEE2.tu2:valueRange  
UEL lag time constant (T<sub>U2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu3-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu3`  
**Name:** C:302:DY:UnderexcLimIEEE2.tu3:valueRange  
UEL lead time constant (T<sub>U3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu4-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu4`  
**Name:** C:302:DY:UnderexcLimIEEE2.tu4:valueRange  
UEL lag time constant (T<sub>U4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tul-valueRange

**Path:** `cim:UnderexcLimIEEE2.tul`  
**Name:** C:302:DY:UnderexcLimIEEE2.tul:valueRange  
Time constant associated with optional integrator feedback input signal to UEL (T<sub>UL</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tup-valueRange

**Path:** `cim:UnderexcLimIEEE2.tup`  
**Name:** C:302:DY:UnderexcLimIEEE2.tup:valueRange  
Real power filter time constant (T<sub>UP</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tuq-valueRange

**Path:** `cim:UnderexcLimIEEE2.tuq`  
**Name:** C:302:DY:UnderexcLimIEEE2.tuq:valueRange  
Reactive power filter time constant (T<sub>UQ</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tuv-valueRange

**Path:** `cim:UnderexcLimIEEE2.tuv`  
**Name:** C:302:DY:UnderexcLimIEEE2.tuv:valueRange  
Voltage filter time constant (T<sub>UV</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.vuimin-valueRangePair

**Path:** `cim:UnderexcLimIEEE2.vuimin`  
**Name:** C:302:DY:UnderexcLimIEEE2.vuimin:valueRangePair  
UEL integrator output minimum limit (V<sub>UIMIN</sub>) (< UnderexcLimIEEE2.vuimax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE2.vuimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE2.vuimax` 

### dy302c:UnderexcLimIEEE2.vulmin-valueRangePair

**Path:** `cim:UnderexcLimIEEE2.vulmin`  
**Name:** C:302:DY:UnderexcLimIEEE2.vulmin:valueRangePair  
UEL output minimum limit (V<sub>ULMIN</sub>) (< UnderexcLimIEEE2.vulmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE2.vulmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE2.vulmax` 

## dy302c:UnderexcLimX1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimX1

**Nested Properties:**

### dy302c:UnderexcLimX1.k-valueRange

**Path:** `cim:UnderexcLimX1.k`  
**Name:** C:302:DY:UnderexcLimX1.k:valueRange  
Minimum excitation limit slope (K) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX1.tf2-valueRange

**Path:** `cim:UnderexcLimX1.tf2`  
**Name:** C:302:DY:UnderexcLimX1.tf2:valueRange  
Differential time constant (T<sub>F2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX1.tm-valueRange

**Path:** `cim:UnderexcLimX1.tm`  
**Name:** C:302:DY:UnderexcLimX1.tm:valueRange  
Minimum excitation limit time constant (T<sub>M</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:UnderexcLimX2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimX2

**Nested Properties:**

### dy302c:UnderexcLimX2.tf2-valueRange

**Path:** `cim:UnderexcLimX2.tf2`  
**Name:** C:302:DY:UnderexcLimX2.tf2:valueRange  
Differential time constant (T<sub>F2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX2.tm-valueRange

**Path:** `cim:UnderexcLimX2.tm`  
**Name:** C:302:DY:UnderexcLimX2.tm:valueRange  
Minimum excitation limit time constant (T<sub>M</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:VAdjIEEE

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VAdjIEEE

**Nested Properties:**

### dy302c:VAdjIEEE.taoff-valueRange

**Path:** `cim:VAdjIEEE.taoff`  
**Name:** C:302:DY:VAdjIEEE.taoff:valueRange  
Time that adjuster pulses are off (T<sub>AOFF</sub>) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VAdjIEEE.taon-valueRange

**Path:** `cim:VAdjIEEE.taon`  
**Name:** C:302:DY:VAdjIEEE.taon:valueRange  
Time that adjuster pulses are on (T<sub>AON</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VAdjIEEE.vadjmin-valueRangePair

**Path:** `cim:VAdjIEEE.vadjmin`  
**Name:** C:302:DY:VAdjIEEE.vadjmin:valueRangePair  
Minimum output of the adjuster (V<sub>ADJMIN</sub>) (< VAdjIEEE.vadjmax).  Typical value = 0,9.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than VAdjIEEE.vadjmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:VAdjIEEE.vadjmax` 

## dy302c:VCompIEEEType1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VCompIEEEType1

**Nested Properties:**

### dy302c:VCompIEEEType1.rc-valueRange

**Path:** `cim:VCompIEEEType1.rc`  
**Name:** C:302:DY:VCompIEEEType1.rc:valueRange  
<font color=\"#0f0f0f\">Resistive component of compensation of a generator (Rc) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VCompIEEEType1.tr-valueRange

**Path:** `cim:VCompIEEEType1.tr`  
**Name:** C:302:DY:VCompIEEEType1.tr:valueRange  
<font color=\"#0f0f0f\">Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VCompIEEEType1.xc-valueRange

**Path:** `cim:VCompIEEEType1.xc`  
**Name:** C:302:DY:VCompIEEEType1.xc:valueRange  
<font color=\"#0f0f0f\">Reactive component of compensation of a generator (Xc) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:VCompIEEEType2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VCompIEEEType2

**Nested Properties:**

### dy302c:VCompIEEEType2.tr-valueRange

**Path:** `cim:VCompIEEEType2.tr`  
**Name:** C:302:DY:VCompIEEEType2.tr:valueRange  
<font color=\"#0f0f0f\">Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContPType3IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType3IEC

**Nested Properties:**

### dy302c:WindContPType3IEC.tdvs-valueRange

**Path:** `cim:WindContPType3IEC.tdvs`  
**Name:** C:302:DY:WindContPType3IEC.tdvs:valueRange  
Time<sub> </sub>delay after deep voltage sags (T<sub>DVS</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tomegafiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tomegafiltp3`  
**Name:** C:302:DY:WindContPType3IEC.tomegafiltp3:valueRange  
Filter time constant for generator speed measurement (T<sub>omegafiltp3</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tomegaref-valueRange

**Path:** `cim:WindContPType3IEC.tomegaref`  
**Name:** C:302:DY:WindContPType3IEC.tomegaref:valueRange  
Time constant in speed reference filter (T<sub>omega,ref</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tpfiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tpfiltp3`  
**Name:** C:302:DY:WindContPType3IEC.tpfiltp3:valueRange  
Filter time constant for power measurement (T<sub>pfiltp3</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tufiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tufiltp3`  
**Name:** C:302:DY:WindContPType3IEC.tufiltp3:valueRange  
Filter time constant for voltage measurement (T<sub>ufiltp3</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContPType4aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4aIEC

**Nested Properties:**

### dy302c:WindContPType4aIEC.tpordp4a-valueRange

**Path:** `cim:WindContPType4aIEC.tpordp4a`  
**Name:** C:302:DY:WindContPType4aIEC.tpordp4a:valueRange  
Time constant in power order lag (T<sub>pordp4A</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4aIEC.tufiltp4a-valueRange

**Path:** `cim:WindContPType4aIEC.tufiltp4a`  
**Name:** C:302:DY:WindContPType4aIEC.tufiltp4a:valueRange  
Voltage measurement filter time constant (T<sub>ufiltp4A</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContPType4bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4bIEC

**Nested Properties:**

### dy302c:WindContPType4bIEC.tpaero-valueRange

**Path:** `cim:WindContPType4bIEC.tpaero`  
**Name:** C:302:DY:WindContPType4bIEC.tpaero:valueRange  
Time constant in aerodynamic power response (T<sub>paero</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4bIEC.tpordp4b-valueRange

**Path:** `cim:WindContPType4bIEC.tpordp4b`  
**Name:** C:302:DY:WindContPType4bIEC.tpordp4b:valueRange  
Time constant in power order lag (T<sub>pordp4B</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4bIEC.tufiltp4b-valueRange

**Path:** `cim:WindContPType4bIEC.tufiltp4b`  
**Name:** C:302:DY:WindContPType4bIEC.tufiltp4b:valueRange  
Voltage measurement filter time constant (T<sub>ufiltp4B</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContPitchAngleIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPitchAngleIEC

**Nested Properties:**

### dy302c:WindContPitchAngleIEC.dthetamin-valueRangePair

**Path:** `cim:WindContPitchAngleIEC.dthetamin`  
**Name:** C:302:DY:WindContPitchAngleIEC.dthetamin:valueRangePair  
Maximum pitch negative ramp rate (dtheta<sub>min</sub>) (< WindContPitchAngleIEC.dthetamax). It is a type-dependent parameter. Unit = degrees / s. 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContPitchAngleIEC.dthetamax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContPitchAngleIEC.dthetamax` 

### dy302c:WindContPitchAngleIEC.thetamin-valueRangePair

**Path:** `cim:WindContPitchAngleIEC.thetamin`  
**Name:** C:302:DY:WindContPitchAngleIEC.thetamin:valueRangePair  
Minimum pitch angle (theta<sub>min</sub>) (< WindContPitchAngleIEC.thetamax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContPitchAngleIEC.thetamax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContPitchAngleIEC.thetamax` 

### dy302c:WindContPitchAngleIEC.ttheta-valueRange

**Path:** `cim:WindContPitchAngleIEC.ttheta`  
**Name:** C:302:DY:WindContPitchAngleIEC.ttheta:valueRange  
Pitch time constant (ttheta) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContQIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQIEC

**Nested Properties:**

### dy302c:WindContQIEC.iqmin-valueRangePair

**Path:** `cim:WindContQIEC.iqmin`  
**Name:** C:302:DY:WindContQIEC.iqmin:valueRangePair  
Minimum reactive current injection (i<sub>qmin</sub>) (< WindContQIEC.iqmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContQIEC.iqmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContQIEC.iqmax` 

### dy302c:WindContQIEC.rdroop-valueRange

**Path:** `cim:WindContQIEC.rdroop`  
**Name:** C:302:DY:WindContQIEC.rdroop:valueRange  
Resistive component of voltage drop impedance (r<sub>droop</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tpfiltq-valueRange

**Path:** `cim:WindContQIEC.tpfiltq`  
**Name:** C:302:DY:WindContQIEC.tpfiltq:valueRange  
Power measurement filter time constant (T<sub>pfiltq</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tpost-valueRange

**Path:** `cim:WindContQIEC.tpost`  
**Name:** C:302:DY:WindContQIEC.tpost:valueRange  
Length of time period where post fault reactive power is injected (T<sub>post</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tqord-valueRange

**Path:** `cim:WindContQIEC.tqord`  
**Name:** C:302:DY:WindContQIEC.tqord:valueRange  
Time constant in reactive power order lag (T<sub>qord</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tufiltq-valueRange

**Path:** `cim:WindContQIEC.tufiltq`  
**Name:** C:302:DY:WindContQIEC.tufiltq:valueRange  
Voltage measurement filter time constant (T<sub>ufiltq</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.umin-valueRangePair

**Path:** `cim:WindContQIEC.umin`  
**Name:** C:302:DY:WindContQIEC.umin:valueRangePair  
Minimum voltage in voltage PI controller integral term (u<sub>min</sub>) (< WindContQIEC.umax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContQIEC.umax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContQIEC.umax` 

### dy302c:WindContQIEC.xdroop-valueRange

**Path:** `cim:WindContQIEC.xdroop`  
**Name:** C:302:DY:WindContQIEC.xdroop:valueRange  
Inductive component of voltage drop impedance (x<sub>droop</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContQLimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQLimIEC

**Nested Properties:**

### dy302c:WindContQLimIEC.qmin-valueRangePair

**Path:** `cim:WindContQLimIEC.qmin`  
**Name:** C:302:DY:WindContQLimIEC.qmin:valueRangePair  
Minimum reactive power (q<sub>min</sub>) (< WindContQLimIEC.qmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContQLimIEC.qmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContQLimIEC.qmax` 

## dy302c:WindContQPQULimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQPQULimIEC

**Nested Properties:**

### dy302c:WindContQPQULimIEC.tpfiltql-valueRange

**Path:** `cim:WindContQPQULimIEC.tpfiltql`  
**Name:** C:302:DY:WindContQPQULimIEC.tpfiltql:valueRange  
Power measurement filter time constant for Q capacity (T<sub>pfiltql</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQPQULimIEC.tufiltql-valueRange

**Path:** `cim:WindContQPQULimIEC.tufiltql`  
**Name:** C:302:DY:WindContQPQULimIEC.tufiltql:valueRange  
Voltage measurement filter time constant for Q capacity (T<sub>ufiltql</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindContRotorRIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContRotorRIEC

**Nested Properties:**

### dy302c:WindContRotorRIEC.rmin-valueRangePair

**Path:** `cim:WindContRotorRIEC.rmin`  
**Name:** C:302:DY:WindContRotorRIEC.rmin:valueRangePair  
Minimum rotor resistance (r<sub>min</sub>) (< WindContRotorRIEC.rmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContRotorRIEC.rmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContRotorRIEC.rmax` 

### dy302c:WindContRotorRIEC.tomegafiltrr-valueRange

**Path:** `cim:WindContRotorRIEC.tomegafiltrr`  
**Name:** C:302:DY:WindContRotorRIEC.tomegafiltrr:valueRange  
Filter time constant for generator speed measurement (T<sub>omegafiltrr</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContRotorRIEC.tpfiltrr-valueRange

**Path:** `cim:WindContRotorRIEC.tpfiltrr`  
**Name:** C:302:DY:WindContRotorRIEC.tpfiltrr:valueRange  
Filter time constant for power measurement (T<sub>pfiltrr</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindGenType3aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3aIEC

**Nested Properties:**

### dy302c:WindGenType3aIEC.tic-valueRange

**Path:** `cim:WindGenType3aIEC.tic`  
**Name:** C:302:DY:WindGenType3aIEC.tic:valueRange  
Current PI controller integration time constant (T<sub>Ic</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindGenType3bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3bIEC

**Nested Properties:**

### dy302c:WindGenType3bIEC.tg-valueRange

**Path:** `cim:WindGenType3bIEC.tg`  
**Name:** C:302:DY:WindGenType3bIEC.tg:valueRange  
Current generation time constant (T<sub>g</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindGenType3bIEC.two-valueRange

**Path:** `cim:WindGenType3bIEC.two`  
**Name:** C:302:DY:WindGenType3bIEC.two:valueRange  
Time constant for crowbar washout filter (T<sub>wo</sub>) (>= 0). It is a case-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindGenType4IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType4IEC

**Nested Properties:**

### dy302c:WindGenType4IEC.tg-valueRange

**Path:** `cim:WindGenType4IEC.tg`  
**Name:** C:302:DY:WindGenType4IEC.tg:valueRange  
Time constant (T<sub>g</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindMechIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindMechIEC

**Nested Properties:**

### dy302c:WindMechIEC.hgen-valueRange

**Path:** `cim:WindMechIEC.hgen`  
**Name:** C:302:DY:WindMechIEC.hgen:valueRange  
Inertia constant of generator (H<sub>gen</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindMechIEC.hwtr-valueRange

**Path:** `cim:WindMechIEC.hwtr`  
**Name:** C:302:DY:WindMechIEC.hwtr:valueRange  
Inertia constant of wind turbine rotor (H<sub>WTR</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindPitchContPowerIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPitchContPowerIEC

**Nested Properties:**

### dy302c:WindPitchContPowerIEC.dpmin-valueRangePair

**Path:** `cim:WindPitchContPowerIEC.dpmin`  
**Name:** C:302:DY:WindPitchContPowerIEC.dpmin:valueRangePair  
Rate limit for decreasing power (dp<sub>min</sub>) (< WindPitchContPowerIEC.dpmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPitchContPowerIEC.dpmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPitchContPowerIEC.dpmax` 

### dy302c:WindPitchContPowerIEC.t1-valueRange

**Path:** `cim:WindPitchContPowerIEC.t1`  
**Name:** C:302:DY:WindPitchContPowerIEC.t1:valueRange  
Lag time constant (T<sub>1</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPitchContPowerIEC.tr-valueRange

**Path:** `cim:WindPitchContPowerIEC.tr`  
**Name:** C:302:DY:WindPitchContPowerIEC.tr:valueRange  
Voltage measurement time constant (T<sub>r</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindPlantFreqPcontrolIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantFreqPcontrolIEC

**Nested Properties:**

### dy302c:WindPlantFreqPcontrolIEC.dprefmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.dprefmin`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.dprefmin:valueRangePair  
Minimum (negative) ramp rate of p<sub>WTref</sub> request from the plant controller to the wind turbines (dp<sub>refmin</sub>) (< WindPlantFreqPcontrolIEC.dprefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.dprefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.dprefmax` 

### dy302c:WindPlantFreqPcontrolIEC.dpwprefmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.dpwprefmin`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.dpwprefmin:valueRangePair  
Maximum negative ramp rate for wind plant power reference (dp<sub>WPrefmin</sub>) (< WindPlantFreqPcontrolIEC.dpwprefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.dpwprefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.dpwprefmax` 

### dy302c:WindPlantFreqPcontrolIEC.kiwppmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.kiwppmin`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.kiwppmin:valueRangePair  
Minimum PI integrator term (K<sub>IWPpmin</sub>) (< WindPlantFreqPcontrolIEC.kiwppmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.kiwppmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.kiwppmax` 

### dy302c:WindPlantFreqPcontrolIEC.prefmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.prefmin`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.prefmin:valueRangePair  
Minimum p<sub>WTref</sub> request from the plant controller to the wind turbines (p<sub>refmin</sub>) (< WindPlantFreqPcontrolIEC.prefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.prefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.prefmax` 

### dy302c:WindPlantFreqPcontrolIEC.tpft-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.tpft`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.tpft:valueRange  
Lead time constant in reference value transfer function (T<sub>pft</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.tpfv-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.tpfv`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.tpfv:valueRange  
Lag time constant in reference value transfer function (T<sub>pfv</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.twpffiltp-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.twpffiltp`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.twpffiltp:valueRange  
Filter time constant for frequency measurement (T<sub>WPffiltp</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.twppfiltp-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.twppfiltp`  
**Name:** C:302:DY:WindPlantFreqPcontrolIEC.twppfiltp:valueRange  
Filter time constant for active power measurement (T<sub>WPpfiltp</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindPlantReactiveControlIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantReactiveControlIEC

**Nested Properties:**

### dy302c:WindPlantReactiveControlIEC.dxrefmin-valueRangePair

**Path:** `cim:WindPlantReactiveControlIEC.dxrefmin`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.dxrefmin:valueRangePair  
Maximum negative ramp rate for wind turbine reactive power/voltage reference (dx<sub>refmin</sub>) (< WindPlantReactiveControlIEC.dxrefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantReactiveControlIEC.dxrefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantReactiveControlIEC.dxrefmax` 

### dy302c:WindPlantReactiveControlIEC.kiwpxmin-valueRangePair

**Path:** `cim:WindPlantReactiveControlIEC.kiwpxmin`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.kiwpxmin:valueRangePair  
Minimum reactive power/voltage reference from integration (K<sub>IWPxmin</sub>) (< WindPlantReactiveControlIEC.kiwpxmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantReactiveControlIEC.kiwpxmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantReactiveControlIEC.kiwpxmax` 

### dy302c:WindPlantReactiveControlIEC.tuqfilt-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.tuqfilt`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.tuqfilt:valueRange  
Filter time constant for voltage-dependent reactive power (T<sub>uqfilt</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twppfiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twppfiltq`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.twppfiltq:valueRange  
Filter time constant for active power measurement (T<sub>WPpfiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twpqfiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twpqfiltq`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.twpqfiltq:valueRange  
Filter time constant for reactive power measurement (T<sub>WPqfiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twpufiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twpufiltq`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.twpufiltq:valueRange  
Filter time constant for voltage measurement (T<sub>WPufiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.txft-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.txft`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.txft:valueRange  
Lead time constant in reference value transfer function (T<sub>xft</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.txfv-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.txfv`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.txfv:valueRange  
Lag time constant in reference value transfer function (T<sub>xfv</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.xrefmin-valueRangePair

**Path:** `cim:WindPlantReactiveControlIEC.xrefmin`  
**Name:** C:302:DY:WindPlantReactiveControlIEC.xrefmin:valueRangePair  
Minimum x<sub>WTref</sub> (q<sub>WTref</sub> or delta u<sub>WTref</sub>) request from the plant controller (x<sub>refmin</sub>) (< WindPlantReactiveControlIEC.xrefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantReactiveControlIEC.xrefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantReactiveControlIEC.xrefmax` 

## dy302c:WindProtectionIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindProtectionIEC

**Nested Properties:**

### dy302c:WindProtectionIEC.tfma-valueRange

**Path:** `cim:WindProtectionIEC.tfma`  
**Name:** C:302:DY:WindProtectionIEC.tfma:valueRange  
Time interval of moving average window (TfMA) (>= 0).  It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:WindRefFrameRotIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindRefFrameRotIEC

**Nested Properties:**

### dy302c:WindRefFrameRotIEC.tpll-valueRange

**Path:** `cim:WindRefFrameRotIEC.tpll`  
**Name:** C:302:DY:WindRefFrameRotIEC.tpll:valueRange  
Time constant for PLL first order filter model (T<sub>PLL</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

