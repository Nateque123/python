# Scope of Global and Local Variables

x = 5 # Global Var

def scope_var():
    global x
    x = 7 # Local var
    return x

print(x)
print(scope_var())
print(x)