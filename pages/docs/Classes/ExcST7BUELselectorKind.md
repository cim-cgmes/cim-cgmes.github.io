# ExcST7BUELselectorKind (Enumeration)

Types of connections for the UEL input used for static excitation systems type 7B.

## Values

| Label | Comment |
|-------|---------|
| noUELinput | No UEL input is used. Corresponds to UELin not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this UELin = 0. |
| addVref | The signal is added to Vref. Corresponds to UELin = 1 on the ExcST7B diagram. |
| inputHVgate | The signal is connected into the input HVGate. Corresponds to UELin = 2 on the ExcST7B diagram. |
| outputHVgate | The signal is connected into the output HVGate. Corresponds to UELin = 3 on the ExcST7B diagram. |

