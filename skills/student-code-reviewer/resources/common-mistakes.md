# Common Beginner Programming Mistakes

Use this checklist when reviewing beginner assignments in C, Java, or Python. Treat each item as a prompt for investigation, not proof that the student's code is wrong. Confirm the issue against the code, the assignment requirements, and the reported behavior.

## Review checklist

### Off-by-one errors in loops

**Look for**

- A loop that starts one position too early or too late.
- A loop that stops before the final item or accesses one position past the end.
- Confusion between a count and the last valid index.
- Boundary conditions such as `<` versus `<=`, or equivalent range limits in Python.

**Leading questions**

- How many times should this loop run, and how many times does it actually run?
- What is the first valid position? What is the last valid position?
- What happens on the first iteration and on the iteration that should process the final item?

### Misunderstanding variable scope

**Look for**

- A variable created inside a function, block, loop, or conditional being used outside that region.
- A local variable unintentionally hiding another variable with the same name.
- A variable being read before it is available in the current scope.
- Code that assumes a change to a local variable changes a separate outer variable.

**Leading questions**

- Where is this variable declared, and which parts of the program can see that declaration?
- Is this the same variable as the one with the matching name elsewhere, or a different one?
- What value is available at the exact point where the variable is used?

### Missing return statements or returning the wrong type

**Look for**

- A function whose result is used even though one or more paths do not return a value.
- A function returning a value that does not match its declared or expected type.
- A returned value being confused with printing a value.
- A caller expecting a result that the function never sends back.

**Leading questions**

- What value should this function give back on every possible path?
- Is the function displaying a value, or is it returning one to its caller?
- What type does the function promise, and what type reaches the caller?

### Infinite loops

**Look for**

- A loop condition that never becomes false.
- A counter or state value that is never updated.
- An update that moves the value in the wrong direction.
- A `continue` path that skips the update needed to make progress.

**Leading questions**

- Which value changes each time through the loop?
- Can you trace that value through two or three iterations?
- What exact event is supposed to make the condition false, and can that event actually happen?

### Confusing assignment (`=`) with equality (`==`)

**Look for**

- A condition that changes a variable when it should compare values.
- A comparison written with assignment syntax, where the language permits or rejects it differently.
- A condition whose result is surprising because a value was stored instead of tested.

**Leading questions**

- Is this line trying to store a value or ask whether two values are equal?
- After this expression runs, what value does the variable contain?
- What would the condition evaluate to if you traced the values before and after the line?

## Additional checks

### Uninitialized or unexpected values

- Is every variable assigned a meaningful value before it is read?
- Could a previous iteration or branch leave behind a value the current path did not expect?
- What do the smallest and simplest inputs reveal?

### Incorrect condition or operator

- Does the condition describe the requirement exactly?
- Should the operation be logical AND or OR, integer division or regular division, or another nearby operator?
- What happens when the input is zero, empty, negative, or at a boundary?

### Type and input mismatches

- Does the input conversion match the data the program expects?
- Could a value be truncated, treated as text, or compared with an incompatible type?
- What type does each expression produce at this point?

### Incorrect update or state mutation

- Is the value updated in the intended variable?
- Does the update happen once per iteration, in the right order?
- Could an alias, reference, or shared object change more than intended?

### Misplaced output or side effects

- Is a print or other side effect inside a loop or branch when it should happen once, or outside when it should happen repeatedly?
- Does the output show the intermediate value or the final value the assignment asks for?
- Can the student trace when the output statement executes?

## Review discipline

- Treat compiler errors, runtime errors, wrong output, and inefficient behavior as different symptoms.
- Prefer a small experiment or trace the student can perform themselves.
- Do not turn a checklist item into a diagnosis without evidence from the student's code.
- When several issues exist, start with the one that prevents the student from observing the next issue.
