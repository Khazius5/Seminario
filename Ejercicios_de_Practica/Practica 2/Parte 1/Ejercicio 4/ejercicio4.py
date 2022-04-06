evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

contador = [0, 0, 0, 0]
oraciones = evaluar.split(".")

titulo = oraciones[0][9:]


# oraciones
if len(titulo.split()) > 10:
    print("titulo esta mal")
else:
    print("titulo esta ok")

for oracion in oraciones[1:]:
    words = len(oracion.split())
    if words < 12:
        contador[0] += 1
    elif words < 17:
        contador[1] += 1
    elif words < 25:
        contador[2] += 1
    else:
        contador[3] += 1
        
print(f"""Cantidad de oraciones fáciles de leer: {contador[0]}, aceptables para leer: {contador[1]}, dificil de leer: {contador[2]}, , muy dificil
de leer:{contador[3]}""")