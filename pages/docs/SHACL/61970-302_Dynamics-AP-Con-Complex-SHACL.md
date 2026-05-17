# 61970-302_Dynamics-AP-Con-Complex-SHACL

## dy302c:AsynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineEquivalentCircuit

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
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
Subtransient rotor time constant (T''o) (> 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.tpo-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.tppo`  
Transient rotor time constant (T'o) (> AsynchronousMachineTimeConstantReactance.tppo).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.tpo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.tpo` 

### dy302c:AsynchronousMachineTimeConstantReactance.xs-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.xp`  
Synchronous reactance (Xs) (>= AsynchronousMachineTimeConstantReactance.xp).  Typical value = 1,8.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than AsynchronousMachineTimeConstantReactance.xs."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xs` 

### dy302c:AsynchronousMachineTimeConstantReactance.xp-valueRangePair

**Path:** `cim:AsynchronousMachineTimeConstantReactance.xpp`  
Transient reactance (unsaturated) (X') (>= AsynchronousMachineTimeConstantReactance.xpp).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than AsynchronousMachineTimeConstantReactance.xp."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xp` 

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
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
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
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
Discontinuous controller time constant (T<sub>AN</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.td-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.td`  
Time constant (T<sub>D</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tl1-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tl1`  
Time constant (T<sub>L</sub><sub>1</sub>) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tl2-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tl2`  
Time constant (T<sub>L</sub><sub>2</sub>) (>= 0).  Typical value = 1,25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.tw5-valueRange

**Path:** `cim:DiscExcContIEEEDEC1A.tw5`  
DEC washout time constant (T<sub>W</sub><sub>5</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC1A.vomin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC1A.vomin`  
Limiter (V<sub>OMIN</sub>) (< DiscExcContIEEEDEC1A.vomax).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than DiscExcContIEEEDEC1A.vomax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:DiscExcContIEEEDEC1A.vomax` 

### dy302c:DiscExcContIEEEDEC1A.vsmin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC1A.vsmin`  
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
Discontinuous controller time constant (T<sub>D1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC2A.td2-valueRange

**Path:** `cim:DiscExcContIEEEDEC2A.td2`  
Discontinuous controller washout time constant (T<sub>D2</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:DiscExcContIEEEDEC2A.vdmin-valueRangePair

**Path:** `cim:DiscExcContIEEEDEC2A.vdmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kc-valueRange

**Path:** `cim:ExcAC1A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kd-valueRange

**Path:** `cim:ExcAC1A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,38.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf-valueRange

**Path:** `cim:ExcAC1A.kf`  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf1-valueRange

**Path:** `cim:ExcAC1A.kf1`  
Coefficient to allow different usage of the model (Kf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.kf2-valueRange

**Path:** `cim:ExcAC1A.kf2`  
Coefficient to allow different usage of the model (Kf2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ks-valueRange

**Path:** `cim:ExcAC1A.ks`  
Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.seve1-valueRange

**Path:** `cim:ExcAC1A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.seve2-valueRange

**Path:** `cim:ExcAC1A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ta-valueRange

**Path:** `cim:ExcAC1A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tb-valueRange

**Path:** `cim:ExcAC1A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tc-valueRange

**Path:** `cim:ExcAC1A.tc`  
Voltage regulator time constant (T<sub>c</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.te-valueRange

**Path:** `cim:ExcAC1A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.tf-valueRange

**Path:** `cim:ExcAC1A.tf`  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vamax-valueRange

**Path:** `cim:ExcAC1A.vamax`  
Maximum voltage regulator output (V<sub>amax</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vamin-valueRange

**Path:** `cim:ExcAC1A.vamin`  
Minimum voltage regulator output (V<sub>amin</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ve1-valueRange

**Path:** `cim:ExcAC1A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).  Typical value = 4,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.ve2-valueRange

**Path:** `cim:ExcAC1A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).  Typical value = 3,14.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vrmax-valueRange

**Path:** `cim:ExcAC1A.vrmax`  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 6,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC1A.vrmin-valueRange

**Path:** `cim:ExcAC1A.vrmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kb-valueRange

**Path:** `cim:ExcAC2A.kb`  
Second stage regulator gain (Kb) (> 0).  Exciter field current controller gain.  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kc-valueRange

**Path:** `cim:ExcAC2A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,28.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kd-valueRange

**Path:** `cim:ExcAC2A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kf-valueRange

**Path:** `cim:ExcAC2A.kf`  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.kh-valueRange

**Path:** `cim:ExcAC2A.kh`  
Exciter field current feedback gain (Kh) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ks-valueRange

**Path:** `cim:ExcAC2A.ks`  
Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.seve1-valueRange

**Path:** `cim:ExcAC2A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.seve2-valueRange

**Path:** `cim:ExcAC2A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ta-valueRange

**Path:** `cim:ExcAC2A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tb-valueRange

**Path:** `cim:ExcAC2A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tc-valueRange

**Path:** `cim:ExcAC2A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.te-valueRange

**Path:** `cim:ExcAC2A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.tf-valueRange

**Path:** `cim:ExcAC2A.tf`  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vamax-valueRange

**Path:** `cim:ExcAC2A.vamax`  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vamin-valueRange

**Path:** `cim:ExcAC2A.vamin`  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -8.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ve1-valueRange

**Path:** `cim:ExcAC2A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.ve2-valueRange

**Path:** `cim:ExcAC2A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vfemax-valueRange

**Path:** `cim:ExcAC2A.vfemax`  
Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vlr-valueRange

**Path:** `cim:ExcAC2A.vlr`  
Maximum exciter field current (Vlr) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vrmax-valueRange

**Path:** `cim:ExcAC2A.vrmax`  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 105.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC2A.vrmin-valueRange

**Path:** `cim:ExcAC2A.vrmin`  
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
Value of Efd at which feedback gain changes (Efdn) (> 0).  Typical value = 2,36.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ka-valueRange

**Path:** `cim:ExcAC3A.ka`  
Voltage regulator gain (Ka) (> 0).  Typical value = 45,62.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kc-valueRange

**Path:** `cim:ExcAC3A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,104.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kd-valueRange

**Path:** `cim:ExcAC3A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,499.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kf-valueRange

**Path:** `cim:ExcAC3A.kf`  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kn-valueRange

**Path:** `cim:ExcAC3A.kn`  
Excitation control system stabilizer gain (Kn) (>= 0).  Typical value =0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.kr-valueRange

**Path:** `cim:ExcAC3A.kr`  
Constant associated with regulator and alternator field power supply (Kr) (> 0).  Typical value =3,77.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.seve1-valueRange

**Path:** `cim:ExcAC3A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 1,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.seve2-valueRange

**Path:** `cim:ExcAC3A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ta-valueRange

**Path:** `cim:ExcAC3A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,013.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tb-valueRange

**Path:** `cim:ExcAC3A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tc-valueRange

**Path:** `cim:ExcAC3A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.te-valueRange

**Path:** `cim:ExcAC3A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,17.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.tf-valueRange

**Path:** `cim:ExcAC3A.tf`  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vamax-valueRange

**Path:** `cim:ExcAC3A.vamax`  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vamin-valueRange

**Path:** `cim:ExcAC3A.vamin`  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ve1-valueRange

**Path:** `cim:ExcAC3A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 6.24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.ve2-valueRange

**Path:** `cim:ExcAC3A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 4,68.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vemin-valueRange

**Path:** `cim:ExcAC3A.vemin`  
Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC3A.vfemax-valueRange

**Path:** `cim:ExcAC3A.vfemax`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.kc-valueRange

**Path:** `cim:ExcAC4A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.ta-valueRange

**Path:** `cim:ExcAC4A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,015.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.tb-valueRange

**Path:** `cim:ExcAC4A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.tc-valueRange

**Path:** `cim:ExcAC4A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vimax-valueRange

**Path:** `cim:ExcAC4A.vimax`  
Maximum voltage regulator input limit (Vimax)  (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vimin-valueRange

**Path:** `cim:ExcAC4A.vimin`  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vrmax-valueRange

**Path:** `cim:ExcAC4A.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5,64.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC4A.vrmin-valueRange

**Path:** `cim:ExcAC4A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 5,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.efd2-valueRange

**Path:** `cim:ExcAC5A.efd2`  
Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 4,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.ka-valueRange

**Path:** `cim:ExcAC5A.ka`  
Voltage regulator gain (Ka) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.kf-valueRange

**Path:** `cim:ExcAC5A.kf`  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.seefd1-valueRange

**Path:** `cim:ExcAC5A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,86.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.seefd2-valueRange

**Path:** `cim:ExcAC5A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.ta-valueRange

**Path:** `cim:ExcAC5A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tb-valueRange

**Path:** `cim:ExcAC5A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tc-valueRange

**Path:** `cim:ExcAC5A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.te-valueRange

**Path:** `cim:ExcAC5A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf1-valueRange

**Path:** `cim:ExcAC5A.tf1`  
Excitation control system stabilizer time constant (Tf1) (> 0).  Typical value  = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf2-valueRange

**Path:** `cim:ExcAC5A.tf2`  
Excitation control system stabilizer time constant (Tf2) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.tf3-valueRange

**Path:** `cim:ExcAC5A.tf3`  
Excitation control system stabilizer time constant (Tf3) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.vrmax-valueRange

**Path:** `cim:ExcAC5A.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC5A.vrmin-valueRange

**Path:** `cim:ExcAC5A.vrmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 536.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kc-valueRange

**Path:** `cim:ExcAC6A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kd-valueRange

**Path:** `cim:ExcAC6A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,91.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.kh-valueRange

**Path:** `cim:ExcAC6A.kh`  
Exciter field current limiter gain (Kh) (>= 0).  Typical value = 92.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.seve1-valueRange

**Path:** `cim:ExcAC6A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,214.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.seve2-valueRange

**Path:** `cim:ExcAC6A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 0,044.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ta-valueRange

**Path:** `cim:ExcAC6A.ta`  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tb-valueRange

**Path:** `cim:ExcAC6A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tc-valueRange

**Path:** `cim:ExcAC6A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.te-valueRange

**Path:** `cim:ExcAC6A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.th-valueRange

**Path:** `cim:ExcAC6A.th`  
Exciter field current limiter time constant (Th) (> 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tj-valueRange

**Path:** `cim:ExcAC6A.tj`  
Exciter field current limiter time constant (Tj) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.tk-valueRange

**Path:** `cim:ExcAC6A.tk`  
Voltage regulator time constant (Tk) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vamax-valueRange

**Path:** `cim:ExcAC6A.vamax`  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vamin-valueRange

**Path:** `cim:ExcAC6A.vamin`  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -75.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ve1-valueRange

**Path:** `cim:ExcAC6A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 7,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.ve2-valueRange

**Path:** `cim:ExcAC6A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 5,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vfelim-valueRange

**Path:** `cim:ExcAC6A.vfelim`  
Exciter field current limit reference (Vfelim) (> 0).  Typical value = 19.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vhmax-valueRange

**Path:** `cim:ExcAC6A.vhmax`  
Maximum field current limiter signal reference (Vhmax) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vrmax-valueRange

**Path:** `cim:ExcAC6A.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC6A.vrmin-valueRange

**Path:** `cim:ExcAC6A.vrmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kc-valueRange

**Path:** `cim:ExcAC8B.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kd-valueRange

**Path:** `cim:ExcAC8B.kd`  
Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kdr-valueRange

**Path:** `cim:ExcAC8B.kdr`  
Voltage regulator derivative gain (Kdr) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.kir-valueRange

**Path:** `cim:ExcAC8B.kir`  
Voltage regulator integral gain (Kir) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.seve1-valueRange

**Path:** `cim:ExcAC8B.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.seve2-valueRange

**Path:** `cim:ExcAC8B.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ta-valueRange

**Path:** `cim:ExcAC8B.ta`  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.tdr-valueRange

**Path:** `cim:ExcAC8B.tdr`  
Lag time constant (Tdr) (> 0 if ExcAC8B.kdr > 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.te-valueRange

**Path:** `cim:ExcAC8B.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ve1-valueRange

**Path:** `cim:ExcAC8B.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 6,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.ve2-valueRange

**Path:** `cim:ExcAC8B.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>2</sub>) (> 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vemin-valueRange

**Path:** `cim:ExcAC8B.vemin`  
Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vimin-valueRangePair

**Path:** `cim:ExcAC8B.vimin`  
Input signal minimum (Vimin) (< ExcAC8B.vimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAC8B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAC8B.vimax` 

### dy302c:ExcAC8B.vpidmin-valueRangePair

**Path:** `cim:ExcAC8B.vpidmin`  
PID minimum controller output (Vpidmin) (< ExcAC8B.vpidmax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAC8B.vpidmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAC8B.vpidmax` 

### dy302c:ExcAC8B.vrmax-valueRange

**Path:** `cim:ExcAC8B.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0). Typical value = 35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAC8B.vrmin-valueRange

**Path:** `cim:ExcAC8B.vrmin`  
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
Time constant (T<sub>1</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.t2-valueRange

**Path:** `cim:ExcANS.t2`  
Time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.t3-valueRange

**Path:** `cim:ExcANS.t3`  
Time constant (T<sub>3</sub>) (>= 0).  Typical value = 1,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcANS.tb-valueRange

**Path:** `cim:ExcANS.tb`  
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
AVR time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.tb-valueRange

**Path:** `cim:ExcAVR1.tb`  
AVR time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.te-valueRange

**Path:** `cim:ExcAVR1.te`  
Exciter time constant (T<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR1.tf-valueRange

**Path:** `cim:ExcAVR1.tf`  
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
AVR time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tb-valueRange

**Path:** `cim:ExcAVR2.tb`  
AVR time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.te-valueRange

**Path:** `cim:ExcAVR2.te`  
Exciter time constant (T<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tf1-valueRange

**Path:** `cim:ExcAVR2.tf1`  
Rate feedback time constant (T<sub>F1</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR2.tf2-valueRange

**Path:** `cim:ExcAVR2.tf2`  
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
AVR time constant (T<sub>1</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t2-valueRange

**Path:** `cim:ExcAVR3.t2`  
AVR time constant (T<sub>2</sub>) (>= 0).  Typical value = 1,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t3-valueRange

**Path:** `cim:ExcAVR3.t3`  
AVR time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,66.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.t4-valueRange

**Path:** `cim:ExcAVR3.t4`  
AVR time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,07.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR3.te-valueRange

**Path:** `cim:ExcAVR3.te`  
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
AVR time constant (T<sub>1</sub>) (>= 0).  Typical value = 4,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t1if-valueRange

**Path:** `cim:ExcAVR4.t1if`  
Exciter current feedback time constant (T<sub>1IF</sub>) (>= 0).  Typical value = 60.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t2-valueRange

**Path:** `cim:ExcAVR4.t2`  
AVR time constant (T<sub>2</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t3-valueRange

**Path:** `cim:ExcAVR4.t3`  
AVR time constant (T<sub>3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.t4-valueRange

**Path:** `cim:ExcAVR4.t4`  
AVR time constant (T<sub>4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR4.tif-valueRange

**Path:** `cim:ExcAVR4.tif`  
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
Lead time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t2-valueRange

**Path:** `cim:ExcAVR7.t2`  
Lag time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t3-valueRange

**Path:** `cim:ExcAVR7.t3`  
Lead time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t4-valueRange

**Path:** `cim:ExcAVR7.t4`  
Lag time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t5-valueRange

**Path:** `cim:ExcAVR7.t5`  
Lead time constant (T<sub>5</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.t6-valueRange

**Path:** `cim:ExcAVR7.t6`  
Lag time constant (T<sub>6</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcAVR7.vmin1-valueRangePair

**Path:** `cim:ExcAVR7.vmin1`  
Lead-lag minimum limit (Vmin1) (< ExcAVR7.vmax1).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAVR7.vmax1."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAVR7.vmax1` 

### dy302c:ExcAVR7.vmin3-valueRangePair

**Path:** `cim:ExcAVR7.vmin3`  
Lead-lag minimum limit (Vmin3) (< ExcAVR7.vmax3).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcAVR7.vmax3."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcAVR7.vmax3` 

### dy302c:ExcAVR7.vmin5-valueRangePair

**Path:** `cim:ExcAVR7.vmin5`  
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
Minimum open circuit exciter voltage (Efdmin) (< ExcBBC.efdmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcBBC.efdmax` 

### dy302c:ExcBBC.t1-valueRange

**Path:** `cim:ExcBBC.t1`  
Controller time constant (T1) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t2-valueRange

**Path:** `cim:ExcBBC.t2`  
Controller time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t3-valueRange

**Path:** `cim:ExcBBC.t3`  
Lead/lag time constant (T3) (>= 0).  If = 0, block is bypassed.  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.t4-valueRange

**Path:** `cim:ExcBBC.t4`  
Lead/lag time constant (T4) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcBBC.vrmin-valueRangePair

**Path:** `cim:ExcBBC.vrmin`  
Minimum control element output (Vrmin) (< ExcBBC.vrmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcBBC.vrmax` 

### dy302c:ExcBBC.xe-valueRange

**Path:** `cim:ExcBBC.xe`  
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
Exciter output minimum limit (Efdmin) (< ExcCZ.efdmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcCZ.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcCZ.efdmax` 

### dy302c:ExcCZ.ta-valueRange

**Path:** `cim:ExcCZ.ta`  
Regulator time constant (Ta) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.tc-valueRange

**Path:** `cim:ExcCZ.tc`  
Regulator integral time constant (Tc) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.te-valueRange

**Path:** `cim:ExcCZ.te`  
Exciter time constant, integration rate associated with exciter control (Te) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcCZ.vrmin-valueRangePair

**Path:** `cim:ExcCZ.vrmin`  
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
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 3,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.efd2-valueRange

**Path:** `cim:ExcDC1A.efd2`  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 2,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.efdmin-valueRangePair

**Path:** `cim:ExcDC1A.efdmin`  
Minimum voltage exciter output limiter (Efdmin) (< ExcDC1A.edfmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC1A.edfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC1A.edfmax` 

### dy302c:ExcDC1A.ka-valueRange

**Path:** `cim:ExcDC1A.ka`  
Voltage regulator gain (Ka) (> 0).  Typical value = 46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.kf-valueRange

**Path:** `cim:ExcDC1A.kf`  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.seefd1-valueRange

**Path:** `cim:ExcDC1A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Eefd<sub>1</sub>]) (>= 0).  Typical value = 0,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.seefd2-valueRange

**Path:** `cim:ExcDC1A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Eefd<sub>2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.ta-valueRange

**Path:** `cim:ExcDC1A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,06.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tb-valueRange

**Path:** `cim:ExcDC1A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tc-valueRange

**Path:** `cim:ExcDC1A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.te-valueRange

**Path:** `cim:ExcDC1A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.tf-valueRange

**Path:** `cim:ExcDC1A.tf`  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC1A.vrmin-valueRangePair

**Path:** `cim:ExcDC1A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 3,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.efd2-valueRange

**Path:** `cim:ExcDC2A.efd2`  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 2,29.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.ka-valueRange

**Path:** `cim:ExcDC2A.ka`  
Voltage regulator gain (Ka) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.kf-valueRange

**Path:** `cim:ExcDC2A.kf`  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.seefd1-valueRange

**Path:** `cim:ExcDC2A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,279.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.seefd2-valueRange

**Path:** `cim:ExcDC2A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,117.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.ta-valueRange

**Path:** `cim:ExcDC2A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tb-valueRange

**Path:** `cim:ExcDC2A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tc-valueRange

**Path:** `cim:ExcDC2A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.te-valueRange

**Path:** `cim:ExcDC2A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tf-valueRange

**Path:** `cim:ExcDC2A.tf`  
Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.tf1-valueRange

**Path:** `cim:ExcDC2A.tf1`  
Excitation control system stabilizer time constant (Tf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC2A.vrmin-valueRangePair

**Path:** `cim:ExcDC2A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (Efd<sub>1</sub>) (> 0).  Typical value = 2,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.efd2-valueRange

**Path:** `cim:ExcDC3A.efd2`  
Exciter voltage at which exciter saturation is defined (Efd<sub>2</sub>) (> 0).  Typical value = 3,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.efdmin-valueRangePair

**Path:** `cim:ExcDC3A.efdmin`  
Minimum voltage exciter output limiter (Efdmin) (< ExcDC3A.efdmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcDC3A.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcDC3A.efdmax` 

### dy302c:ExcDC3A.kv-valueRange

**Path:** `cim:ExcDC3A.kv`  
Fast raise/lower contact setting (Kv) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.seefd1-valueRange

**Path:** `cim:ExcDC3A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>1</sub> (Se[Efd<sub>1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.seefd2-valueRange

**Path:** `cim:ExcDC3A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, Efd<sub>2</sub> (Se[Efd<sub>2</sub>]) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.te-valueRange

**Path:** `cim:ExcDC3A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.trh-valueRange

**Path:** `cim:ExcDC3A.trh`  
Rheostat travel time (Trh) (> 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.vrmax-valueRange

**Path:** `cim:ExcDC3A.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A.vrmin-valueRange

**Path:** `cim:ExcDC3A.vrmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.kf-valueRange

**Path:** `cim:ExcDC3A1.kf`  
Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.ki-valueRange

**Path:** `cim:ExcDC3A1.ki`  
Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 4,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.kp-valueRange

**Path:** `cim:ExcDC3A1.kp`  
Potential circuit gain coefficient (Kp) (>= 0).  Typical value = 4,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.ta-valueRange

**Path:** `cim:ExcDC3A1.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.te-valueRange

**Path:** `cim:ExcDC3A1.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.tf-valueRange

**Path:** `cim:ExcDC3A1.tf`  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vb1max-valueRange

**Path:** `cim:ExcDC3A1.vb1max`  
Available exciter voltage limiter (Vb1max) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vbmax-valueRange

**Path:** `cim:ExcDC3A1.vbmax`  
Available exciter voltage limiter (Vbmax) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcDC3A1.vrmin-valueRangePair

**Path:** `cim:ExcDC3A1.vrmin`  
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
Minimum open circuit excitation voltage (Efmin) (< ExcELIN1.efmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN1.efmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN1.efmax` 

### dy302c:ExcELIN1.tfi-valueRange

**Path:** `cim:ExcELIN1.tfi`  
Current transducer time constant (Tfi) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.tnu-valueRange

**Path:** `cim:ExcELIN1.tnu`  
Controller reset time constant (Tnu) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.ts1-valueRange

**Path:** `cim:ExcELIN1.ts1`  
Stabilizer phase lag time constant (Ts1) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.ts2-valueRange

**Path:** `cim:ExcELIN1.ts2`  
Stabilizer filter time constant (Ts2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.tsw-valueRange

**Path:** `cim:ExcELIN1.tsw`  
Stabilizer parameters (Tsw) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN1.xe-valueRange

**Path:** `cim:ExcELIN1.xe`  
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
Limiter (I<sub>efmin</sub>) (< ExcELIN2.iefmax).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN2.iefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN2.iefmax` 

### dy302c:ExcELIN2.seve1-valueRange

**Path:** `cim:ExcELIN2.seve1`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.seve2-valueRange

**Path:** `cim:ExcELIN2.seve2`  
Exciter saturation function value at the corresponding exciter voltage, Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.tb1-valueRange

**Path:** `cim:ExcELIN2.tb1`  
Voltage controller derivative washout time constant (Tb1) (>= 0).  Typical value = 12,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.te-valueRange

**Path:** `cim:ExcELIN2.te`  
Time constant (Te) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.te2-valueRange

**Path:** `cim:ExcELIN2.te2`  
Time Constant (T<sub>e2</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ti3-valueRange

**Path:** `cim:ExcELIN2.ti3`  
Time constant (T<sub>i3</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ti4-valueRange

**Path:** `cim:ExcELIN2.ti4`  
Time constant (T<sub>i4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.tr4-valueRange

**Path:** `cim:ExcELIN2.tr4`  
Time constant (T<sub>r4</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.upmin-valueRangePair

**Path:** `cim:ExcELIN2.upmin`  
Limiter (Upmin) (< ExcELIN2.upmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcELIN2.upmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcELIN2.upmax` 

### dy302c:ExcELIN2.ve1-valueRange

**Path:** `cim:ExcELIN2.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve<sub>1</sub>) (> 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcELIN2.ve2-valueRange

**Path:** `cim:ExcELIN2.ve2`  
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
Field voltage control signal lower limit on AVR base (Emin) (< ExcHU.emax).  Typical value = -0,866.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcHU.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcHU.emax` 

### dy302c:ExcHU.imin-valueRangePair

**Path:** `cim:ExcHU.imin`  
Major loop PI tag output signal lower limit (Imin) (< ExcHU.imax).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcBBC.vrmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcHU.imax` 

### dy302c:ExcHU.te-valueRange

**Path:** `cim:ExcHU.te`  
Major loop PI tag integration time constant (Te) (>= 0).  Typical value = 0,154.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcHU.ti-valueRange

**Path:** `cim:ExcHU.ti`  
Minor loop PI control tag integration time constant (Ti) (>= 0).  Typical value = 0,01333.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcHU.tr-valueRange

**Path:** `cim:ExcHU.tr`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kc-valueRange

**Path:** `cim:ExcIEEEAC1A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kd-valueRange

**Path:** `cim:ExcIEEEAC1A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,38.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.kf-valueRange

**Path:** `cim:ExcIEEEAC1A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.seve1-valueRange

**Path:** `cim:ExcIEEEAC1A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.seve2-valueRange

**Path:** `cim:ExcIEEEAC1A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ta-valueRange

**Path:** `cim:ExcIEEEAC1A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tb-valueRange

**Path:** `cim:ExcIEEEAC1A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tc-valueRange

**Path:** `cim:ExcIEEEAC1A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.te-valueRange

**Path:** `cim:ExcIEEEAC1A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.tf-valueRange

**Path:** `cim:ExcIEEEAC1A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vamax-valueRange

**Path:** `cim:ExcIEEEAC1A.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vamin-valueRange

**Path:** `cim:ExcIEEEAC1A.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ve1-valueRange

**Path:** `cim:ExcIEEEAC1A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 4,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.ve2-valueRange

**Path:** `cim:ExcIEEEAC1A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,14.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC1A.vrmax`  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 6,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC1A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC1A.vrmin`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kb-valueRange

**Path:** `cim:ExcIEEEAC2A.kb`  
Second stage regulator gain (K<sub>B</sub>) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kc-valueRange

**Path:** `cim:ExcIEEEAC2A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,28.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kd-valueRange

**Path:** `cim:ExcIEEEAC2A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ke-valueRange

**Path:** `cim:ExcIEEEAC2A.ke`  
Exciter constant related to self-excited field (K<sub>E</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kf-valueRange

**Path:** `cim:ExcIEEEAC2A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.kh-valueRange

**Path:** `cim:ExcIEEEAC2A.kh`  
Exciter field current feedback gain (K<sub>H</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.seve1-valueRange

**Path:** `cim:ExcIEEEAC2A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.seve2-valueRange

**Path:** `cim:ExcIEEEAC2A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ta-valueRange

**Path:** `cim:ExcIEEEAC2A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tb-valueRange

**Path:** `cim:ExcIEEEAC2A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tc-valueRange

**Path:** `cim:ExcIEEEAC2A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.te-valueRange

**Path:** `cim:ExcIEEEAC2A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.tf-valueRange

**Path:** `cim:ExcIEEEAC2A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vamax-valueRange

**Path:** `cim:ExcIEEEAC2A.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vamin-valueRange

**Path:** `cim:ExcIEEEAC2A.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -8.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ve1-valueRange

**Path:** `cim:ExcIEEEAC2A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.ve2-valueRange

**Path:** `cim:ExcIEEEAC2A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vfemax-valueRange

**Path:** `cim:ExcIEEEAC2A.vfemax`  
Exciter field current limit reference (V<sub>FEMAX</sub>) (> 0).  Typical value = 4,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC2A.vrmax`  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 105.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC2A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC2A.vrmin`  
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
Value of Efd at which feedback gain changes (E<sub>FDN</sub>) (> 0).  Typical value = 2,36.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ka-valueRange

**Path:** `cim:ExcIEEEAC3A.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 45,62.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kc-valueRange

**Path:** `cim:ExcIEEEAC3A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0,104.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kd-valueRange

**Path:** `cim:ExcIEEEAC3A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,499.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kf-valueRange

**Path:** `cim:ExcIEEEAC3A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kn-valueRange

**Path:** `cim:ExcIEEEAC3A.kn`  
Excitation control system stabilizer gain (K<sub>N</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.kr-valueRange

**Path:** `cim:ExcIEEEAC3A.kr`  
Constant associated with regulator and alternator field power supply (K<sub>R</sub>) (> 0).  Typical value = 3,77.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.seve1-valueRange

**Path:** `cim:ExcIEEEAC3A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 1,143.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.seve2-valueRange

**Path:** `cim:ExcIEEEAC3A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ta-valueRange

**Path:** `cim:ExcIEEEAC3A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,013.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tb-valueRange

**Path:** `cim:ExcIEEEAC3A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tc-valueRange

**Path:** `cim:ExcIEEEAC3A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.te-valueRange

**Path:** `cim:ExcIEEEAC3A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,17.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.tf-valueRange

**Path:** `cim:ExcIEEEAC3A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vamax-valueRange

**Path:** `cim:ExcIEEEAC3A.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vamin-valueRange

**Path:** `cim:ExcIEEEAC3A.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ve1-valueRange

**Path:** `cim:ExcIEEEAC3A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.ve2-valueRange

**Path:** `cim:ExcIEEEAC3A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 4,68.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vemin-valueRange

**Path:** `cim:ExcIEEEAC3A.vemin`  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC3A.vfemax-valueRange

**Path:** `cim:ExcIEEEAC3A.vfemax`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.kc-valueRange

**Path:** `cim:ExcIEEEAC4A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.ta-valueRange

**Path:** `cim:ExcIEEEAC4A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,015.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.tb-valueRange

**Path:** `cim:ExcIEEEAC4A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.tc-valueRange

**Path:** `cim:ExcIEEEAC4A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vimax-valueRange

**Path:** `cim:ExcIEEEAC4A.vimax`  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vimin-valueRange

**Path:** `cim:ExcIEEEAC4A.vimin`  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC4A.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5,64.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC4A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC4A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 5,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.efd2-valueRange

**Path:** `cim:ExcIEEEAC5A.efd2`  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 4,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.ka-valueRange

**Path:** `cim:ExcIEEEAC5A.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 400.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.kf-valueRange

**Path:** `cim:ExcIEEEAC5A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.seefd1-valueRange

**Path:** `cim:ExcIEEEAC5A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,86.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.seefd2-valueRange

**Path:** `cim:ExcIEEEAC5A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.ta-valueRange

**Path:** `cim:ExcIEEEAC5A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.te-valueRange

**Path:** `cim:ExcIEEEAC5A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf1-valueRange

**Path:** `cim:ExcIEEEAC5A.tf1`  
Excitation control system stabilizer time constant (T<sub>F1</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf2-valueRange

**Path:** `cim:ExcIEEEAC5A.tf2`  
Excitation control system stabilizer time constant (T<sub>F2</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.tf3-valueRange

**Path:** `cim:ExcIEEEAC5A.tf3`  
Excitation control system stabilizer time constant (T<sub>F3</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC5A.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 7,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC5A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC5A.vrmin`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 536.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kc-valueRange

**Path:** `cim:ExcIEEEAC6A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kd-valueRange

**Path:** `cim:ExcIEEEAC6A.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 1,91.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.kh-valueRange

**Path:** `cim:ExcIEEEAC6A.kh`  
Exciter field current limiter gain (K<sub>H</sub>) (>= 0).  Typical value = 92.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.seve1-valueRange

**Path:** `cim:ExcIEEEAC6A.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,214.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.seve2-valueRange

**Path:** `cim:ExcIEEEAC6A.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,044.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ta-valueRange

**Path:** `cim:ExcIEEEAC6A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tb-valueRange

**Path:** `cim:ExcIEEEAC6A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tc-valueRange

**Path:** `cim:ExcIEEEAC6A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.te-valueRange

**Path:** `cim:ExcIEEEAC6A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.th-valueRange

**Path:** `cim:ExcIEEEAC6A.th`  
Exciter field current limiter time constant (T<sub>H</sub>) (> 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tj-valueRange

**Path:** `cim:ExcIEEEAC6A.tj`  
Exciter field current limiter time constant (T<sub>J</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.tk-valueRange

**Path:** `cim:ExcIEEEAC6A.tk`  
Voltage regulator time constant (T<sub>K</sub>) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vamax-valueRange

**Path:** `cim:ExcIEEEAC6A.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vamin-valueRange

**Path:** `cim:ExcIEEEAC6A.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -75.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ve1-valueRange

**Path:** `cim:ExcIEEEAC6A.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 7,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.ve2-valueRange

**Path:** `cim:ExcIEEEAC6A.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 5,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vfelim-valueRange

**Path:** `cim:ExcIEEEAC6A.vfelim`  
Exciter field current limit reference (V<sub>FELIM</sub>) (> 0).  Typical value = 19.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vhmax-valueRange

**Path:** `cim:ExcIEEEAC6A.vhmax`  
Maximum field current limiter signal reference (V<sub>HMAX</sub>) (> 0).  Typical value = 75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vrmax-valueRange

**Path:** `cim:ExcIEEEAC6A.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC6A.vrmin-valueRange

**Path:** `cim:ExcIEEEAC6A.vrmin`  
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
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kd-valueRange

**Path:** `cim:ExcIEEEAC7B.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kdr-valueRange

**Path:** `cim:ExcIEEEAC7B.kdr`  
Voltage regulator derivative gain (K<sub>DR</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf1-valueRange

**Path:** `cim:ExcIEEEAC7B.kf1`  
Excitation control system stabilizer gain (K<sub>F1</sub>) (>= 0).  Typical value = 0,212.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf2-valueRange

**Path:** `cim:ExcIEEEAC7B.kf2`  
Excitation control system stabilizer gain (K<sub>F2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kf3-valueRange

**Path:** `cim:ExcIEEEAC7B.kf3`  
Excitation control system stabilizer gain (K<sub>F3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kia-valueRange

**Path:** `cim:ExcIEEEAC7B.kia`  
Voltage regulator integral gain (K<sub>IA</sub>) (>= 0).  Typical value = 59,69.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kir-valueRange

**Path:** `cim:ExcIEEEAC7B.kir`  
Voltage regulator integral gain (K<sub>IR</sub>) (>= 0).  Typical value = 4,24.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.kp-valueRange

**Path:** `cim:ExcIEEEAC7B.kp`  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 4,96.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.seve1-valueRange

**Path:** `cim:ExcIEEEAC7B.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,44.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.seve2-valueRange

**Path:** `cim:ExcIEEEAC7B.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 0,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.tdr-valueRange

**Path:** `cim:ExcIEEEAC7B.tdr`  
Lag time constant (T<sub>DR</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.te-valueRange

**Path:** `cim:ExcIEEEAC7B.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.tf-valueRange

**Path:** `cim:ExcIEEEAC7B.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vamax-valueRange

**Path:** `cim:ExcIEEEAC7B.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vamin-valueRange

**Path:** `cim:ExcIEEEAC7B.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -0,95.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.ve1-valueRange

**Path:** `cim:ExcIEEEAC7B.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.ve2-valueRange

**Path:** `cim:ExcIEEEAC7B.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 3,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vemin-valueRange

**Path:** `cim:ExcIEEEAC7B.vemin`  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vrmax-valueRange

**Path:** `cim:ExcIEEEAC7B.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5,79.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC7B.vrmin-valueRange

**Path:** `cim:ExcIEEEAC7B.vrmin`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kc-valueRange

**Path:** `cim:ExcIEEEAC8B.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,55.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kd-valueRange

**Path:** `cim:ExcIEEEAC8B.kd`  
Demagnetizing factor, a function of exciter alternator reactances (K<sub>D</sub>) (>= 0).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kdr-valueRange

**Path:** `cim:ExcIEEEAC8B.kdr`  
Voltage regulator derivative gain (K<sub>DR</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.kir-valueRange

**Path:** `cim:ExcIEEEAC8B.kir`  
Voltage regulator integral gain (K<sub>IR</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.seve1-valueRange

**Path:** `cim:ExcIEEEAC8B.seve1`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.seve2-valueRange

**Path:** `cim:ExcIEEEAC8B.seve2`  
Exciter saturation function value at the corresponding exciter voltage, V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ta-valueRange

**Path:** `cim:ExcIEEEAC8B.ta`  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.tdr-valueRange

**Path:** `cim:ExcIEEEAC8B.tdr`  
Lag time constant (T<sub>DR</sub>) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.te-valueRange

**Path:** `cim:ExcIEEEAC8B.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ve1-valueRange

**Path:** `cim:ExcIEEEAC8B.ve1`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E1</sub>) (> 0).  Typical value = 6,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.ve2-valueRange

**Path:** `cim:ExcIEEEAC8B.ve2`  
Exciter alternator output voltages back of commutating reactance at which saturation is defined (V<sub>E2</sub>) (> 0).  Typical value = 9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vemin-valueRange

**Path:** `cim:ExcIEEEAC8B.vemin`  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vrmax-valueRange

**Path:** `cim:ExcIEEEAC8B.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEAC8B.vrmin-valueRange

**Path:** `cim:ExcIEEEAC8B.vrmin`  
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
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.efd2-valueRange

**Path:** `cim:ExcIEEEDC1A.efd2`  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.ka-valueRange

**Path:** `cim:ExcIEEEDC1A.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.kf-valueRange

**Path:** `cim:ExcIEEEDC1A.kf`  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0.1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC1A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0.33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC1A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.ta-valueRange

**Path:** `cim:ExcIEEEDC1A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,06.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tb-valueRange

**Path:** `cim:ExcIEEEDC1A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tc-valueRange

**Path:** `cim:ExcIEEEDC1A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.te-valueRange

**Path:** `cim:ExcIEEEDC1A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,46.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.tf-valueRange

**Path:** `cim:ExcIEEEDC1A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC1A.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC1A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.efd2-valueRange

**Path:** `cim:ExcIEEEDC2A.efd2`  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,29.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.ka-valueRange

**Path:** `cim:ExcIEEEDC2A.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 300.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.kf-valueRange

**Path:** `cim:ExcIEEEDC2A.kf`  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC2A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,279.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC2A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,117.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.ta-valueRange

**Path:** `cim:ExcIEEEDC2A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tb-valueRange

**Path:** `cim:ExcIEEEDC2A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tc-valueRange

**Path:** `cim:ExcIEEEDC2A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.te-valueRange

**Path:** `cim:ExcIEEEDC2A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 1,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.tf-valueRange

**Path:** `cim:ExcIEEEDC2A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (> 0).  Typical value = 0,675.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC2A.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC2A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 3,375.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.efd2-valueRange

**Path:** `cim:ExcIEEEDC3A.efd2`  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 3,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.kv-valueRange

**Path:** `cim:ExcIEEEDC3A.kv`  
Fast raise/lower contact setting (K<sub>V</sub>) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.seefd1-valueRange

**Path:** `cim:ExcIEEEDC3A.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,267.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.seefd2-valueRange

**Path:** `cim:ExcIEEEDC3A.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,068.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.te-valueRange

**Path:** `cim:ExcIEEEDC3A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.trh-valueRange

**Path:** `cim:ExcIEEEDC3A.trh`  
Rheostat travel time (T<sub>RH</sub>) (> 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.vrmax-valueRange

**Path:** `cim:ExcIEEEDC3A.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC3A.vrmin-valueRange

**Path:** `cim:ExcIEEEDC3A.vrmin`  
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
Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>) (> 0).  Typical value = 1,75.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.efd2-valueRange

**Path:** `cim:ExcIEEEDC4B.efd2`  
Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>) (> 0).  Typical value = 2,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ka-valueRange

**Path:** `cim:ExcIEEEDC4B.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kd-valueRange

**Path:** `cim:ExcIEEEDC4B.kd`  
Regulator derivative gain (K<sub>D</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kf-valueRange

**Path:** `cim:ExcIEEEDC4B.kf`  
Excitation control system stabilizer gain (K<sub>F</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ki-valueRange

**Path:** `cim:ExcIEEEDC4B.ki`  
Regulator integral gain (K<sub>I</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.kp-valueRange

**Path:** `cim:ExcIEEEDC4B.kp`  
Regulator proportional gain (K<sub>P</sub>) (>= 0).  Typical value = 20.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.seefd1-valueRange

**Path:** `cim:ExcIEEEDC4B.seefd1`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.seefd2-valueRange

**Path:** `cim:ExcIEEEDC4B.seefd2`  
Exciter saturation function value at the corresponding exciter voltage, E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]) (>= 0).  Typical value = 0,27.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.ta-valueRange

**Path:** `cim:ExcIEEEDC4B.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.te-valueRange

**Path:** `cim:ExcIEEEDC4B.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.tf-valueRange

**Path:** `cim:ExcIEEEDC4B.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.vemin-valueRange

**Path:** `cim:ExcIEEEDC4B.vemin`  
Minimum exciter voltage output (V<sub>EMIN</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEDC4B.vrmin-valueRangePair

**Path:** `cim:ExcIEEEDC4B.vrmin`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 190.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.kc-valueRange

**Path:** `cim:ExcIEEEST1A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.kf-valueRange

**Path:** `cim:ExcIEEEST1A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.ta-valueRange

**Path:** `cim:ExcIEEEST1A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tb-valueRange

**Path:** `cim:ExcIEEEST1A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tb1-valueRange

**Path:** `cim:ExcIEEEST1A.tb1`  
Voltage regulator time constant (T<sub>B1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tc-valueRange

**Path:** `cim:ExcIEEEST1A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tc1-valueRange

**Path:** `cim:ExcIEEEST1A.tc1`  
Voltage regulator time constant (T<sub>C1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.tf-valueRange

**Path:** `cim:ExcIEEEST1A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vamax-valueRange

**Path:** `cim:ExcIEEEST1A.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vamin-valueRange

**Path:** `cim:ExcIEEEST1A.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -14,5.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vimax-valueRange

**Path:** `cim:ExcIEEEST1A.vimax`  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vimin-valueRange

**Path:** `cim:ExcIEEEST1A.vimin`  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vrmax-valueRange

**Path:** `cim:ExcIEEEST1A.vrmax`  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 7,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST1A.vrmin-valueRange

**Path:** `cim:ExcIEEEST1A.vrmin`  
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
Maximum field voltage (E<sub>FDMax</sub>) (>= 0).  Typical value = 99.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ka-valueRange

**Path:** `cim:ExcIEEEST2A.ka`  
Voltage regulator gain (K<sub>A</sub>) (> 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kc-valueRange

**Path:** `cim:ExcIEEEST2A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 1,82.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kf-valueRange

**Path:** `cim:ExcIEEEST2A.kf`  
Excitation control system stabilizer gains (K<sub>F</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ki-valueRange

**Path:** `cim:ExcIEEEST2A.ki`  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.kp-valueRange

**Path:** `cim:ExcIEEEST2A.kp`  
Potential circuit gain coefficient (K<sub>P</sub>) (>= 0).  Typical value = 4,88.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.ta-valueRange

**Path:** `cim:ExcIEEEST2A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (> 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.te-valueRange

**Path:** `cim:ExcIEEEST2A.te`  
Exciter time constant, integration rate associated with exciter control (T<sub>E</sub>) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.tf-valueRange

**Path:** `cim:ExcIEEEST2A.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.vrmax-valueRange

**Path:** `cim:ExcIEEEST2A.vrmax`  
Maximum voltage regulator outputs (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST2A.vrmin-valueRange

**Path:** `cim:ExcIEEEST2A.vrmin`  
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
Voltage regulator gain (K<sub>A</sub>) (> 0). This is parameter K in the IEEE standard. Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kc-valueRange

**Path:** `cim:ExcIEEEST3A.kc`  
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kg-valueRange

**Path:** `cim:ExcIEEEST3A.kg`  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.ki-valueRange

**Path:** `cim:ExcIEEEST3A.ki`  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.km-valueRange

**Path:** `cim:ExcIEEEST3A.km`  
Forward gain constant of the inner loop field regulator (K<sub>M</sub>) (> 0).  Typical value = 7,93.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.kp-valueRange

**Path:** `cim:ExcIEEEST3A.kp`  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 6,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.ta-valueRange

**Path:** `cim:ExcIEEEST3A.ta`  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tb-valueRange

**Path:** `cim:ExcIEEEST3A.tb`  
Voltage regulator time constant (T<sub>B</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tc-valueRange

**Path:** `cim:ExcIEEEST3A.tc`  
Voltage regulator time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.tm-valueRange

**Path:** `cim:ExcIEEEST3A.tm`  
Forward time constant of inner loop field regulator (T<sub>M</sub>) (> 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vbmax-valueRange

**Path:** `cim:ExcIEEEST3A.vbmax`  
Maximum excitation voltage (V<sub>BMax</sub>) (> 0).  Typical value = 6,9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vgmax-valueRange

**Path:** `cim:ExcIEEEST3A.vgmax`  
Maximum inner loop feedback voltage (V<sub>GMax</sub>) (>= 0).  Typical value = 5,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vimax-valueRange

**Path:** `cim:ExcIEEEST3A.vimax`  
Maximum voltage regulator input limit (V<sub>IMAX</sub>) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vimin-valueRange

**Path:** `cim:ExcIEEEST3A.vimin`  
Minimum voltage regulator input limit (V<sub>IMIN</sub>) (< 0).  Typical value = -0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vmmax-valueRange

**Path:** `cim:ExcIEEEST3A.vmmax`  
Maximum inner loop output (V<sub>MMax</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vmmin-valueRange

**Path:** `cim:ExcIEEEST3A.vmmin`  
Minimum inner loop output (V<sub>MMin</sub>) (<= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vrmax-valueRange

**Path:** `cim:ExcIEEEST3A.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.vrmin-valueRange

**Path:** `cim:ExcIEEEST3A.vrmin`  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST3A.xl-valueRange

**Path:** `cim:ExcIEEEST3A.xl`  
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
Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>) (>= 0). Typical value = 0,113.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.kg-valueRange

**Path:** `cim:ExcIEEEST4B.kg`  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.ki-valueRange

**Path:** `cim:ExcIEEEST4B.ki`  
Potential circuit gain coefficient (K<sub>I</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.kp-valueRange

**Path:** `cim:ExcIEEEST4B.kp`  
Potential circuit gain coefficient (K<sub>P</sub>) (> 0).  Typical value = 9,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.ta-valueRange

**Path:** `cim:ExcIEEEST4B.ta`  
Voltage regulator time constant (T<sub>A</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vbmax-valueRange

**Path:** `cim:ExcIEEEST4B.vbmax`  
Maximum excitation voltage (V<sub>BMax</sub>) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vmmin-valueRangePair

**Path:** `cim:ExcIEEEST4B.vmmin`  
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
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.vrmin-valueRange

**Path:** `cim:ExcIEEEST4B.vrmin`  
Minimum voltage regulator output (V<sub>RMIN</sub>) (< 0).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST4B.xl-valueRange

**Path:** `cim:ExcIEEEST4B.xl`  
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
Rectifier regulation factor (K<sub>C</sub>) (>= 0).  Typical value = 0,004.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.kr-valueRange

**Path:** `cim:ExcIEEEST5B.kr`  
Regulator gain (K<sub>R</sub>) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.t1-valueRange

**Path:** `cim:ExcIEEEST5B.t1`  
Firing circuit time constant (T1) (>= 0).  Typical value = 0,004.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tb1-valueRange

**Path:** `cim:ExcIEEEST5B.tb1`  
Regulator lag time constant (T<sub>B1</sub>) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tb2-valueRange

**Path:** `cim:ExcIEEEST5B.tb2`  
Regulator lag time constant (T<sub>B2</sub>) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tc1-valueRange

**Path:** `cim:ExcIEEEST5B.tc1`  
Regulator lead time constant (T<sub>C1</sub>) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tc2-valueRange

**Path:** `cim:ExcIEEEST5B.tc2`  
Regulator lead time constant (T<sub>C2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tob1-valueRange

**Path:** `cim:ExcIEEEST5B.tob1`  
OEL lag time constant (T<sub>OB1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tob2-valueRange

**Path:** `cim:ExcIEEEST5B.tob2`  
OEL lag time constant (T<sub>OB2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.toc1-valueRange

**Path:** `cim:ExcIEEEST5B.toc1`  
OEL lead time constant (T<sub>OC1</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.toc2-valueRange

**Path:** `cim:ExcIEEEST5B.toc2`  
OEL lead time constant (T<sub>OC2</sub>) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tub1-valueRange

**Path:** `cim:ExcIEEEST5B.tub1`  
UEL lag time constant (T<sub>UB1</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tub2-valueRange

**Path:** `cim:ExcIEEEST5B.tub2`  
UEL lag time constant (T<sub>UB2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tuc1-valueRange

**Path:** `cim:ExcIEEEST5B.tuc1`  
UEL lead time constant (T<sub>UC1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.tuc2-valueRange

**Path:** `cim:ExcIEEEST5B.tuc2`  
UEL lead time constant (T<sub>UC2</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.vrmax-valueRange

**Path:** `cim:ExcIEEEST5B.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST5B.vrmin-valueRange

**Path:** `cim:ExcIEEEST5B.vrmin`  
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
Exciter output current limit reference (I<sub>LR</sub>) (> 0).  Typical value = 4,164.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kci-valueRange

**Path:** `cim:ExcIEEEST6B.kci`  
Exciter output current limit adjustment (K<sub>CI</sub>) (> 0).  Typical value = 1,0577.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kg-valueRange

**Path:** `cim:ExcIEEEST6B.kg`  
Feedback gain constant of the inner loop field regulator (K<sub>G</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kia-valueRange

**Path:** `cim:ExcIEEEST6B.kia`  
Voltage regulator integral gain (K<sub>IA</sub>) (> 0).  Typical value = 45,094.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.klr-valueRange

**Path:** `cim:ExcIEEEST6B.klr`  
Exciter output current limiter gain (K<sub>LR</sub>) (> 0).  Typical value = 17,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.kpa-valueRange

**Path:** `cim:ExcIEEEST6B.kpa`  
Voltage regulator proportional gain (<u>K</u><u><sub>PA</sub></u>) (> 0).  Typical value = 18,038.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.tg-valueRange

**Path:** `cim:ExcIEEEST6B.tg`  
Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vamax-valueRange

**Path:** `cim:ExcIEEEST6B.vamax`  
Maximum voltage regulator output (V<sub>AMAX</sub>) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vamin-valueRange

**Path:** `cim:ExcIEEEST6B.vamin`  
Minimum voltage regulator output (V<sub>AMIN</sub>) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vrmax-valueRange

**Path:** `cim:ExcIEEEST6B.vrmax`  
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST6B.vrmin-valueRange

**Path:** `cim:ExcIEEEST6B.vrmin`  
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
High-value gate feedback gain (K<sub>H</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kia-valueRange

**Path:** `cim:ExcIEEEST7B.kia`  
Voltage regulator integral gain (K<sub>IA</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kl-valueRange

**Path:** `cim:ExcIEEEST7B.kl`  
Low-value gate feedback gain (K<sub>L</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.kpa-valueRange

**Path:** `cim:ExcIEEEST7B.kpa`  
Voltage regulator proportional gain (K<sub>PA</sub>) (> 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tb-valueRange

**Path:** `cim:ExcIEEEST7B.tb`  
Regulator lag time constant (T<sub>B</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tc-valueRange

**Path:** `cim:ExcIEEEST7B.tc`  
Regulator lead time constant (T<sub>C</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tf-valueRange

**Path:** `cim:ExcIEEEST7B.tf`  
Excitation control system stabilizer time constant (T<sub>F</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tg-valueRange

**Path:** `cim:ExcIEEEST7B.tg`  
Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>) (>= 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.tia-valueRange

**Path:** `cim:ExcIEEEST7B.tia`  
Feedback time constant (T<sub>IA</sub>) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vmax-valueRange

**Path:** `cim:ExcIEEEST7B.vmax`  
Maximum voltage reference signal (V<sub>MAX</sub>) (> 0 and > ExcIEEEST7B.vmin).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vmin-valueRangePair

**Path:** `cim:ExcIEEEST7B.vmin`  
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
Maximum voltage regulator output (V<sub>RMAX</sub>) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcIEEEST7B.vrmin-valueRange

**Path:** `cim:ExcIEEEST7B.vrmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 210.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.kf-valueRange

**Path:** `cim:ExcNI.kf`  
Excitation control system stabilizer gain (Kf) (> 0).  Typical value 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.r-valueRange

**Path:** `cim:ExcNI.r`  
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
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tf1-valueRange

**Path:** `cim:ExcNI.tf1`  
Excitation control system stabilizer time constant (Tf1) (> 0). Typical value = 1,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tf2-valueRange

**Path:** `cim:ExcNI.tf2`  
Excitation control system stabilizer time constant (Tf2) (> 0). Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.tr-valueRange

**Path:** `cim:ExcNI.tr`  
Time constant (Tr) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcNI.vrmin-valueRangePair

**Path:** `cim:ExcNI.vrmin`  
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
Time constant (T<sub>1</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t2-valueRange

**Path:** `cim:ExcOEX3T.t2`  
Time constant (T<sub>2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t3-valueRange

**Path:** `cim:ExcOEX3T.t3`  
Time constant (T<sub>3</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t4-valueRange

**Path:** `cim:ExcOEX3T.t4`  
Time constant (T<sub>4</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t5-valueRange

**Path:** `cim:ExcOEX3T.t5`  
Time constant (T<sub>5</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.t6-valueRange

**Path:** `cim:ExcOEX3T.t6`  
Time constant (T<sub>6</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.te-valueRange

**Path:** `cim:ExcOEX3T.te`  
Time constant (T<sub>E</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.tf-valueRange

**Path:** `cim:ExcOEX3T.tf`  
Time constant (T<sub>F</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcOEX3T.vrmin-valueRangePair

**Path:** `cim:ExcOEX3T.vrmin`  
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
Exciter minimum limit (E<sub>fdmin</sub>) (< ExcPIC.efdmax).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcPIC.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcPIC.efdmax` 

### dy302c:ExcPIC.ta1-valueRange

**Path:** `cim:ExcPIC.ta1`  
PI controller time constant (T<sub>a1</sub>) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta2-valueRange

**Path:** `cim:ExcPIC.ta2`  
Voltage regulator time constant (T<sub>a2</sub>) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta3-valueRange

**Path:** `cim:ExcPIC.ta3`  
Lead time constant (T<sub>a3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.ta4-valueRange

**Path:** `cim:ExcPIC.ta4`  
Lag time constant (T<sub>a4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.te-valueRange

**Path:** `cim:ExcPIC.te`  
Exciter time constant (T<sub>e</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.tf1-valueRange

**Path:** `cim:ExcPIC.tf1`  
Rate feedback time constant (T<sub>f1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.tf2-valueRange

**Path:** `cim:ExcPIC.tf2`  
Rate feedback lag time constant (T<sub>f2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcPIC.vrmin-valueRangePair

**Path:** `cim:ExcPIC.vrmin`  
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
Rate feedback gain (Kf) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.ta-valueRange

**Path:** `cim:ExcREXS.ta`  
Voltage regulator time constant (Ta) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tb1-valueRange

**Path:** `cim:ExcREXS.tb1`  
Lag time constant (Tb1) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tb2-valueRange

**Path:** `cim:ExcREXS.tb2`  
Lag time constant (Tb2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tc1-valueRange

**Path:** `cim:ExcREXS.tc1`  
Lead time constant (Tc1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tc2-valueRange

**Path:** `cim:ExcREXS.tc2`  
Lead time constant (Tc2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.te-valueRange

**Path:** `cim:ExcREXS.te`  
Exciter field time constant (Te) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf-valueRange

**Path:** `cim:ExcREXS.tf`  
Rate feedback time constant (Tf) (>= 0).  If = 0, the feedback path is not used.  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf1-valueRange

**Path:** `cim:ExcREXS.tf1`  
Feedback lead time constant (Tf1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tf2-valueRange

**Path:** `cim:ExcREXS.tf2`  
Feedback lag time constant (Tf2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.tp-valueRange

**Path:** `cim:ExcREXS.tp`  
Field current bridge time constant (Tp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcREXS.vfmin-valueRangePair

**Path:** `cim:ExcREXS.vfmin`  
Minimum exciter field current (Vfmin) (< ExcREXS.vfmax).  Typical value = -20.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcREXS.vfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcREXS.vfmax` 

### dy302c:ExcREXS.vrmin-valueRangePair

**Path:** `cim:ExcREXS.vrmin`  
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
Voltage input time constant (MESU) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.t4m-valueRange

**Path:** `cim:ExcRQB.t4m`  
Input time constant (T4M) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.tc-valueRange

**Path:** `cim:ExcRQB.tc`  
Lead lag time constant (TC) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.te-valueRange

**Path:** `cim:ExcRQB.te`  
Lead lag time constant (TE) (>= 0).  Typical value = 0,22.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.tf-valueRange

**Path:** `cim:ExcRQB.tf`  
Exciter time constant (TF) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcRQB.ucmin-valueRangePair

**Path:** `cim:ExcRQB.ucmin`  
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
Minimum field voltage output (Emin) (< ExcSCRX.emax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSCRX.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSCRX.emax` 

### dy302c:ExcSCRX.k-valueRange

**Path:** `cim:ExcSCRX.k`  
Gain (K) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSCRX.tb-valueRange

**Path:** `cim:ExcSCRX.tb`  
Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSCRX.te-valueRange

**Path:** `cim:ExcSCRX.te`  
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
Field voltage clipping minimum limit (Efdmin) (< ExcSEXS.efdmax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSEXS.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSEXS.efdmax` 

### dy302c:ExcSEXS.emin-valueRangePair

**Path:** `cim:ExcSEXS.emin`  
Minimum field voltage output (Emin) (< ExcSEXS.emax).  Typical value = -5.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSEXS.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSEXS.emax` 

### dy302c:ExcSEXS.k-valueRange

**Path:** `cim:ExcSEXS.k`  
Gain (K) (> 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.tb-valueRange

**Path:** `cim:ExcSEXS.tb`  
Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.tc-valueRange

**Path:** `cim:ExcSEXS.tc`  
PI controller phase lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSEXS.te-valueRange

**Path:** `cim:ExcSEXS.te`  
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
Field voltage clipping lower level limit (Efdmin) (< ExcSK.efdmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.efdmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.efdmax` 

### dy302c:ExcSK.emin-valueRangePair

**Path:** `cim:ExcSK.emin`  
Minimum field voltage output (Emin) (< ExcSK.emax).  Typical value = -20.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.emax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.emax` 

### dy302c:ExcSK.sbase-valueRange

**Path:** `cim:ExcSK.sbase`  
Apparent power of the unit (Sbase) (> 0).  Unit = MVA.  Typical value = 259.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tc-valueRange

**Path:** `cim:ExcSK.tc`  
PI controller phase lead time constant (Tc) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.te-valueRange

**Path:** `cim:ExcSK.te`  
Time constant of gain block (Te) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.ti-valueRange

**Path:** `cim:ExcSK.ti`  
PI controller phase lead time constant (Ti) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tp-valueRange

**Path:** `cim:ExcSK.tp`  
Time constant (Tp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.tr-valueRange

**Path:** `cim:ExcSK.tr`  
Voltage transducer time constant (Tr) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcSK.uimin-valueRangePair

**Path:** `cim:ExcSK.uimin`  
Minimum error (UImin) (< ExcSK.uimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.uimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.uimax` 

### dy302c:ExcSK.urmin-valueRangePair

**Path:** `cim:ExcSK.urmin`  
Minimum controller output (URmin) (< ExcSK.urmax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcSK.urmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcSK.urmax` 

### dy302c:ExcSK.vtmin-valueRangePair

**Path:** `cim:ExcSK.vtmin`  
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
Voltage regulator gain (Ka) (> 0).  Typical value = 190.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.kc-valueRange

**Path:** `cim:ExcST1A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.kf-valueRange

**Path:** `cim:ExcST1A.kf`  
Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.ta-valueRange

**Path:** `cim:ExcST1A.ta`  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tb-valueRange

**Path:** `cim:ExcST1A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tb1-valueRange

**Path:** `cim:ExcST1A.tb1`  
Voltage regulator time constant (Tb1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tc-valueRange

**Path:** `cim:ExcST1A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tc1-valueRange

**Path:** `cim:ExcST1A.tc1`  
Voltage regulator time constant (Tc1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.tf-valueRange

**Path:** `cim:ExcST1A.tf`  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vamax-valueRange

**Path:** `cim:ExcST1A.vamax`  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vamin-valueRange

**Path:** `cim:ExcST1A.vamin`  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vimax-valueRange

**Path:** `cim:ExcST1A.vimax`  
Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 999.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vimin-valueRange

**Path:** `cim:ExcST1A.vimin`  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -999.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vrmax-valueRange

**Path:** `cim:ExcST1A.vrmax`  
Maximum voltage regulator outputs (Vrmax) (> 0) .  Typical value = 7,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST1A.vrmin-valueRange

**Path:** `cim:ExcST1A.vrmin`  
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
Maximum field voltage (Efdmax) (>= 0).  Typical value = 99.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ka-valueRange

**Path:** `cim:ExcST2A.ka`  
Voltage regulator gain (Ka) (> 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kc-valueRange

**Path:** `cim:ExcST2A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 1,82.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kf-valueRange

**Path:** `cim:ExcST2A.kf`  
Excitation control system stabilizer gains (kf) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ki-valueRange

**Path:** `cim:ExcST2A.ki`  
Potential circuit gain coefficient (K<sub>i</sub>) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.kp-valueRange

**Path:** `cim:ExcST2A.kp`  
Potential circuit gain coefficient (K<sub>p</sub>) (>= 0).  Typical value = 4,88.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.ta-valueRange

**Path:** `cim:ExcST2A.ta`  
Voltage regulator time constant (Ta) (> 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tb-valueRange

**Path:** `cim:ExcST2A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tc-valueRange

**Path:** `cim:ExcST2A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.te-valueRange

**Path:** `cim:ExcST2A.te`  
Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.tf-valueRange

**Path:** `cim:ExcST2A.tf`  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.vrmax-valueRange

**Path:** `cim:ExcST2A.vrmax`  
Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST2A.vrmin-valueRange

**Path:** `cim:ExcST2A.vrmin`  
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
Maximum AVR output (Efdmax) (>= 0).  Typical value = 6,9.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kc-valueRange

**Path:** `cim:ExcST3A.kc`  
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kg-valueRange

**Path:** `cim:ExcST3A.kg`  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.ki-valueRange

**Path:** `cim:ExcST3A.ki`  
Potential circuit gain coefficient (K<sub>i</sub>) (>= 0).  Typical value = 4,83.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kj-valueRange

**Path:** `cim:ExcST3A.kj`  
AVR gain (Kj) (> 0).  Typical value = 200.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.km-valueRange

**Path:** `cim:ExcST3A.km`  
Forward gain constant of the inner loop field regulator (Km) (> 0).  Typical value = 7,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.kp-valueRange

**Path:** `cim:ExcST3A.kp`  
Potential source gain (K<sub>p</sub>) (> 0).  Typical value = 4,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tb-valueRange

**Path:** `cim:ExcST3A.tb`  
Voltage regulator time constant (Tb) (>= 0).  Typical value = 6,67.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tc-valueRange

**Path:** `cim:ExcST3A.tc`  
Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.tm-valueRange

**Path:** `cim:ExcST3A.tm`  
Forward time constant of inner loop field regulator (Tm) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vbmax-valueRange

**Path:** `cim:ExcST3A.vbmax`  
Maximum excitation voltage (Vbmax) (> 0).  Typical value = 8,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vgmax-valueRange

**Path:** `cim:ExcST3A.vgmax`  
Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 6,53.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vimax-valueRange

**Path:** `cim:ExcST3A.vimax`  
Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vimin-valueRange

**Path:** `cim:ExcST3A.vimin`  
Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vrmax-valueRange

**Path:** `cim:ExcST3A.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.vrmin-valueRange

**Path:** `cim:ExcST3A.vrmin`  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST3A.xl-valueRange

**Path:** `cim:ExcST3A.xl`  
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
Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,113.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.kg-valueRange

**Path:** `cim:ExcST4B.kg`  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0). Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.ki-valueRange

**Path:** `cim:ExcST4B.ki`  
Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.kp-valueRange

**Path:** `cim:ExcST4B.kp`  
Potential circuit gain coefficient (Kp) (> 0).  Typical value = 9,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.ta-valueRange

**Path:** `cim:ExcST4B.ta`  
Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vbmax-valueRange

**Path:** `cim:ExcST4B.vbmax`  
Maximum excitation voltage (Vbmax) (> 0).  Typical value = 11,63.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vgmax-valueRange

**Path:** `cim:ExcST4B.vgmax`  
Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 5,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vmmin-valueRangePair

**Path:** `cim:ExcST4B.vmmin`  
Minimum inner loop output (Vmmin) (< ExcST4B.vmmax).  Typical value = -99.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcST4B.vmmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcST4B.vmmax` 

### dy302c:ExcST4B.vrmax-valueRange

**Path:** `cim:ExcST4B.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.vrmin-valueRange

**Path:** `cim:ExcST4B.vrmin`  
Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -0,87.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST4B.xl-valueRange

**Path:** `cim:ExcST4B.xl`  
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
Exciter output current limit reference (Ilr) (> 0).  Typical value = 4,164.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kcl-valueRange

**Path:** `cim:ExcST6B.kcl`  
Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 1,0577.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kg-valueRange

**Path:** `cim:ExcST6B.kg`  
Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kia-valueRange

**Path:** `cim:ExcST6B.kia`  
Voltage regulator integral gain (Kia) (> 0).  Typical value = 45,094.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.klr-valueRange

**Path:** `cim:ExcST6B.klr`  
Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 17,33.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.kpa-valueRange

**Path:** `cim:ExcST6B.kpa`  
Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 18,038.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.tg-valueRange

**Path:** `cim:ExcST6B.tg`  
Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.ts-valueRange

**Path:** `cim:ExcST6B.ts`  
Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.tvd-valueRange

**Path:** `cim:ExcST6B.tvd`  
Voltage regulator derivative gain (Tvd) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vamax-valueRange

**Path:** `cim:ExcST6B.vamax`  
Maximum voltage regulator output (Vamax) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vamin-valueRange

**Path:** `cim:ExcST6B.vamin`  
Minimum voltage regulator output (Vamin) (< 0).  Typical value = -3,85.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vimin-valueRangePair

**Path:** `cim:ExcST6B.vimin`  
Minimum voltage regulator input limit (Vimin) (< ExcST6B.vimax).  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than ExcST6B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ExcST6B.vimax` 

### dy302c:ExcST6B.vrmax-valueRange

**Path:** `cim:ExcST6B.vrmax`  
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 4,81.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST6B.vrmin-valueRange

**Path:** `cim:ExcST6B.vrmin`  
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
High-value gate feedback gain (Kh) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kia-valueRange

**Path:** `cim:ExcST7B.kia`  
Voltage regulator integral gain (Kia) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kl-valueRange

**Path:** `cim:ExcST7B.kl`  
Low-value gate feedback gain (Kl) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.kpa-valueRange

**Path:** `cim:ExcST7B.kpa`  
Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tb-valueRange

**Path:** `cim:ExcST7B.tb`  
Regulator lag time constant (Tb) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tc-valueRange

**Path:** `cim:ExcST7B.tc`  
Regulator lead time constant (Tc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tf-valueRange

**Path:** `cim:ExcST7B.tf`  
Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tg-valueRange

**Path:** `cim:ExcST7B.tg`  
Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.tia-valueRange

**Path:** `cim:ExcST7B.tia`  
Feedback time constant (Tia) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.ts-valueRange

**Path:** `cim:ExcST7B.ts`  
Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vmax-valueRange

**Path:** `cim:ExcST7B.vmax`  
Maximum voltage reference signal (Vmax) (> 0 and > ExcST7B.vmin)).  Typical value = 1,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vmin-valueRangePair

**Path:** `cim:ExcST7B.vmin`  
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
Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:ExcST7B.vrmin-valueRange

**Path:** `cim:ExcST7B.vrmin`  
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
Turbine gain (Kturb) (> 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.minerr-valueRangePair

**Path:** `cim:GovCT1.minerr`  
Minimum value for speed error signal (minerr) (< GovCT1.maxerr).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT1.maxerr."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT1.maxerr` 

### dy302c:GovCT1.mwbase-valueRange

**Path:** `cim:GovCT1.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.ta-valueRange

**Path:** `cim:GovCT1.ta`  
Acceleration limiter time constant (Ta) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tact-valueRange

**Path:** `cim:GovCT1.tact`  
Actuator time constant (Tact) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tb-valueRange

**Path:** `cim:GovCT1.tb`  
Turbine lag time constant (Tb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tc-valueRange

**Path:** `cim:GovCT1.tc`  
Turbine lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tdgov-valueRange

**Path:** `cim:GovCT1.tdgov`  
Governor derivative controller time constant (Tdgov) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.teng-valueRange

**Path:** `cim:GovCT1.teng`  
Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng) (>= 0).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tfload-valueRange

**Path:** `cim:GovCT1.tfload`  
Load-limiter time constant (Tfload) (> 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tpelec-valueRange

**Path:** `cim:GovCT1.tpelec`  
Electrical power transducer time constant (Tpelec) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tsa-valueRange

**Path:** `cim:GovCT1.tsa`  
Temperature detection lead time constant (Tsa) (>= 0).  Typical value = 4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.tsb-valueRange

**Path:** `cim:GovCT1.tsb`  
Temperature detection lag time constant (Tsb) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT1.vmin-valueRangePair

**Path:** `cim:GovCT1.vmin`  
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
Minimum value for speed error signal (Minerr) (< GovCT2.maxerr).  Typical value = -1.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovCT2.maxerr."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovCT2.maxerr` 

### dy302c:GovCT2.mwbase-valueRange

**Path:** `cim:GovCT2.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.ta-valueRange

**Path:** `cim:GovCT2.ta`  
Acceleration limiter time constant (Ta) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tact-valueRange

**Path:** `cim:GovCT2.tact`  
Actuator time constant (Tact) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tb-valueRange

**Path:** `cim:GovCT2.tb`  
Turbine lag time constant (Tb) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tc-valueRange

**Path:** `cim:GovCT2.tc`  
Turbine lead time constant (Tc) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tdgov-valueRange

**Path:** `cim:GovCT2.tdgov`  
Governor derivative controller time constant (Tdgov) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.teng-valueRange

**Path:** `cim:GovCT2.teng`  
Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng) (>= 0).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tfload-valueRange

**Path:** `cim:GovCT2.tfload`  
Load limiter time constant (Tfload) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tpelec-valueRange

**Path:** `cim:GovCT2.tpelec`  
Electrical power transducer time constant (Tpelec) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tsa-valueRange

**Path:** `cim:GovCT2.tsa`  
Temperature detection lead time constant (Tsa) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.tsb-valueRange

**Path:** `cim:GovCT2.tsb`  
Temperature detection lag time constant (Tsb) (>= 0).  Typical value = 50.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovCT2.vmin-valueRangePair

**Path:** `cim:GovCT2.vmin`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.r-valueRange

**Path:** `cim:GovGAST.r`  
Permanent droop (R) (>0). Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t1-valueRange

**Path:** `cim:GovGAST.t1`  
Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t2-valueRange

**Path:** `cim:GovGAST.t2`  
Turbine power time constant (T2) (>= 0).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power turbine of an aero-derivative unit, for example.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.t3-valueRange

**Path:** `cim:GovGAST.t3`  
Turbine exhaust temperature time constant (T3) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST.vmin-valueRangePair

**Path:** `cim:GovGAST.vmin`  
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
Turbine power time constant denominator scale factor (b) (>0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.mwbase-valueRange

**Path:** `cim:GovGAST1.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.r-valueRange

**Path:** `cim:GovGAST1.r`  
Permanent droop (R) (>0).  Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t1-valueRange

**Path:** `cim:GovGAST1.t1`  
Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t2-valueRange

**Path:** `cim:GovGAST1.t2`  
Turbine power time constant (T2) (>= 0). T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t3-valueRange

**Path:** `cim:GovGAST1.t3`  
Turbine exhaust temperature time constant (T3) (>= 0).  T3 represents delay in the exhaust temperature and load limiting system. Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t4-valueRange

**Path:** `cim:GovGAST1.t4`  
Governor lead time constant (T4) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.t5-valueRange

**Path:** `cim:GovGAST1.t5`  
Governor lag time constant (T5) (>= 0).  If = 0, entire gain and lead-lag block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.tltr-valueRange

**Path:** `cim:GovGAST1.tltr`  
Valve position averaging time constant (Tltr) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST1.vmin-valueRangePair

**Path:** `cim:GovGAST1.vmin`  
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
Combustion reaction time delay (Ecr) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.etd-valueRange

**Path:** `cim:GovGAST2.etd`  
Turbine and exhaust delay (Etd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.mwbase-valueRange

**Path:** `cim:GovGAST2.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t-valueRange

**Path:** `cim:GovGAST2.t`  
Fuel control time constant (T) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t3-valueRange

**Path:** `cim:GovGAST2.t3`  
Radiation shield time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t4-valueRange

**Path:** `cim:GovGAST2.t4`  
Thermocouple time constant (T4) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.t5-valueRange

**Path:** `cim:GovGAST2.t5`  
Temperature control time constant (T5) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tcd-valueRange

**Path:** `cim:GovGAST2.tcd`  
Compressor discharge time constant (Tcd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tf-valueRange

**Path:** `cim:GovGAST2.tf`  
Fuel system time constant (Tf) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.tmin-valueRangePair

**Path:** `cim:GovGAST2.tmin`  
Minimum turbine limit (Tmin) (< GovGAST2.tmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGAST2.tmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGAST2.tmax` 

### dy302c:GovGAST2.tt-valueRange

**Path:** `cim:GovGAST2.tt`  
Temperature controller integration rate (Tt) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.x-valueRange

**Path:** `cim:GovGAST2.x`  
Governor lead time constant (X) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST2.y-valueRange

**Path:** `cim:GovGAST2.y`  
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
Fuel control time constant (Tac) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tc-valueRange

**Path:** `cim:GovGAST3.tc`  
Compressor discharge volume time constant (Tc) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.td-valueRange

**Path:** `cim:GovGAST3.td`  
Temperature controller derivative gain (Td) (>= 0).  Typical value = 3,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tg-valueRange

**Path:** `cim:GovGAST3.tg`  
Time constant of speed governor (Tg) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.tsi-valueRange

**Path:** `cim:GovGAST3.tsi`  
Time constant of radiation shield (Tsi) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.ttc-valueRange

**Path:** `cim:GovGAST3.ttc`  
Time constant of thermocouple (Ttc) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST3.ty-valueRange

**Path:** `cim:GovGAST3.ty`  
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
Maximum gate opening velocity (TA) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tc-valueRange

**Path:** `cim:GovGAST4.tc`  
Maximum gate closing velocity (TC) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tcm-valueRange

**Path:** `cim:GovGAST4.tcm`  
Fuel control time constant (Tcm) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.tm-valueRange

**Path:** `cim:GovGAST4.tm`  
Compressor discharge volume time constant (Tm) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGAST4.ty-valueRange

**Path:** `cim:GovGAST4.ty`  
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
Combustion reaction time delay (Ecr) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.etd-valueRange

**Path:** `cim:GovGASTWD.etd`  
Turbine and exhaust delay (Etd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.kdroop-valueRange

**Path:** `cim:GovGASTWD.kdroop`  
(Kdroop) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.mwbase-valueRange

**Path:** `cim:GovGASTWD.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t-valueRange

**Path:** `cim:GovGASTWD.t`  
Fuel control time constant (T) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t3-valueRange

**Path:** `cim:GovGASTWD.t3`  
Radiation shield time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t4-valueRange

**Path:** `cim:GovGASTWD.t4`  
Thermocouple time constant (T4) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.t5-valueRange

**Path:** `cim:GovGASTWD.t5`  
Temperature control time constant (T5) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tcd-valueRange

**Path:** `cim:GovGASTWD.tcd`  
Compressor discharge time constant (Tcd) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.td-valueRange

**Path:** `cim:GovGASTWD.td`  
Power transducer time constant (Td) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tf-valueRange

**Path:** `cim:GovGASTWD.tf`  
Fuel system time constant (Tf) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovGASTWD.tmin-valueRangePair

**Path:** `cim:GovGASTWD.tmin`  
Minimum turbine limit (Tmin) (< GovGASTWD.tmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovGASTWD.tmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovGASTWD.tmax` 

### dy302c:GovGASTWD.tt-valueRange

**Path:** `cim:GovGASTWD.tt`  
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
Turbine gain (At) (> 0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.dturb-valueRange

**Path:** `cim:GovHydro1.dturb`  
Turbine damping factor (Dturb) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.gmin-valueRangePair

**Path:** `cim:GovHydro1.gmin`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.qnl-valueRange

**Path:** `cim:GovHydro1.qnl`  
No-load flow at nominal head (qnl) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.rperm-valueRange

**Path:** `cim:GovHydro1.rperm`  
Permanent droop (R) (> 0).  Typical value = 0,04.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.rperm-valueRangePair

**Path:** `cim:GovHydro1.rperm`  
Temporary droop (r) (GovHydro1.rtemp > GovHydro1.rperm).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value of GovHydro1.rperm is either equal to or greater than GovHydro1.rtemp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro1.rtemp` 

### dy302c:GovHydro1.tf-valueRange

**Path:** `cim:GovHydro1.tf`  
Filter time constant (Tf) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tg-valueRange

**Path:** `cim:GovHydro1.tg`  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tr-valueRange

**Path:** `cim:GovHydro1.tr`  
Washout time constant (Tr) (> 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.tw-valueRange

**Path:** `cim:GovHydro1.tw`  
Water inertia time constant (Tw) (> 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro1.velm-valueRange

**Path:** `cim:GovHydro1.velm`  
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
Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.mwbase-valueRange

**Path:** `cim:GovHydro2.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.pmin-valueRangePair

**Path:** `cim:GovHydro2.pmin`  
Minimum gate opening (Pmin) (< GovHydro2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro2.pmax` 

### dy302c:GovHydro2.tg-valueRange

**Path:** `cim:GovHydro2.tg`  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tp-valueRange

**Path:** `cim:GovHydro2.tp`  
Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tr-valueRange

**Path:** `cim:GovHydro2.tr`  
Dashpot time constant (Tr) (>= 0).  Typical value = 12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.tw-valueRange

**Path:** `cim:GovHydro2.tw`  
Water inertia time constant (Tw) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro2.uc-valueRange

**Path:** `cim:GovHydro2.uc`  
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
Turbine gain (At) (>0).  Typical value = 1,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.mwbase-valueRange

**Path:** `cim:GovHydro3.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.pmin-valueRangePair

**Path:** `cim:GovHydro3.pmin`  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydro3.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro3.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro3.pmax` 

### dy302c:GovHydro3.td-valueRange

**Path:** `cim:GovHydro3.td`  
Input filter time constant (Td) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tf-valueRange

**Path:** `cim:GovHydro3.tf`  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tp-valueRange

**Path:** `cim:GovHydro3.tp`  
Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tt-valueRange

**Path:** `cim:GovHydro3.tt`  
Power feedback time constant (Tt) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro3.tw-valueRange

**Path:** `cim:GovHydro3.tw`  
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
Minimum gate opening, PU of MWbase (Gmin) (< GovHydro4.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydro4.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydro4.gmax` 

### dy302c:GovHydro4.mwbase-valueRange

**Path:** `cim:GovHydro4.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.rperm-valueRange

**Path:** `cim:GovHydro4.rperm`  
Permanent droop (Rperm) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.rtemp-valueRange

**Path:** `cim:GovHydro4.rtemp`  
Temporary droop (Rtemp) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tblade-valueRange

**Path:** `cim:GovHydro4.tblade`  
Blade servo time constant (Tblade) (>= 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tg-valueRange

**Path:** `cim:GovHydro4.tg`  
Gate servo time constant (Tg) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tp-valueRange

**Path:** `cim:GovHydro4.tp`  
Pilot servo time constant (Tp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tr-valueRange

**Path:** `cim:GovHydro4.tr`  
Dashpot time constant (Tr) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydro4.tw-valueRange

**Path:** `cim:GovHydro4.tw`  
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
Minimum gate opening (Gmin) (< GovHydroDD.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroDD.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroDD.gmax` 

### dy302c:GovHydroDD.mwbase-valueRange

**Path:** `cim:GovHydroDD.mwbase`  
Base for power values (MWbase) (>0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.pmin-valueRangePair

**Path:** `cim:GovHydroDD.pmin`  
Minimum gate opening, PU of MWbase (Pmin) (> GovHydroDD.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroDD.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroDD.pmax` 

### dy302c:GovHydroDD.td-valueRange

**Path:** `cim:GovHydroDD.td`  
Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tf-valueRange

**Path:** `cim:GovHydroDD.tf`  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tp-valueRange

**Path:** `cim:GovHydroDD.tp`  
Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tt-valueRange

**Path:** `cim:GovHydroDD.tt`  
Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroDD.tturb-valueRange

**Path:** `cim:GovHydroDD.tturb`  
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
Derivative gain (Ta) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.td-valueRange

**Path:** `cim:GovHydroFrancis.td`  
Washout time constant (Td) (>= 0).  Typical value = 6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.ts-valueRange

**Path:** `cim:GovHydroFrancis.ts`  
Gate servo time constant (Ts) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.twnc-valueRange

**Path:** `cim:GovHydroFrancis.twnc`  
Water inertia time constant (Twnc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.twng-valueRange

**Path:** `cim:GovHydroFrancis.twng`  
Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.tx-valueRange

**Path:** `cim:GovHydroFrancis.tx`  
Derivative feedback gain (Tx) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroFrancis.valvmin-valueRangePair

**Path:** `cim:GovHydroFrancis.valvmin`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.pmin-valueRangePair

**Path:** `cim:GovHydroIEEE0.pmin`  
Gate minimum (Pmin) (< GovHydroIEEE.pmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroIEEE.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroIEEE.pmax` 

### dy302c:GovHydroIEEE0.t1-valueRange

**Path:** `cim:GovHydroIEEE0.t1`  
Governor lag time constant (T1) (>= 0).  Typical value = 0,25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t2-valueRange

**Path:** `cim:GovHydroIEEE0.t2`  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t3-valueRange

**Path:** `cim:GovHydroIEEE0.t3`  
Gate actuator time constant (T3) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE0.t4-valueRange

**Path:** `cim:GovHydroIEEE0.t4`  
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
Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.mwbase-valueRange

**Path:** `cim:GovHydroIEEE2.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.pmin-valueRangePair

**Path:** `cim:GovHydroIEEE2.pmin`  
Minimum gate opening (Pmin) (<GovHydroIEEE2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroIEEE2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroIEEE2.pmax` 

### dy302c:GovHydroIEEE2.tg-valueRange

**Path:** `cim:GovHydroIEEE2.tg`  
Gate servo time constant (Tg) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tp-valueRange

**Path:** `cim:GovHydroIEEE2.tp`  
Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tr-valueRange

**Path:** `cim:GovHydroIEEE2.tr`  
Dashpot time constant (Tr) (>= 0).  Typical value = 12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.tw-valueRange

**Path:** `cim:GovHydroIEEE2.tw`  
Water inertia time constant (Tw) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroIEEE2.uc-valueRange

**Path:** `cim:GovHydroIEEE2.uc`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.pmin-valueRangePair

**Path:** `cim:GovHydroPID.pmin`  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydroPID.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPID.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPID.pmax` 

### dy302c:GovHydroPID.td-valueRange

**Path:** `cim:GovHydroPID.td`  
Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tf-valueRange

**Path:** `cim:GovHydroPID.tf`  
Washout time constant (Tf) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tp-valueRange

**Path:** `cim:GovHydroPID.tp`  
Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tt-valueRange

**Path:** `cim:GovHydroPID.tt`  
Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID.tturb-valueRange

**Path:** `cim:GovHydroPID.tturb`  
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
Minimum gate opening (Gmin) (> GovHydroPID2.gmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroPID2.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroPID2.gmax` 

### dy302c:GovHydroPID2.mwbase-valueRange

**Path:** `cim:GovHydroPID2.mwbase`  
Base for power values (MWbase) (>0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.ta-valueRange

**Path:** `cim:GovHydroPID2.ta`  
Controller time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.tb-valueRange

**Path:** `cim:GovHydroPID2.tb`  
Gate servo time constant (Tb) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.treg-valueRange

**Path:** `cim:GovHydroPID2.treg`  
Speed detector time constant (Treg) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.tw-valueRange

**Path:** `cim:GovHydroPID2.tw`  
Water inertia time constant (Tw) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPID2.velmax-valueRangePair

**Path:** `cim:GovHydroPID2.velmax`  
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
Derivative gain (accelerometer time constant) (Ta) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.ts-valueRange

**Path:** `cim:GovHydroPelton.ts`  
Gate servo time constant (Ts) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.tv-valueRange

**Path:** `cim:GovHydroPelton.tv`  
Servomotor integrator time constant (Tv) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.twnc-valueRange

**Path:** `cim:GovHydroPelton.twnc`  
Water inertia time constant (Twnc) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.twng-valueRange

**Path:** `cim:GovHydroPelton.twng`  
Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.tx-valueRange

**Path:** `cim:GovHydroPelton.tx`  
Electronic integrator time constant (Tx) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroPelton.valvmin-valueRangePair

**Path:** `cim:GovHydroPelton.valvmin`  
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
Minimum governor output (Gmin) (< GovHydroR.gmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroR.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroR.gmax` 

### dy302c:GovHydroR.mwbase-valueRange

**Path:** `cim:GovHydroR.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.pmin-valueRangePair

**Path:** `cim:GovHydroR.pmin`  
Minimum gate opening, PU of MWbase (Pmin) (< GovHydroR.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroR.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroR.pmax` 

### dy302c:GovHydroR.t1-valueRange

**Path:** `cim:GovHydroR.t1`  
Lead time constant 1 (T1) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t2-valueRange

**Path:** `cim:GovHydroR.t2`  
Lag time constant 1 (T2) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t3-valueRange

**Path:** `cim:GovHydroR.t3`  
Lead time constant 2 (T3) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t4-valueRange

**Path:** `cim:GovHydroR.t4`  
Lag time constant 2 (T4) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t5-valueRange

**Path:** `cim:GovHydroR.t5`  
Lead time constant 3 (T5) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t6-valueRange

**Path:** `cim:GovHydroR.t6`  
Lag time constant 3 (T6) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t7-valueRange

**Path:** `cim:GovHydroR.t7`  
Lead time constant 4 (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.t8-valueRange

**Path:** `cim:GovHydroR.t8`  
Lag time constant 4 (T8) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.td-valueRange

**Path:** `cim:GovHydroR.td`  
Input filter time constant (Td) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tp-valueRange

**Path:** `cim:GovHydroR.tp`  
Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tt-valueRange

**Path:** `cim:GovHydroR.tt`  
Power feedback time constant (Tt) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroR.tw-valueRange

**Path:** `cim:GovHydroR.tw`  
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
Minimum gate position (Gmin) (< GovHydroWEH.gmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWEH.gmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWEH.gmax` 

### dy302c:GovHydroWEH.mwbase-valueRange

**Path:** `cim:GovHydroWEH.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.td-valueRange

**Path:** `cim:GovHydroWEH.td`  
Derivative controller time constant (Td) (>= 0).  Limits the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tdv-valueRange

**Path:** `cim:GovHydroWEH.tdv`  
Distributive valve time lag time constant (Tdv) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tg-valueRange

**Path:** `cim:GovHydroWEH.tg`  
Value to allow the distribution valve controller to advance beyond the gate movement rate limit (Tg) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tp-valueRange

**Path:** `cim:GovHydroWEH.tp`  
Pilot valve time lag time constant (Tp) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tpe-valueRange

**Path:** `cim:GovHydroWEH.tpe`  
Electrical power droop time constant (Tpe) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWEH.tw-valueRange

**Path:** `cim:GovHydroWEH.tw`  
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
Gate opening limit minimum (Gatmin) (< GovHydroWPID.gatmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWPID.gatmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWPID.gatmax` 

### dy302c:GovHydroWPID.mwbase-valueRange

**Path:** `cim:GovHydroWPID.mwbase`  
Base for power values  (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.pmin-valueRangePair

**Path:** `cim:GovHydroWPID.pmin`  
Minimum power output (Pmin) (< GovHydroWPID.pmax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovHydroWPID.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovHydroWPID.pmax` 

### dy302c:GovHydroWPID.ta-valueRange

**Path:** `cim:GovHydroWPID.ta`  
Controller time constant (Ta) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.tb-valueRange

**Path:** `cim:GovHydroWPID.tb`  
Gate servo time constant (Tb) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.treg-valueRange

**Path:** `cim:GovHydroWPID.treg`  
Speed detector time constant (Treg) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.tw-valueRange

**Path:** `cim:GovHydroWPID.tw`  
Water inertia time constant (Tw) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovHydroWPID.velmin-valueRangePair

**Path:** `cim:GovHydroWPID.velmin`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t1-valueRange

**Path:** `cim:GovSteam0.t1`  
Steam bowl time constant (T1) (> 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t2-valueRange

**Path:** `cim:GovSteam0.t2`  
Numerator time constant of T2/T3 block (T2) (>= 0).  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.t3-valueRange

**Path:** `cim:GovSteam0.t3`  
Reheater time constant (T3) (> 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam0.vmin-valueRangePair

**Path:** `cim:GovSteam0.vmin`  
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
Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.mwbase-valueRange

**Path:** `cim:GovSteam1.mwbase`  
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.pmin-valueRangePair

**Path:** `cim:GovSteam1.pmin`  
Minimum valve opening (Pmin) (>= 0 and < GovSteam1.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteam1.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteam1.pmax` 

### dy302c:GovSteam1.t1-valueRange

**Path:** `cim:GovSteam1.t1`  
Governor lag time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t2-valueRange

**Path:** `cim:GovSteam1.t2`  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t3-valueRange

**Path:** `cim:GovSteam1.t3`  
Valve positioner time constant (T3) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t4-valueRange

**Path:** `cim:GovSteam1.t4`  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t5-valueRange

**Path:** `cim:GovSteam1.t5`  
Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t6-valueRange

**Path:** `cim:GovSteam1.t6`  
Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.t7-valueRange

**Path:** `cim:GovSteam1.t7`  
Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.uc-valueRange

**Path:** `cim:GovSteam1.uc`  
Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam1.uo-valueRange

**Path:** `cim:GovSteam1.uo`  
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
Minimum fuel flow (P<sub>MIN</sub>) (< GovSteam2.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteam2.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteam2.pmax` 

### dy302c:GovSteam2.t1-valueRange

**Path:** `cim:GovSteam2.t1`  
Governor lag time constant (T<sub>1</sub>) (> 0).  Typical value = 0,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteam2.t2-valueRange

**Path:** `cim:GovSteam2.t2`  
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
Frequency deadband (f<sub>cut</sub>) (>= 0).  Typical value = 0,002.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.kls-valueRange

**Path:** `cim:GovSteamBB.kls`  
Gain (Kls) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.pmin-valueRangePair

**Path:** `cim:GovSteamBB.pmin`  
Low power limit (Pmin) (< GovSteamBB.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamBB.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamBB.pmax` 

### dy302c:GovSteamBB.td-valueRange

**Path:** `cim:GovSteamBB.td`  
Time constant (Td) (> 0).  Typical value = 1,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamBB.tn-valueRange

**Path:** `cim:GovSteamBB.tn`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.rhp-valueRange

**Path:** `cim:GovSteamCC.rhp`  
HP governor droop (Rhp) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.rlp-valueRange

**Path:** `cim:GovSteamCC.rlp`  
LP governor droop (Rlp) (> 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t1hp-valueRange

**Path:** `cim:GovSteamCC.t1hp`  
HP governor time constant (T1hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t1lp-valueRange

**Path:** `cim:GovSteamCC.t1lp`  
LP governor time constant (T1lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t3hp-valueRange

**Path:** `cim:GovSteamCC.t3hp`  
HP turbine time constant (T3hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t3lp-valueRange

**Path:** `cim:GovSteamCC.t3lp`  
LP turbine time constant (T3lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t4hp-valueRange

**Path:** `cim:GovSteamCC.t4hp`  
HP turbine time constant (T4hp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t4lp-valueRange

**Path:** `cim:GovSteamCC.t4lp`  
LP turbine time constant (T4lp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t5hp-valueRange

**Path:** `cim:GovSteamCC.t5hp`  
HP reheater time constant (T5hp) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamCC.t5lp-valueRange

**Path:** `cim:GovSteamCC.t5lp`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tb-valueRange

**Path:** `cim:GovSteamEU.tb`  
Boiler time constant (Tb) (>= 0).  Typical value = 100.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tdp-valueRange

**Path:** `cim:GovSteamEU.tdp`  
Derivative time constant of the power controller (Tdp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.ten-valueRange

**Path:** `cim:GovSteamEU.ten`  
Electro hydraulic transducer (Ten) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tf-valueRange

**Path:** `cim:GovSteamEU.tf`  
Frequency transducer time constant (Tf) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tfp-valueRange

**Path:** `cim:GovSteamEU.tfp`  
Time constant of the power controller (Tfp) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.thp-valueRange

**Path:** `cim:GovSteamEU.thp`  
High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,31.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tip-valueRange

**Path:** `cim:GovSteamEU.tip`  
Integral time constant of the power controller (Tip) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tlp-valueRange

**Path:** `cim:GovSteamEU.tlp`  
Low pressure (LP) time constant of the turbine (Tlp) (>= 0).  Typical value = 0,45.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tp-valueRange

**Path:** `cim:GovSteamEU.tp`  
Power transducer time constant (Tp) (>= 0).  Typical value = 0,07.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.trh-valueRange

**Path:** `cim:GovSteamEU.trh`  
Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tvhp-valueRange

**Path:** `cim:GovSteamEU.tvhp`  
Control valves servo time constant (Tvhp) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tvip-valueRange

**Path:** `cim:GovSteamEU.tvip`  
Intercept valves servo time constant (Tvip) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.tw-valueRange

**Path:** `cim:GovSteamEU.tw`  
Speed transducer time constant (Tw) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamEU.wfmin-valueRangePair

**Path:** `cim:GovSteamEU.wfmin`  
Lower limit for frequency correction (Wfmin) (< GovSteamEU.wfmax).  Typical value = -0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamEU.wfmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamEU.wfmax` 

### dy302c:GovSteamEU.wwmin-valueRangePair

**Path:** `cim:GovSteamEU.wwmin`  
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
Alternate base used instead of machine base in equipment model if necessary (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.t1-valueRange

**Path:** `cim:GovSteamFV2.t1`  
Governor time constant (T1) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.t3-valueRange

**Path:** `cim:GovSteamFV2.t3`  
Reheater time constant (T3) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.ta-valueRange

**Path:** `cim:GovSteamFV2.ta`  
Time after initial time for valve to close (Ta) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tb-valueRange

**Path:** `cim:GovSteamFV2.tb`  
Time after initial time for valve to begin opening (Tb) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tc-valueRange

**Path:** `cim:GovSteamFV2.tc`  
Time after initial time for valve to become fully open (Tc) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.tt-valueRange

**Path:** `cim:GovSteamFV2.tt`  
Time constant with which power falls off after intercept valve closure (Tt) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV2.vmin-valueRangePair

**Path:** `cim:GovSteamFV2.vmin`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.pmin-valueRangePair

**Path:** `cim:GovSteamFV3.pmin`  
Minimum valve opening, PU of MWbase (Pmin) (< GovSteamFV3.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamFV3.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamFV3.pmax` 

### dy302c:GovSteamFV3.t1-valueRange

**Path:** `cim:GovSteamFV3.t1`  
Governor lead time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t2-valueRange

**Path:** `cim:GovSteamFV3.t2`  
Governor lag time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t3-valueRange

**Path:** `cim:GovSteamFV3.t3`  
Valve positioner time constant (T3) (> 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t4-valueRange

**Path:** `cim:GovSteamFV3.t4`  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.t6-valueRange

**Path:** `cim:GovSteamFV3.t6`  
Time constant of crossover or third boiler pass (T6) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.ta-valueRange

**Path:** `cim:GovSteamFV3.ta`  
Time to close intercept valve (IV) (Ta) (>= 0).  Typical value = 0,97.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.tb-valueRange

**Path:** `cim:GovSteamFV3.tb`  
Time until IV starts to reopen (Tb) (>= 0).  Typical value = 0,98.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV3.tc-valueRange

**Path:** `cim:GovSteamFV3.tc`  
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
Control valves rate opening time (Ta) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tam-valueRange

**Path:** `cim:GovSteamFV4.tam`  
Intercept valves rate opening time (Tam) (>= 0).  Typical value = 0,8.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tc-valueRange

**Path:** `cim:GovSteamFV4.tc`  
Control valves rate closing time (Tc) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tcm-valueRange

**Path:** `cim:GovSteamFV4.tcm`  
Intercept valves rate closing time (Tcm) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tdc-valueRange

**Path:** `cim:GovSteamFV4.tdc`  
Derivative time constant of pressure regulator (Tdc) (>= 0).  Typical value = 90.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tf1-valueRange

**Path:** `cim:GovSteamFV4.tf1`  
Time constant of fuel regulation (Tf1) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tf2-valueRange

**Path:** `cim:GovSteamFV4.tf2`  
Time constant of steam chest (Tf2) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.thp-valueRange

**Path:** `cim:GovSteamFV4.thp`  
High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tmp-valueRange

**Path:** `cim:GovSteamFV4.tmp`  
Low pressure (LP) time constant of the turbine (Tmp) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.trh-valueRange

**Path:** `cim:GovSteamFV4.trh`  
Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.tv-valueRange

**Path:** `cim:GovSteamFV4.tv`  
Boiler time constant (Tv) (>= 0).  Typical value = 60.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamFV4.ty-valueRange

**Path:** `cim:GovSteamFV4.ty`  
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
Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.mwbase-valueRange

**Path:** `cim:GovSteamIEEE1.mwbase`  
Base for power values (MWbase) (> 0). Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.pmin-valueRangePair

**Path:** `cim:GovSteamIEEE1.pmin`  
Minimum valve opening (Pmin) (>= 0 and < GovSteamIEEE1.pmax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than GovSteamIEEE1.pmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GovSteamIEEE1.pmax` 

### dy302c:GovSteamIEEE1.t1-valueRange

**Path:** `cim:GovSteamIEEE1.t1`  
Governor lag time constant (T1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t2-valueRange

**Path:** `cim:GovSteamIEEE1.t2`  
Governor lead time constant (T2) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t3-valueRange

**Path:** `cim:GovSteamIEEE1.t3`  
Valve positioner time constant (T3) (> 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t4-valueRange

**Path:** `cim:GovSteamIEEE1.t4`  
Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t5-valueRange

**Path:** `cim:GovSteamIEEE1.t5`  
Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t6-valueRange

**Path:** `cim:GovSteamIEEE1.t6`  
Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.t7-valueRange

**Path:** `cim:GovSteamIEEE1.t7`  
Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.uc-valueRange

**Path:** `cim:GovSteamIEEE1.uc`  
Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamIEEE1.uo-valueRange

**Path:** `cim:GovSteamIEEE1.uo`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.pmin-valueRangePair

**Path:** `cim:GovSteamSGO.pmin`  
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
Controller lag (T1) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t2-valueRange

**Path:** `cim:GovSteamSGO.t2`  
Controller lead compensation (T2) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t3-valueRange

**Path:** `cim:GovSteamSGO.t3`  
Governor lag (T3) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t4-valueRange

**Path:** `cim:GovSteamSGO.t4`  
Delay due to steam inlet volumes associated with steam chest and inlet piping (T4) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t5-valueRange

**Path:** `cim:GovSteamSGO.t5`  
Reheater delay including hot and cold leads (T5) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:GovSteamSGO.t6-valueRange

**Path:** `cim:GovSteamSGO.t6`  
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
Inertia constant (H) (>= 0).  Typical value = 2,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadComposite.pfrac-valueRange

**Path:** `cim:LoadComposite.pfrac`  
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
Time constant of lag function of active power (T<sub>P</sub>) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadGenericNonLinear.tq-valueRange

**Path:** `cim:LoadGenericNonLinear.tq`  
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
Inertia constant (H) (>= 0).  Typical value = 0,4.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.pfrac-valueRange

**Path:** `cim:LoadMotor.pfrac`  
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
Circuit breaker operating time (Tbkr) (>= 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tpo-valueRange

**Path:** `cim:LoadMotor.tpo`  
Transient rotor time constant (Tpo) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tppo-valueRange

**Path:** `cim:LoadMotor.tppo`  
Subtransient rotor time constant (Tppo) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:LoadMotor.tv-valueRange

**Path:** `cim:LoadMotor.tv`  
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

MechanicalLoadDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:MechanicalLoadUserDefined
- targetClass: cim:MechLoad1

**Constraints:**

- **sh:XoneConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[cim:MechanicalLoadDynamics.AsynchronousMachineDynamics] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}] [{[cim:MechanicalLoadDynamics.SynchronousMachineDynamics] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}]]` 

## dy302c:OverexcLim2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLim2

**Nested Properties:**

### dy302c:OverexcLim2.voimin-valueRangePair

**Path:** `cim:OverexcLim2.voimin`  
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
Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME<sub>1</sub>) (>= 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.t2-valueRange

**Path:** `cim:OverexcLimX1.t2`  
Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME<sub>2</sub>) (>= 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.t3-valueRange

**Path:** `cim:OverexcLimX1.t3`  
Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME<sub>3</sub>) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX1.vlow-valueRange

**Path:** `cim:OverexcLimX1.vlow`  
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
Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME<sub>1</sub>) (>= 0).  Typical value = 120.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.t2-valueRange

**Path:** `cim:OverexcLimX2.t2`  
Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME<sub>2</sub>) (>= 0).  Typical value = 40.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.t3-valueRange

**Path:** `cim:OverexcLimX2.t3`  
Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME<sub>3</sub>) (>= 0).  Typical value = 15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:OverexcLimX2.vlow-valueRange

**Path:** `cim:OverexcLimX2.vlow`  
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
PF controller time delay (T<sub>PFC</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PFVArType1IEEEPFController.vvtmin-valueRangePair

**Path:** `cim:PFVArType1IEEEPFController.vvtmin`  
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
Var controller time delay (T<sub>VARC</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PFVArType1IEEEVArController.vvtmin-valueRangePair

**Path:** `cim:PFVArType1IEEEVArController.vvtmin`  
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
Lead/lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t5-valueRange

**Path:** `cim:Pss1.t5`  
Washout (T<sub>5</sub>) (>= 0).  Typical value = 3,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t6-valueRange

**Path:** `cim:Pss1.t6`  
Filter time constant (T<sub>6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t7-valueRange

**Path:** `cim:Pss1.t7`  
Lead/lag time constant (T<sub>7</sub>) (>= 0). If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t8-valueRange

**Path:** `cim:Pss1.t8`  
Lead/lag time constant (T<sub>8</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.t9-valueRange

**Path:** `cim:Pss1.t9`  
Lead/lag time constant (T<sub>9</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1.tpe-valueRange

**Path:** `cim:Pss1.tpe`  
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
Lead/lag time constant (T<sub>1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t2-valueRange

**Path:** `cim:Pss1A.t2`  
Lead/lag time constant (T<sub>2</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t3-valueRange

**Path:** `cim:Pss1A.t3`  
Lead/lag time constant (T<sub>3</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t4-valueRange

**Path:** `cim:Pss1A.t4`  
Lead/lag time constant (T<sub>4</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t5-valueRange

**Path:** `cim:Pss1A.t5`  
Washout time constant (T<sub>5</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.t6-valueRange

**Path:** `cim:Pss1A.t6`  
Transducer time constant (T<sub>6</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.tdelay-valueRange

**Path:** `cim:Pss1A.tdelay`  
Time constant (Tdelay) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss1A.vrmin-valueRangePair

**Path:** `cim:Pss1A.vrmin`  
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
Lead/lag time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t10-valueRange

**Path:** `cim:Pss2B.t10`  
Lead/lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t11-valueRange

**Path:** `cim:Pss2B.t11`  
Lead/lag time constant (T<sub>11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t2-valueRange

**Path:** `cim:Pss2B.t2`  
Lead/lag time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t3-valueRange

**Path:** `cim:Pss2B.t3`  
Lead/lag time constant (T<sub>3</sub>) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t4-valueRange

**Path:** `cim:Pss2B.t4`  
Lead/lag time constant (T<sub>4</sub>) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t6-valueRange

**Path:** `cim:Pss2B.t6`  
Time constant on signal #1 (T<sub>6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t7-valueRange

**Path:** `cim:Pss2B.t7`  
Time constant on signal #2 (T<sub>7</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t8-valueRange

**Path:** `cim:Pss2B.t8`  
Lead of ramp tracking filter (T<sub>8</sub>) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.t9-valueRange

**Path:** `cim:Pss2B.t9`  
Lag of ramp tracking filter (T<sub>9</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.ta-valueRange

**Path:** `cim:Pss2B.ta`  
Lead constant (T<sub>a</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tb-valueRange

**Path:** `cim:Pss2B.tb`  
Lag time constant (T<sub>b</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw1-valueRange

**Path:** `cim:Pss2B.tw1`  
First washout on signal #1 (T<sub>w1</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw2-valueRange

**Path:** `cim:Pss2B.tw2`  
Second washout on signal #1 (T<sub>w2</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw3-valueRange

**Path:** `cim:Pss2B.tw3`  
First washout on signal #2 (T<sub>w3</sub>) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.tw4-valueRange

**Path:** `cim:Pss2B.tw4`  
Second washout on signal #2 (T<sub>w4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2B.vsi1min-valueRangePair

**Path:** `cim:Pss2B.vsi1min`  
Input signal #1 minimum limit (Vsi1min) (< Pss2B.vsi1max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2B.vsi1max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2B.vsi1max` 

### dy302c:Pss2B.vsi2min-valueRangePair

**Path:** `cim:Pss2B.vsi2min`  
Input signal #2 minimum limit (Vsi2min) (< Pss2B.vsi2max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2B.vsi2max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2B.vsi2max` 

### dy302c:Pss2B.vstmin-valueRangePair

**Path:** `cim:Pss2B.vstmin`  
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
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:Pss2ST.inputSignal2Type-allowedValues

**Path:** `cim:Pss2ST.inputSignal2Type`  
Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative - shall be different than Pss2ST.inputSignal1Type).  Typical value = busVoltageDerivative.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:Pss2ST.lsmin-valueRangePair

**Path:** `cim:Pss2ST.lsmin`  
Limiter (L<sub>SMIN</sub>) (< Pss2ST.lsmax). 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than Pss2ST.lsmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:Pss2ST.lsmax` 

### dy302c:Pss2ST.t1-valueRange

**Path:** `cim:Pss2ST.t1`  
Time constant (T<sub>1</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t10-valueRange

**Path:** `cim:Pss2ST.t10`  
Time constant (T<sub>10</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t2-valueRange

**Path:** `cim:Pss2ST.t2`  
Time constant (T<sub>2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t3-valueRange

**Path:** `cim:Pss2ST.t3`  
Time constant (T<sub>3</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t4-valueRange

**Path:** `cim:Pss2ST.t4`  
Time constant (T<sub>4</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t5-valueRange

**Path:** `cim:Pss2ST.t5`  
Time constant (T<sub>5</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t6-valueRange

**Path:** `cim:Pss2ST.t6`  
Time constant (T<sub>6</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t7-valueRange

**Path:** `cim:Pss2ST.t7`  
Time constant (T<sub>7</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t8-valueRange

**Path:** `cim:Pss2ST.t8`  
Time constant (T<sub>8</sub>) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss2ST.t9-valueRange

**Path:** `cim:Pss2ST.t9`  
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
Lead/lag time constant (T<sub>L1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl2-valueRange

**Path:** `cim:Pss5.tl2`  
Lead/lag time constant (T<sub>L2</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl3-valueRange

**Path:** `cim:Pss5.tl3`  
Lead/lag time constant (T<sub>L3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tl4-valueRange

**Path:** `cim:Pss5.tl4`  
Lead/lag time constant (T<sub>L4</sub>) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tpe-valueRange

**Path:** `cim:Pss5.tpe`  
Electric power filter time constant (T<sub>PE</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tw1-valueRange

**Path:** `cim:Pss5.tw1`  
First washout (T<sub>W1</sub>) (>= 0).  Typical value = 3,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:Pss5.tw2-valueRange

**Path:** `cim:Pss5.tw2`  
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
Time constant (Ts1) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts2-valueRange

**Path:** `cim:PssELIN2.ts2`  
Time constant (Ts2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts3-valueRange

**Path:** `cim:PssELIN2.ts3`  
Time constant (Ts3) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts4-valueRange

**Path:** `cim:PssELIN2.ts4`  
Time constant (Ts4) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts5-valueRange

**Path:** `cim:PssELIN2.ts5`  
Time constant (Ts5) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssELIN2.ts6-valueRange

**Path:** `cim:PssELIN2.ts6`  
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
Type of input signal (rotorAngularFrequencyDeviation, generatorElectricalPower, or busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssIEEE1A.t1-valueRange

**Path:** `cim:PssIEEE1A.t1`  
Lead/lag time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t2-valueRange

**Path:** `cim:PssIEEE1A.t2`  
Lead/lag time constant (T2) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t3-valueRange

**Path:** `cim:PssIEEE1A.t3`  
Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t4-valueRange

**Path:** `cim:PssIEEE1A.t4`  
Lead/lag time constant (T4) (>= 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t5-valueRange

**Path:** `cim:PssIEEE1A.t5`  
Washout time constant (T5) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.t6-valueRange

**Path:** `cim:PssIEEE1A.t6`  
Transducer time constant (T6) (>= 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE1A.vrmin-valueRangePair

**Path:** `cim:PssIEEE1A.vrmin`  
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
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssIEEE2B.inputSignal2Type-allowedValues

**Path:** `cim:PssIEEE2B.inputSignal2Type`  
Type of input signal #2 (generatorElectricalPower).  Typical value = generatorElectricalPower.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.generatorElectricalPower]` 

### dy302c:PssIEEE2B.t1-valueRange

**Path:** `cim:PssIEEE2B.t1`  
Lead/lag time constant (T1) (>= 0).  Typical value = 0,12.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t10-valueRange

**Path:** `cim:PssIEEE2B.t10`  
Lead/lag time constant (T10) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t11-valueRange

**Path:** `cim:PssIEEE2B.t11`  
Lead/lag time constant (T11) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t2-valueRange

**Path:** `cim:PssIEEE2B.t2`  
Lead/lag time constant (T2) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t3-valueRange

**Path:** `cim:PssIEEE2B.t3`  
Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t4-valueRange

**Path:** `cim:PssIEEE2B.t4`  
Lead/lag time constant (T4) (>= 0).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t6-valueRange

**Path:** `cim:PssIEEE2B.t6`  
Time constant on signal #1 (T6) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t7-valueRange

**Path:** `cim:PssIEEE2B.t7`  
Time constant on signal #2 (T7) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t8-valueRange

**Path:** `cim:PssIEEE2B.t8`  
Lead of ramp tracking filter (T8) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.t9-valueRange

**Path:** `cim:PssIEEE2B.t9`  
Lag of ramp tracking filter (T9) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw1-valueRange

**Path:** `cim:PssIEEE2B.tw1`  
First washout on signal #1 (Tw1) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw2-valueRange

**Path:** `cim:PssIEEE2B.tw2`  
Second washout on signal #1 (Tw2) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw3-valueRange

**Path:** `cim:PssIEEE2B.tw3`  
First washout on signal #2 (Tw3) (>= 0).  Typical value = 2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.tw4-valueRange

**Path:** `cim:PssIEEE2B.tw4`  
Second washout on signal #2 (Tw4) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE2B.vsi1min-valueRangePair

**Path:** `cim:PssIEEE2B.vsi1min`  
Input signal #1 minimum limit (Vsi1min) (< PssIEEE2B.vsi1max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE2B.vsi1max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE2B.vsi1max` 

### dy302c:PssIEEE2B.vsi2min-valueRangePair

**Path:** `cim:PssIEEE2B.vsi2min`  
Input signal #2 minimum limit (Vsi2min) (< PssIEEE2B.vsi2max).  Typical value = -2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE2B.vsi2max."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE2B.vsi2max` 

### dy302c:PssIEEE2B.vstmin-valueRangePair

**Path:** `cim:PssIEEE2B.vstmin`  
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
Transducer time constant (T1) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.t2-valueRange

**Path:** `cim:PssIEEE3B.t2`  
Transducer time constant (T2) (>= 0).  Typical value = 0,012.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw1-valueRange

**Path:** `cim:PssIEEE3B.tw1`  
Washout time constant (Tw1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw2-valueRange

**Path:** `cim:PssIEEE3B.tw2`  
Washout time constant (Tw2) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.tw3-valueRange

**Path:** `cim:PssIEEE3B.tw3`  
Washout time constant (Tw3) (>= 0).  Typical value = 0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE3B.vstmin-valueRangePair

**Path:** `cim:PssIEEE3B.vstmin`  
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
High band time constant (T<sub>H1</sub>) (>= 0).  Typical value = 0,01513.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th10-valueRange

**Path:** `cim:PssIEEE4B.th10`  
High band time constant (T<sub>H10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th11-valueRange

**Path:** `cim:PssIEEE4B.th11`  
High band time constant (T<sub>H11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th12-valueRange

**Path:** `cim:PssIEEE4B.th12`  
High band time constant (T<sub>H12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th2-valueRange

**Path:** `cim:PssIEEE4B.th2`  
High band time constant (T<sub>H2</sub>) (>= 0).  Typical value = 0,01816.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th3-valueRange

**Path:** `cim:PssIEEE4B.th3`  
High band time constant (T<sub>H3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th4-valueRange

**Path:** `cim:PssIEEE4B.th4`  
High band time constant (T<sub>H4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th5-valueRange

**Path:** `cim:PssIEEE4B.th5`  
High band time constant (T<sub>H5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th6-valueRange

**Path:** `cim:PssIEEE4B.th6`  
High band time constant (T<sub>H6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th7-valueRange

**Path:** `cim:PssIEEE4B.th7`  
High band time constant (T<sub>H7</sub>) (>= 0).  Typical value = 0,01816.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th8-valueRange

**Path:** `cim:PssIEEE4B.th8`  
High band time constant (T<sub>H8</sub>) (>= 0).  Typical value = 0,02179.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.th9-valueRange

**Path:** `cim:PssIEEE4B.th9`  
High band time constant (T<sub>H9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti1-valueRange

**Path:** `cim:PssIEEE4B.ti1`  
Intermediate band time constant (T<sub>I1</sub>) (>= 0).  Typical value = 0,173.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti10-valueRange

**Path:** `cim:PssIEEE4B.ti10`  
Intermediate band time constant (T<sub>I10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti11-valueRange

**Path:** `cim:PssIEEE4B.ti11`  
Intermediate band time constant (T<sub>I11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti12-valueRange

**Path:** `cim:PssIEEE4B.ti12`  
Intermediate band time constant (T<sub>I12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti2-valueRange

**Path:** `cim:PssIEEE4B.ti2`  
Intermediate band time constant (T<sub>I2</sub>) (>= 0).  Typical value = 0,2075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti3-valueRange

**Path:** `cim:PssIEEE4B.ti3`  
Intermediate band time constant (T<sub>I3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti4-valueRange

**Path:** `cim:PssIEEE4B.ti4`  
Intermediate band time constant (T<sub>I4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti5-valueRange

**Path:** `cim:PssIEEE4B.ti5`  
Intermediate band time constant (T<sub>I5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti6-valueRange

**Path:** `cim:PssIEEE4B.ti6`  
Intermediate band time constant (T<sub>I6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti7-valueRange

**Path:** `cim:PssIEEE4B.ti7`  
Intermediate band time constant (T<sub>I7</sub>) (>= 0).  Typical value = 0,2075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti8-valueRange

**Path:** `cim:PssIEEE4B.ti8`  
Intermediate band time constant (T<sub>I8</sub>) (>= 0).  Typical value = 0,2491.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.ti9-valueRange

**Path:** `cim:PssIEEE4B.ti9`  
Intermediate band time constant (T<sub>I9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl1-valueRange

**Path:** `cim:PssIEEE4B.tl1`  
Low band time constant (T<sub>L1</sub>) (>= 0).  Typical value = 1,73.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl10-valueRange

**Path:** `cim:PssIEEE4B.tl10`  
Low band time constant (T<sub>L10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl11-valueRange

**Path:** `cim:PssIEEE4B.tl11`  
Low band time constant (T<sub>L11</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl12-valueRange

**Path:** `cim:PssIEEE4B.tl12`  
Low band time constant (T<sub>L12</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl2-valueRange

**Path:** `cim:PssIEEE4B.tl2`  
Low band time constant (T<sub>L2</sub>) (>= 0).  Typical value = 2,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl3-valueRange

**Path:** `cim:PssIEEE4B.tl3`  
Low band time constant (T<sub>L3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl4-valueRange

**Path:** `cim:PssIEEE4B.tl4`  
Low band time constant (T<sub>L4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl5-valueRange

**Path:** `cim:PssIEEE4B.tl5`  
Low band time constant (T<sub>L5</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl6-valueRange

**Path:** `cim:PssIEEE4B.tl6`  
Low band time constant (T<sub>L6</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl7-valueRange

**Path:** `cim:PssIEEE4B.tl7`  
Low band time constant (T<sub>L7</sub>) (>= 0).  Typical value = 2,075.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl8-valueRange

**Path:** `cim:PssIEEE4B.tl8`  
Low band time constant (T<sub>L8</sub>) (>= 0).  Typical value = 2,491.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.tl9-valueRange

**Path:** `cim:PssIEEE4B.tl9`  
Low band time constant (T<sub>L9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssIEEE4B.vhmin-valueRangePair

**Path:** `cim:PssIEEE4B.vhmin`  
High band output minimum limit (V<sub>Hmin</sub>) (< PssIEEE4V.vhmax).  Typical value = -0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4V.vhmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4V.vhmax` 

### dy302c:PssIEEE4B.vimin-valueRangePair

**Path:** `cim:PssIEEE4B.vimin`  
Intermediate band output minimum limit (V<sub>Imin</sub>) (< PssIEEE4B.vimax).  Typical value = -0,6.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4B.vimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4B.vimax` 

### dy302c:PssIEEE4B.vlmin-valueRangePair

**Path:** `cim:PssIEEE4B.vlmin`  
Low band output minimum limit (V<sub>Lmin</sub>) (< PssIEEE4B.vlmax).  Typical value = -0,075.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than PssIEEE4B.vlmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:PssIEEE4B.vlmax` 

### dy302c:PssIEEE4B.vstmin-valueRangePair

**Path:** `cim:PssIEEE4B.vstmin`  
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
Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.dtf-valueRange

**Path:** `cim:PssPTIST1.dtf`  
Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.dtp-valueRange

**Path:** `cim:PssPTIST1.dtp`  
Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t1-valueRange

**Path:** `cim:PssPTIST1.t1`  
Time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t2-valueRange

**Path:** `cim:PssPTIST1.t2`  
Time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t3-valueRange

**Path:** `cim:PssPTIST1.t3`  
Time constant (T3) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.t4-valueRange

**Path:** `cim:PssPTIST1.t4`  
Time constant (T4) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.tf-valueRange

**Path:** `cim:PssPTIST1.tf`  
Time constant (Tf) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST1.tp-valueRange

**Path:** `cim:PssPTIST1.tp`  
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
Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.dtf-valueRange

**Path:** `cim:PssPTIST3.dtf`  
Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.dtp-valueRange

**Path:** `cim:PssPTIST3.dtp`  
Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125  (0,015 for 50 Hz).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.nav-valueRange

**Path:** `cim:PssPTIST3.nav`  
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
Number of counts at limit to active limit function (NCL) (> 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t1-valueRange

**Path:** `cim:PssPTIST3.t1`  
Time constant (T1) (>= 0).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t2-valueRange

**Path:** `cim:PssPTIST3.t2`  
Time constant (T2) (>= 0).  Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t3-valueRange

**Path:** `cim:PssPTIST3.t3`  
Time constant (T3) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t4-valueRange

**Path:** `cim:PssPTIST3.t4`  
Time constant (T4) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t5-valueRange

**Path:** `cim:PssPTIST3.t5`  
Time constant (T5) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.t6-valueRange

**Path:** `cim:PssPTIST3.t6`  
Time constant (T6) (>= 0). 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.tf-valueRange

**Path:** `cim:PssPTIST3.tf`  
Time constant (Tf) (>= 0).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssPTIST3.tp-valueRange

**Path:** `cim:PssPTIST3.tp`  
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
Lead lag time constant (T4F) (>= 0). Typical value = 0,045.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.t4m-valueRange

**Path:** `cim:PssRQB.t4m`  
Input time constant (T4M) (>= 0). Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.t4mom-valueRange

**Path:** `cim:PssRQB.t4mom`  
Speed time constant (T4MOM) (>= 0). Typical value = 1,27.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.tomd-valueRange

**Path:** `cim:PssRQB.tomd`  
Speed delay (TOMD) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssRQB.tomsl-valueRange

**Path:** `cim:PssRQB.tomsl`  
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
Time constant (Ta) (>= 0).  Typical value = 0,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tb-valueRange

**Path:** `cim:PssSB4.tb`  
Time constant (Tb) (>= 0).  Typical value = 0,37.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tc-valueRange

**Path:** `cim:PssSB4.tc`  
Time constant (Tc) (>= 0).  Typical value = 0,035.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.td-valueRange

**Path:** `cim:PssSB4.td`  
Time constant (Td) (>= 0).  Typical value = 0,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.te-valueRange

**Path:** `cim:PssSB4.te`  
Time constant (Te) (>= 0).  Typical value = 0,0169.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tt-valueRange

**Path:** `cim:PssSB4.tt`  
Time constant (Tt) (>= 0).  Typical value = 0,18.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tx1-valueRange

**Path:** `cim:PssSB4.tx1`  
Reset time constant (Tx1) (>= 0).  Typical value = 0,035.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.tx2-valueRange

**Path:** `cim:PssSB4.tx2`  
Time constant (Tx2) (>= 0).  Typical value = 5,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSB4.vsmin-valueRangePair

**Path:** `cim:PssSB4.vsmin`  
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
Time constant 1 (T1) (> 0).  Typical value = 0,076.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t2-valueRange

**Path:** `cim:PssSH.t2`  
Time constant 2 (T2) (> 0).  Typical value = 0,086.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t3-valueRange

**Path:** `cim:PssSH.t3`  
Time constant 3 (T3) (> 0).   Typical value = 1,068.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.t4-valueRange

**Path:** `cim:PssSH.t4`  
Time constant 4 (T4) (> 0).  Typical value = 1,913.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.td-valueRange

**Path:** `cim:PssSH.td`  
Input time constant (T<sub>d</sub>) (>= 0).  Typical value = 10.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssSH.vsmin-valueRangePair

**Path:** `cim:PssSH.vsmin`  
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
Denominator time constant (T<sub>1</sub>) (> 0,005).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t2-valueRange

**Path:** `cim:PssSK.t2`  
Filter time constant (T<sub>2</sub>) (> 0,005).  Typical value = 0,35.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t3-valueRange

**Path:** `cim:PssSK.t3`  
Denominator time constant (T<sub>3</sub>) (> 0,005).  Typical value = 0,22.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t4-valueRange

**Path:** `cim:PssSK.t4`  
Filter time constant (T<sub>4</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t5-valueRange

**Path:** `cim:PssSK.t5`  
Denominator time constant (T<sub>5</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.t6-valueRange

**Path:** `cim:PssSK.t6`  
Filter time constant (T<sub>6</sub>) (> 0,005).  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is less than or equal to 0.005."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.005` 

### dy302c:PssSK.vsmin-valueRangePair

**Path:** `cim:PssSK.vsmin`  
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
Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative).  Typical value = rotorAngularFrequencyDeviation.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #1."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssWECC.inputSignal2Type-allowedValues

**Path:** `cim:PssWECC.inputSignal2Type`  
Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, busVoltageDerivative - shall be different than PssWECC.inputSignal1Type).  Typical value = busVoltageDerivative.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value for input signal #2."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:InputSignalKind.busVoltage cim:InputSignalKind.generatorElectricalPower cim:InputSignalKind.generatorAcceleratingPower cim:InputSignalKind.busVoltageDerivative cim:InputSignalKind.rotorAngularFrequencyDeviation cim:InputSignalKind.busFrequencyDeviation]` 

### dy302c:PssWECC.t1-valueRange

**Path:** `cim:PssWECC.t1`  
Input signal 1 transducer time constant (T<sub>1</sub>) (>= 0).  Typical value = 0,037.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t10-valueRange

**Path:** `cim:PssWECC.t10`  
Lag time constant (T<sub>10</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t2-valueRange

**Path:** `cim:PssWECC.t2`  
Input signal 2 transducer time constant (T<sub>2</sub>) (>= 0).  Typical value = 0,0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t3-valueRange

**Path:** `cim:PssWECC.t3`  
Stabilizer washout time constant (T<sub>3</sub>) (>= 0).  Typical value = 9,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t4-valueRange

**Path:** `cim:PssWECC.t4`  
Stabilizer washout time lag constant (T<sub>4</sub>) (>= 0).  Typical value = 9,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t5-valueRange

**Path:** `cim:PssWECC.t5`  
Lead time constant (T<sub>5</sub>) (>= 0).  Typical value = 1,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t6-valueRange

**Path:** `cim:PssWECC.t6`  
Lag time constant (T<sub>6</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t7-valueRange

**Path:** `cim:PssWECC.t7`  
Lead time constant (T<sub>7</sub>) (>= 0).  Typical value = 1,7.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t8-valueRange

**Path:** `cim:PssWECC.t8`  
Lag time constant (T<sub>8</sub>) (>= 0).  Typical value = 1,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.t9-valueRange

**Path:** `cim:PssWECC.t9`  
Lead time constant (T<sub>9</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:PssWECC.vsmin-valueRangePair

**Path:** `cim:PssWECC.vsmin`  
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
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineTimeConstantReactance
- targetClass: cim:AsynchronousMachineEquivalentCircuit
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineTimeConstantReactance

## dy302c:SynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineEquivalentCircuit

**Nested Properties:**

### dy302c:RotatingMachineDynamics.damping-valueRange

**Path:** `cim:RotatingMachineDynamics.damping`  
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.efdBaseRatio-valueRange

**Path:** `cim:SynchronousMachineDetailed.efdBaseRatio`  
Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.saturationFactorQAxis-valueRange

**Path:** `cim:SynchronousMachineDetailed.saturationFactorQAxis`  
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
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
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
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.efdBaseRatio-valueRange

**Path:** `cim:SynchronousMachineDetailed.efdBaseRatio`  
Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical value = 1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineDetailed.saturationFactorQAxis-valueRange

**Path:** `cim:SynchronousMachineDetailed.saturationFactorQAxis`  
Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.ks-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.ks`  
Saturation loading correction factor (Ks) (>= 0).  Used only by type J model.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tc-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tc`  
Damping time constant for “Canay” reactance (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tppdo-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppdo`  
Direct-axis subtransient rotor time constant (T''do) (> 0).  Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tpdo-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppdo`  
Direct-axis transient rotor time constant (T'do) (> SynchronousMachineTimeConstantReactance.tppdo).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.tpdo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.tpdo` 

### dy302c:SynchronousMachineTimeConstantReactance.tppqo-valueRange

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppqo`  
Quadrature-axis subtransient rotor time constant (T''qo) (> 0). Typical value = 0,03.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.tpqo-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.tppqo`  
Quadrature-axis transient rotor time constant (T'qo) (> SynchronousMachineTimeConstantReactance.tppqo). Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.tpqo."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.tpqo` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectTrans-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans`  
Direct-axis transient reactance (unsaturated) (X'd) (>= SynchronousMachineTimeConstantReactance.xDirectSubtrans).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xDirectTrans."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectTrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSync-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xDirectTrans`  
Direct-axis synchronous reactance (Xd) (>= SynchronousMachineTimeConstantReactance.xDirectTrans). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed.  Typical value = 1,8.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xDirectSync."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSync` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadTrans-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans`  
Quadrature-axis transient reactance (X'q) (>= SynchronousMachineTimeConstantReactance.xQuadSubtrans).  Typical value = 0,3.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than SynchronousMachineTimeConstantReactance.xQuadTrans."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadTrans` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSync-valueRangePair

**Path:** `cim:SynchronousMachineTimeConstantReactance.xQuadTrans`  
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
Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.inertia-valueRange

**Path:** `cim:RotatingMachineDynamics.inertia`  
Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:RotatingMachineDynamics.saturationFactor-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor`  
Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:SynchronousMachineTimeConstantReactance.xDirectSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Direct-axis subtransient reactance (unsaturated) (X''d) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xDirectSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans` 

### dy302c:RotatingMachineDynamics.statorLeakageReactance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:AsynchronousMachineTimeConstantReactance.xpp-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Subtransient reactance (unsaturated) (X'') (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than AsynchronousMachineTimeConstantReactance.xpp."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:AsynchronousMachineTimeConstantReactance.xpp` 

### dy302c:SynchronousMachineTimeConstantReactance.xQuadSubtrans-valueRangePair

**Path:** `cim:RotatingMachineDynamics.statorLeakageReactance`  
Quadrature-axis subtransient reactance (X''q) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than or equal to SynchronousMachineTimeConstantReactance.xQuadSubtrans."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans` 

### dy302c:RotatingMachineDynamics.statorResistance-valueRange

**Path:** `cim:RotatingMachineDynamics.statorResistance`  
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
Base for power values (MWbase) (> 0).  Unit = MW.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:TurbLCFB1.tpelec-valueRange

**Path:** `cim:TurbLCFB1.tpelec`  
Power transducer time constant (Tpelec) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## dy302c:TurbineGovernorDynamics

TurbineGovernorDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:GovGAST
- targetClass: cim:GovHydroFrancis
- targetClass: cim:GovHydroPelton
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovSteam2
- targetClass: cim:GovSteamEU
- targetClass: cim:GovCT1
- targetClass: cim:TurbineGovernorUserDefined
- targetClass: cim:GovHydroIEEE2
- targetClass: cim:GovSteam1
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydro4
- targetClass: cim:GovGAST2
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovSteam0
- targetClass: cim:GovHydro1
- targetClass: cim:GovGAST3
- targetClass: cim:GovHydro3
- targetClass: cim:GovCT2
- targetClass: cim:GovHydroPID
- targetClass: cim:GovHydroDD
- targetClass: cim:GovHydroR
- targetClass: cim:GovGAST1
- targetClass: cim:GovGAST4
- targetClass: cim:GovSteamBB
- targetClass: cim:GovSteamFV4
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovHydro2
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovGASTWD

**Constraints:**

- **sh:XoneConstraintComponent** (Severity: sh:Violation)
  - Shapes: `[[{[cim:TurbineGovernorDynamics.AsynchronousMachineDynamics] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}] [{[cim:TurbineGovernorDynamics.SynchronousMachineDynamics] sh:Violation    sh:MinCountConstraintComponent map[MinCount:1]}]]` 

## dy302c:UnderexcLim2Simplified

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLim2Simplified

**Nested Properties:**

### dy302c:UnderexcLim2Simplified.vuimin-valueRangePair

**Path:** `cim:UnderexcLim2Simplified.vuimin`  
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
UEL lead time constant (T<sub>U1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu2-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu2`  
UEL lag time constant (T<sub>U2</sub>) (>= 0).  Typical value = 0,05.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu3-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu3`  
UEL lead time constant (T<sub>U3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.tu4-valueRange

**Path:** `cim:UnderexcLimIEEE1.tu4`  
UEL lag time constant (T<sub>U4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE1.vuimin-valueRangePair

**Path:** `cim:UnderexcLimIEEE1.vuimin`  
UEL integrator output minimum limit (V<sub>UIMIN</sub>) (< UnderexcLimIEEE1.vuimax).

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE1.vuimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE1.vuimax` 

### dy302c:UnderexcLimIEEE1.vulmin-valueRangePair

**Path:** `cim:UnderexcLimIEEE1.vulmin`  
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
UEL lead time constant (T<sub>U1</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu2-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu2`  
UEL lag time constant (T<sub>U2</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu3-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu3`  
UEL lead time constant (T<sub>U3</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tu4-valueRange

**Path:** `cim:UnderexcLimIEEE2.tu4`  
UEL lag time constant (T<sub>U4</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tul-valueRange

**Path:** `cim:UnderexcLimIEEE2.tul`  
Time constant associated with optional integrator feedback input signal to UEL (T<sub>UL</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tup-valueRange

**Path:** `cim:UnderexcLimIEEE2.tup`  
Real power filter time constant (T<sub>UP</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tuq-valueRange

**Path:** `cim:UnderexcLimIEEE2.tuq`  
Reactive power filter time constant (T<sub>UQ</sub>) (>= 0).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.tuv-valueRange

**Path:** `cim:UnderexcLimIEEE2.tuv`  
Voltage filter time constant (T<sub>UV</sub>) (>= 0).  Typical value = 5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimIEEE2.vuimin-valueRangePair

**Path:** `cim:UnderexcLimIEEE2.vuimin`  
UEL integrator output minimum limit (V<sub>UIMIN</sub>) (< UnderexcLimIEEE2.vuimax).  Typical value = 0.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than UnderexcLimIEEE2.vuimax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:UnderexcLimIEEE2.vuimax` 

### dy302c:UnderexcLimIEEE2.vulmin-valueRangePair

**Path:** `cim:UnderexcLimIEEE2.vulmin`  
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
Minimum excitation limit slope (K) (> 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX1.tf2-valueRange

**Path:** `cim:UnderexcLimX1.tf2`  
Differential time constant (T<sub>F2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX1.tm-valueRange

**Path:** `cim:UnderexcLimX1.tm`  
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
Differential time constant (T<sub>F2</sub>) (>= 0).

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:UnderexcLimX2.tm-valueRange

**Path:** `cim:UnderexcLimX2.tm`  
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
Time that adjuster pulses are off (T<sub>AOFF</sub>) (>= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VAdjIEEE.taon-valueRange

**Path:** `cim:VAdjIEEE.taon`  
Time that adjuster pulses are on (T<sub>AON</sub>) (>= 0).  Typical value = 0,1.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VAdjIEEE.vadjmin-valueRangePair

**Path:** `cim:VAdjIEEE.vadjmin`  
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
<font color=\"#0f0f0f\">Resistive component of compensation of a generator (Rc) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VCompIEEEType1.tr-valueRange

**Path:** `cim:VCompIEEEType1.tr`  
<font color=\"#0f0f0f\">Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).</font>

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:VCompIEEEType1.xc-valueRange

**Path:** `cim:VCompIEEEType1.xc`  
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
Time<sub> </sub>delay after deep voltage sags (T<sub>DVS</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tomegafiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tomegafiltp3`  
Filter time constant for generator speed measurement (T<sub>omegafiltp3</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tomegaref-valueRange

**Path:** `cim:WindContPType3IEC.tomegaref`  
Time constant in speed reference filter (T<sub>omega,ref</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tpfiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tpfiltp3`  
Filter time constant for power measurement (T<sub>pfiltp3</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType3IEC.tufiltp3-valueRange

**Path:** `cim:WindContPType3IEC.tufiltp3`  
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
Time constant in power order lag (T<sub>pordp4A</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4aIEC.tufiltp4a-valueRange

**Path:** `cim:WindContPType4aIEC.tufiltp4a`  
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
Time constant in aerodynamic power response (T<sub>paero</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4bIEC.tpordp4b-valueRange

**Path:** `cim:WindContPType4bIEC.tpordp4b`  
Time constant in power order lag (T<sub>pordp4B</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContPType4bIEC.tufiltp4b-valueRange

**Path:** `cim:WindContPType4bIEC.tufiltp4b`  
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
Maximum pitch negative ramp rate (dtheta<sub>min</sub>) (< WindContPitchAngleIEC.dthetamax). It is a type-dependent parameter. Unit = degrees / s. 

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContPitchAngleIEC.dthetamax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContPitchAngleIEC.dthetamax` 

### dy302c:WindContPitchAngleIEC.thetamin-valueRangePair

**Path:** `cim:WindContPitchAngleIEC.thetamin`  
Minimum pitch angle (theta<sub>min</sub>) (< WindContPitchAngleIEC.thetamax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContPitchAngleIEC.thetamax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContPitchAngleIEC.thetamax` 

### dy302c:WindContPitchAngleIEC.ttheta-valueRange

**Path:** `cim:WindContPitchAngleIEC.ttheta`  
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
Minimum reactive current injection (i<sub>qmin</sub>) (< WindContQIEC.iqmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContQIEC.iqmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContQIEC.iqmax` 

### dy302c:WindContQIEC.rdroop-valueRange

**Path:** `cim:WindContQIEC.rdroop`  
Resistive component of voltage drop impedance (r<sub>droop</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tpfiltq-valueRange

**Path:** `cim:WindContQIEC.tpfiltq`  
Power measurement filter time constant (T<sub>pfiltq</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tpost-valueRange

**Path:** `cim:WindContQIEC.tpost`  
Length of time period where post fault reactive power is injected (T<sub>post</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tqord-valueRange

**Path:** `cim:WindContQIEC.tqord`  
Time constant in reactive power order lag (T<sub>qord</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.tufiltq-valueRange

**Path:** `cim:WindContQIEC.tufiltq`  
Voltage measurement filter time constant (T<sub>ufiltq</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQIEC.umin-valueRangePair

**Path:** `cim:WindContQIEC.umin`  
Minimum voltage in voltage PI controller integral term (u<sub>min</sub>) (< WindContQIEC.umax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContQIEC.umax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContQIEC.umax` 

### dy302c:WindContQIEC.xdroop-valueRange

**Path:** `cim:WindContQIEC.xdroop`  
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
Power measurement filter time constant for Q capacity (T<sub>pfiltql</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContQPQULimIEC.tufiltql-valueRange

**Path:** `cim:WindContQPQULimIEC.tufiltql`  
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
Minimum rotor resistance (r<sub>min</sub>) (< WindContRotorRIEC.rmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindContRotorRIEC.rmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindContRotorRIEC.rmax` 

### dy302c:WindContRotorRIEC.tomegafiltrr-valueRange

**Path:** `cim:WindContRotorRIEC.tomegafiltrr`  
Filter time constant for generator speed measurement (T<sub>omegafiltrr</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindContRotorRIEC.tpfiltrr-valueRange

**Path:** `cim:WindContRotorRIEC.tpfiltrr`  
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
Current generation time constant (T<sub>g</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindGenType3bIEC.two-valueRange

**Path:** `cim:WindGenType3bIEC.two`  
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
Inertia constant of generator (H<sub>gen</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindMechIEC.hwtr-valueRange

**Path:** `cim:WindMechIEC.hwtr`  
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
Rate limit for decreasing power (dp<sub>min</sub>) (< WindPitchContPowerIEC.dpmax). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPitchContPowerIEC.dpmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPitchContPowerIEC.dpmax` 

### dy302c:WindPitchContPowerIEC.t1-valueRange

**Path:** `cim:WindPitchContPowerIEC.t1`  
Lag time constant (T<sub>1</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPitchContPowerIEC.tr-valueRange

**Path:** `cim:WindPitchContPowerIEC.tr`  
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
Minimum (negative) ramp rate of p<sub>WTref</sub> request from the plant controller to the wind turbines (dp<sub>refmin</sub>) (< WindPlantFreqPcontrolIEC.dprefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.dprefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.dprefmax` 

### dy302c:WindPlantFreqPcontrolIEC.dpwprefmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.dpwprefmin`  
Maximum negative ramp rate for wind plant power reference (dp<sub>WPrefmin</sub>) (< WindPlantFreqPcontrolIEC.dpwprefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.dpwprefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.dpwprefmax` 

### dy302c:WindPlantFreqPcontrolIEC.kiwppmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.kiwppmin`  
Minimum PI integrator term (K<sub>IWPpmin</sub>) (< WindPlantFreqPcontrolIEC.kiwppmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.kiwppmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.kiwppmax` 

### dy302c:WindPlantFreqPcontrolIEC.prefmin-valueRangePair

**Path:** `cim:WindPlantFreqPcontrolIEC.prefmin`  
Minimum p<sub>WTref</sub> request from the plant controller to the wind turbines (p<sub>refmin</sub>) (< WindPlantFreqPcontrolIEC.prefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantFreqPcontrolIEC.prefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantFreqPcontrolIEC.prefmax` 

### dy302c:WindPlantFreqPcontrolIEC.tpft-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.tpft`  
Lead time constant in reference value transfer function (T<sub>pft</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.tpfv-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.tpfv`  
Lag time constant in reference value transfer function (T<sub>pfv</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.twpffiltp-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.twpffiltp`  
Filter time constant for frequency measurement (T<sub>WPffiltp</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantFreqPcontrolIEC.twppfiltp-valueRange

**Path:** `cim:WindPlantFreqPcontrolIEC.twppfiltp`  
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
Maximum negative ramp rate for wind turbine reactive power/voltage reference (dx<sub>refmin</sub>) (< WindPlantReactiveControlIEC.dxrefmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantReactiveControlIEC.dxrefmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantReactiveControlIEC.dxrefmax` 

### dy302c:WindPlantReactiveControlIEC.kiwpxmin-valueRangePair

**Path:** `cim:WindPlantReactiveControlIEC.kiwpxmin`  
Minimum reactive power/voltage reference from integration (K<sub>IWPxmin</sub>) (< WindPlantReactiveControlIEC.kiwpxmax). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is either equal to or greater than WindPlantReactiveControlIEC.kiwpxmax."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:WindPlantReactiveControlIEC.kiwpxmax` 

### dy302c:WindPlantReactiveControlIEC.tuqfilt-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.tuqfilt`  
Filter time constant for voltage-dependent reactive power (T<sub>uqfilt</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twppfiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twppfiltq`  
Filter time constant for active power measurement (T<sub>WPpfiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twpqfiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twpqfiltq`  
Filter time constant for reactive power measurement (T<sub>WPqfiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.twpufiltq-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.twpufiltq`  
Filter time constant for voltage measurement (T<sub>WPufiltq</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.txft-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.txft`  
Lead time constant in reference value transfer function (T<sub>xft</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.txfv-valueRange

**Path:** `cim:WindPlantReactiveControlIEC.txfv`  
Lag time constant in reference value transfer function (T<sub>xfv</sub>) (>= 0). It is a project-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### dy302c:WindPlantReactiveControlIEC.xrefmin-valueRangePair

**Path:** `cim:WindPlantReactiveControlIEC.xrefmin`  
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
Time constant for PLL first order filter model (T<sub>PLL</sub>) (>= 0). It is a type-dependent parameter.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

