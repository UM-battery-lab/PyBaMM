from pybamm import exp, constants, Parameter


def graphite_LGM50_electrolyte_exchange_current_density_Chen2020(
    c_e, c_s_surf, T, phase=None
):
    """
    Exchange-current density for Butler-Volmer reactions between graphite and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

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
    if phase == "phase 1":
        p_name = " of phase 1"
    elif phase == "phase 2":
        p_name = " of phase 2"
    else:
        p_name = ""
    m_ref = 6.48e-7  # (A/m2)(mol/m3)**1.5 - includes ref concentrations
    E_r = 35000
    arrhenius = exp(E_r / constants.R * (1 / 298.15 - 1 / T))

    c_n_max = Parameter(
        f"Maximum concentration in negative electrode{p_name} [mol.m-3]"
    )

    return (
        m_ref * arrhenius * c_e ** 0.5 * c_s_surf ** 0.5 * (c_n_max - c_s_surf) ** 0.5
    )
