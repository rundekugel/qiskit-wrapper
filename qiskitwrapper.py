#quantum computer test qiskit
"""
#quantum computer test qiskit libs wrapper for small, lean and faster experiments
"""
#import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.test.mock import FakeBoeblingen
backend = FakeBoeblingen()

# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
#from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
#provider = IBMQ.load_account()

def get2qb():
  """Create a Quantum Circuit acting on the q register"""
  circuit = QuantumCircuit(2, 2)
  return circuit

class QuTest:
  """
  generate a qiskit test 
  """
  circuit=None
  result=None
  verbose=1
  drawAlways=0
  simulator = Aer.get_backend('qasm_simulator')
  
  def __init__(self, bitcount=2):
    """parameter: number of qubits"""
    self.bitcount = bitcount
    self.circuit = QuantumCircuit(bitcount, bitcount)
    self._drawP()
    
  def _drawP(self):
    if self.drawAlways:  self.draw()
  
  def addMeasure(self, q="all"):
    """set """
    if q=="all":
      q=[*range(self.bitcount)]
    else:
      if not isinstance(q, list):
        q=[q]
    self.circuit.measure(q, q)
    self._drawP()
    
  def run(self, shots=1024):
    print("Circuit:")
    print(self.circuit)
    print("Execute...")
    self.job = execute(self.circuit, self.simulator, shots=shots)
    print("done.")
    return self.getResult()
  
  def getResult(self):
    self.result = self.job.result()
    c=self.result.get_counts(self.circuit)
    return c
    
  def draw(self):
    print(self.circuit)
    
    
# - end of file -
