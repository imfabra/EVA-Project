import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath import SE3


class EVA(DHRobot):
    """
    Class that models a EVA manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool

    ``EVA()`` is an object which models a HDI Group EVA robot and
    describes its kinematic and dynamic characteristics using standard DH
    conventions.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.DH.EVA()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration
    - qr, arm horizontal along x-axis

    .. note::
        - SI units are used.

    :References:

        - `Parameters for calculations of kinematics and dynamics <https://www.universal-robots.com/articles/ur/parameters-for-calculations-of-kinematics-and-dynamics>`_

    :sealso: :func:`UR4`, :func:`UR10`


    .. codeauthor:: Peter Corke
    """  # noqa

    def __init__(self, symbolic=False):

        if symbolic:
            import spatialmath.base.symbolic as sym

            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import pi

            zero = 0.0

        deg = pi / 180
        inch = 0.0254

        # robot length values (metres)
        a = [ 0, -0.300, -0.200, 0, 0]
        d = [0.1155, 0, 0.066, 0, 0.205]

        alpha = [pi / 2, zero, zero, -pi / 2, zero]
        theta = [pi / 2, -pi / 2, zero, pi / 2, zero]
        
        # mass data, no inertia available
        mass = [0.497137238, 0.83823869976, 1.03, 0.91761736451, 0.37557448236]
        
        #
        q_lim = [
            [-118*deg, 118*deg],
            [-108*deg, 126*deg],
            [-159*deg, 159*deg],
            [-170*deg, 170*deg],
            [-180*deg, 180*deg],
            ]
        
        center_of_mass = [
            [0, -0.00092, 0.012212],
            [0.006555, 0, 0.095733],
            [0.059549 , 0.148359 , 0.099393],
            [0.003394 , 0.397281, 0.0994],
            [0.063950 , 0.485, 0.091115 ],
            
        ]
        links = []

        for j in range(5):
            link = RevoluteDH(
                offset=theta[j],d=d[j], a=a[j], alpha=alpha[j],qlim=q_lim[j], m=mass[j], r=center_of_mass[j], G=1
            )
            links.append(link)

        super().__init__(
            links,
            name="EVA",
            manufacturer="HDI Group",
            keywords=("dynamics", "symbolic"),
            symbolic=symbolic,
        )

        self.qr = np.array([-90, 45, -45, 90, 90]) * deg
        self.qz = np.zeros(5)

        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover
    
    

    eva = EVA(symbolic=False)
    # print(eva)
    # print(eva.dyntable())
