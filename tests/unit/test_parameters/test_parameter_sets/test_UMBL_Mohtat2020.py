#
# Tests for LG M50 parameter set loads
#
import pybamm
import unittest


class TestMohtat(unittest.TestCase):
    def test_load_params(self):
        anode = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/anodes/graphite_UMBL_Mohtat2020/parameters.csv"
            )
        )
        self.assertEqual(anode["Reference temperature [K]"], "298.15")

        cathode = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/cathodes/NMC_UMBL_Mohtat2020/parameters.csv"
            )
        )
        self.assertEqual(cathode["Reference temperature [K]"], "298.15")

        electrolyte = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/electrolytes/LiPF6_Mohtat2020/"
                + "parameters.csv"
            )
        )
        self.assertEqual(electrolyte["Reference temperature [K]"], "298.15")

        cell = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/cells/UMBL_Mohtat2020/parameters.csv"
            )
        )
        self.assertAlmostEqual(
            cell["Negative current collector thickness [m]"], 2.5e-05
        )

    def test_standard_lithium_parameters(self):

        chemistry = pybamm.parameter_sets.Mohtat2020
        parameter_values = pybamm.ParameterValues(chemistry=chemistry)

        model = pybamm.lithium_ion.DFN()
        sim = pybamm.Simulation(model, parameter_values=parameter_values)
        sim.set_parameters()
        sim.build()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
