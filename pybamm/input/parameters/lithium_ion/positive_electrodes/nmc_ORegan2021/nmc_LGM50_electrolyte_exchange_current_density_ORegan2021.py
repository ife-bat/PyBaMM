from pybamm import exp, constants, Parameter


def nmc_LGM50_electrolyte_exchange_current_density_ORegan2021(c_e, c_s_surf, T):
    """
    Exchange-current density for Butler-Volmer reactions between NMC and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Kieran O’Regan, Ferran Brosa Planella, W. Dhammika Widanage, and Emma
    Kendrick. "Thermal-electrochemical parametrisation of a lithium-ion battery:
    mapping Li concentration and temperature dependencies." Journal of the
    Electrochemical Society, submitted (2021).
    
    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    i_ref = 5.028  # (A/m2)
    alpha = 0.43
    E_r = 2.401e4
    arrhenius = exp(E_r / constants.R * (1 / 298.15 - 1 / T))

    c_p_max = Parameter("Maximum concentration in positive electrode [mol.m-3]")
    c_e_ref = Parameter("Typical electrolyte concentration [mol.m-3]")

    return (
        i_ref
        * arrhenius
        * (c_e / c_e_ref) ** (1 - alpha)
        * (c_s_surf / c_p_max) ** alpha
        * (1 - c_s_surf / c_p_max) ** (1 - alpha)
    )
