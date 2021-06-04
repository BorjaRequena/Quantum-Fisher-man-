# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_compuncomp.ipynb (unless otherwise specified).

__all__ = ['compute_uncompute_overlap']

# Cell
import numpy as np
from ..utils import sym_from_triu, is_exact_simulation

from qiskit import QuantumCircuit
from qiskit.providers import Backend
from qiskit.utils import QuantumInstance
from qiskit.circuit import ParameterExpression
from qiskit.opflow import ListOp, StateFn, ExpectationBase, CircuitSampler

from collections.abc import Iterable
from typing import Optional, Union, Dict, List

# Cell
def compute_uncompute_overlap(
    state0: StateFn,
    state1: Optional[Union[StateFn, ListOp]] = None,
    param_dict: Optional[Dict[ParameterExpression, List[float]]] = None,
    expectation: Optional[ExpectationBase] = None,
    backend: Optional[Union[Backend, QuantumInstance]] = None
) -> np.ndarray:
    """Compute-uncompute method """

    if state1 is not None and param_dict is not None:
        raise ValueError(
            "swap_test_overlap only accepts one optional input "
            "either `state1` or `param_dict`."
                        )

    qi = QuantumInstance(backend) if isinstance(backend, Backend) else backend

    if qi is None or is_exact_simulation(qi):
        if param_dict is not None:
            states = state0.bind_parameters(param_dict)
            observable = ~states @ states
        elif state1 is not None:
            states = state1 if isinstance(state1, ListOp) else ListOp([state1])
            observable = ~state0 @ states
        else:
            observable = ~state0 @ state0

        if expectation is not None:
            observable = expectation.convert(observable)

        if qi is not None:
            observable = CircuitSampler(qi).convert(observable)

        return np.abs(observable.eval())**2

    else:
        # Workaround to prevent the compiler from converting the circuit to identity
        # forcing the explicit execution with a noisy simulator or a quantum circuit.
        def _cu_circuit(s0, s1):
            circuit = s0.primitive.copy()
            circuit.barrier()
            circuit = circuit.compose((~s1).primitive)
            circuit.measure_all()
            return circuit

        if param_dict is not None:
            states = state0.bind_parameters(param_dict)
            circuits = [_cu_circuit(s_i, s_j)
                        for i, s_i in enumerate(states) for s_j in states[i:]]
        elif state1 is not None:
            state1 = state1 if isinstance(state1, Iterable) else [state1]
            circuits = [_cu_circuit(state0, s) for s in state1]
        else:
            circuits = [_cu_circuit(state0, state0)]

        counts = qi.execute(circuits).get_counts()
        counts = counts if isinstance(counts, list) else [counts]
        zero_state = '0'*state0.num_qubits
        overlap = np.array([c.get(zero_state, 0)/sum(c.values()) for c in counts])

        return overlap.squeeze() if param_dict is None else sym_from_triu(overlap, len(states))