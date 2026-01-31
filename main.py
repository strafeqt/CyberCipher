from observer import observe
from reasoner import reason
from decision import decide
from actions import act

context = observe()
analysis = reason(context)
decision = decide(analysis)
result = act(decision)

print("\n--- AGENT THINKING ---")
print(analysis)

print("\n--- AGENT DECISION ---")
print(result)
