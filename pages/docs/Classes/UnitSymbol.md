# UnitSymbol (Enumeration)

The derived units defined for usage in the CIM. In some cases, the derived unit is equal to an SI unit. Whenever possible, the standard derived symbol is used instead of the formula for the derived unit. For example, the unit symbol Farad is defined as 'F' instead of 'CPerV'. In cases where a standard symbol does not exist for a derived unit, the formula for the unit is used as the unit symbol. For example, density does not have a standard symbol and so it is represented as 'kgPerm3'. With the exception of the 'kg', which is an SI unit, the unit symbols do not contain multipliers and therefore represent the base derived unit to which a multiplier can be applied as a whole. Every unit symbol is treated as an unparseable text as if it were a single-letter symbol. The meaning of each unit symbol is defined by the accompanying descriptive text and not by the text contents of the unit symbol. To allow the widest possible range of serializations without requiring special character handling, several substitutions are made which deviate from the format described in IEC 80000-1. The division symbol '/' is replaced by the letters 'Per'. Exponents are written in plain text after the unit as 'm3' instead of being formatted as 'm' with a superscript of 3 or introducing a symbol as in 'm^3'. The degree symbol '°' is replaced with the letters 'deg'. Any clarification of the meaning for a substitution is included in the description for the unit symbol. Non-SI units are included in list of unit symbols to allow sources of data to be correctly labelled with their non-SI units (for example, a GPS sensor that is reporting numbers that represent feet instead of meters). This allows software to use the unit symbol information correctly convert and scale the raw data of those sources into SI-based units. The integer values are used for harmonization with IEC 61850.

## Values

| Label | Comment |
|-------|---------|
| none | Dimension less quantity, e.g. count, per unit, etc. |
| m | Length in metres. |
| kg | Mass in kilograms. Note: multiplier “k” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| s | Time in seconds. |
| A | Current in amperes. |
| K | Temperature in kelvins. |
| mol | Amount of substance in moles. |
| cd | Luminous intensity in candelas. |
| deg | Plane angle in degrees. |
| rad | Plane angle in radians (m/m). |
| sr | Solid angle in steradians (m2/m2). |
| Gy | Absorbed dose in grays (J/kg). |
| Bq | Radioactivity in becquerels (1/s). |
| degC | Relative temperature in degrees Celsius. In the SI unit system the symbol is °C. Electric charge is measured in coulomb that has the unit symbol C. To distinguish degree Celsius from coulomb the symbol used in the UML is degC. The reason for not using °C is that the special character ° is difficult to manage in software. |
| Sv | Dose equivalent in sieverts (J/kg). |
| F | Electric capacitance in farads (C/V). |
| C | Electric charge in coulombs (A·s). |
| S | Conductance in siemens. |
| H | Electric inductance in henrys (Wb/A). |
| V | Electric potential in volts (W/A). |
| ohm | Electric resistance in ohms (V/A). |
| J | Energy in joules (N·m = C·V = W·s). |
| N | Force in newtons (kg·m/s²). |
| Hz | Frequency in hertz (1/s). |
| lx | Illuminance in lux (lm/m²). |
| lm | Luminous flux in lumens (cd·sr). |
| Wb | Magnetic flux in webers (V·s). |
| T | Magnetic flux density in teslas (Wb/m2). |
| W | Real power in watts (J/s). Electrical power may have real and reactive components. The real portion of electrical power (I²R or VIcos(phi)), is expressed in Watts. See also apparent power and reactive power. |
| Pa | Pressure in pascals (N/m²). Note: the absolute or relative measurement of pressure is implied with this entry. See below for more explicit forms. |
| m2 | Area in square metres (m²). |
| m3 | Volume in cubic metres (m³). |
| mPers | Velocity in metres per second (m/s). |
| mPers2 | Acceleration in metres per second squared (m/s²). |
| m3Pers | Volumetric flow rate in cubic metres per second (m³/s). |
| mPerm3 | Fuel efficiency in metres per cubic metres (m/m³). |
| kgm | Moment of mass in kilogram metres (kg·m) (first moment of mass). Note: multiplier “k” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| kgPerm3 | Density in kilogram/cubic metres (kg/m³). Note: multiplier “k” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| m2Pers | Viscosity in square metres / second (m²/s). |
| WPermK | Thermal conductivity in watt/metres kelvin. |
| JPerK | Heat capacity in joules/kelvin. |
| ppm | Concentration in parts per million. |
| rotPers | Rotations per second (1/s). See also Hz (1/s). |
| radPers | Angular velocity in radians per second (rad/s). |
| WPerm2 | Heat flux density, irradiance, watts per square metre. |
| JPerm2 | Insulation energy density, joules per square metre or watt second per square metre. |
| SPerm | Conductance per length (F/m). |
| KPers | Temperature change rate in kelvins per second. |
| PaPers | Pressure change rate in pascals per second. |
| JPerkgK | Specific heat capacity, specific entropy, joules per kilogram Kelvin. |
| VA | Apparent power in volt amperes. See also real power and reactive power. |
| VAr | Reactive power in volt amperes reactive. The “reactive” or “imaginary” component of electrical power (VIsin(phi)). (See also real power and apparent power). Note: Different meter designs use different methods to arrive at their results. Some meters may compute reactive power as an arithmetic value, while others compute the value vectorially. The data consumer should determine the method in use and the suitability of the measurement for the intended purpose. |
| cosPhi | Power factor, dimensionless. Note 1: This definition of power factor only holds for balanced systems. See the alternative definition under code 153. Note 2 : Beware of differing sign conventions in use between the IEC and EEI. It is assumed that the data consumer understands the type of meter in use and the sign convention in use by the utility. |
| Vs | Volt seconds (Ws/A). |
| V2 | Volt squared (W²/A²). |
| As | Ampere seconds (A·s). |
| A2 | Amperes squared (A²). |
| A2s | Ampere squared time in square amperes (A²s). |
| VAh | Apparent energy in volt ampere hours. |
| Wh | Real energy in watt hours. |
| VArh | Reactive energy in volt ampere reactive hours. |
| VPerHz | Magnetic flux in volt per hertz. |
| HzPers | Rate of change of frequency in hertz per second. |
| character | Number of characters. |
| charPers | Data rate (baud) in characters per second. |
| kgm2 | Moment of mass in kilogram square metres (kg·m²) (Second moment of mass, commonly called the moment of inertia). Note: multiplier “k” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| dB | Sound pressure level in decibels. Note: multiplier “d” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| WPers | Ramp rate in watts per second. |
| lPers | Volumetric flow rate in litres per second. |
| dBm | Power level (logarithmic ratio of signal strength , Bel-mW), normalized to 1mW. Note: multiplier “d” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| h | Time in hours, hour = 60 min = 3600 s. |
| min | Time in minutes, minute = 60 s. |
| Q | Quantity power, Q. |
| Qh | Quantity energy, Qh. |
| ohmm | Resistivity, ohm metres, (rho). |
| APerm | A/m, magnetic field strength, amperes per metre. |
| V2h | Volt-squared hour, volt-squared-hours. |
| A2h | Ampere-squared hour, ampere-squared hour. |
| Ah | Ampere-hours, ampere-hours. |
| count | Amount of substance, Counter value. |
| ft3 | Volume, cubic feet. |
| m3Perh | Volumetric flow rate, cubic metres per hour. |
| gal | Volume in gallons, US gallon (1 gal = 231 in3 = 128 fl ounce). |
| Btu | Energy, British Thermal Units. |
| l | Volume in litres, litre = dm3 = m3/1000. |
| lPerh | Volumetric flow rate, litres per hour. |
| lPerl | Concentration, The ratio of the volume of a solute divided by the volume of the solution. Note: Users may need use a prefix such a ‘µ’ to express a quantity such as ‘µL/L’. |
| gPerg | Concentration, The ratio of the mass of a solute divided by the mass of the solution. Note: Users may need use a prefix such a ‘µ’ to express a quantity such as ‘µg/g’. |
| molPerm3 | Concentration, The amount of substance concentration, (c), the amount of solvent in moles divided by the volume of solution in m³. |
| molPermol | Concentration, Molar fraction, the ratio of the molar amount of a solute divided by the molar amount of the solution. |
| molPerkg | Concentration, Molality, the amount of solute in moles and the amount of solvent in kilograms. |
| sPers | Time, Ratio of time. Note: Users may need to supply a prefix such as ‘µ’ to show rates such as ‘µs/s’. |
| HzPerHz | Frequency, rate of frequency change. Note: Users may need to supply a prefix such as ‘m’ to show rates such as ‘mHz/Hz’. |
| VPerV | Voltage, ratio of voltages. Note: Users may need to supply a prefix such as ‘m’ to show rates such as ‘mV/V’. |
| APerA | Current, ratio of amperages. Note: Users may need to supply a prefix such as ‘m’ to show rates such as ‘mA/A’. |
| VPerVA | Power factor, PF, the ratio of the active power to the apparent power. Note: The sign convention used for power factor will differ between IEC meters and EEI (ANSI) meters. It is assumed that the data consumers understand the type of meter being used and agree on the sign convention in use at any given utility. |
| rev | Amount of rotation, revolutions. |
| kat | Catalytic activity, katal = mol / s. |
| JPerkg | Specific energy, Joules / kg. |
| m3Uncompensated | Volume, cubic metres, with the value uncompensated for weather effects. |
| m3Compensated | Volume, cubic metres, with the value compensated for weather effects. |
| WPerW | Signal Strength, ratio of power. Note: Users may need to supply a prefix such as ‘m’ to show rates such as ‘mW/W’. |
| therm | Energy, therms. |
| onePerm | Wavenumber, reciprocal metres, (1/m). |
| m3Perkg | Specific volume, cubic metres per kilogram, v. |
| Pas | Dynamic viscosity, pascal seconds. |
| Nm | Moment of force, newton metres. |
| NPerm | Surface tension, newton per metre. |
| radPers2 | Angular acceleration, radians per second squared. |
| JPerm3 | Energy density, joules per cubic metre. |
| VPerm | Electric field strength, volts per metre. |
| CPerm3 | Electric charge density, coulombs per cubic metre. |
| CPerm2 | Surface charge density, coulombs per square metre. |
| FPerm | Permittivity, farads per metre. |
| HPerm | Permeability, henrys per metre. |
| JPermol | Molar energy, joules per mole. |
| JPermolK | Molar entropy, molar heat capacity, joules per mole kelvin. |
| CPerkg | Exposure (x rays), coulombs per kilogram. |
| GyPers | Absorbed dose rate, grays per second. |
| WPersr | Radiant intensity, watts per steradian. |
| WPerm2sr | Radiance, watts per square metre steradian. |
| katPerm3 | Catalytic activity concentration, katals per cubic metre. |
| d | Time in days, day = 24 h = 86400 s. |
| anglemin | Plane angle, minutes. |
| anglesec | Plane angle, seconds. |
| ha | Area, hectares. |
| tonne | Mass in tons, “tonne” or “metric ton” (1000 kg = 1 Mg). |
| bar | Pressure in bars, (1 bar = 100 kPa). |
| mmHg | Pressure, millimetres of mercury (1 mmHg is approximately 133.3 Pa). |
| M | Length, nautical miles (1 M = 1852 m). |
| kn | Speed, knots (1 kn = 1852/3600) m/s. |
| Mx | Magnetic flux, maxwells (1 Mx = 10-8 Wb). |
| G | Magnetic flux density, gausses (1 G = 10-4 T). |
| Oe | Magnetic field in oersteds, (1 Oe = (103/4p) A/m). |
| Vh | Volt-hour, Volt hours. |
| WPerA | Active power per current flow, watts per Ampere. |
| onePerHz | Reciprocal of frequency (1/Hz). |
| VPerVAr | Power factor, PF, the ratio of the active power to the apparent power. Note: The sign convention used for power factor will differ between IEC meters and EEI (ANSI) meters. It is assumed that the data consumers understand the type of meter being used and agree on the sign convention in use at any given utility. |
| ohmPerm | Electric resistance per length in ohms per metre ((V/A)/m). |
| kgPerJ | Weight per energy in kilograms per joule (kg/J). Note: multiplier “k” is included in this unit symbol for compatibility with IEC 61850-7-3. |
| JPers | Energy rate in joules per second (J/s). |

