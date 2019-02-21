# The simulators above are useful because they provide information about the state output by the ideal circuit and the matrix representation of the circuit. However, a real experiment terminates by _measuring_ each qubit(usually in the computational $| 0\rangle, | 1\rangle$ basis). Without measurement, we cannot gain information about the state. Measurements cause the quantum system to collapse into classical bits.

# For example, suppose we make independent measurements on each qubit of the three-qubit GHZ state
# $$|\psi\rangle = |000\rangle + |111\rangle) /\sqrt{2}, $$
#     and let $xyz$ denote the bitstring that results. Recall that, under the qubit labeling used by Qiskit, $x$ would correspond to the outcome on qubit 2, $y$ to the outcome on qubit 1, and $z$ to the outcome on qubit 0. This representation of the bitstring puts the most significant bit(MSB) on the left, and the least significant bit(LSB) on the right. This is the standard ordering of binary bitstrings. We order the qubits in the same way, which is why Qiskit uses a non-standard tensor product order.

#     The probability of obtaining outcome $xyz$ is given by
#     $$\mathrm{Pr}(xyz)=|\langle xyz | \psi \rangle | ^{2}.$$
#     By explicit computation, we see there are only two bitstrings that will occur: $000$ and $111$. If the bitstring $000$ is obtained, the state of the qubits is $| 000\rangle$, and if the bitstring is $111$, the qubits are left in the state $| 111\rangle$. The probability of obtaining 000 or 111 is the same; namely, 1/2:
#     $$\begin{align}
#     \mathrm{Pr}(000) &= |\langle 000 | \psi \rangle | ^{2}= \frac{1}{2}
#     \mathrm{Pr}(111) &= |\langle 111 | \psi \rangle | ^{2}= \frac{1}{2}.
#     \end{align}$$

#     To simulate a circuit that includes measurement, we need to add measurements to the original circuit above, and use a different Aer backend.


# Create a Classical Register with 3 bits.
c = ClassicalRegister(3, 'c')
# Create a Quantum Circuit
meas = QuantumCircuit(q, c)
meas.barrier(q)
# map the quantum measurement to the classical bits
meas.measure(q, c)

# The Qiskit circuit object supports composition using
# the addition operator.
qc = circ+meas

#drawing the circuit
qc.draw()

