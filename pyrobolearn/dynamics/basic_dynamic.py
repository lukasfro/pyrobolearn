#!/usr/bin/env python
"""Provides the various basic dynamic transition function approximators (e.g. table and linear approximators)

It can use learning models as most of these models learn a function (that is how to map inputs to outputs).
For instance, a dynamic network is a function represented by a neural network that maps a state-action to the next
state.
"""

from pyrobolearn.approximators import LinearApproximator
from pyrobolearn.dynamics.dynamic import ParametrizedDynamicModel


__author__ = "Brian Delhaisse"
__copyright__ = "Copyright 2018, PyRoboLearn"
__credits__ = ["Brian Delhaisse"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Brian Delhaisse"
__email__ = "briandelhaisse@gmail.com"
__status__ = "Development"


class LinearDynamicModel(ParametrizedDynamicModel):
    r"""Linear Dynamic Model

    Pros: easy to implement and learn
    Cons: very limited
    """

    def __init__(self, states, actions, next_states=None, distributions=None, preprocessors=None, postprocessors=None):
        """
        Initialize the linear dynamic transition function / probability :math:`p(s_{t+1} | s_t, a_t)`.

        Args:
            states (State): state inputs.
            actions (Action): action inputs.
            next_states (State, None): state outputs. If None, it will take the state inputs as the outputs.
            distributions (torch.distributions.Distribution): distribution to use to sample the next state. If None,
                it will be deterministic.
            preprocessors (Processor, list of Processor, None): pre-processors to be applied to the given input
            postprocessors (Processor, list of Processor, None): post-processors to be applied to the output
        """
        if next_states is None:
            next_states = states
        model = LinearApproximator(inputs=[states, actions], outputs=next_states, preprocessors=preprocessors,
                                   postprocessors=postprocessors)
        super(LinearDynamicModel, self).__init__(states, actions, model=model, next_states=next_states,
                                                 distributions=distributions)


class PieceWiseLinearDynamicModel(ParametrizedDynamicModel):
    r"""Piecewise linear dynamic model

    Pros: easy to implement, often good predictions in local regions
    Cons: poor scalability
    """

    def __init__(self, states, actions, next_states=None, distributions=None, preprocessors=None, postprocessors=None):
        """
        Initialize the piece wise linear dynamic transition function / probability :math:`p(s_{t+1} | s_t, a_t)`.

        Args:
            states (State): state inputs.
            actions (Action): action inputs.
            next_states (State, None): state outputs. If None, it will take the state inputs as the outputs.
            distributions (torch.distributions.Distribution): distribution to use to sample the next state. If None,
                it will be deterministic.
            preprocessors (Processor, list of Processor, None): pre-processors to be applied to the given input
            postprocessors (Processor, list of Processor, None): post-processors to be applied to the output
        """
        # TODO
        model = None
        super(PieceWiseLinearDynamicModel, self).__init__(states, actions, model=model, next_states=next_states,
                                                          distributions=distributions)
