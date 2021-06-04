# Quantum Fisher(man)
> Quantum Fisher(man) project developed for the <a href='https://qiskithackathoneurope.bemyapp.com'>IBM Qiskit Hackathon 2021</a>. We provide a toolkit to compute the overlap between quantum states. We apply it to obtain the quantum Fisher information from quantum circuits, which allows the optimization through advanced techniques such as the <a href='https://quantum-journal.org/papers/q-2020-05-25-269/pdf/'> quantum natural gradient</a>, as well as to study the loss landscape of such circuits. Furthermore, we provide a functionality to compute the overlap between quantum states from devices, which enables device-independent certification. 


## Quantum Fisher information

The Fisher information is a key metric widely used in physics and optimization. It has recently gathered great interest due to its applications in Machine Learning (ML), as it provides information about the local curvature of the Loss function, which can be leveraged to enhance vanilla gradient descent algorithms to perform [natural gradient](https://direct.mit.edu/neco/article/10/2/251/6143/Natural-Gradient-Works-Efficiently-in-Learning).

Its quantum version, the quantum Fisher information (QFI), plays a fundamental role in [multiple fields of quantum physics](https://arxiv.org/abs/2103.15191) such as quantum metrology, quantum information processing and quantum many-body physics. Furthermore, it lies at the core of recent quantum algorithms, such as the [quantum natural gradient](https://quantum-journal.org/papers/q-2020-05-25-269/pdf/), variational quantum imaginary time evolution or [quantum Boltzmann machines](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.021050).

However, the QFI is not directly related to any physical observable, which makes it very hard to measure. While fileds like quantum sensing or quantum machine learning would greatly benefit from it, its elevetaed cost makes it impractical to use in actual applications. 

A central element in the calculation of the QFI is the notion of distance between quantum states, which corresponds to their overlaps. In this hackathon we have developed a toolbox to compute the overlap between quantum states implementing various methods that do not require the explicit calculation of the state-vectors. Even more, they allow the computation of overlaps between mixed states and states in different devices. 

## Quantum Overlaps

The overlap between two states $\rho_0, \rho_1$ is defined as the trace of their product $\text{Tr}\left[\rho_0\rho_1\right]$ and measures the similarity between the two states. For pure states, the overlap coincides with the Fidelity and can be expressed as $|\langle\psi|\phi\rangle|^2$ for two pure states $|\psi\rangle, |\phi\rangle$.
